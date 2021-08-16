"""
удаление туалета
"""

from telethon import events


# import json


@tlgbot.on(events.NewMessage(chats=tlgbot.settings.get_all_user_id(), pattern='/deltoilet'))
async def del_toilet(event):
    await event.respond("Удаление туалета.")
