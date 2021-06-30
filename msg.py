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

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

store = -1001154905882
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

async def message_handler(client, message, text):
    if text == "mtp":
        await message.reply_text(
            quote=True,
            text="**SELECT THE GROUP**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Group-I", callback_data="mtpgrp1"
                        ),
                        InlineKeyboardButton(
                            text="Group-II", callback_data="mtpgrp2"
                        ),
                    ]
                    
                ]
            ),
        )
    elif text == "mtpgrp1":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
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
                    InlineKeyboardButton(text="Taxation", callback_data="mtptax")
                ]
                ]
            ),
        )
    elif text == "mtpgrp2":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below** ",
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
                    InlineKeyboardButton(text="FM & Economics for Finance", callback_data="mtpfm")
                ],
                ]
            ),
        )
    elif text =="mtpacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="mtpaccold")
                    ]
                ]
            ),
        )
    elif text =="mtplaw":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="mtplawold")
                    ]
                ]
            ),
        )
    elif text =="mtpcost":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="mtpcostold")
                    ]
                ]
            ),
        )
    elif text =="mtptax":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="mtptaxold")
                    ]
                ]
            ),
        )
    elif text =="mtpadvacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="mtpadvaccold")
                    ]
                ]
            ),
        )
    elif text =="mtpaudit":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                    ]
                ]
            ),
        )
    elif text =="mtpeis":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="mtpeisold")
                    ]
                ]
            ),
        )
    elif text =="mtpfm":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="mtpfmold")
                    ]
                ]
            ),
        )

    elif text =="mtpacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpacc2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpaccold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)

   
    elif text =="mtplaw2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtplaw2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtplaw2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtplaw2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtplaw2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtplaw2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtplawold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)

    elif text =="mtpcost2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpcost2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpcost2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpcost2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpcost2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpcost2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpcostold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)
    
    elif text =="mtptax2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtptax2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtptax2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtptax2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtptax2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtptax2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtptaxold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=48)

    elif text =="mtpadvacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpadvacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpadvacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpadvacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpadvacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpadvacc2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpadvaccold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=47)
    elif text =="mtpaudit2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpaudit2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpaudit2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpaudit2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpaudit2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpaudit2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpauditold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=47)
    elif text =="mtpeis2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpeis2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpeis2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpeis2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpeis2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpeis2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpeisold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=47)

    elif text =="mtpfm2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpfm2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpfm2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpfm2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="mtpfm2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="mtpfm2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="mtpfmold":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available!!")

    elif text == "rtp":
        await message.reply_text(
            quote=True,
            text="**SELECT THE GROUP**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Group-I", callback_data="rtpgrp1"
                        ),
                        InlineKeyboardButton(
                            text="Group-II", callback_data="rtpgrp2"
                        ),
                    ]
                    
                ]
            ),
        )
    elif text == "rtpgrp1":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
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
                    InlineKeyboardButton(text="Taxation", callback_data="rtptax")
                ]
                ]
            ),
        )
    elif text == "rtpgrp2":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
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
                    InlineKeyboardButton(text="FM & Economics for Finance", callback_data="rtpfm")
                ]
                ]
            ),
        )
    elif text =="rtpacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtpaccold")
                    ]
                ]
            ),
        )
    elif text =="rtplaw":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtplawold")
                    ]
                ]
            ),
        )
    elif text =="rtpcost":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtpcostold")
                    ]
                ]
            ),
        )
    elif text =="rtptax":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtptaxold")
                    ]
                ]
            ),
        )
    elif text =="rtpadvacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtpadvaccold")
                    ]
                ]
            ),
        )
    elif text =="rtpaudit":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtpauditold")
                    ]
                ]
            ),
        )
    elif text =="rtpeis":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtpeisold")
                    ]
                ]
            ),
        )
    elif text =="rtpfm":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="rtpfmold")
                    ]
                ]
            ),
        )

    elif text =="rtpacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpacc2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpaccold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=2)

   
    elif text =="rtplaw2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtplaw2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtplaw2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtplaw2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtplaw2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtplaw2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtplawold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=4)

    elif text =="rtpcost2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpcost2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpcost2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpcost2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpcost2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpcost2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpcostold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=170)
    
    elif text =="rtptax2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtptax2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtptax2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtptax2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtptax2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtptax2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtptaxold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=6)

    elif text =="rtpadvacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpadvacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpadvacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpadvacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpadvacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpadvacc2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpadvaccold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=7)
    elif text =="rtpaudit2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpaudit2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpaudit2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpaudit2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpaudit2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpaudit2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpauditold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=83)
    elif text =="rtpeis2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpeis2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpeis2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpeis2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpeis2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpeis2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpeisold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=145)

    elif text =="rtpfm2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpfm2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpfm2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpfm2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="rtpfm2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="rtpfm2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="rtpfmold":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available!!")

    elif text == "sa":
        await message.reply_text(
            quote=True,
            text="**SELECT THE GROUP**ㅤㅤㅤㅤ",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            text="Group-I", callback_data="sagrp1"
                        ),
                        InlineKeyboardButton(
                            text="Group-II", callback_data="sagrp2"
                        ),
                    ]
                    
                ]
            ),
        )
    elif text == "sagrp1":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
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
                    InlineKeyboardButton(text="Taxation", callback_data="satax")
                ]
                ]
            ),
        )
    elif text == "sagrp2":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
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
                    InlineKeyboardButton(text="FM & Economics for Finance", callback_data="safm")
                ]
                ]
            ),
        )
    elif text =="saacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="saaccold")
                    ]
                ]
            ),
        )
    elif text =="salaw":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="salawold")
                    ]
                ]
            ),
        )
    elif text =="sacost":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="sacostold")
                    ]
                ]
            ),
        )
    elif text =="satax":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="sataxold")
                    ]
                ]
            ),
        )
    elif text =="saadvacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="saadvaccold")
                    ]
                ]
            ),
        )
    elif text =="saaudit":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="saauditold")
                    ]
                ]
            ),
        )
    elif text =="saeis":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="saeisold")
                    ]
                ]
            ),
        )
    elif text =="safm":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
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
                        InlineKeyboardButton(text="OLDER", callback_data="safmold")
                    ]
                ]
            ),
        )

    elif text =="saacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saacc2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saaccold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=19)

   
    elif text =="salaw2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="salaw2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="salaw2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="salaw2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="salaw2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="salaw2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="salawold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=4)

    elif text =="sacost2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="sacost2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="sacost2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="sacost2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="sacost2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="sacost2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="sacostold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=169)
    
    elif text =="satax2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="satax2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="satax2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="satax2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="satax2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="satax2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="sataxold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=6)

    elif text =="saadvacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saadvacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saadvacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saadvacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saadvacc2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saadvacc2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saadvaccold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=7)
    elif text =="saaudit2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saaudit2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saaudit2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saaudit2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saaudit2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saaudit2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saauditold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=82)
    elif text =="saeis2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saeis2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saeis2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saeis2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="saeis2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="saeis2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="saeisold":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=144)

    elif text =="safm2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2018may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2018nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="safm2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2019may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2019nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="safm2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2020may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2020nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="safm2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(text="MAY", callback_data="safm2021may"),
                        InlineKeyboardButton(text="NOVEMBER", callback_data="safm2021nov"),
                    ]
                    
                ]
            ),
        )
    elif text =="safmold":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available!!")
    
    
#DATABASE
##ACCOUNTS
    elif text =="saacc2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=11)
    
    elif text =="saacc2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=50)
    
    elif text =="saacc2020may":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available, since No exam conducted!!")
    
    elif text =="saacc2021may":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available at the moment.")
    
    elif text =="saacc2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=20)
    
    elif text =="saacc2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=12)

    elif text =="saacc2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=13)
    
    elif text =="saacc2021nov":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not Released Yet!!")


## LAW

    elif text =="salaw2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=85)
    
    elif text =="salaw2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=50)
    
    elif text =="salaw2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif text =="salaw2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif text =="salaw2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=89)
    
    elif text =="salaw2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=88)

    elif text =="salaw2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=87)
    
    elif text =="salaw2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)


##COST
    elif text =="sacost2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=151)
    
    elif text =="sacost2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=50)
    
    elif text =="sacost2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif text =="sacost2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)
    
    elif text =="sacost2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=153)
    
    elif text =="sacost2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=154)

    elif text =="sacost2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=152)
    
    elif text =="sacost2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

##TAX
    elif text =="satax2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=171)
    
    elif text =="satax2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=174)
    
    elif text =="satax2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="satax2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="satax2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=172)
    
    elif text =="satax2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=173)

    elif text =="satax2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)#NA
    
    elif text =="satax2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

#ADVANCED ACCOUNTING
    elif text =="saadvacc2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=190)
    
    elif text =="saadvacc2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif text =="saadvacc2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="saadvacc2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="saadvacc2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=193)
    
    elif text =="saadvacc2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=192)

    elif text =="saadvacc2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=191)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=258)
    
    elif text =="saadvacc2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

## AUDITING

    elif text =="saaudit2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=60)
    
    elif text =="saaudit2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif text =="saaudit2020may":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available since no exams conducted.")
    
    elif text =="saaudit2021may":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available since no exams conducted.")
    
    elif text =="saaudit2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=65)
    
    elif text =="saaudit2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=64)

    elif text =="saaudit2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=61)
    
    elif text =="saaudit2021nov":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not available since no exams conducted.")

##EIS
    elif text =="saeis2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=128)
    
    elif text =="saeis2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif text =="saeis2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="saeis2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="saeis2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=137)
    
    elif text =="saeis2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=129)

    elif text =="saeis2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=132)
    
    elif text =="saeis2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)


#FM and ECO
    elif text =="safm2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=213)
    
    elif text =="safm2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=49)
    
    elif text =="safm2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="safm2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    
    elif text =="safm2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=212)
    
    elif text =="safm2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=211)

    elif text =="safm2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=209)#NA
    
    elif text =="safm2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
##ACCOUNTS
    elif text =="rtpacc2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=18)
    
    elif text =="rtpacc2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=17)
    
    elif text =="rtpacc2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=40)
    
    elif text =="rtpacc2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=43)
    
    elif text =="rtpacc2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=14)
    
    elif text =="rtpacc2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif text =="rtpacc2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=42)
    
    elif text =="rtpacc2021nov":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not Yet Released!!")


## LAW

    elif text =="rtplaw2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=107)
    
    elif text =="rtplaw2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=105)
    
    elif text =="rtplaw2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=104)
    
    elif text =="rtplaw2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=84)
    
    elif text =="rtplaw2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=106)
    
    elif text =="rtplaw2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif text =="rtplaw2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=103)
    
    elif text =="rtplaw2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)


##COST
    elif text =="rtpcost2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=163)
    
    elif text =="rtpcost2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=168)
    
    elif text =="rtpcost2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=166)
    
    elif text =="rtpcost2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=167)
    
    elif text =="rtpcost2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=164)
    
    elif text =="rtpcost2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif text =="rtpcost2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=165)
    
    elif text =="rtpcost2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

##TAX
    elif text =="rtptax2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=182)
    
    elif text =="rtptax2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=186)
    
    elif text =="rtptax2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=183)
    
    elif text =="rtptax2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=185)
    
    elif text =="rtptax2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=181)
    
    elif text =="rtptax2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=56)

    elif text =="rtptax2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=189)
    
    elif text =="rtptax2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

#ADVANCED ACCOUNTING
    elif text =="rtpadvacc2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=205)
    
    elif text =="rtpadvacc2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=204)
    
    elif text =="rtpadvacc2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=201)
    
    elif text =="rtpadvacc2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=202)
    
    elif text =="rtpadvacc2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=189)
    
    elif text =="rtpadvacc2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif text =="rtpadvacc2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=200)
    
    elif text =="rtpadvacc2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

## AUDITING

    elif text =="rtpaudit2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=79)
    
    elif text =="rtpaudit2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=78)
    
    elif text =="rtpaudit2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=80)
    
    elif text =="rtpaudit2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=63)
    
    elif text =="rtpaudit2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=62)
    
    elif text =="rtpaudit2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif text =="rtpaudit2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=81)
    
    elif text =="rtpaudit2021nov":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not yet released!!")

##EIS
    elif text =="rtpeis2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=141)
    
    elif text =="rtpeis2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=140)
    
    elif text =="rtpeis2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=142)
    
    elif text =="rtpeis2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=143)
    
    elif text =="rtpeis2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=135)
    
    elif text =="rtpeis2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif text =="rtpeis2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=136)
    
    elif text =="rtpeis2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)


#FM and ECO
    elif text =="rtpfm2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)#NA
    
    elif text =="rtpfm2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)#NA
    
    elif text =="rtpfm2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=221)
    
    elif text =="rtpfm2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=219)
    
    elif text =="rtpfm2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=222)
    
    elif text =="rtpfm2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=57)

    elif text =="rtpfm2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=220)
    
    elif text =="rtpfm2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    


#DATABASE

##ACCOUNTS
    elif text =="mtpacc2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=39)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=38)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
    
    elif text =="mtpacc2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=32)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=33)
    
    elif text =="mtpacc2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=22)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=21)
    
    elif text =="mtpacc2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=16)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=15)
    
    elif text =="mtpacc2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=34)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=35)
        
    
    elif text =="mtpacc2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=23)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=24)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=26)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=25)

    elif text =="mtpacc2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=28)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=27)
    
    elif text =="mtpacc2021nov":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not Released Yet")


## LAW

    elif text =="mtplaw2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=55)
    
    elif text =="mtplaw2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        
    
    elif text =="mtplaw2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=144)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=143)
    
    elif text =="mtplaw2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=262)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=261)
    
    elif text =="mtplaw2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif text =="mtplaw2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=147)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=148)

    elif text =="mtplaw2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=141)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=140)
    
    elif text =="mtplaw2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=146)


##COST
    elif text =="mtpcost2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=55)
    
    elif text =="mtpcost2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=161)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=162)
    
    elif text =="mtpcost2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=157)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=158)
    
    elif text =="mtpcost2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=239)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=140)
    
    elif text =="mtpcost2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif text =="mtpcost2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=159)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=160)

    elif text =="mtpcost2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=155)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=156)
    
    elif text =="mtpcost2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=240)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=239)

##TAX
    elif text =="mtptax2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=53)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=55)
    
    elif text =="mtptax2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
    
    elif text =="mtptax2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=178)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=177)
    
    elif text =="mtptax2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=241)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=242)
    
    elif text =="mtptax2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif text =="mtptax2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=176)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=175)

    elif text =="mtptax2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=180)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=179)
    
    elif text =="mtptax2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

#ADVANCED ACCOUNTING
    elif text =="mtpadvacc2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
        
    
    elif text =="mtpadvacc2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        
    
    elif text =="mtpadvacc2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=197)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=196)
    
    elif text =="mtpadvacc2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=254)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=255)
    
    elif text =="mtpadvacc2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    elif text =="mtpadvacc2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=198)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=199)

    elif text =="mtpadvacc2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=195)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=194)
    
    elif text =="mtpadvacc2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)

## AUDITING

    elif text =="mtpaudit2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
    
    elif text =="mtpaudit2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=73)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=72)
    
    elif text =="mtpaudit2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=59)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=69)
    
    elif text =="mtpaudit2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=238)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=237)
    
    elif text =="mtpaudit2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=74)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=75)
    elif text =="mtpaudit2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=71)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=70)

    elif text =="mtpaudit2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=67)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=66)
    
    elif text =="mtpaudit2021nov":
        await client.send_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, text="Not yet released!!")

##EIS
    elif text =="mtpeis2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
    
    elif text =="mtpeis2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
    
    elif text =="mtpeis2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=130)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=131)
    
    elif text =="mtpeis2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=233)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=234)
    
    elif text =="mtpeis2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif text =="mtpeis2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=138)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=139)

    elif text =="mtpeis2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=133)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=134)
    
    elif text =="mtpeis2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)


#FM and ECO
    elif text =="mtpfm2018may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=52)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=54)
    
    elif text =="mtpfm2019may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=31)
    
    elif text =="mtpfm2020may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=215)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=216)
    
    elif text =="mtpfm2021may":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=236)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=235)
    
    elif text =="mtpfm2018nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=29)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=30)
    
    elif text =="mtpfm2019nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=263)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=264)
        

    elif text =="mtpfm2020nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=218)
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=217)
    
    elif text =="mtpfm2021nov":
        await client.copy_message(chat_id=message.chat.id, reply_to_message_id=message.message_id, reply_markup=reply_markup, from_chat_id=store, message_id=149)
    else:
        await message.reply_text(
            """Use proper syntax for requesting.
You have to use proper keywords to get the desired files.

<b>Available Files</b>
RTP(Keyword- rtp)
MTP(Keyword- mtp)
Suggested Answers(Keyword- sa)

<b>Available Subjects</b>
Accounts(Keyword - acc)
Business Laws, Ethics and Communication(Keyword- law)
Cost Accounting and Financial Management(Keyword- cost)
Taxation(Keyword- tax)
Advanced Accounting(Keyword- advacc)
Auditing and Assurance(Keyword- audit)
Enterprise Information Systems & Strategic Management(Keyword- eis)
Financial Management & Economics for Finance(Keyword- fm)

<b>Available Years</b>
2018(Keyword- 2018)
2019(Keyword- 2019)
2020(Keyword- 2020)
2021(Keyword- 2021)
IPCC Old Syllabus Papers 2013-2018(Keyword - old)

<b>Available Examination</b>
May Attempt(Keyword-may)
November Attempt(Keyword-nov)


You can combine these keywords as per your wish in proper syntax. That is <code>file|subject|year|exam</code>  
For example to get <i>"Accouting RTP MAY 2019"</i>, You have to use <code>/pdf rtpacc2019may</code>
Now to get all RTP of accounting, You have to use <code>/pdf rtpacc</code>
To get MTP of law for 2018 (Both attempt) - <code>/pdf mtplaw2018

Tip- To get MTP of all subjects in Group 1 = <code>/pdf mtpgrp1


Note: All the above are examples , Similarly you can combine keywords as you wish, like rtpgrp1, mtpgrp2, sagrp1, mtp, rtp, sa, rtpacc, mtpacc, salaw2021, etc..
            
"""
)
