from fastapi import FastAPI, WebSocket
from services import media_player
import asyncio

app = FastAPI()

@app.get("/media")
async def media(action: str = None):
    if action is None:
        return await media_player.get_current_media_info()
    else:
        return await media_player.control_media(action)

@app.websocket("/ws/media")
async def websocket_media(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await media_player.get_current_media_info()
            await websocket.send_json(data)
            await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket connection closed: {e}")
    # finally:
    #     await websocket.close()

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=3728, reload=True)