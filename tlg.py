import sys
import asyncio
import logging
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
tlgSessionPath = Path.joinpath(Path(__file__).parent.absolute(), 'tlgdb', 'leo123')  # change this last name to your session variable

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

tlg = TelegramClient(
    session=str(tlgSessionPath),
    api_id=c.api_id,
    api_hash=c.api_hash,
)

@tlg.on(events.NewMessage)
async def my_handler(update):
    """update properties:
        id
        reply_to_msg_id
        chat_id
        raw_text
        await update.get_chat()
        await update.get_sender()"""
    # chat = await update.get_chat()
    # sender = await update.get_sender()
    print(f'chat_id: {update.chat_id}')
    print(f'id: {update.id}')
    print(f'msg: {update.raw_text}')
    print(f'is_channel: {update.is_channel}')
    print('-----------------')


@tlg.on(events.MessageDeleted)
async def delete_handler(update):
    # chat = await update.get_chat()
    # sender = await update.get_sender()
    # print(update.chat_id)
    # print(update.raw_text)
    # print('-----------------')
    print(f'chat_id: {update.chat_id}')
    print(f'is_channel: {update.is_channel}')
    for msg_id in update.deleted_ids:
        print('id: ', msg_id)
    print(update)
    print('-----------------')


try:
    phone = '+'
    print(f'escutando para o número: {phone}')
    tlg.start(phone)
    asyncio.get_event_loop().run_until_complete(main())
except KeyboardInterrupt:
    print('\nEvent removed and program finished.')
    tlg.remove_event_handler(my_handler)
