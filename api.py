from fastapi import FastAPI
import uvicorn

# Import the Vulnerability scan function
import os
import subprocess
# from holyEye import vulnerability_scan

app = FastAPI()


# Vulnerability Scan
@app.get("/vulnerability")
async def vulnerability_api():
    cmd = "nmap -sV -oG --script vulners --script-args mincvss=5.0 192.168.0.106"
    returned_output = subprocess.check_output(cmd, shell=True)
    return returned_output.decode("utf-8")


# Quick Scan
@app.get("/quick")
async def quick_api():
    cmd = "nmap -sS -oG -sV -Pn -T4 192.168.0.106"
    returned_output = subprocess.check_output(cmd, shell=True)
    return returned_output.decode("utf-8")


uvicorn.run(app, port=1337) 
