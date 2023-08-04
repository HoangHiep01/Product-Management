# !/usr/bin/env python

import asyncio
import websockets

async def listener(websocket):

	while True:
		message = await websocket.recv()
		greeting = f"Recv: {message}"

		await websocket.send("Oke")
		print(f">>> {greeting}")

async def main():
	async with websockets.serve(listener, "192.168.1.18", 8765):
		await asyncio.Future()  # run forever

if __name__ == "__main__":
	# asyncio.run(main())
	asyncio.create_task(main())