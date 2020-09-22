import sys
import asyncio
from pathlib import Path
from telethon import TelegramClient, events
from iqlogger import Logger
from tlg_constants import TelegramConstants

# your main work, never block this thread
async def main():
    i = 0
    while True:
        i += 1
        await asyncio.sleep(1)

c = TelegramConstants()
sys.stdout = Logger(Path(__file__).parent.absolute())
tlgSessionPath = Path.joinpath(Path(__file__).parent.absolute(), 'tlgdb', 'leo')

tlg = TelegramClient(
    session=str(tlgSessionPath),
    api_id=c.api_id,
    api_hash=c.api_hash,
)
tlg.start('+5511993774025')

@tlg.on(events.NewMessage)
async def my_handler(update):
    # chat = await update.get_chat()
    # sender = await update.get_sender()
    print(update.chat_id)
    print(update.raw_text)


loop = asyncio.get_event_loop()
loop.run_until_complete(main())
