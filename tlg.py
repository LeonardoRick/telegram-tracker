import sys
from telegram.client import Telegram
from iqlogger import Logger
from pathlib import Path
import tlg_constants

# CLASS just to test telegram
def tlgMsgHandler(update):
    # we want to process only text messages

    message_content = update['message']['content'].get('text', {})
    msg = message_content.get('text', '')
    chat_id = str(update['message']['chat_id'])
    print(f'chat Id: : {chat_id}\nmessage: {msg}')


constants = tlg_constants.TelegramConstants()

tlg: Telegram = Telegram(
    api_id=constants.api_id,
    api_hash=constants.api_hash,
    phone=constants.phone,
    database_encryption_key=constants.api_hash
)

sys.stdout = Logger(Path(__file__).parent.absolute())

tlg.login()  # connect to Telegram
tlg.add_message_handler(tlgMsgHandler)

tlg.idle()
