#!/usr/bin/env python3
from starlette.applications import Starlette
from starlette.responses import HTMLResponse
from starlette.routing import Route, WebSocketRoute
from starlette.staticfiles import StaticFiles

async def homepage(request):
    with open("index.html", "r", encoding="utf-8") as f:
        return HTMLResponse(f.read())


async def websocket_endpoint(websocket):
    await websocket.accept()
    try:
        while True:
            message = await websocket.receive_text()
            await websocket.send_text(message)
    except Exception:
        pass

app = Starlette(routes=[
    Route("/", homepage),
    WebSocketRoute("/ws", websocket_endpoint),
])

app.mount("/", StaticFiles(directory="."), name="static")
