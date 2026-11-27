from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.middleware.cors import CORSMiddleware

from app.config import settings
from app.schemas import Flow

app = FastAPI(title="HITL IDS API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.cors_origins.split(","),
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health() -> dict:
    return {"status": "ok"}


@app.post("/api/flows", status_code=202)
def ingest_flows(flows: list[Flow]) -> dict:
    """Placeholder for package B (ingest API). Checks the sensor key and stores flows later."""
    return {"received": len(flows)}


class AlertHub:
    """Keeps the open dashboard connections so new alerts can be pushed to all of them."""

    def __init__(self) -> None:
        self.clients: set[WebSocket] = set()

    async def connect(self, ws: WebSocket) -> None:
        await ws.accept()
        self.clients.add(ws)

    def disconnect(self, ws: WebSocket) -> None:
        self.clients.discard(ws)

    async def broadcast(self, message: dict) -> None:
        for ws in list(self.clients):
            await ws.send_json(message)


hub = AlertHub()


@app.websocket("/ws/alerts")
async def alerts_socket(ws: WebSocket) -> None:
    """Placeholder for package D. The dashboard listens here for new alerts."""
    await hub.connect(ws)
    try:
        while True:
            await ws.receive_text()
    except WebSocketDisconnect:
        hub.disconnect(ws)
