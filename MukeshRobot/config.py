
class Config(object):
    LOGGER = True
    # REQUIRED
    # Login to https://my.telegram.org and fill in these slots with the details given by it

    API_ID = "27383453"
    API_HASH = "4c246fb0c649477cc2e79b6a178ddfaa"
    TOKEN = "7436017266:AAEDHTYLMCd5EismewzemzKr-PJg5lr42Ks"
    OWNER_ID = "6898413162"
    
    SUPPORT_CHAT = "PBX_PERMOT"
    START_IMG = "https://te.legra.ph/file/9b504719e85ac6b88933e.jpg"
    EVENT_LOGS = ()  # Prints information like gbans, sudo promotes, AI enabled disable states that may help in debugging and shit
    MONGO_DB_URI= "mongodb+srv://BADMUNDA:BADMYDAD@badhacker.i5nw9na.mongodb.net"
    # RECOMMENDED
    BOT_USERNAME ="BrokenRobot_Bot"
    DATABASE_URL ="postgres://iarfggbc:Vxzh_kG7cxa1kHR5faxcd1kuA4R-UT9E@rosie.db.elephantsql.com/iarfggbc"
    CASH_API_KEY = "LO45IQSSY1TI8B1U"
    
    TIME_API_KEY = "3RV16TWH8JT9"

    # Optional fields
    BL_CHATS = [-1002093247039]  # List of groups that you want blacklisted.
    DRAGONS = [6898413162]  # User id of sudo users
    DEV_USERS = [6898413162]  # User id of dev users
    DEMONS = [6898413162    ]  # User id of support users
    TIGERS = [6898413162]  # User id of tiger users
    WOLVES = [6898413162]  # User id of whitelist users

    ALLOW_CHATS = True
    ALLOW_EXCL = True
    DEL_CMDS = True
    INFOPIC = True
    LOAD = []
    NO_LOAD = []
    STRICT_GBAN = True
    TEMP_DOWNLOAD_DIRECTORY = "./"
    WORKERS = 8
    

class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
