from fastapi import APIRouter
from starlette.websockets import WebSocket, WebSocketDisconnect

from managers import manager as ws_manager

router = APIRouter(
    prefix='/chat',
    tags=['chat']
)

@router.websocket('/chat/{client_id}')
async def index(websocket: WebSocket, client_id: int):
    await ws_manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            await ws_manager.broadcast(f"Client #{client_id} says: {data}")
    except WebSocketDisconnect:
        ws_manager.disconnect(websocket)
        await ws_manager.broadcast(f"Client #{client_id} left the chat")
