"""
редактирование описания туалета
"""

from telethon import events


# import json


@tlgbot.on(events.NewMessage(chats=tlgbot.settings.get_all_user_id(), pattern='/edit_toilet'))
async def add_toilet(event):
    await event.respond("Редактирование описания туалета.")