# Sensor agent (package B)

Runs on a Linux machine that can see the monitored traffic. Needs root rights.

What it must do (PRD 1.3 and 4.4):

1. Capture live traffic with CICFlowMeter (Python version, live mode).
2. Send flow records to the backend over HTTPS with its sensor key (`POST /api/flows`).
3. Send a heartbeat about every 30 seconds.
4. Keep flows in `buffer/` if the backend can't be reached, and resend them later.

Until the ingest API is ready, write flows to a local file instead.

## Setup (Ubuntu / WSL)

```bash
sudo apt install -y python3-venv libpcap-dev tcpreplay
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
```

## Test without an attacker machine

Replay a CIC-IDS2017 capture onto the network card the sensor watches:

```bash
sudo tcpreplay -i eth0 --mbps 10 Wednesday-workingHours.pcap
```
