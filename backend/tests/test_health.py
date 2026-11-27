from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_ingest_accepts_flows():
    flow = {
        "sensor_id": "sensor-1",
        "src_ip": "10.0.0.5",
        "dst_ip": "10.0.0.9",
        "src_port": 51514,
        "dst_port": 22,
        "protocol": 6,
        "timestamp": "2026-12-01T10:00:00Z",
        "duration_ms": 1200.5,
    }
    response = client.post("/api/flows", json=[flow])
    assert response.status_code == 202
    assert response.json() == {"received": 1}


def test_alert_websocket_connects():
    with client.websocket_connect("/ws/alerts") as ws:
        ws.send_text("ping")
