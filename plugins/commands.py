#   Copyright [2021] [SUBIN]

#   Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0

#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.

import os
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from msg import message_handler
from ReplyKeyBoard import key_handler
UPDATES_CHANNEL=int(os.environ.get("UPDATE_CHANNEL", ""))
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nThis is a simple bot by [SUBIN](tg://user?id=626664225) written in Python to Search RTP, MTP, and SUGGESTED ANSWERS for CA Intermediate students.\n\nWith this bot you can get all Question papers released by ICAI(RTP, MTP, Suggested Answers.) from</b> <code>2013-2020</code>.\n<b>Use /help to Know How to use the bot.\n\nFeel Free to report any bug if found any or any missing Question Papers to my [Deleloper](tg://user?id=626664225)</b>"
HELP=""" You can ask any file by using <code>/pdf keyword </code>


You have to use proper keywords to get the desired files.

<b>Available Files</b>
<i>RTP(Keyword- rtp)
MTP(Keyword- mtp)
Suggested Answers(Keyword- sa)</i>

<b>Available Subjects</b>
<i>Accounts(Keyword - acc)
Business Laws, Ethics and Communication(Keyword- law)
Cost Accounting and Financial Management(Keyword- cost)
Taxation(Keyword- tax)
Advanced Accounting(Keyword- advacc)
Auditing and Assurance(Keyword- audit)
Enterprise Information Systems & Strategic Management(Keyword- eis)
Financial Management & Economics for Finance(Keyword- fm)</i>

<b>Available Years</b>
<i>2018(Keyword- 2018)
2019(Keyword- 2019)
2020(Keyword- 2020)
2021(Keyword- 2021)
IPCC Old Syllabus Papers 2013-2018(Keyword - old)</i>

<b>Available Examination</b>
<i>May Attempt(Keyword-may)
November Attempt(Keyword-nov)</i>


You can combine these keywords as per your wish in proper syntax. That is <code>file|subject|year|exam</code>  

For example to get <i>"Accouting RTP MAY 2019"</i>, You have to use <code>/pdf rtpacc2019may</code>

Now to get all RTP of accounting, You have to use <code>/pdf rtpacc</code>

To get MTP of law for 2018 (Both attempt) - <code>/pdf mtplaw2018</code>


Tip- To get MTP of all subjects in Group 1 = <code>/pdf mtpgrp1</code>


Note: All the above are examples , Similarly you can combine keywords as you wish, like rtpgrp1, mtpgrp2, sagrp1, mtp, rtp, sa, rtpacc, mtpacc, salaw2021, etc..
            
"""
int(os.environ.get("DB", ""))
buttons=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="🧩 Join My Update Channel", url="https://t.me/subin_works"),
            InlineKeyboardButton(text="👨🏼‍💻 Developer", url="https://t.me/subinps"),
        ]
    ]
    )
@Client.on_message(filters.command(["start", "start@InterHelperBot"]))
async def start(client, cmd): 
  await cmd.reply(
    HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
    quote=True,
    disable_web_page_preview=True,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("👨🏼‍🦯How To Use", callback_data="help"),
        ],
        [
          InlineKeyboardButton("🧩 Join My Update Channel", url="https://t.me/subin_works"),
          InlineKeyboardButton("🤖 More Useful Bots", url="https://t.me/subin_works/122")
        ],
        [
          InlineKeyboardButton("👨🏼‍💻Developer", url="https://t.me/subinps"),
        ],
      ]
    )
  )
  if cmd.chat.type == "private":
    await key_handler(client, cmd, "mainmenu")

@Client.on_message(filters.command(["pdf", "pdf@InterHelperBot"]))
async def msg(client, cmd):
  nav=cmd.text
  nav = nav.replace('/pdf', "")
  if " " in nav:
    try:
      nav = nav.replace(' ', "")
    except ValueError:
      await cmd.reply(
        text="😢Sorry I Cannot Match That.\nPlease Use Proper Syntax For Requesting Files\nUse /help To Know How To Use Proper KeyWords.\n\nTell Me What You Want",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
          [
            [
              InlineKeyboardButton("RTP", callback_data="rtp"),
              InlineKeyboardButton("MTP", callback_data="mtp")
            ],
            [
              InlineKeyboardButton("SUGGESTED ANSWERS", callback_data="sa"),
            ]
          ]
        )
      )
      return
  if "/" in nav:
    try:
      nav = nav.replace('/', "")
    except ValueError:
      await cmd.reply(
        text="😢Sorry I Cannot Match That.\nPlease Use Proper Syntax For Requesting Files\nUse /help To Know How To Use Proper KeyWords.\n\nTell Me What You Want",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
          [
            [
              InlineKeyboardButton("RTP", callback_data="rtp"),
              InlineKeyboardButton("MTP", callback_data="mtp")
            ],
            [
              InlineKeyboardButton("SUGGESTED ANSWERS", callback_data="sa"),
            ]
          ]
        )
      )
      return
  nav = nav.lower().strip().rstrip()
  await message_handler(client, cmd, nav)
  
  if cmd.chat.type != "supergroup":
    invite_link = "https://t.me/subin_works"
    try:
      user = await client.get_chat_member(int(UPDATES_CHANNEL), cmd.from_user.id)
      if user.status == "kicked":
        await cmd.reply(
          text="Sorry Sir, You are Banned to use me.",
          parse_mode="markdown",
          quote=True,
          disable_web_page_preview=True
          )
        return
    except UserNotParticipant:
      await cmd.reply(
        text="**Please Consider Joining My Update Channel to get the latest updates on my Projects.**\n\nThat Count Of Subscribers are the only motivation for me to make similar bots.",
        reply_markup=InlineKeyboardMarkup(
          [
            [
              InlineKeyboardButton("🤖Join Updates Channel", url=invite_link)
            ]
          ]
        ),
        quote=True,
        parse_mode="markdown"
      )
      return
    except Exception:
      await cmd.reply(
        text="Something went Wrong.",
        parse_mode="markdown",
        quote=True,
        disable_web_page_preview=True
        )
      return
  


@Client.on_message(filters.command(["help", "help@InterHelperBot"]))
async def help(client, cmd):
  await cmd.reply_text(HELP, reply_markup=buttons)



@Client.on_message(filters.text & filters.private & filters.incoming)
async def mssssg(client, cmd):
  nav=cmd.text
  if "/" in nav:
    try:
      nav = nav.replace('/', "")
    except ValueError:
      await cmd.reply(
        text="😢Sorry I Cannot Match That.\nPlease Use Proper Syntax For Requesting Files\nUse /help To Know How To Use Proper KeyWords.\n\nTell Me What You Want",
        parse_mode="Markdown",
        disable_web_page_preview=True,
        quote=True,
        reply_markup=InlineKeyboardMarkup(
          [
            [
              InlineKeyboardButton("RTP", callback_data="rtp"),
              InlineKeyboardButton("MTP", callback_data="mtp")
            ],
            [
              InlineKeyboardButton("SUGGESTED ANSWERS", callback_data="sa"),
            ]
          ]
        )
      )
      return
  nav = nav.lower().strip().rstrip()
  await key_handler(client, cmd, nav)
  
  if cmd.chat.type != "supergroup":
    invite_link = "https://t.me/subin_works"
    try:
      user = await client.get_chat_member(int(UPDATES_CHANNEL), cmd.from_user.id)
      if user.status == "kicked":
        await cmd.reply(
          text="Sorry Sir, You are Banned to use me.",
          parse_mode="markdown",
          quote=True,
          disable_web_page_preview=True
          )
        return
    except UserNotParticipant:
      await cmd.reply(
        text="**Please Consider Joining My Update Channel to get the latest updates on my Projects.**\n\nThat Count Of Subscribers are the only motivation for me to make similar bots.",
        reply_markup=InlineKeyboardMarkup(
          [
            [
              InlineKeyboardButton("🤖Join Updates Channel", url=invite_link)
            ]
          ]
        ),
        quote=True,
        parse_mode="markdown"
      )
      return
    except Exception:
      await cmd.reply(
        text="Something went Wrong.",
        parse_mode="markdown",
        quote=True,
        disable_web_page_preview=True
        )
      return
  
