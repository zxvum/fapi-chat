from fastapi import APIRouter, Depends
from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from starlette.websockets import WebSocket, WebSocketDisconnect

from chat.manager import manager
from database import get_async_session
from models import chat

router = APIRouter(
    prefix='/chat',
    tags=['chat']
)


# @router.websocket('/chat/{client_id}')
# async def index(websocket: WebSocket, client_id: int):
#     await ws_manager.connect(websocket)
#     try:
#         while True:
#             data = await websocket.receive_text()
#             await ws_manager.broadcast(f"Client #{client_id} says: {data}")
#     except WebSocketDisconnect:
#         ws_manager.disconnect(websocket)
#         await ws_manager.broadcast(f"Client #{client_id} left the chat")


@router.get('/')
async def get_messages(session: AsyncSession = Depends()):
    query = select(chat)
    result = await session.execute(query)
    return result.all()