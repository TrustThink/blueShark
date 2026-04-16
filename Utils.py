import pyshark
import collections
import asyncio
import sys


def read_capture_file(filepath):
    loop = asyncio.ProactorEventLoop()
    asyncio.set_event_loop(loop)
    capture = pyshark.FileCapture(
        filepath,
        eventloop=loop
    )
    return capture
#Extract known protocols works as is
def extractknownprotocols(filepath): 
    capture = read_capture_file(filepath)
    protocol_list = []
    for packet in capture:
        protocol = packet.highest_layer
        if protocol not in protocol_list: 
            protocol_list.append(protocol)
    return protocol_list
#endpoint function
def list_endpoints(filepath):
    capture = read_capture_file(filepath)
    endpoints = set()
    for packet in capture:
        if hasattr(packet, "ip"):
            endpoints.add(packet.ip.src)
            endpoints.add(packet.ip.dst)
    return list(endpoints)
#ERROR

def identifytoptalkers(filepath, top_n=5): 
    capture = read_capture_file(filepath)
    counter = collections.Counter()
    for packet in capture:
        try:
            counter[packet.ip.src] += 1
        except AttributeError:
            continue
    return counter.most_common(top_n)

print(list_endpoints("wiresharkfile.pcap"))
