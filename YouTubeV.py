##################



import asyncio
import requests
import wget
import yt_dlp

from pyrogram import Client, filters
from pyrogram.types import Message

from youtube_search import YoutubeSearch
from yt_dlp import YoutubeDL


app = Client(
    "Bot",
    api_id = 22163598,
 api_hash = "994ff0becda5f784801d3697111c3b70",
 bot_token = "6147602769:AAHM1UKjCyt6h360D4qCRktUzqgNgpJrMQQ"
)

                                           
@app.on_message(filters.command("تحميل فيديو⬇️", [".", ""]))
async def vsong(client, message):
    ydl_opts = {
        "format": "best",
        "keepvideo": True,
        "prefer_ffmpeg": False,
        "geo_bypass": True,
        "outtmpl": "%(title)s.%(ext)s",
        "quite": True,
    }
    query = " ".join(message.command[1:])
    try:
        results = YoutubeSearch(query, max_results=1).to_dict()
        link = f"https://youtube.com{results[0]['url_suffix']}"
        title = results[0]["title"][:40]
        thumbnail = results[0]["thumbnails"][0]
        thumb_name = f"{title}.jpg"
        thumb = requests.get(thumbnail, allow_redirects=True)
        open(thumb_name, "wb").write(thumb.content)
        results[0]["duration"]
        results[0]["url_suffix"]
        results[0]["views"]
        message.from_user.mention
    except Exception as e:
        print(e)
    try:
        msg = await message.reply("**جاري تحميل الفيديو🔍 ...**")
        with YoutubeDL(ydl_opts) as ytdl:
            ytdl_data = ytdl.extract_info(link, download=True)
            file_name = ytdl.prepare_filename(ytdl_data)
    except Exception as e:
        return await msg.edit(f"🚫 **خطا:** {e}")
    preview = wget.download(thumbnail)
    await msg.edit("**✅تاكيد التحميل ...**")
    await message.reply_video(
        file_name,
        duration=int(ytdl_data["duration"]),
        thumb=preview,
        caption=ytdl_data["title"],
    )
    try:
        os.remove(file_name)
        await msg.delete()
    except Exception as e:
        print(e)                                                                                                                                             
print("Work⚡")
app.run()
