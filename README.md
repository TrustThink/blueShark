# blueShark
BlueShark is an open-source defensive PCAP analysis tool that converts packet captures into structured security insights.

The project analyzes network traffic using deterministic packet analysis tools (such as tshark) and generates inventories, protocol extracts, traffic summaries, and security findings that help analysts quickly understand what occurred in a capture. BlueShark is designed to make PCAP analysis more repeatable, structured, and accessible, while also serving as a platform for experimentation with AI-assisted network security analysis. This project is part of a cybersecurity research initiative with high school students participating in TrustThink's Our Lady of Peace cybersecurity internship program.

Overview
Analyzing packet captures is a core task in network security, but it can be time-consuming and difficult for new analysts. BlueShark was created to automate the early stages of network forensic analysis by: 

- Identifying protocols present in a capture

- Mapping endpoints and conversations
- Extracting structured protocol metadata
- Summarizing traffic patterns
- Producing machine-readable security findings

The goal is to turn raw packet data into structured artifacts that analysts or automated systems can quickly review.

## Features

- PCAP ingestion and structured case workspace
- Protocol and traffic inventory
- Endpoint and conversation mapping
- Protocol metadata extraction for:
- Traffic summarization and statistics
- Structured JSON outputs
- Security findings and Markdown reports
- Support for AI-assisted analysis workflows

## Why This Project Exists

BlueShark was created as part of a student cybersecurity research project focused on exploring how automation and AI can assist with defensive network analysis.

The goals of the project are to:

- Teach students practical network security analysis
- Demonstrate structured PCAP analysis pipelines
- Explore how AI can assist security analysts
- Build open-source tools that others can learn from and extend

The project emphasizes defensive security analysis, education, and research.

## Project Structure



# Dependencies

BlueShark relies on widely used open-source packet analysis tools.

Primary dependency:

- Wireshark 
- tshark

Wireshark project website:
 https://www.wireshark.org

# Authors

This library was developed and is maintained by:

- Allison Lane
- Kathleen Michalowski
- Maria De Santi
- Aurelia Dunne
- Mila Halvorson
- Sarah Ivanjack
- Sierra Ratonel
- Inanna Arsova-Klejnot
- Camila Soto Aceves
- Anabelle Rojas Morgan
- Lily Goncalves

TrustThink, LLC

TrustThink is a cybersecurity engineering firm specializing in secure system architecture, transportation, healthcare and defense cybersecurity, and secure communications frameworks.

