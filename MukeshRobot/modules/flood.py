from pyrogram import filters

from MukeshRobot import pbot
from MukeshRobot.utils.errors import capture_err
from MukeshRobot.modules.helper_funcs.misc import is_module_loaded

mod_name = "ғʟᴏᴏᴅ"

help = """
*Aɴᴛɪ Fʟᴏᴏᴅ
Usᴇʀ Cᴏᴍᴍᴀɴᴅs:
• /ғʟᴏᴏᴅ: ᴛᴏ ᴄʜᴇᴄᴋ ᴡᴇᴀᴛʜᴇʀ ᴛʜᴇ ɢʀᴏᴜᴘ ɪs ᴘʀᴏᴛᴇᴄᴛᴇᴅ ғʀᴏᴍ sᴘᴀᴍ ᴏʀ ɴᴏᴛ.

Aᴅᴍɪɴ ᴏɴʟʏ:
• /sᴇᴛғʟᴏᴏᴅ ᴏɴ/ᴏғғ: Tᴏ ᴀᴄᴛɪᴠᴀᴛᴇ ᴏʀ ᴅᴇᴀᴄᴛɪᴠᴀᴛᴇ ᴛʜᴇ ғʟᴏᴏᴅ ᴘʀᴏᴛᴇᴄᴛɪᴏɴ
• /ғʟᴏᴏᴅᴀᴄᴛɪᴏɴ: Tᴏ ᴄᴜsᴛᴏᴍɪᴢᴇ ᴛʜᴇ ғʟᴏᴏᴅ sᴇᴛᴛɪɴɢs.

Exᴀᴍᴘʟᴇ:
/sᴇᴛғʟᴏᴏᴅ ᴏɴ
"""
