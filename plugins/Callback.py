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


from pyrogram import Client
from pyrogram.types import CallbackQuery
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import os
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
store = int(os.environ.get("DB", ""))
reply_markup=InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="⚡️ Join My Update Channel", url="https://t.me/subin_works")
        ],
        [
            InlineKeyboardButton(text="👨🏼‍💻Developer", url="https://t.me/subinps"),
        ]
    ]
    )
@Client.on_callback_query()
async def cb_handler(client: Client, query: CallbackQuery):
    if query.from_user.id != query.message.reply_to_message.from_user.id:
        await query.answer(
            f"ചീള് പിള്ളേർസ് സ്വന്തമായി Request ചെയ്യാൻ പഠിക്കണം😒. ഇത് {query.message.reply_to_message.from_user.first_name} -ക്ക് കൊടുത്ത Reply ആണ്. നിനക്കുള്ളതല്ല.🙊\nSent /pdf by own.",
            show_alert=True
            )
        return
    await query.answer()
    reply_id=query.message.reply_to_message.message_id
    if query.data == "help":
        await query.message.edit(HELP, reply_markup=reply_markup)
    if query.data == "mtp":
        await query.message.edit_text(
            "**SELECT THE GROUP**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Group-I", callback_data="mtpgrp1"
                        ),
                        InlineKeyboardButton(
                            text="Group-II", callback_data="mtpgrp2"
                        ),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mainmenu")
                    ]
                    
                ]
            ),
        )
    elif query.data == "mtpgrp1":
        await query.message.edit(
            "**Select the Subject From Below**",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton(text="Accounting", callback_data="mtpacc"),
                ],
                [
                    InlineKeyboardButton(text="Corporate and Other Laws", callback_data="mtplaw"),
                ],
                [
                    InlineKeyboardButton(text="Cost and Management Accounting", callback_data="mtpcost"),
                ],
                [
                    InlineKeyboardButton(text="Taxation", callback_data="mtptax"),
                ],
                [
                    InlineKeyboardButton("◀️Back", "mtp")
                ]
                ]
            ),
        )
    elif query.data == "mtpgrp2":
        await query.message.edit(
            "**Select the Subject From Below**",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton(text="Advanced Accounting", callback_data="mtpadvacc"),
                ],
                [
                    InlineKeyboardButton(text="Auditing and Assurance", callback_data="mtpaudit"),
                ],
                [
                    InlineKeyboardButton(text="EIS & Strategic Management", callback_data="mtpeis"),
                ],
                [
                    InlineKeyboardButton(text="FM & Economics for Finance", callback_data="mtpfm"),
                ],
                [
                    InlineKeyboardButton("◀️Back", "mtp")
                ]
                ]
            ),
        )
    elif query.data =="mtpacc":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtpacc2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtpacc2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtpacc2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtpacc2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtpaccold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="mtplaw":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtplaw2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtplaw2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtplaw2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtplaw2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtplawold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="mtpcost":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtpcost2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtpcost2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtpcost2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtpcost2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtpcostold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="mtptax":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtptax2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtptax2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtptax2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtptax2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtptaxold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="mtpadvacc":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtpadvacc2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtpadvacc2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtpadvacc2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtpadvacc2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtpadvaccold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp2")
                    ]
                ]
            ),
        )
    elif query.data =="mtpaudit":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtpaudit2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtpaudit2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtpaudit2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtpaudit2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtpauditold")
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp2")
                    ]
                ]
            ),
        )
    elif query.data =="mtpeis":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtpeis2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtpeis2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtpeis2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtpeis2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtpeisold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp2")
                    ]
                ]
            ),
        )
    elif query.data =="mtpfm":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="mtpfm2018"),
                        InlineKeyboardButton(text="2019", callback_data="mtpfm2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="mtpfm2020"),
                        InlineKeyboardButton(text="2021", callback_data="mtpfm2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="mtpfmold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpgrp2")
                    ]
                ]
            ),
        )

    elif query.data =="mtpacc2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpacc2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpacc2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpacc2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpaccold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)

   
    elif query.data =="mtplaw2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtplaw2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtplaw2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtplaw2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtplawold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)

    elif query.data =="mtpcost2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpcost2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpcost2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpcost2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpcostold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)
    
    elif query.data =="mtptax2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtptax2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtptax2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtptax2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtptaxold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)

    elif query.data =="mtpadvacc2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpadvacc2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpadvacc2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpadvacc2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpadvaccold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=47)
    elif query.data =="mtpaudit2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpaudit2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpaudit2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpaudit2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpauditold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=47)
    elif query.data =="mtpeis2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpeis2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpeis2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpeis2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpeisold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=47)

    elif query.data =="mtpfm2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpfm2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpfm2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpfm2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="mtpfmold":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available!!")

    elif query.data == "rtp":
        await query.message.edit_text(
            "**SELECT THE GROUP**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Group-I", callback_data="rtpgrp1"
                        ),
                        InlineKeyboardButton(
                            text="Group-II", callback_data="rtpgrp2"
                        ),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mainmenu")
                    ]
                    
                ]
            ),
        )
    elif query.data == "rtpgrp1":
        await query.message.edit(
            "**Select the Subject From Below**",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton(text="Accounting", callback_data="rtpacc"),
                ],
                [
                    InlineKeyboardButton(text="Corporate and Other Laws", callback_data="rtplaw"),
                ],
                [
                    InlineKeyboardButton(text="Cost and Management Accounting", callback_data="rtpcost"),
                ],
                [
                    InlineKeyboardButton(text="Taxation", callback_data="rtptax"),
                ],
                [
                    InlineKeyboardButton("◀️Back", "rtp")
                ]
                ]
            ),
        )
    elif query.data == "rtpgrp2":
        await query.message.edit(
            "**Select the Subject From Below**",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton(text="Advanced Accounting", callback_data="rtpadvacc"),
                ],
                [
                    InlineKeyboardButton(text="Auditing and Assurance", callback_data="rtpaudit"),
                ],
                [
                    InlineKeyboardButton(text="EIS & Strategic Management", callback_data="rtpeis"),
                ],
                [
                    InlineKeyboardButton(text="FM & Economics for Finance", callback_data="rtpfm"),
                ],
                [
                    InlineKeyboardButton("◀️Back", "rtp")
                ]
                ]
            ),
        )
    elif query.data =="rtpacc":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtpacc2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtpacc2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtpacc2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtpacc2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtpaccold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="rtplaw":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtplaw2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtplaw2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtplaw2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtplaw2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtplawold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="rtpcost":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtpcost2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtpcost2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtpcost2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtpcost2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtpcostold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="rtptax":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtptax2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtptax2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtptax2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtptax2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtptaxold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp1")
                    ]
                ]
            ),
        )
    elif query.data =="rtpadvacc":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtpadvacc2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtpadvacc2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtpadvacc2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtpadvacc2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtpadvaccold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp2")
                    ]
                ]
            ),
        )
    elif query.data =="rtpaudit":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtpaudit2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtpaudit2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtpaudit2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtpaudit2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtpauditold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp2")
                    ]
                ]
            ),
        )
    elif query.data =="rtpeis":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtpeis2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtpeis2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtpeis2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtpeis2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtpeisold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp2")
                    ]
                ]
            ),
        )
    elif query.data =="rtpfm":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="rtpfm2018"),
                        InlineKeyboardButton(text="2019", callback_data="rtpfm2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="rtpfm2020"),
                        InlineKeyboardButton(text="2021", callback_data="rtpfm2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="rtpfmold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpgrp2")
                    ]
                ]
            ),
        )

    elif query.data =="rtpacc2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpacc2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpacc2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpacc2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpaccold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=2)

   
    elif query.data =="rtplaw2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtplaw2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtplaw2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtplaw2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtplaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtplawold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=4)

    elif query.data =="rtpcost2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpcost2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpcost2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpcost2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpcost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpcostold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=170)
    
    elif query.data =="rtptax2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtptax2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtptax2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtptax2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtptax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtptaxold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=6)

    elif query.data =="rtpadvacc2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpadvacc2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpadvacc2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpadvacc2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpadvaccold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=7)
    elif query.data =="rtpaudit2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpaudit2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpaudit2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpaudit2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpauditold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=83)
    elif query.data =="rtpeis2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpeis2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpeis2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpeis2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpeisold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=145)

    elif query.data =="rtpfm2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpfm2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpfm2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpfm2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "rtpfm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="rtpfmold":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available!!")

    elif query.data == "sa":
        await query.message.edit_text(
            "**SELECT THE GROUP**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Group-I", callback_data="sagrp1"
                        ),
                        InlineKeyboardButton(
                            text="Group-II", callback_data="sagrp2"
                        ),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "mainmenu")
                    ]
                    
                ]
            ),
        )
    elif query.data == "sagrp1":
        await query.message.edit(
            "**Select the Subject From Below**",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton(text="Accounting", callback_data="saacc"),
                ],
                [
                    InlineKeyboardButton(text="Corporate and Other Laws", callback_data="salaw"),
                ],
                [
                    InlineKeyboardButton(text="Cost and Management Accounting", callback_data="sacost"),
                ],
                [
                    InlineKeyboardButton(text="Taxation", callback_data="satax"),
                ],
                [
                    InlineKeyboardButton("◀️Back", "sa")
                ]
                ]
            ),
        )
    elif query.data == "sagrp2":
        await query.message.edit(
            "**Select the Subject From Below**",
            reply_markup=InlineKeyboardMarkup(
                [
                [
                    InlineKeyboardButton(text="Advanced Accounting", callback_data="saadvacc"),
                ],
                [
                    InlineKeyboardButton(text="Auditing and Assurance", callback_data="saaudit"),
                ],
                [
                    InlineKeyboardButton(text="EIS & Strategic Management", callback_data="saeis"),
                ],
                [
                    InlineKeyboardButton(text="FM & Economics for Finance", callback_data="safm"),
                ],
                [
                    InlineKeyboardButton("◀️Back", "sa")
                ]
                ]
            ),
        )
    elif query.data =="saacc":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="saacc2018"),
                        InlineKeyboardButton(text="2019", callback_data="saacc2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="saacc2020"),
                        InlineKeyboardButton(text="2021", callback_data="saacc2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="saaccold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp1")
                    ]
                ]
            ),
        )
    elif query.data =="salaw":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="salaw2018"),
                        InlineKeyboardButton(text="2019", callback_data="salaw2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="salaw2020"),
                        InlineKeyboardButton(text="2021", callback_data="salaw2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="salawold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp1")
                    ]
                ]
            ),
        )
    elif query.data =="sacost":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="sacost2018"),
                        InlineKeyboardButton(text="2019", callback_data="sacost2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="sacost2020"),
                        InlineKeyboardButton(text="2021", callback_data="sacost2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="sacostold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp1")
                    ]
                ]
            ),
        )
    elif query.data =="satax":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="satax2018"),
                        InlineKeyboardButton(text="2019", callback_data="satax2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="satax2020"),
                        InlineKeyboardButton(text="2021", callback_data="satax2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="sataxold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp1")
                    ]
                ]
            ),
        )
    elif query.data =="saadvacc":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="saadvacc2018"),
                        InlineKeyboardButton(text="2019", callback_data="saadvacc2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="saadvacc2020"),
                        InlineKeyboardButton(text="2021", callback_data="saadvacc2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="saadvaccold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp2")
                    ]
                ]
            ),
        )
    elif query.data =="saaudit":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="saaudit2018"),
                        InlineKeyboardButton(text="2019", callback_data="saaudit2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="saaudit2020"),
                        InlineKeyboardButton(text="2021", callback_data="saaudit2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="saauditold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp2")
                    ]
                ]
            ),
        )
    elif query.data =="saeis":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="saeis2018"),
                        InlineKeyboardButton(text="2019", callback_data="saeis2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="saeis2020"),
                        InlineKeyboardButton(text="2021", callback_data="saeis2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="saeisold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp2")
                    ]
                ]
            ),
        )
    elif query.data =="safm":
        await query.message.edit(
            "**SELECT THE YEAR**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="2018", callback_data="safm2018"),
                        InlineKeyboardButton(text="2019", callback_data="safm2019"),
                    ],
                    [
                        InlineKeyboardButton(text="2020", callback_data="safm2020"),
                        InlineKeyboardButton(text="2021", callback_data="safm2021"),
                    ],
                    [
                        InlineKeyboardButton(text="OLDER", callback_data="safmold"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sagrp2")
                    ]
                ]
            ),
        )

    elif query.data =="saacc2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saacc2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saacc2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saacc2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saaccold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=19)

   
    elif query.data =="salaw2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "salaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="salaw2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "salaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="salaw2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "salaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="salaw2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "salaw")
                    ]
                    
                ]
            ),
        )
    elif query.data =="salawold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=125)

    elif query.data =="sacost2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sacost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="sacost2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sacost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="sacost2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sacost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="sacost2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "sacost")
                    ]
                    
                ]
            ),
        )
    elif query.data =="sacostold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=169)
    
    elif query.data =="satax2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "satax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="satax2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "satax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="satax2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "satax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="satax2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "satax")
                    ]
                    
                ]
            ),
        )
    elif query.data =="sataxold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=187)

    elif query.data =="saadvacc2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saadvacc2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saadvacc2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saadvacc2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saadvacc")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saadvaccold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=203)
    elif query.data =="saaudit2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saaudit2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saaudit2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saaudit2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saaudit")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saauditold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=82)
    elif query.data =="saeis2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saeis2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saeis2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saeis2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "saeis")
                    ]
                    
                ]
            ),
        )
    elif query.data =="saeisold":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=144)

    elif query.data =="safm2018":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2018nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "safm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="safm2019":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2019nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "safm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="safm2020":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2020nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "safm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="safm2021":
        await query.message.edit(
            "**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2021nov"),
                    ],
                    [
                        InlineKeyboardButton("◀️Back", "safm")
                    ]
                    
                ]
            ),
        )
    elif query.data =="safmold":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available!!")
    
    
#DATABASE
##ACCOUNTS
    elif query.data =="saacc2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=11)
    
    elif query.data =="saacc2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=50)
    
    elif query.data =="saacc2020may":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available, since No exam conducted!!")
    
    elif query.data =="saacc2021may":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available at the moment.")
    
    elif query.data =="saacc2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=20)
    
    elif query.data =="saacc2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=12)

    elif query.data =="saacc2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=13)
    
    elif query.data =="saacc2021nov":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not Released Yet!!")


## LAW

    elif query.data =="salaw2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=85)
    
    elif query.data =="salaw2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=50)
    
    elif query.data =="salaw2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif query.data =="salaw2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif query.data =="salaw2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=89)
    
    elif query.data =="salaw2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=88)

    elif query.data =="salaw2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=87)
    
    elif query.data =="salaw2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)


##COST
    elif query.data =="sacost2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=151)
    
    elif query.data =="sacost2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=50)
    
    elif query.data =="sacost2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif query.data =="sacost2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif query.data =="sacost2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=153)
    
    elif query.data =="sacost2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=154)

    elif query.data =="sacost2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=152)
    
    elif query.data =="sacost2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

##TAX
    elif query.data =="satax2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=171)
    
    elif query.data =="satax2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=174)
    
    elif query.data =="satax2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="satax2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="satax2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=172)
    
    elif query.data =="satax2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=173)

    elif query.data =="satax2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)#NA
    
    elif query.data =="satax2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

#ADVANCED ACCOUNTING
    elif query.data =="saadvacc2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=190)
    
    elif query.data =="saadvacc2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif query.data =="saadvacc2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="saadvacc2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="saadvacc2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=193)
    
    elif query.data =="saadvacc2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=192)

    elif query.data =="saadvacc2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=191)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=258)
    
    elif query.data =="saadvacc2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

## AUDITING

    elif query.data =="saaudit2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=60)
    
    elif query.data =="saaudit2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif query.data =="saaudit2020may":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available since no exams conducted.")
    
    elif query.data =="saaudit2021may":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available since no exams conducted.")
    
    elif query.data =="saaudit2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=65)
    
    elif query.data =="saaudit2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=64)

    elif query.data =="saaudit2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=61)
    
    elif query.data =="saaudit2021nov":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not available since no exams conducted.")

##EIS
    elif query.data =="saeis2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=128)
    
    elif query.data =="saeis2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif query.data =="saeis2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="saeis2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="saeis2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=137)
    
    elif query.data =="saeis2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=129)

    elif query.data =="saeis2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=132)
    
    elif query.data =="saeis2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)


#FM and ECO
    elif query.data =="safm2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=213)
    
    elif query.data =="safm2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif query.data =="safm2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="safm2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif query.data =="safm2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=212)
    
    elif query.data =="safm2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=211)

    elif query.data =="safm2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=209)#NA
    
    elif query.data =="safm2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
##ACCOUNTS
    elif query.data =="rtpacc2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=18)
    
    elif query.data =="rtpacc2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=17)
    
    elif query.data =="rtpacc2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=40)
    
    elif query.data =="rtpacc2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=43)
    
    elif query.data =="rtpacc2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=14)
    
    elif query.data =="rtpacc2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif query.data =="rtpacc2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=42)
    
    elif query.data =="rtpacc2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=270)


## LAW

    elif query.data =="rtplaw2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=107)
    
    elif query.data =="rtplaw2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=105)
    
    elif query.data =="rtplaw2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=104)
    
    elif query.data =="rtplaw2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=84)
    
    elif query.data =="rtplaw2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=106)
    
    elif query.data =="rtplaw2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif query.data =="rtplaw2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=103)
    
    elif query.data =="rtplaw2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=272)


##COST
    elif query.data =="rtpcost2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=163)
    
    elif query.data =="rtpcost2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=168)
    
    elif query.data =="rtpcost2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=166)
    
    elif query.data =="rtpcost2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=167)
    
    elif query.data =="rtpcost2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=164)
    
    elif query.data =="rtpcost2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif query.data =="rtpcost2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=165)
    
    elif query.data =="rtpcost2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=273)

##TAX
    elif query.data =="rtptax2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=182)
    
    elif query.data =="rtptax2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=186)
    
    elif query.data =="rtptax2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=183)
    
    elif query.data =="rtptax2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=185)
    
    elif query.data =="rtptax2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=181)
    
    elif query.data =="rtptax2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif query.data =="rtptax2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=189)
    
    elif query.data =="rtptax2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=276)

#ADVANCED ACCOUNTING
    elif query.data =="rtpadvacc2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=205)
    
    elif query.data =="rtpadvacc2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=204)
    
    elif query.data =="rtpadvacc2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=201)
    
    elif query.data =="rtpadvacc2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=202)
    
    elif query.data =="rtpadvacc2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=189)
    
    elif query.data =="rtpadvacc2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif query.data =="rtpadvacc2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=200)
    
    elif query.data =="rtpadvacc2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=274)

## AUDITING

    elif query.data =="rtpaudit2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=79)
    
    elif query.data =="rtpaudit2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=78)
    
    elif query.data =="rtpaudit2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=80)
    
    elif query.data =="rtpaudit2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=63)
    
    elif query.data =="rtpaudit2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=62)
    
    elif query.data =="rtpaudit2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif query.data =="rtpaudit2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=81)
    
    elif query.data =="rtpaudit2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=271)

##EIS
    elif query.data =="rtpeis2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=141)
    
    elif query.data =="rtpeis2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=140)
    
    elif query.data =="rtpeis2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=142)
    
    elif query.data =="rtpeis2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=143)
    
    elif query.data =="rtpeis2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=135)
    
    elif query.data =="rtpeis2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif query.data =="rtpeis2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=136)
    
    elif query.data =="rtpeis2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=275)


#FM and ECO
    elif query.data =="rtpfm2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)#NA
    
    elif query.data =="rtpfm2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)#NA
    
    elif query.data =="rtpfm2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=221)
    
    elif query.data =="rtpfm2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=219)
    
    elif query.data =="rtpfm2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=222)
    
    elif query.data =="rtpfm2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif query.data =="rtpfm2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=220)
    
    elif query.data =="rtpfm2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=277)
    


#DATABASE

##ACCOUNTS
    elif query.data =="mtpacc2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=39)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=38)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
    
    elif query.data =="mtpacc2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=32)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=33)
    
    elif query.data =="mtpacc2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=22)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=21)
    
    elif query.data =="mtpacc2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=16)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=15)
    
    elif query.data =="mtpacc2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=34)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=35)
        
    
    elif query.data =="mtpacc2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=23)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=24)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=26)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=25)

    elif query.data =="mtpacc2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=28)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=27)
    
    elif query.data =="mtpacc2021nov":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not Released Yet")


## LAW

    elif query.data =="mtplaw2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=55)
    
    elif query.data =="mtplaw2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        
    
    elif query.data =="mtplaw2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=144)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=143)
    
    elif query.data =="mtplaw2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=262)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=261)
    
    elif query.data =="mtplaw2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif query.data =="mtplaw2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=147)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=148)

    elif query.data =="mtplaw2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=141)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=140)
    
    elif query.data =="mtplaw2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)


##COST
    elif query.data =="mtpcost2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=55)
    
    elif query.data =="mtpcost2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=161)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=162)
    
    elif query.data =="mtpcost2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=157)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=158)
    
    elif query.data =="mtpcost2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=239)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=140)
    
    elif query.data =="mtpcost2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif query.data =="mtpcost2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=159)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=160)

    elif query.data =="mtpcost2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=155)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=156)
    
    elif query.data =="mtpcost2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=240)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=239)

##TAX
    elif query.data =="mtptax2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=55)
    
    elif query.data =="mtptax2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
    
    elif query.data =="mtptax2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=178)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=177)
    
    elif query.data =="mtptax2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=241)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=242)
    
    elif query.data =="mtptax2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif query.data =="mtptax2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=176)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=175)

    elif query.data =="mtptax2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=180)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=179)
    
    elif query.data =="mtptax2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

#ADVANCED ACCOUNTING
    elif query.data =="mtpadvacc2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
        
    
    elif query.data =="mtpadvacc2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        
    
    elif query.data =="mtpadvacc2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=197)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=196)
    
    elif query.data =="mtpadvacc2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=254)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=255)
    
    elif query.data =="mtpadvacc2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    elif query.data =="mtpadvacc2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=198)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=199)

    elif query.data =="mtpadvacc2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=195)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=194)
    
    elif query.data =="mtpadvacc2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

## AUDITING

    elif query.data =="mtpaudit2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
    
    elif query.data =="mtpaudit2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=73)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=72)
    
    elif query.data =="mtpaudit2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=59)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=69)
    
    elif query.data =="mtpaudit2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=238)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=237)
    
    elif query.data =="mtpaudit2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=74)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=75)
    elif query.data =="mtpaudit2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=71)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=70)

    elif query.data =="mtpaudit2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=67)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=66)
    
    elif query.data =="mtpaudit2021nov":
        await client.send_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, text="Not yet released!!")

##EIS
    elif query.data =="mtpeis2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
    
    elif query.data =="mtpeis2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
    
    elif query.data =="mtpeis2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=130)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=131)
    
    elif query.data =="mtpeis2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=233)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=234)
    
    elif query.data =="mtpeis2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif query.data =="mtpeis2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=138)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=139)

    elif query.data =="mtpeis2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=133)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=134)
    
    elif query.data =="mtpeis2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)


#FM and ECO
    elif query.data =="mtpfm2018may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
    
    elif query.data =="mtpfm2019may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
    
    elif query.data =="mtpfm2020may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=215)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=216)
    
    elif query.data =="mtpfm2021may":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=236)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=235)
    
    elif query.data =="mtpfm2018nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif query.data =="mtpfm2019nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=263)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=264)
        

    elif query.data =="mtpfm2020nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=218)
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=217)
    
    elif query.data =="mtpfm2021nov":
        await client.copy_message(chat_id=query.message.chat.id, reply_to_message_id=reply_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    elif query.data == "mainmenu":
        await query.message.edit(
            text="Tell Me What You Want",
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


