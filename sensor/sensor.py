"""Sensor agent entry point (package B). Fill in capture, send, heartbeat and buffer."""

import os

BACKEND_URL = os.getenv("BACKEND_URL", "http://localhost:8000")
SENSOR_KEY = os.getenv("SENSOR_KEY", "")
INTERFACE = os.getenv("SENSOR_INTERFACE", "eth0")
HEARTBEAT_SECONDS = 30


def main() -> None:
    print(f"Sensor starting on {INTERFACE}, sending to {BACKEND_URL}")
    # TODO: start CICFlowMeter live capture on INTERFACE
    # TODO: send each batch of flows to f"{BACKEND_URL}/api/flows" with SENSOR_KEY
    # TODO: heartbeat every HEARTBEAT_SECONDS
    # TODO: buffer flows locally when the backend is unreachable


if __name__ == "__main__":
    main()
