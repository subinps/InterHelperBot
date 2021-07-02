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

from pyrogram.types import ReplyKeyboardMarkup, KeyboardButton
from msg import message_handler

async def key_handler(client, message, text):
    if "back" in text:
        text=text.replace("↩️back ", "")
        text=text.replace("(", "")
        text=text.replace(")", "")

    if " " in text:
        text = text.replace(' ', "")

    if text == "mtp":
        await message.reply_text(
            quote=True,
            text="**SELECT THE GROUP**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(
                            text="MTP GRP 1"
                        ),
                        KeyboardButton(
                            text="MTP  GRP 2"
                        ),
                        
                    ],
                    [
                        KeyboardButton(text="↩️Back (Main Menu)")
                    ]
                    
                ]
            ),
        )
    elif text == "mtpgrp1":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                [
                    KeyboardButton(text="MTP Acc "),
                    KeyboardButton(text="MTP Law "),
                ],
                [
                    KeyboardButton(text="MTP Cost "),
                    KeyboardButton(text="MTP Tax "),
                ],
                [
                    KeyboardButton(text="↩️Back (MTP)")
                ]
                ]
            ),
        )
    elif text == "mtpgrp2":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below** ",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                [
                    KeyboardButton(text="MTP Adv Acc "),
                    KeyboardButton(text="MTP Audit "),
                ],
                [
                    KeyboardButton(text="MTP EIS "),
                    KeyboardButton(text="MTP FM "),
                ],
                [
                    KeyboardButton(text="↩️Back (MTP)")
                ]
                ]
            ),
        )
    elif text =="mtpacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Acc 2018"),
                        KeyboardButton(text="MTP Acc 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP Acc 2020"),
                        KeyboardButton(text="MTP Acc 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP Acc Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 1)")
                    ]
                ]
            ),
        )
    elif text =="mtplaw":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Law 2018"),
                        KeyboardButton(text="MTP Law 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP Law 2020"),
                        KeyboardButton(text="MTP Law 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP Law Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 1)")
                    ]
                ]
            ),
        )
    elif text =="mtpcost":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Cost 2018"),
                        KeyboardButton(text="MTP Cost 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP Cost 2020"),
                        KeyboardButton(text="MTP Cost 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP Cost Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 1)")
                    ]
                ]
            ),
        )
    elif text =="mtptax":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Tax 2018"),
                        KeyboardButton(text="MTP Tax 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP Tax 2020"),
                        KeyboardButton(text="MTP Tax 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP Tax Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 1)")
                    ]
                ]
            ),
        )
    elif text =="mtpadvacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Adv Acc 2018"),
                        KeyboardButton(text="MTP Adv Acc 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP Adv Acc 2020"),
                        KeyboardButton(text="MTP Adv Acc 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP Adv Acc Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 2)")
                    ]
                ]
            ),
        )
    elif text =="mtpaudit":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Audit 2018"),
                        KeyboardButton(text="MTP Audit 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP Audit 2020"),
                        KeyboardButton(text="MTP Audit 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP Audit Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 2)")
                    ]
                ]
            ),
        )
    elif text =="mtpeis":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP EIS 2018"),
                        KeyboardButton(text="MTP EIS 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP EIS 2020"),
                        KeyboardButton(text="MTP EIS 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP EIS Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 2)")
                    ]
                ]
            ),
        )
    elif text =="mtpfm":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP FM 2018"),
                        KeyboardButton(text="MTP FM 2019"),
                    ],
                    [
                        KeyboardButton(text="MTP FM 2020"),
                        KeyboardButton(text="MTP FM 2021"),
                    ],
                    [
                        KeyboardButton(text="MTP FM Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP GRP 2)")
                    ]
                ]
            ),
        )

    elif text =="mtpacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Acc 2018 May"),
                        KeyboardButton(text="MTP Acc 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Acc 2019 May"),
                        KeyboardButton(text="MTP Acc 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Acc 2020 May"),
                        KeyboardButton(text="MTP Acc 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Acc 2021 May"),
                        KeyboardButton(text="MTP Acc 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Acc)")
                    ]
                    
                ]
            ),
        )
   
    elif text =="mtplaw2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Law 2018 May"),
                        KeyboardButton(text="MTP Law 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Law)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtplaw2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Law 2019 May"),
                        KeyboardButton(text="MTP Law 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Law)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtplaw2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Law 2020 May"),
                        KeyboardButton(text="MTP Law 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Law)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtplaw2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Law 2021 May"),
                        KeyboardButton(text="MTP Law 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Law)")
                    ]
                    
                ]
            ),
        )


    elif text =="mtpcost2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Cost 2018 May"),
                        KeyboardButton(text="MTP Cost 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Cost)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpcost2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Cost 2019 May"),
                        KeyboardButton(text="MTP Cost 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Cost)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpcost2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Cost 2020 May"),
                        KeyboardButton(text="MTP Cost 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Cost)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpcost2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Cost 2021 May"),
                        KeyboardButton(text="MTP Cost 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Cost)")
                    ]
                    
                ]
            ),
        )

    
    elif text =="mtptax2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Tax 2018 May"),
                        KeyboardButton(text="MTP Tax 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Tax)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtptax2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Tax 2019 May"),
                        KeyboardButton(text="MTP Tax 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Tax)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtptax2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Tax 2020 May"),
                        KeyboardButton(text="MTP Tax 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Tax)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtptax2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Tax 2021 May"),
                        KeyboardButton(text="MTP Tax 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Tax)")
                    ]
                    
                ]
            ),
        )


    elif text =="mtpadvacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Adv Acc 2018 May"),
                        KeyboardButton(text="MTP Adv Acc 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Adv Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpadvacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Adv Acc 2019 May"),
                        KeyboardButton(text="MTP Adv Acc 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Adv Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpadvacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Adv Acc 2020 May"),
                        KeyboardButton(text="MTP Adv Acc 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Adv Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpadvacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Adv Acc 2021 May"),
                        KeyboardButton(text="MTP Adv Acc 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Adv Acc)")
                    ]
                    
                ]
            ),
        )

    elif text =="mtpaudit2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Audit 2018 May"),
                        KeyboardButton(text="MTP Audit 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Audit)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpaudit2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Audit 2019 May"),
                        KeyboardButton(text="MTP Audit 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Audit)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpaudit2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Audit 2020 May"),
                        KeyboardButton(text="MTP Audit 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Audit)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpaudit2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP Audit 2021 May"),
                        KeyboardButton(text="MTP Audit 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP Audit)")
                    ]
                    
                ]
            ),
        )

    elif text =="mtpeis2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP EIS 2018 May"),
                        KeyboardButton(text="MTP EIS 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP EIS)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpeis2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP EIS 2019 May"),
                        KeyboardButton(text="MTP EIS 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP EIS)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpeis2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP EIS 2020 May"),
                        KeyboardButton(text="MTP EIS 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP EIS)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpeis2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP EIS 2021 May"),
                        KeyboardButton(text="MTP EIS 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP EIS)")
                    ]
                    
                ]
            ),
        )

    elif text =="mtpfm2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP FM 2018 May"),
                        KeyboardButton(text="MTP FM 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP FM)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpfm2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP FM 2019 May"),
                        KeyboardButton(text="MTP FM 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP FM)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpfm2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP FM 2020 May"),
                        KeyboardButton(text="MTP FM 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP FM)")
                    ]
                    
                ]
            ),
        )
    elif text =="mtpfm2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="MTP FM 2021 May"),
                        KeyboardButton(text="MTP FM 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (MTP FM)")
                    ]
                    
                ]
            ),
        )

    elif text == "rtp":
        await message.reply_text(
            quote=True,
            text="**SELECT THE GROUP**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(
                            text="RTP Grp 1"
                        ),
                        KeyboardButton(
                            text="RTP Grp 2"
                        ),
                    ],
                    [
                        KeyboardButton(text="↩️Back (Main Menu)")
                    ]

                    
                    
                ]
            ),
        )
    elif text == "rtpgrp1":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                [
                    KeyboardButton(text="RTP Acc "),
                    KeyboardButton(text="RTP Law "),
                ],
                [
                    KeyboardButton(text="RTP Cost "),
                    KeyboardButton(text="RTP Tax "),
                ],
                [
                    KeyboardButton(text="↩️Back (RTP)")
                ]
                ]
            ),
        )
    elif text == "rtpgrp2":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                [
                    KeyboardButton(text="RTP Adv Acc "),
                    KeyboardButton(text="RTP Audit "),
                ],
                [
                    KeyboardButton(text="RTP EIS "),
                    KeyboardButton(text="RTP FM "),
                ],
                [
                    KeyboardButton(text="↩️Back (RTP)")
                ]
                ]
            ),
        )
    elif text =="rtpacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Acc 2018"),
                        KeyboardButton(text="RTP Acc 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP Acc 2020"),
                        KeyboardButton(text="RTP Acc 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP Acc Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 1)")
                    ]
                    
                ]
            ),
        )
    elif text =="rtplaw":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Law 2018"),
                        KeyboardButton(text="RTP Law 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP Law 2020"),
                        KeyboardButton(text="RTP Law 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP Law Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 1)")
                    ]
                ]
            ),
        )
    elif text =="rtpcost":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Cost 2018"),
                        KeyboardButton(text="RTP Cost 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP Cost 2020"),
                        KeyboardButton(text="RTP Cost 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP Cost Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 1)")
                    ]
                ]
            ),
        )
    elif text =="rtptax":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Tax 2018"),
                        KeyboardButton(text="RTP Tax 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP Tax 2020"),
                        KeyboardButton(text="RTP Tax 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP Tax Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 1)")
                    ]
                ]
            ),
        )
    elif text =="rtpadvacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Adv Acc 2018"),
                        KeyboardButton(text="RTP Adv Acc 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP Adv Acc 2020"),
                        KeyboardButton(text="RTP Adv Acc 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP Adv Acc Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 2)")
                    ]
                ]
            ),
        )
    elif text =="rtpaudit":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Audit 2018"),
                        KeyboardButton(text="RTP Audit 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP Audit 2020"),
                        KeyboardButton(text="RTP Audit 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP Audit Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 2)")
                    ]
                ]
            ),
        )
    elif text =="rtpeis":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP EIS 2018"),
                        KeyboardButton(text="RTP EIS 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP EIS 2020"),
                        KeyboardButton(text="RTP EIS 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP EIS Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 2)")
                    ]
                ]
            ),
        )
    elif text =="rtpfm":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP FM 2018"),
                        KeyboardButton(text="RTP FM 2019"),
                    ],
                    [
                        KeyboardButton(text="RTP FM 2020"),
                        KeyboardButton(text="RTP FM 2021"),
                    ],
                    [
                        KeyboardButton(text="RTP FM Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Grp 2)")
                    ]
                ]
            ),
        )

    elif text =="rtpacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Acc 2018 May"),
                        KeyboardButton(text="RTP Acc 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Acc)")
                    ]                 
                ]
            ),
        )
    elif text =="rtpacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Acc 2019 May"),
                        KeyboardButton(text="RTP Acc 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Acc)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Acc 2020 May"),
                        KeyboardButton(text="RTP Acc 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Acc)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Acc 2021 May"),
                        KeyboardButton(text="RTP Acc 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Acc)")
                    ] 
                    
                ]
            ),
        )
   
    elif text =="rtplaw2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Law 2018 May"),
                        KeyboardButton(text="RTP Law 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Law)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtplaw2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Law 2019 May"),
                        KeyboardButton(text="RTP Law 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Law)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtplaw2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Law 2020 May"),
                        KeyboardButton(text="RTP Law 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Law)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtplaw2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Law 2021 May"),
                        KeyboardButton(text="RTP Law 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Law)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpcost2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Cost 2018 May"),
                        KeyboardButton(text="RTP Cost 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Cost)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpcost2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Cost 2019 May"),
                        KeyboardButton(text="RTP Cost 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Cost)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpcost2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Cost 2020 May"),
                        KeyboardButton(text="RTP Cost 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Cost)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpcost2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Cost 2021 May"),
                        KeyboardButton(text="RTP Cost 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Cost)")
                    ] 
                    
                ]
            ),
        )
    
    elif text =="rtptax2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Tax 2018 May"),
                        KeyboardButton(text="RTP Tax 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Tax)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtptax2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Tax 2019 May"),
                        KeyboardButton(text="RTP Tax 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Tax)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtptax2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Tax 2020 May"),
                        KeyboardButton(text="RTP Tax 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Tax)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtptax2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Tax 2021 May"),
                        KeyboardButton(text="RTP Tax 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Tax)")
                    ] 
                    
                ]
            ),
        )
   

    elif text =="rtpadvacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Adv Acc 2018 May"),
                        KeyboardButton(text="RTP Adv Acc 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Adv Acc)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpadvacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Adv Acc 2019 May"),
                        KeyboardButton(text="RTP Adv Acc 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Adv Acc)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpadvacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Adv Acc 2020 May"),
                        KeyboardButton(text="RTP Adv Acc 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Adv Acc)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpadvacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Adv Acc 2021 May"),
                        KeyboardButton(text="RTP Adv Acc 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Adv Acc)")
                    ] 
                    
                ]
            ),
        )
  
    elif text =="rtpaudit2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Audit 2018 May"),
                        KeyboardButton(text="RTP Audit 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Audit)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpaudit2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Audit 2019 May"),
                        KeyboardButton(text="RTP Audit 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Audit)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpaudit2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Audit 2020 May"),
                        KeyboardButton(text="RTP Audit 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Audit)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpaudit2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP Audit 2021 May"),
                        KeyboardButton(text="RTP Audit 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP Audit)")
                    ] 
                    
                ]
            ),
        )
   
    elif text =="rtpeis2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP EIS 2018 May"),
                        KeyboardButton(text="RTP EIS 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP EIS)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpeis2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP EIS 2019 May"),
                        KeyboardButton(text="RTP EIS 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP EIS)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpeis2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP EIS 2020 May"),
                        KeyboardButton(text="RTP EIS 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP EIS)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpeis2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP EIS 2021 May"),
                        KeyboardButton(text="RTP EIS 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP EIS)")
                    ] 
                    
                ]
            ),
        )
   

    elif text =="rtpfm2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP FM 2018 May"),
                        KeyboardButton(text="RTP FM 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP FM)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpfm2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP FM 2019 May"),
                        KeyboardButton(text="RTP FM 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP FM)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpfm2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP FM 2020 May"),
                        KeyboardButton(text="RTP FM 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP FM)")
                    ] 
                    
                ]
            ),
        )
    elif text =="rtpfm2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="RTP FM 2021 May"),
                        KeyboardButton(text="RTP FM 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (RTP FM)")
                    ] 
                    
                ]
            ),
        )
    

    elif text == "sa":
        await message.reply_text(
            quote=True,
            text="**SELECT THE GROUP**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(
                            text="SA Grp 1"
                        ),
                        KeyboardButton(
                            text="SA Grp 2"
                        ),
                    ],
                    [
                        KeyboardButton(text="↩️Back (Main Menu)")
                    ] 
                    
                ]
            ),
        )
    elif text == "sagrp1":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                [
                    KeyboardButton(text="SA Acc "),
                    KeyboardButton(text="SA Law "),
                ],
                [
                    KeyboardButton(text="SA Cost "),
                    KeyboardButton(text="SA Tax "),
                ],
                [
                    KeyboardButton(text="↩️Back (SA)")
                ]
                ]
            ),
        )
    elif text == "sagrp2":
        await message.reply_text(
            quote=True,
            text="**Select the Subject From Below**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                [
                    KeyboardButton(text="SA Adv Acc "),
                    KeyboardButton(text="SA Audit "),
                ],
                [
                    KeyboardButton(text="SA EIS "),
                    KeyboardButton(text="SA FM "),
                ],
                [
                    KeyboardButton(text="↩️Back (SA)")
                ]
                ]
            ),
        )
    elif text =="saacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Acc 2018"),
                        KeyboardButton(text="SA Acc 2019"),
                    ],
                    [
                        KeyboardButton(text="SA Acc 2020"),
                        KeyboardButton(text="SA Acc 2021"),
                    ],
                    [
                        KeyboardButton(text="SA Acc Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 1)")
                    ]
                ]
            ),
        )
    elif text =="salaw":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Law 2018"),
                        KeyboardButton(text="SA Law 2019"),
                    ],
                    [
                        KeyboardButton(text="SA Law 2020"),
                        KeyboardButton(text="SA Law 2021"),
                    ],
                    [
                        KeyboardButton(text="SA Law Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 1)")
                    ]
                ]
            ),
        )
    elif text =="sacost":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Cost 2018"),
                        KeyboardButton(text="SA Cost 2019"),
                    ],
                    [
                        KeyboardButton(text="SA Cost 2020"),
                        KeyboardButton(text="SA Cost 2021"),
                    ],
                    [
                        KeyboardButton(text="SA Cost Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 1)")
                    ]
                ]
            ),
        )
    elif text =="satax":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Tax 2018"),
                        KeyboardButton(text="SA Tax 2019"),
                    ],
                    [
                        KeyboardButton(text="SA Tax 2020"),
                        KeyboardButton(text="SA Tax 2021"),
                    ],
                    [
                        KeyboardButton(text="SA Tax Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 1)")
                    ]
                ]
            ),
        )
    elif text =="saadvacc":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Adv Acc 2018"),
                        KeyboardButton(text="SA Adv Acc 2019"),
                    ],
                    [
                        KeyboardButton(text="SA Adv Acc 2020"),
                        KeyboardButton(text="SA Adv Acc 2021"),
                    ],
                    [
                        KeyboardButton(text="SA Adv Acc Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 2)")
                    ]
                ]
            ),
        )
    elif text =="saaudit":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Audit 2018"),
                        KeyboardButton(text="SA Audit 2019"),
                    ],
                    [
                        KeyboardButton(text="SA Audit 2020"),
                        KeyboardButton(text="SA Audit 2021"),
                    ],
                    [
                        KeyboardButton(text="SA Audit Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 2)")
                    ]
                ]
            ),
        )
    elif text =="saeis":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA EIS 2018"),
                        KeyboardButton(text="SA EIS 2019"),
                    ],
                    [
                        KeyboardButton(text="SA EIS 2020"),
                        KeyboardButton(text="SA EIS 2021"),
                    ],
                    [
                        KeyboardButton(text="SA EIS Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 2)")
                    ]
                ]
            ),
        )
    elif text =="safm":
        await message.reply_text(
            quote=True,
            text="**SELECT THE YEAR**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA FM 2018"),
                        KeyboardButton(text="SA FM 2019"),
                    ],
                    [
                        KeyboardButton(text="SA FM 2020"),
                        KeyboardButton(text="SA FM 2021"),
                    ],
                    [
                        KeyboardButton(text="SA FM Old"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Grp 2)")
                    ]
                ]
            ),
        )

    elif text =="saacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Acc 2018 May"),
                        KeyboardButton(text="SA Acc 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="saacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Acc 2019 May"),
                        KeyboardButton(text="SA Acc 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="saacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Acc 2020 May"),
                        KeyboardButton(text="SA Acc 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="saacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Acc 2021 May"),
                        KeyboardButton(text="SA Acc 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Acc)")
                    ]
                    
                ]
            ),
        )
    

   
    elif text =="salaw2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Law 2018 May"),
                        KeyboardButton(text="SA Law 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Law)")
                    ]
                    
                ]
            ),
        )
    elif text =="salaw2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Law 2019 May"),
                        KeyboardButton(text="SA Law 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Law)")
                    ]
                    
                ]
            ),
        )
    elif text =="salaw2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Law 2020 May"),
                        KeyboardButton(text="SA Law 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Law)")
                    ]
                    
                ]
            ),
        )
    elif text =="salaw2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Law 2021 May"),
                        KeyboardButton(text="SA Law 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Law)")
                    ]
                    
                ]
            ),
        )

    elif text =="sacost2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Cost 2018 May"),
                        KeyboardButton(text="SA Cost 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Cost)")
                    ]
                    
                ]
            ),
        )
    elif text =="sacost2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Cost 2019 May"),
                        KeyboardButton(text="SA Cost 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Cost)")
                    ]
                    
                ]
            ),
        )
    elif text =="sacost2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Cost 2020 May"),
                        KeyboardButton(text="SA Cost 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Cost)")
                    ]
                    
                ]
            ),
        )
    elif text =="sacost2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Cost 2021 May"),
                        KeyboardButton(text="SA Cost 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Cost)")
                    ]
                    
                ]
            ),
        )

    
    elif text =="satax2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Tax 2018 May"),
                        KeyboardButton(text="SA Tax 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Tax)")
                    ]
                    
                ]
            ),
        )
    elif text =="satax2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Tax 2019 May"),
                        KeyboardButton(text="SA Tax 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Tax)")
                    ]
                    
                ]
            ),
        )
    elif text =="satax2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Tax 2020 May"),
                        KeyboardButton(text="SA Tax 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Tax)")
                    ]
                    
                ]
            ),
        )
    elif text =="satax2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Tax 2021 May"),
                        KeyboardButton(text="SA Tax 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Tax)")
                    ]
                    
                ]
            ),
        )


    elif text =="saadvacc2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Adv Acc 2018 May"),
                        KeyboardButton(text="SA Adv Acc 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Adv Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="saadvacc2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Adv Acc 2019 May"),
                        KeyboardButton(text="SA Adv Acc 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Adv Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="saadvacc2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Adv Acc 2020 May"),
                        KeyboardButton(text="SA Adv Acc 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Adv Acc)")
                    ]
                    
                ]
            ),
        )
    elif text =="saadvacc2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Adv Acc 2021 May"),
                        KeyboardButton(text="SA Adv Acc 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Adv Acc)")
                    ]
                    
                ]
            ),
        )

    elif text =="saaudit2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Audit 2018 May"),
                        KeyboardButton(text="SA Audit 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Audit)")
                    ]
                    
                ]
            ),
        )
    elif text =="saaudit2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Audit 2019 May"),
                        KeyboardButton(text="SA Audit 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Audit)")
                    ]
                    
                ]
            ),
        )
    elif text =="saaudit2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Audit 2020 May"),
                        KeyboardButton(text="SA Audit 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Audit)")
                    ]
                    
                ]
            ),
        )
    elif text =="saaudit2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA Audit 2021 May"),
                        KeyboardButton(text="SA Audit 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA Audit)")
                    ]
                    
                ]
            ),
        )
    elif text =="saeis2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA EIS 2018 May"),
                        KeyboardButton(text="SA EIS 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA EIS)")
                    ]
                    
                ]
            ),
        )
    elif text =="saeis2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA EIS 2019 May"),
                        KeyboardButton(text="SA EIS 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA EIS)")
                    ]
                    
                ]
            ),
        )
    elif text =="saeis2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA EIS 2020 May"),
                        KeyboardButton(text="SA EIS 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA EIS)")
                    ]
                    
                ]
            ),
        )
    elif text =="saeis2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA EIS 2021 May"),
                        KeyboardButton(text="SA EIS 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA EIS)")
                    ]
                    
                ]
            ),
        )


    elif text =="safm2018":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA FM 2018 May"),
                        KeyboardButton(text="SA FM 2018 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA FM)")
                    ]
                    
                ]
            ),
        )
    elif text =="safm2019":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA FM 2019 May"),
                        KeyboardButton(text="SA FM 2019 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA FM)")
                    ]
                    
                ]
            ),
        )
    elif text =="safm2020":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA FM 2020 May"),
                        KeyboardButton(text="SA FM 2020 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA FM)")
                    ]
                    
                ]
            ),
        )
    elif text =="safm2021":
        await message.reply_text(
            quote=True,
            text="**SELECT THE EXAM**",
            reply_markup=ReplyKeyboardMarkup(
                resize_keyboard=True,
                keyboard=
                [
                    [
                        KeyboardButton(text="SA FM 2021 May"),
                        KeyboardButton(text="SA FM 2021 Nov"),
                    ],
                    [
                        KeyboardButton(text="↩️Back (SA FM)")
                    ]
                    
                ]
            ),
        )
    elif text == "mainmenu":
        await message.reply_text(
            quote=True,
            text="**Tell Me What You Want?**",
            reply_markup=ReplyKeyboardMarkup(
                [
                [
                    KeyboardButton("RTP"),
                ],
                [
                    KeyboardButton("MTP")
                ],
                [
                    KeyboardButton("SA"),
                ]
                ],
                resize_keyboard=True
                ),
            
        )
    else:
        await message_handler(client, message, text)

