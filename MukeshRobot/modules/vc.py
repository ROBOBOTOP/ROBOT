from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

__mod_name__ = "ᴠᴄ ᴛᴏᴏʟs"

__help__ = """
**ᴠᴄ ᴛᴏᴏʟs**
๏ /startvc - sᴛᴀʀᴛ ᴛʜᴇ ᴠᴄ [ᴍᴀᴋᴇ sᴜʀᴇ ᴍᴜsɪᴄ ᴀssɪsɪᴛᴀɴᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ]
๏ /vcend - Eɴᴅ ᴛʜᴇ ᴠᴄ [ᴍᴀᴋᴇ sᴜʀᴇ ᴍᴜsɪᴄ ᴀssɪsɪᴛᴀɴᴛ ɪs ᴀɴ ᴀᴅᴍɪɴ ᴡɪᴛʜ ᴍᴀɴᴀɢᴇ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ ᴘᴇʀᴍɪssɪᴏɴ]
๏ /vclink - ɢᴇᴛ ᴠᴏɪᴄᴇᴄʜᴀᴛ ʟɪɴᴋ
๏ /vcmembers - Gᴇᴛ ᴍᴇᴍᴇʙᴇʀ ʟɪsᴛ ᴛʜᴀᴛ ɪs ɪɴ ᴠᴏɪᴄᴇ ᴄʜᴀᴛ .

"""
