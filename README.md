# telegram-tracker
Basic telegram tracker using telethon library that read all messages sent to logged user and save on a file

# Requirements
Python >= 3.6

# Configuration

`pip install requirements.txt`

1) First, config your own telegram API and writedown your API_HASH and API_ID:
https://my.telegram.org/auth

2) on tlg.py update those infos (API_HASH and API_ID) on it's fields over Telegram Object

3) run python tlg.py. Your log will be saved on log.txt

Keep in mind that each time you run, log.txt will be re-writed and that is the expected behavior. If you want to change that, change iqlogger.py option on openning

# Run

`python tlg.py`