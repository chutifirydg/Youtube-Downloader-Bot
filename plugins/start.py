from pyrogram import Client, Filters, StopPropagation, InlineKeyboardButton, InlineKeyboardMarkup


@Client.on_message(Filters.command(["start"]), group=-2)
async def start(client, message):
    # return
    joinButton = InlineKeyboardMarkup([
        [InlineKeyboardButton("Channel", url="https://t.me/aryan_bots")],
        [InlineKeyboardButton(
            "Report Bugs 😊", url="https://t.me/aryanvikash")]
    ])
    welcomed = f"Hey <b>{message.from_user.first_name}</b>\n
   >>> import datetime

>>> currentTime = datetime.datetime.now()

>>> currentTime.hour

0

>>> if currentTime.hour < 12:

...     print('Good morning.')

... elif 12 <= currentTime.hour < 18:

...     print('Good afternoon.')

... else:

...     print('Good evening.')

...

Good morning. /help for More info"
    await message.reply_text(welcomed, reply_markup=joinButton)
    raise StopPropagation
