import os

class Config:

    BOT_TOKEN=os.environ['BOT_TOKEN']

    API_HASH=os.environ['API_HASH']

    API_ID=int(os.environ['API_ID'])

    

    if not BOT_TOKEN:

        raise ValueError('BOT TOKEN not set')

    

    if not API_HASH:

        raise ValueError("API_HASH not set")

    if not API_ID:

        raise ValueError("API_ID not set")
