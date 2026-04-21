import pyshark
import asyncio
import collections
import ipaddress


#MAIN  
def read_capture_file(filepath):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)

    return pyshark.FileCapture(
        filepath,
        eventloop=loop,
        keep_packets=False
    )


#VALID IP ADDRESS CHECK
def is_valid_ip(ip):
    try:
        ipaddress.ip_address(ip)
        return True
    except ValueError:
        return False


#PROTOCOLS
def extract_known_protocols(filepath):
    capture = read_capture_file(filepath)
    protocols = set()

    for packet in capture:
        try:
            protocols.add(packet.highest_layer)
        except AttributeError:
            continue

    capture.close()

    return {
        "protocols": list(protocols),
        "count": len(protocols)
    }


#ENDPOINTS
def list_endpoints(filepath):
    capture = read_capture_file(filepath)
    endpoints = set()
    skipped = 0

    for packet in capture:
        try:
            src = packet.ip.src
            dst = packet.ip.dst

            if is_valid_ip(src):
                endpoints.add(src)
            if is_valid_ip(dst):
                endpoints.add(dst)

        except AttributeError:
            skipped += 1
            continue

    capture.close()

    return {
        "endpoints": list(endpoints),
        "count": len(endpoints),
        "skipped_packets": skipped
    }


#ALL CONVERSATIONS
def identify_conversations(filepath):
    capture = read_capture_file(filepath)

    tcp_conversations = {}
    udp_conversations = {}
    skipped = 0

    for packet in capture:
        try:
            src = packet.ip.src
            dst = packet.ip.dst
            protocol = packet.transport_layer
        except AttributeError:
            skipped += 1
            continue

        if protocol not in ["TCP", "UDP"]:
            continue

        #ports
        src_port = None
        dst_port = None

        try:
            if protocol == "TCP":
                src_port = packet.tcp.srcport
                dst_port = packet.tcp.dstport
            elif protocol == "UDP":
                src_port = packet.udp.srcport
                dst_port = packet.udp.dstport
        except AttributeError:
            pass

        #JSON key
        key = f"{src}:{src_port}->{dst}:{dst_port}"
        target = tcp_conversations if protocol == "TCP" else udp_conversations

        if key not in target:
            target[key] = {
                "src": src,
                "dst": dst,
                "protocol": protocol,
                "src_port": src_port,
                "dst_port": dst_port,
                "packet_count": 0,
                "bytes": 0
            }

        target[key]["packet_count"] += 1

        try:
            if hasattr(packet, "length"):
                target[key]["bytes"] += int(packet.length)
        except ValueError:
            pass

    capture.close()

    return {
        "tcp": tcp_conversations,
        "udp": udp_conversations,
        "skipped_packets": skipped
    }


#TOP TALKERS
def identify_top_talkers(filepath, top_n=5):
    capture = read_capture_file(filepath)
    counter = collections.Counter()
    skipped = 0

    for packet in capture:
        try:
            src = packet.ip.src
            if is_valid_ip(src):
                counter[src] += 1
        except AttributeError:
            skipped += 1
            continue

    capture.close()

    return {
        "top_talkers": {
            ip: {"packet_count": count}
            for ip, count in counter.most_common(top_n)
        },
        "skipped_packets": skipped
    }


#TESTRUN
if __name__ == "__main__":
    filepath = "wiresharkfile.pcap"

    print("\nPROTOCOLS")
    print(extract_known_protocols(filepath))

    print("\nENDPOINTS")
    print(list_endpoints(filepath))

    print("\nCONVERSATIONS")
    convos = identify_conversations(filepath)
    print("TCP conversations:", len(convos["tcp"]))
    print("UDP conversations:", len(convos["udp"]))
    print("Skipped packets:", convos["skipped_packets"])

    print("\nTOP TALKERS")
    print(identify_top_talkers(filepath))
