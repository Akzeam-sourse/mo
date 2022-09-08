import os
AKI_MONGO_HOST = os.environ.get('aki_mongo_host', "mongodb+srv://mhmd:mhmd@cluster0.knp5tug.mongodb.net/?retryWrites=true&w=majority")
BOT_TOKEN = os.environ.get('bot_token', "")