# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24064094"))
API_HASH = getenv("API_HASH", "49ceca00ad75c0491a74093f6893626a")
BOT_TOKEN = getenv("BOT_TOKEN", "7631178531:AAHmlOGqq8ysC_J61oi23APsoVH9cRKOHew")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6969281500").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://savebot:RxxBfvkv1xnGsbPL@cluster0.9zpw7.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "")
CHANNEL_ID = int(getenv("CHANNEL_ID", "2269674003"))
