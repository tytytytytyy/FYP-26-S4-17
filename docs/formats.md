# Agreed data formats (draft, confirm at sprint planning on 28 Nov)

The code version of these lives in `backend/app/schemas.py`. Change both together.

## Flow (sensor to backend)

```json
{
  "sensor_id": "sensor-1",
  "src_ip": "10.0.0.5",
  "dst_ip": "10.0.0.9",
  "src_port": 51514,
  "dst_port": 22,
  "protocol": 6,
  "timestamp": "2026-12-01T10:00:00Z",
  "duration_ms": 1200.5,
  "features": { "Flow Bytes/s": 5321.2, "Total Fwd Packets": 14 }
}
```

## Alert (backend to dashboard, also sent over the WebSocket)

```json
{
  "id": 101,
  "created_at": "2026-12-01T10:00:03Z",
  "severity": "high",
  "confidence": 0.92,
  "detection_type": "Known attack",
  "attack_category": "Brute Force",
  "status": "New",
  "disposition": null,
  "disposition_reason": null,
  "assigned_to": null,
  "flow": { "...": "the Flow above" }
}
```

- `severity`: low, medium, high, critical
- `detection_type`: "Known attack" (Random Forest) or "Anomaly" (Isolation Forest, no attack_category)
- `status`: New, In progress, Escalated, Closed
- `disposition`: True Positive, Benign Positive, False Positive (set when closing)
