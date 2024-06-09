"""
BSD 2-Clause License

Copyright (C) 2017-2019, Paul Larsen
Copyright (C) 2021-2022, Awesome-RJ, [ https://github.com/Awesome-RJ ]
Copyright (c) 2021-2022, Yūki • Black Knights Union, [ https://github.com/Awesome-RJ/CutiepiiRobot ]

All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this
   list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice,
   this list of conditions and the following disclaimer in the documentation
   and/or other materials provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import asyncio
import datetime

from telethon.tl import functions, types
from MukeshRobot.events import register
from MukeshRobot import telethn

@register(pattern="^/ss (.*)")
async def alive(event):
    if event.is_group and not await is_register_admin(event.input_chat,
                                                      event.message.sender_id):
        return
    sender = await event.get_sender()
    fname = sender.first_name
    ok = event.pattern_match.group(1)
    k = await event.reply("**Wait for Result.**")
    async with ubot.conversation("@Carol5_bot") as bot_conv:
        await bot_conv.send_message(f"/ss {ok}")
        await asyncio.sleep(9)
        response = await bot_conv.get_response()
        if "Try again after" in response.text:
            await k.edit(response)
            return
        if "Your date is invalid" in response.text:
            await k.edit("Format Wrong or invalid cc.")
            return
        res = response.text
        text = f"{res.splitlines()[0]}\n"
        text += f"{res.splitlines()[1]}\n"
        text += f"{res.splitlines()[2]}\n"
        text += f"{res.splitlines()[3]}\n"
        text += f"{res.splitlines()[4]}\n"
        text += f"{res.splitlines()[5]}\n"
        text += f"{res.splitlines()[6]}\n"
        text += f"Checked By **{fname}**"
        await k.edit(text)


@register(pattern="^/pp (.*)")
async def alive(event):
    if event.is_group and not await is_register_admin(event.input_chat,
                                                      event.message.sender_id):
        return
    sender = await event.get_sender()
    fname = sender.first_name
    ok = event.pattern_match.group(1)
    k = await event.reply("**Wait for Result.**")
    async with ubot.conversation("@Carol5_bot") as bot_conv:
        await bot_conv.send_message(f"/pp {ok}")
        await asyncio.sleep(14)
        response = await bot_conv.get_response()
        if "Try again after" in response.text:
            await k.edit(response)
            return
        if "Your date is invalid" in response.text:
            await k.edit("Format Wrong or invalid cc.")
            return
        res = response.text
        text = f"{res.splitlines()[0]}\n"
        text += f"{res.splitlines()[1]}\n"
        text += f"{res.splitlines()[2]}\n"
        text += f"{res.splitlines()[3]}\n"
        text += f"{res.splitlines()[4]}\n"
        text += f"{res.splitlines()[5]}\n"
        text += f"{res.splitlines()[6]}\n"
        text += f"Checked By **{fname}**"
        await k.edit(text)


@register(pattern="^/ch (.*)")
async def alive(event):
    if event.is_group and not await is_register_admin(event.input_chat,
                                                      event.message.sender_id):
        return
    sender = await event.get_sender()
    fname = sender.first_name
    ok = event.pattern_match.group(1)
    async with ubot.conversation("@Carol5_bot") as bot_conv:
        await bot_conv.send_message(f"/ch {ok}")
        k = await event.reply("**Wait for Result.**")
        await asyncio.sleep(18)
        response = await bot_conv.get_response()
        if "Try again after" in response.text:
            await k.edit(response)
            return
        if "Your date is invalid" in response.text:
            await k.edit("Format Wrong or invalid cc.")
            return
        res = response.text
        text = f"{res.splitlines()[0]}\n"
        text += f"{res.splitlines()[1]}\n"
        text += f"{res.splitlines()[2]}\n"
        text += f"{res.splitlines()[3]}\n"
        text += f"{res.splitlines()[4]}\n"
        text += f"{res.splitlines()[5]}\n"
        text += f"{res.splitlines()[6]}\n"
        text += f"Checked By **{fname}**"
        await k.edit(text)


@register(pattern="^/au (.*)")
async def alive(event):
    if event.is_group and not await is_register_admin(event.input_chat,
                                                      event.message.sender_id):
        return
    sender = await event.get_sender()
    fname = sender.first_name
    ok = event.pattern_match.group(1)
    async with ubot.conversation("@Carol5_bot") as bot_conv:
        await bot_conv.send_message(f"/au {ok}")
        k = await event.reply("**Wait for Result.**")
        await asyncio.sleep(18)
        response = await bot_conv.get_response()
        if "Try again after" in response.text:
            await event.reply(response)
            return
        if "Your date is invalid" in response.text:
            await event.reply("Format Wrong or invalid cc.")
            return
        res = response.text
        text = f"{res.splitlines()[0]}\n"
        text += f"{res.splitlines()[1]}\n"
        text += f"{res.splitlines()[2]}\n"
        text += f"{res.splitlines()[3]}\n"
        text += f"{res.splitlines()[4]}\n"
        text += f"{res.splitlines()[5]}\n"
        text += f"{res.splitlines()[6]}\n"
        text += f"Checked By **{fname}**"
        await k.edit(text)


@register(pattern="^/bin (.*)")
async def alive(event):
    if event.is_group and not await is_register_admin(event.input_chat,
                                                      event.message.sender_id):
        return
    sender = await event.get_sender()
    fname = sender.first_name
    k = await event.reply("**Wait for Result.**")
    ok = event.pattern_match.group(1)
    async with ubot.conversation("@Carol5_bot") as bot_conv:
        await bot_conv.send_message(f"/bin {ok}")
        await asyncio.sleep(5)
        response = await bot_conv.get_response()
        res = response.text
        if "❌" in res:
            text = "🤬❌ INVALID BIN ❌🤬\n"
        else:
            text = f"{res.splitlines()[0]}\n"
            text += f"{res.splitlines()[1]}\n"
            text += f"{res.splitlines()[2]}\n"
            text += f"{res.splitlines()[3]}\n"
            text += f"{res.splitlines()[4]}\n"
            text += f"{res.splitlines()[5]}\n"
            text += f"{res.splitlines()[6]}\n"

        text += f"Checked By **{fname}**"
        await k.edit(text)
