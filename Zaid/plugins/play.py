from pytgcalls import StreamType
from pytgcalls.types import Update
from pytgcalls.types.input_stream import AudioPiped, AudioVideoPiped
from pytgcalls.types.input_stream.quality import (
    HighQualityAudio,
    HighQualityVideo,
    LowQualityVideo,
    MediumQualityVideo,
)
import random
from telethon.tl.functions.channels import LeaveChannelRequest
from telethon.tl.functions.messages import ImportChatInviteRequest
from telethon.tl.functions.messages import ExportChatInviteRequest

from Zaid import random_assistant
from pytgcalls.exceptions import (
    NoActiveGroupCall,
    NotInGroupCallError
)
from Zaid.status import *
from telethon.tl.functions.users import GetFullUserRequest
from telethon.tl.functions.messages import ExportChatInviteRequest
import telethon.utils
from telethon.tl import functions
from telethon.tl import types
from telethon.utils import get_display_name
from telethon.tl.functions.users import GetFullUserRequest
from youtubesearchpython import VideosSearch

 
fotoplay = "https://telegra.ph/file/b6402152be44d90836339.jpg"
ngantri = "https://telegra.ph/file/b6402152be44d90836339.jpg"
from Zaid import call_py, call_py2, call_py3, call_py4, call_py5, Zaid, client as cli1, client2, client3, client4, client5
owner = "1669178360"
from Zaid.helpers.yt_dlp import bash
from Zaid.helpers.chattitle import CHAT_TITLE
from Zaid.helpers.queues import (
    QUEUE,
    add_to_queue,
    clear_queue,
    get_queue,
    pop_an_item,
)
from Zaid.Database.clientdb import *
from telethon import Button, events
import Config

from Zaid.helpers.thumbnail import gen_thumb


def vcmention(user):
    full_name = get_display_name(user)
    if not isinstance(user, types.User):
        return full_name
    return f"[{full_name}](tg://user?id={user.id})"


def ytsearch(query):
    try:
        search = VideosSearch(query, limit=1).result()
        data = search["result"][0]
        songname = data["title"]
        url = data["link"]
        duration = data["duration"]
        thumbnail = f"https://i.ytimg.com/vi/{data['id']}/hqdefault.jpg"
        return [songname, url, duration, thumbnail]
    except Exception as e:
        print(e)
        return 0


async def ytdl(format: str, link: str):
    stdout, stderr = await bash(f'yt-dlp -g -f "{format}" {link}')
    if stdout:
        return 1, stdout.split("\n")[0]
    return 0, stderr


async def skip_item(chat_id: int, x: int):
    if chat_id not in QUEUE:
        return 0
    chat_queue = get_queue(chat_id)
    try:
        songname = chat_queue[x][0]
        chat_queue.pop(x)
        return songname
    except Exception as e:
        print(e)
        return 0


async def skip_current_song(chat_id: int):
    if chat_id not in QUEUE:
        return 0
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    chat_queue = get_queue(chat_id)
    if len(chat_queue) == 1:
        if int(assistant) == 1:
           await call_py.leave_group_call(chat_id)
        if int(assistant) == 2:
           await call_py2.leave_group_call(chat_id)
        if int(assistant) == 3:
           await call_py3.leave_group_call(chat_id)
        if int(assistant) == 4:
           await call_py4.leave_group_call(chat_id)
        if int(assistant) == 5:
           await call_py5.leave_group_call(chat_id)
        if int(assistant) == 6:
           await call_py.leave_group_call(chat_id)
        clear_queue(chat_id)
        return 1
    songname = chat_queue[1][0]
    url = chat_queue[1][1]
    link = chat_queue[1][2]
    type = chat_queue[1][3]
    RESOLUSI = chat_queue[1][4]
    if type == "Audio":
        if int(assistant) == 1:
           await call_py.change_stream(
               chat_id,
               AudioPiped(
                   url,
               ),
           )
        if int(assistant) == 2:
           await call_py2.change_stream(
               chat_id,
               AudioPiped(
                   url,
               ),
           )
        if int(assistant) == 3:
           await call_py3.change_stream(
               chat_id,
               AudioPiped(
                   url,
               ),
           )
        if int(assistant) == 4:
           await call_py4.change_stream(
               chat_id,
               AudioPiped(
                   url,
               ),
           )
        if int(assistant) == 5:
           await call_py5.change_stream(
               chat_id,
               AudioPiped(
                   url,
               ),
           )
        if int(assistant) == 6:
           await call_py.change_stream(
               chat_id,
               AudioPiped(
                   url,
               ),
           )
    elif type == "Video":
        if RESOLUSI == 720:
            hm = HighQualityVideo()
        elif RESOLUSI == 480:
            hm = MediumQualityVideo()
        elif RESOLUSI == 360:
            hm = LowQualityVideo()
        if int(assistant) == 1:
           await call_py.change_stream(
               chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
           )
        if int(assistant) == 2:
           await call_py2.change_stream(
               chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
           )
        if int(assistant) == 3:
           await call_py3.change_stream(
               chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
           )
        if int(assistant) == 4:
           await call_py4.change_stream(
               chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
           )
        if int(assistant) == 5:
           await call_py5.change_stream(
               chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
           )
        if int(assistant) == 6:
           await call_py.change_stream(
               chat_id, AudioVideoPiped(url, HighQualityAudio(), hm)
           )
    pop_an_item(chat_id)
    return [songname, link, type]


@Zaid.on(events.callbackquery.CallbackQuery(data="cls"))
async def _(event):

     await event.delete()

btnn =[
    [Button.url("💁 Sᴜᴘᴘᴏʀᴛ", url=f"t.me/{Config.SUPPORT}"), Button.url("Cʜᴀɴɴᴇʟ 🙋", url=f"t.me/{Config.CHANNEL}")],
    [Button.inline("Cʟᴏꜱᴇ 🗑️", data="cls")]]


#play
@Zaid.on(events.NewMessage(pattern="^[?!/]play"))
async def play(event):
    title = ' '.join(event.text[5:])
    replied = await event.get_reply_message()
    sender = await event.get_sender()
    chat = await event.get_chat()
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    link = await Zaid(ExportChatInviteRequest(event.chat_id))
    _assistant = await get_assistant(chat_id, "assistant")
    if not _assistant:
        ran_ass = random.choice(random_assistant)
        assis = {
            "saveassistant": ran_ass,
        }
        await save_assistant(chat_id, "assistant", assis)
    else:
        ran_ass = _assistant["saveassistant"]
    assistant = _assistant['saveassistant']
    if assistant:
        try:
            if int(assistant) == 1:
               await cli1(ImportChatInviteRequest(link.link))
            if int(assistant) == 2:
               await client2(ImportChatInviteRequest(link.link))
            if int(assistant) == 3:
               await client3(ImportChatInviteRequest(link.link))
            if int(assistant) == 4:
               await client4(ImportChatInviteRequest(link.link))
            if int(assistant) == 5:
               await client5(ImportChatInviteRequest(link.link))
            if int(assistant) == 6:
               await cli1(ImportChatInviteRequest(link.link))
        except Exception as e:
            print(e)
            pass
    if (
        replied
        and not replied.audio
        and not replied.voice
        and not title
        or not replied
        and not title
    ):
        return await event.client.send_file(chat_id, Config.CMD_IMG, caption="**Give Me Your Query Which You want to Play**\n\n **Example**: `/play Nira Ishq Bass boosted`", buttons=btnn)
    elif replied and not replied.audio and not replied.voice or not replied:
        botman = await event.reply("`Featching Details...`")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        if search == 0:
            await botman.edit(
                "**Can't Find Song** Try searching with More Specific Title"
            )    
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            userid = sender.id
            titlegc = chat.title
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, userid, ctitle)
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await botman.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                caption = f"💡 **Song Added To queue »** `#{pos}`\n\n**🏷 Name:** [{songname}]({url})\n**⏱ Duration:** `{duration}`\n🎧 **Requester:** {from_user}"
                await botman.delete()
                await event.client.send_file(chat_id, thumb, caption=caption, buttons=btnn)
            else:
                try:
                    if int(assistant) == 1:
                       await call_py.join_group_call(
                           chat_id,
                           AudioPiped(
                               ytlink,
                           ),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 2:
                       await call_py2.join_group_call(
                           chat_id,
                           AudioPiped(
                               ytlink,
                           ),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 3:
                       await call_py3.join_group_call(
                           chat_id,
                           AudioPiped(
                               ytlink,
                           ),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 4:
                       await call_py4.join_group_call(
                           chat_id,
                           AudioPiped(
                               ytlink,
                           ),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 5:
                       await call_py5.join_group_call(
                           chat_id,
                           AudioPiped(
                               ytlink,
                           ),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 6:
                       await call_py.join_group_call(
                           chat_id,
                           AudioPiped(
                               ytlink,
                           ),
                           stream_type=StreamType().pulse_stream,
                       )
                    add_to_queue(chat_id, songname, ytlink, url, "Audio", 0)
                    caption = f"🏷 **Name:** [{songname}]({url})\n**⏱ Duration:** `{duration}`\n💡 **Status:** `Playing`\n🎧 **Requester:** {from_user}"
                    await botman.delete()
                    await event.client.send_file(chat_id, thumb, caption=caption, buttons=btnn)
                except Exception as ep:
                    clear_queue(chat_id)
                    await botman.edit(f"`{ep}`")

    else:
        botman = await event.reply("📥 **Downloading**")
        dl = await replied.download_media()
        link = f"https://t.me/c/{chat.id}/{event.reply_to_msg_id}"
        if replied.audio:
            songname = "Telegram Music Player"
        elif replied.voice:
            songname = "Voice Note"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Audio", 0)
            caption = f"💡 **Song Added To queue »** `#{pos}`\n\n**🏷 Title:** [{songname}]({link})\n**👥 Chat ID:** `{chat_id}`\n🎧 **Requester:** {from_user}"
            await event.client.send_file(chat_id, ngantri, caption=caption, buttons=btnn)
            await botman.delete()
        else:
            try:
                if int(assistant) == 1:
                   await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                if int(assistant) == 2:
                   await call_py2.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                if int(assistant) == 3:
                   await call_py3.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                if int(assistant) == 4:
                   await call_py4.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                if int(assistant) == 5:
                   await call_py5.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                if int(assistant) == 6:
                   await call_py.join_group_call(
                        chat_id,
                        AudioPiped(
                            dl,
                        ),
                        stream_type=StreamType().pulse_stream,
                    )
                add_to_queue(chat_id, songname, dl, link, "Audio", 0)
                caption = f"🏷 **Title:** [{songname}]({link})\n**👥 Chat ID:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Requested:** {from_user}"
                await event.client.send_file(chat_id, fotoplay, caption=caption, buttons=btnn)
                await botman.delete()
            except Exception as ep:
                clear_queue(chat_id)
                await botman.edit(f"`{ep}`")





#end
@Zaid.on(events.NewMessage(pattern="^[/?!]end"))
@is_admin
async def vc_end(event, perm):
    chat_id = event.chat_id
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if chat_id in QUEUE:
        try:
            if int(assistant) == 1:
               await call_py.leave_group_call(chat_id)
            if int(assistant) == 2:
               await call_py2.leave_group_call(chat_id)
            if int(assistant) == 3:
               await call_py3.leave_group_call(chat_id)
            if int(assistant) == 4:
               await call_py4.leave_group_call(chat_id)
            if int(assistant) == 5:
               await call_py5.leave_group_call(chat_id)
            if int(assistant) == 6:
               await call_py.leave_group_call(chat_id)
            clear_queue(chat_id)
            await event.reply("**Streaming Ended**")
        except Exception as e:
            await event.reply(f"**ERROR:** `{e}`")
    else:
        await event.reply("**Ntg is Streaming**")





@Zaid.on(events.NewMessage(pattern="^[?!/]vplay"))
async def vplay(event):
    if Config.HEROKU_MODE == "ENABLE":
        await event.reply("__Currently Heroku Mode is ENABLED so You Can't Stream Video because Video Streaming Cause of Banning Your Heroku Account__.")
        return
    title = ' '.join(event.text[6:])
    replied = await event.get_reply_message()
    sender = await event.get_sender()
    userid = sender.id
    chat = await event.get_chat()
    titlegc = chat.title
    chat_id = event.chat_id
    public = event.chat_id
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    from_user = vcmention(event.sender)
    if (
        replied
        and not replied.video
        and not replied.document
        and not title
        or not replied
        and not title
    ):
        return await event.client.send_file(chat_id, Config.CMD_IMG, caption="**Give Me Your Query Which You want to Stream**\n\n **Example**: `/vplay Nira Ishq Bass boosted`", buttons=btnn)
    if replied and not replied.video and not replied.document:
        xnxx = await event.reply("`Searching Video Details...`")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit(
                "**Give Me Valid Inputs**"
            )
        else:
            query = event.text.split(maxsplit=1)[1]
            search = ytsearch(query)
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, userid, ctitle)
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                caption = f"💡 **Video Streaming In Queue »** `#{pos}`\n\n**🏷 Title:** [{songname}]({url})\n**⏱ Duration:** `{duration}`\n🎧 **Requested:** {from_user}"
                await xnxx.delete()
                await event.client.send_file(chat_id, thumb, caption=caption, buttons=btnn)
            else:
                try:
                    if int(assistant) == 1:
                       await call_py.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 2:
                       await call_py2.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 3:
                       await call_py3.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 4:
                       await call_py4.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 5:
                       await call_py5.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 6:
                       await call_py.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    await xnxx.delete()
                    await event.client.send_file(event.chat_id,
                        f"**🏷 **__Video Streaming Started__**:** [{songname}]({url})\n**⏱ Duration:** `{duration}`\n💡 **Status:** `Playing`\n🎧 **Requested:** {from_user}, buttons=btnn",
                        link_preview=False,
                    )
                except Exception as ep:
                    clear_queue(chat_id)
                    await xnxx.edit(f"`{ep}`")

    elif replied:
        xnxx = await event.reply("📥 **Downloading Replied File**")
        dl = await replied.download_media()
        link = f"https://t.me/c/{chat.id}/{event.reply_to_msg_id}"
        if len(event.text.split()) < 2:
            RESOLUSI = 720
        else:
            pq = event.text.split(maxsplit=1)[1]
            RESOLUSI = int(pq)
        if replied.video or replied.document:
            songname = "Telegram Video Player"
        if chat_id in QUEUE:
            pos = add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
            caption = f"💡 **Video Streaming Started »** `#{pos}`\n\n**🏷 title:** [{songname}]({link})\n**👥 Chat ID:** `{chat_id}`\n🎧 **Requested:** {from_user}"
            await event.client.send_file(chat_id, ngantri, caption=caption, buttons=btnn)
            await xnxx.delete()
        else:
            if RESOLUSI == 360:
                hmmm = LowQualityVideo()
            elif RESOLUSI == 480:
                hmmm = MediumQualityVideo()
            elif RESOLUSI == 720:
                hmmm = HighQualityVideo()
            try:
                if int(assistant) == 1:
                   await call_py.join_group_call(
                       chat_id,
                       AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                       stream_type=StreamType().pulse_stream,
                   )
                if int(assistant) == 2:
                   await call_py2.join_group_call(
                       chat_id,
                       AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                       stream_type=StreamType().pulse_stream,
                   )
                if int(assistant) == 3:
                   await call_py3.join_group_call(
                       chat_id,
                       AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                       stream_type=StreamType().pulse_stream,
                   )
                if int(assistant) == 4:
                   await call_py4.join_group_call(
                       chat_id,
                       AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                       stream_type=StreamType().pulse_stream,
                   )
                if int(assistant) == 5:
                   await call_py5.join_group_call(
                       chat_id,
                       AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                       stream_type=StreamType().pulse_stream,
                   )
                if int(assistant) == 6:
                   await call_py.join_group_call(
                       chat_id,
                       AudioVideoPiped(dl, HighQualityAudio(), hmmm),
                       stream_type=StreamType().pulse_stream,
                   )
                add_to_queue(chat_id, songname, dl, link, "Video", RESOLUSI)
                caption = f"🏷 **title:** [{songname}]({link})\n**👥 Chat ID:** `{chat_id}`\n💡 **Status:** `Playing`\n🎧 **Requested:** {from_user}"
                await xnxx.delete()
                await event.client.send_file(chat_id, fotoplay, caption=caption, buttons=btnn)
            except Exception as ep:
                clear_queue(chat_id)
                await xnxx.edit(f"`{ep}`")
    else:
        xnxx = await event.reply("`Searching...`")
        query = event.text.split(maxsplit=1)[1]
        search = ytsearch(query)
        RESOLUSI = 720
        hmmm = HighQualityVideo()
        if search == 0:
            await xnxx.edit("**Unable To featch your Query**")
        else:
            songname = search[0]
            title = search[0]
            url = search[1]
            duration = search[2]
            thumbnail = search[3]
            ctitle = await CHAT_TITLE(titlegc)
            thumb = await gen_thumb(thumbnail, title, userid, ctitle)
            format = "best[height<=?720][width<=?1280]"
            hm, ytlink = await ytdl(format, url)
            if hm == 0:
                await xnxx.edit(f"`{ytlink}`")
            elif chat_id in QUEUE:
                pos = add_to_queue(
                    chat_id, songname, ytlink, url, "Video", RESOLUSI)
                caption = f"💡 **Video Streaming Added in Queue »** `#{pos}`\n\n🏷 **title:** [{songname}]({url})\n**⏱ Duration:** `{duration}`\n🎧 **Requested:** {from_user}"
                await xnxx.delete()
                await event.client.send_file(chat_id, thumb, caption=caption, buttons=btnn)
            else:
                try:
                    if int(assistant) == 1:
                       await call_py.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 2:
                       await call_py2.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 3:
                       await call_py3.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 4:
                       await call_py4.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 5:
                       await call_py5.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    if int(assistant) == 6:
                       await call_py.join_group_call(
                           chat_id,
                           AudioVideoPiped(ytlink, HighQualityAudio(), hmmm),
                           stream_type=StreamType().pulse_stream,
                       )
                    add_to_queue(
                        chat_id,
                        songname,
                        ytlink,
                        url,
                        "Video",
                        RESOLUSI)
                    caption = f"🏷 **Title:** [{songname}]({url})\n**⏱ Duration:** `{duration}`\n💡 **Status:** `Playing`\n🎧 **Requested:** {from_user}"
                    await xnxx.delete()
                    await event.client.send_file(chat_id, thumb, caption=caption, buttons=btnn)
                except Exception as ep:
                    clear_queue(chat_id)
                    await xnxx.edit(f"`{ep}`")




#playlist
@Zaid.on(events.NewMessage(pattern="^[?!/]playlist"))
@is_admin
async def vc_playlist(event, perm):
    chat_id = event.chat_id
    if chat_id in QUEUE:
        chat_queue = get_queue(chat_id)
        if len(chat_queue) == 1:
            await event.reply(
                f"**�PlAYLIST:**\n• [{chat_queue[0][0]}]({chat_queue[0][2]}) | `{chat_queue[0][3]}`",
                link_preview=False,
            )
        else:
            PLAYLIST = f"**🎧 PLAYLIST:**\n**• [{chat_queue[0][0]}]({chat_queue[0][2]})** | `{chat_queue[0][3]}` \n\n**• Upcoming Streaming:**"
            l = len(chat_queue)
            for x in range(1, l):
                hmm = chat_queue[x][0]
                hmmm = chat_queue[x][2]
                hmmmm = chat_queue[x][3]
                PLAYLIST = PLAYLIST + "\n" + \
                    f"**#{x}** - [{hmm}]({hmmm}) | `{hmmmm}`"
            await event.reply(PLAYLIST, link_preview=False)
    else:
        await event.reply("**Ntg is Streaming**")






#leavevc
@Zaid.on(events.NewMessage(pattern="^[?!/]leavevc"))
@is_admin
async def leavevc(event, perm):
    xnxx = await event.reply("Processing")
    chat_id = event.chat_id
    from_user = vcmention(event.sender)
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if from_user:
        try:
            if int(assistant) == 1:
               await call_py.leave_group_call(chat_id)
            if int(assistant) == 2:
               await call_py2.leave_group_call(chat_id)
            if int(assistant) == 3:
               await call_py3.leave_group_call(chat_id)
            if int(assistant) == 4:
               await call_py4.leave_group_call(chat_id)
            if int(assistant) == 5:
               await call_py5.leave_group_call(chat_id)
            if int(assistant) == 6:
               await call_py.leave_group_call(chat_id)
        except (NotInGroupCallError, NoActiveGroupCall):
            pass
        await xnxx.edit("**Left the voice chat** `{}`".format(str(event.chat_id)))
    else:
        await xnxx.edit(f"**Sorry {owner} not on Voice Chat**")



@Zaid.on(events.NewMessage(pattern="^[?!/]skip"))
@is_admin
async def vc_skip(event, perm):
    chat_id = event.chat_id
    if len(event.text.split()) < 2:
        op = await skip_current_song(chat_id)
        if op == 0:
            await event.reply("**Nothing Is Streaming**")
        elif op == 1:
            await event.reply("empty queue, leave voice chat", 10)
        else:
            await event.reply(
                f"**⏭ Skipped**\n**🎧 Now Playing** - [{op[0]}]({op[1]})",
                link_preview=False,
            )
    else:
        skip = event.text.split(maxsplit=1)[1]
        DELQUE = "**Removing Following Songs From Queue:**"
        if chat_id in QUEUE:
            items = [int(x) for x in skip.split(" ") if x.isdigit()]
            items.sort(reverse=True)
            for x in items:
                if x != 0:
                    hm = await skip_item(chat_id, x)
                    if hm != 0:
                        DELQUE = DELQUE + "\n" + f"**#{x}** - {hm}"
            await event.reply(DELQUE)


@Zaid.on(events.NewMessage(pattern="^[?!/]pause"))
@is_admin
async def vc_pause(event, perm):
    chat_id = event.chat_id
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if chat_id in QUEUE:
        try:
            if int(assistant) == 1:
               await call_py.pause_stream(chat_id)
            if int(assistant) == 2:
               await call_py2.pause_stream(chat_id)
            if int(assistant) == 3:
               await call_py3.pause_stream(chat_id)
            if int(assistant) == 4:
               await call_py4.pause_stream(chat_id)
            if int(assistant) == 5:
               await call_py5.pause_stream(chat_id)
            if int(assistant) == 6:
               await call_py.pause_stream(chat_id)
            await event.reply("**Streaming Paused**")
        except Exception as e:
            await event.reply(f"**ERROR:** `{e}`")
    else:
        await event.reply("**Nothing Is Playing**")



@Zaid.on(events.NewMessage(pattern="^[?!/]resume"))
@is_admin
async def vc_resume(event, perm):
    chat_id = event.chat_id
    _assistant = await get_assistant(chat_id, "assistant")
    assistant = _assistant["saveassistant"]
    if chat_id in QUEUE:
        try:
            if int(assistant) == 1:
               await call_py.resume_stream(chat_id)
            if int(assistant) == 2:
               await call_py2.resume_stream(chat_id)
            if int(assistant) == 3:
               await call_py3.resume_stream(chat_id)
            if int(assistant) == 4:
               await call_py4.resume_stream(chat_id)
            if int(assistant) == 5:
               await call_py5.resume_stream(chat_id)
            if int(assistant) == 6:
               await call_py.resume_stream(chat_id)
            await event.reply(event, "**Streaming Started Back 🔙**")
        except Exception as e:
            await event.reply(f"**ERROR:** `{e}`")
    else:
        await event.reply("**Nothing Is Streaming**")


@call_py.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)

@call_py2.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)

@call_py3.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)

@call_py4.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)

@call_py5.on_stream_end()
async def stream_end_handler(_, u: Update):
    chat_id = u.chat_id
    print(chat_id)
    await skip_current_song(chat_id)


@call_py.on_closed_voice_chat()
async def closedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py2.on_closed_voice_chat()
async def closedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py3.on_closed_voice_chat()
async def closedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py4.on_closed_voice_chat()
async def closedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py5.on_closed_voice_chat()
async def closedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py.on_left()
async def leftvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py2.on_left()
async def leftvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py3.on_left()
async def leftvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py4.on_left()
async def leftvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py5.on_left()
async def leftvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)


@call_py.on_kicked()
async def kickedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py2.on_kicked()
async def kickedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py3.on_kicked()
async def kickedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py4.on_kicked()
async def kickedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)

@call_py5.on_kicked()
async def kickedvc(_, chat_id: int):
    if chat_id in QUEUE:
        clear_queue(chat_id)
