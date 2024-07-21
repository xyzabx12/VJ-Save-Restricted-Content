import os

#Bot token @Botfather
BOT_TOKEN = os.environ.get("BOT_TOKEN", "")

#Your API ID from my.telegram.org
API_ID = int(os.environ.get("API_ID", "24952505"))

#Your API Hash from my.telegram.org
API_HASH = os.environ.get("API_HASH", "dfb54d3d0b859d1d762aeea9a2660d59")

#Database 
DB_URI = os.environ.get("DB_URI", "mongodb+srv://sudarshanalokeshpunamiya:Ik01u3Xfx0R9izak@cluster0.t2ua2xm.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
