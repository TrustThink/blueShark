from agents import Agent
from datetime import datetime
import argparse
from pathlib import Path
import shutil
import os

from Utils import extractknownprotocols, list_endpoints, identifytoptalkers


# Step 1 : Ingest Filepath

def ingest_filepath(filepath:str) -> None:
    case_directory_path = "case/000"
    case_directory_path = Path(case_directory_path)
    os.makedirs(case_directory_path, exist_ok=True)

    dest = case_directory_path / "capture.pcap"
    shutil.copy2(filepath, dest)


# Step 2 : Determine traffic makeup 

def traffic_makeup(filepath:str) -> None:
    protocol_list = extractknownprotocols(filepath)
    endpoints_list = list_endpoints(filepath)
    top_talkers_list = identifytoptalkers(filepath)
    # TODO: functions should return dicts, write to json files

# Step 3 : Output Structured Files

def structured_files():
    pass
    # deterministic tshark extracts

    # conditional extracts
    # if tls:
        # ...
    # if http:
        # ...
    # if dns:
        # ...
    # if mavlink:
        # ...

# Step 4 : Reduce Json files to summaries

def summarize_json_files():

    pass

# Step 5 : Create Case Context Filepath

def create_case_context_file():
    pass

# Step 6 : Provide Summaries to LLM

def provide_summaries():
    # ---- INITIALIZING AGENT ----- 
    agent = Agent(
        name="blueshark",
        instructions= "You are a open-source defensive PCAP security agent. You must produce actionable and useful security findings with evidence, and analyze and convert packet captures into structured and specific security insights. You can use tools if they are provided",
        model="gpt-5.4-nano",
    )  
    # model input: summaries + case context file
    # function output: findings.json, Report.md


### Main CLI Logic ###
def main():
    ap = argparse.ArgumentParser()
    
    ap.add_argument("--filepath", "-f", required=True, help="Filepath to results .pcap file") 
    args = ap.parse_args()
   
    #raise ValueError(".pcap file does not exist: {args.filepath}")

    filepath = args.filepath

    ingest_filepath(filepath)
    

    

if __name__ == "__main__":
    main() 
    