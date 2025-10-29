from telethon import TelegramClient, events
from telethon.sessions import StringSession
import asyncio

api_id = 25451030
api_hash = "9810f1e7387fc060f76b706844364819"
string_session = "1BVtsOLYBuxvFlJiGt5_Uc4rUj9KObQ9RbOR8uNf6EPBx7DAuVuaXhrHn_kbnZUDlhe1BVw6CNbO5vvTtjeXfhXvJD55IvurILOUD8kb56KiuJh8mcnLLMmLSvDo9cHtOn9YZA838uMEbo3yotNf6uj0LWEP-9ZwpV8v3T_VMt_Fh_ARzVTfEvPHIIFY1KWaIef8zoXFT62Wda0MAMt8V9zfYizy1yV4zdaqZoW2aYHrN8l7YcibVTbBhjw8jFSI5dod9t8m4ZoMq5vi-5WNMQu3FvZcxkxLbVP7ID1YXceuvbCScaUF0juDy_r7nY6Szc-pdJy15QpsFqrYhu5SQb3a9v3rK2Q8="

GROUP_ID = -1003143017105

client = TelegramClient(StringSession(string_session), api_id, api_hash)

@client.on(events.NewMessage(chats=GROUP_ID))
async def auto_leech(event):
    if event.file and event.file.name.endswith(".torrent"):
        print(f"🎯 Detected torrent file: {event.file.name}")
        await event.reply("/qbleech@dump_leech_bot")
        print("✅ Sent /qbleech successfully!")

async def main():
    print("🚀 Auto leech system started... Waiting for torrent files.")
    await client.start()
    await client.run_until_disconnected()

asyncio.run(main())
