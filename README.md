# blueShark
BlueShark is an open-source defensive PCAP analysis tool that converts packet captures into structured security insights.

The project analyzes network traffic using deterministic packet analysis tools (such as tshark) and generates inventories, protocol extracts, traffic summaries, and security findings that help analysts quickly understand what occurred in a capture. BlueShark is designed to make PCAP analysis more repeatable, structured, and accessible, while also serving as a platform for experimentation with AI-assisted network security analysis. This project is part of a cybersecurity research initiative with high school students participating in TrustThink's Our Lady of Peace cybersecurity internship program.

Overview
Analyzing packet captures is a core task in network security, but it can be time-consuming and difficult for new analysts. BlueShark was created to automate the early stages of network forensic analysis by: 

Identifying protocols present in a capture
Mapping endpoints and conversations
Extracting structured protocol metadata
Summarizing traffic patterns
Producing machine-readable security findings

The goal is to turn raw packet data into structured artifacts that analysts or automated systems can quickly review.
