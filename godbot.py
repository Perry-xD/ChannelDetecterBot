from telethon import TelegramClient as tg
import os
from telethon import events
from telethon.tl.types import (ChannelParticipantsAdmins, ChatAdminRights,
                               ChatBannedRights, MessageEntityMentionName,
                               MessageMediaPhoto)

from telethon.tl.functions.channels import (EditAdminRequest,
                                            EditBannedRequest,
                                            EditPhotoRequest)


API_ID = os.environ.get("API_ID")
API_HASH = os.environ.get("API_HASH")
BOT_TOKEN = os.environ.get("BOT_TOKEN")

god = tg("godboy", api_id=API_ID, api_hash=API_HASH).start(bot_token=BOT_TOKEN)

BANNED_RIGHTS = ChatBannedRights(
    until_date=None,
    view_messages=True,
    send_messages=True,
    send_media=True,
    send_stickers=True,
    send_gifs=True,
    send_games=True,
    send_inline=True,
    embed_links=True,
)

@god.on(events.ChatAction)
async def _(e):
  h = await e.message
  ee = await h.sender_id
  if h.is_channel:
    await e.client(EditBannedRequest(e.chat_id, ee, BANNED_RIGHTS))
    await god.send_message(e.chat_id, "**SOMEONE IS SENDING MESSAGE VIA CHANNEL I BANNED THAT SHIT**")
  else:
    await god.send_message(e.chat_id, "**I can't ban you. Why???**")

@god.on(events.NewMessage(pattern="/start"))
async def start(e):
  if e.is_private:
    await god.send_message(e.chat_id, "Aur Badhiya Bro??")
  else:
    pass

god.run_until_disconnected()
