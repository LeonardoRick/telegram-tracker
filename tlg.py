import sys
from telegram.client import Telegram
from iqlogger import Logger
from pathlib import Path

# CLASS just to test telegram
def tlgMsgHandler(update):
    # we want to process only text messages

    message_content = update['message']['content'].get('text', {})
    rawSignal = message_content.get('text', '')
    chat_id = str(update['message']['chat_id'])
    print('chatid :' + chat_id)
    print(rawSignal)


tlg: Telegram = Telegram(
    api_id='1527871',
    api_hash='41e7458d0acf5e2d641af514b73e49ac',
    phone='+5511993774025',

    database_encryption_key='41e7458d0acf5e2d641af514b73e49ac'
)

sys.stdout = Logger(Path.joinpath(Path(__file__).parent.parent.absolute(), 'tlglogs'))

tlg.login()  # connect to Telegram
tlg.add_message_handler(tlgMsgHandler)


while True:
    pass
