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


from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from msg import message_handler

UPDATES_CHANNEL=-1001228162868
DB_CHANNEL = -1001154905882
HOME_TEXT = "<b>Helo, [{}](tg://user?id={})\n\nThis is a simple bot by [SUBIN](tg://user?id=626664225) written in Python to Search RTP, MTP, and SUGGESTED ANSWERS for CA Intermediate students.\n\nWith this bot you can get all Question papers released by ICAI(RTP, MTP, Suggested Answers.) from </b> <code>2013-2020</code>.\n<b>Use /help to Know How to use the bot.\n\nFeel Free to report any bug if found any or any missing Question Papers to my [Deleloper](tg://user?id=626664225)</b>"
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
store = -1001154905882
buttons=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="🧩 Join My Update Channel", url="https://t.me/subin_works"),
            InlineKeyboardButton(text="👨🏼‍💻 Developer", url="https://t.me/subinps"),
        ]
    ]
    )
@Client.on_message(filters.command(["start", "start@InterHelperBot"]) & filters.private)
async def start(client, cmd):
  await cmd.reply(
    HOME_TEXT.format(cmd.from_user.first_name, cmd.from_user.id),
    parse_mode="Markdown",
    quote=True,
    disable_web_page_preview=True,
    reply_markup=InlineKeyboardMarkup(
      [
        [
          InlineKeyboardButton("How To Use", callback_data="help"),
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

@Client.on_message(filters.command(["pdf", "pdf@InterHelperBot"]))
async def msg(client, cmd):
  if UPDATES_CHANNEL:
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
        text="**Please Join My Updates Channel to use this Bot and to get the latest updates on my Projects.**\n\nOnly Channel Subscribers can acces the files saved in Database!",
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
  if " " in cmd.text:
    try:
      a, nav = cmd.text.split(' ')
    except ValueError:
      await cmd.reply_text("Please Use the proper syntax, Use /help to know how to use.")
      return
    await message_handler(client, cmd, nav)
  else:
    await cmd.reply(
      "Tell Me What You Want",
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


@Client.on_message(filters.command(["help", "help@InterHelperBot"]))
async def help(client, cmd):
  await cmd.reply_text(HELP, reply_markup=buttons)
