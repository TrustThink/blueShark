import pyshark
import collections
def read_capture_file(filepath):
    capture = pyshark.FileCapture(
        filepath,
        keep_packets = False
    )
    return capture

def extractknownprotocols(filepath): 
    capture = read_capture_file(filepath)
    protocol_list = []
    for packet in capture:
        protocol = packet.highest_layer
        if protocol not in protocol_list: 
            protocol_list.append(protocol)
    return protocol_list

def list_endpoints(filepath):
    capture = read_capture_file(filepath)
    endpoints = set()
    for packet in capture:
        if hasattr(packet, "ip"):
            endpoints.add(packet.ip.src)
            endpoints.add(packet.ip.dst)
    return list(endpoints)

def identifytoptalkers(filepath): 
    capture = read_capture_file(filepath)
    for packet in capture: 
        ip_dictionary = collections.Counter(packet.ip.src)
        greatest_frequency = ip_dictionary[0][0]
        greatest_frequency_address = ip_dictionary[0]
    for key in range(ip_dictionary.length): 
        if ip_dictionary[key][0] > greatest_frequency:
            greatest_frequency_address = ip_dictionary[key]
    return greatest_frequency_address

