# (c) adarsh-goel 
from Adarsh.bot import StreamBot
from Adarsh.vars import Var
import logging
logger = logging.getLogger(__name__)
from Adarsh.bot.plugins.stream import MY_PASS
from Adarsh.utils.human_readable import humanbytes
from Adarsh.utils.database import Database
from pyrogram import filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram.errors import UserNotParticipant
from Adarsh.utils.file_properties import get_name, get_hash, get_media_file_size
db = Database(Var.DATABASE_URL, Var.name)
from pyrogram.types import ReplyKeyboardMarkup

                     
@StreamBot.on_message(filters.command("start") & filters.private )
async def start(b, m):
    if not await db.is_user_exist(m.from_user.id):
        await db.add_user(m.from_user.id)
        await b.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined**\n\n**New User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started Your Bot**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await b.get_chat_member(Var.UPDATES_CHANNEL, m.chat.id)
            if user.status == "kicked":
                await b.send_message(
                    chat_id=m.chat.id,
                    text="**Sorry, You are Banned from Using this Bot**\n\n**Contact @The_Insomniacs_Club_Bot**",
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
             await StreamBot.send_photo(
                chat_id=m.chat.id,
                photo="https://te.legra.ph/file/7fb3511f344453f59ee3f.jpg",
                caption="**ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ**\n\n**ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ**\n\n**ᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴄʟɪᴄᴋ sᴛᴀʀᴛ ᴀɢᴀɪɴ**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("🔓 ᴊᴏɪɴ ɴᴏᴡ ", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
             return
        except Exception:
            await b.send_message(
                chat_id=m.chat.id,
                text="**Something Went Wrong** <b> <a href='https://t.me/The_Insomniacs_Club_Bot'>CLICK HERE FOR SUPPORT </a></b>",
                
                disable_web_page_preview=True)
            return
    await StreamBot.send_video(
        chat_id=m.chat.id,
        video ="https://te.legra.ph/file/788e1f924f7d8ece7b507.mp4",
        caption =f'🫡 **ʜᴇʏ {m.from_user.mention(style="md")}**\n\n**ɪ ᴀᴍ ᴛɪᴄ ғɪʟᴇ ᴛᴏ ʟɪɴᴋ ʙᴏᴛ**.\n\n**sᴇɴᴅ ᴍᴇ ᴀɴʏ ғɪʟᴇ ᴏʀ ᴠɪᴅᴇᴏ ᴀɴᴅ ɢᴇᴛ ᴀ ᴅɪʀᴇᴄᴛ ᴅᴏᴡɴʟᴏᴀᴅ ᴀɴᴅ sᴛʀᴇᴀᴍ ʟɪɴᴋs**',
        )


@StreamBot.on_message(filters.command("help") & filters.private )
async def help_handler(bot, message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        await bot.send_message(
            Var.BIN_CHANNEL,
            f"**New User Joined**\n\n**New User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) Started Your Bot**"
        )
    if Var.UPDATES_CHANNEL != "None":
        try:
            user = await bot.get_chat_member(Var.UPDATES_CHANNEL, message.chat.id)
            if user.status == "kicked":
                await bot.send_message(
                    chat_id=message.chat.id,
                    text="**Sorry, You are Banned from Using this Bot**\n\n**Contact @The_Insomniacs_Club_Bot**",
                    
                    disable_web_page_preview=True
                )
                return
        except UserNotParticipant:
            await StreamBot.send_photo(
                chat_id=message.chat.id,
                photo="https://te.legra.ph/file/7fb3511f344453f59ee3f.jpg",
                Caption="**ᴅᴜᴇ ᴛᴏ ᴏᴠᴇʀʟᴏᴀᴅ, ᴏɴʟʏ ᴄʜᴀɴɴᴇʟ sᴜʙsᴄʀɪʙᴇʀs ᴄᴀɴ ᴜsᴇ ᴛʜᴇ ʙᴏᴛ**\n\n**ᴊᴏɪɴ ᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴛᴏ ᴜsᴇ ᴛʜɪs ʙᴏᴛ**\n\n**ᴀғᴛᴇʀ ᴊᴏɪɴɪɴɢ ᴄʟɪᴄᴋ sᴛᴀʀᴛ ᴀɢᴀɪɴ**",
                reply_markup=InlineKeyboardMarkup(
                    [
                        [
                            InlineKeyboardButton("Jᴏɪɴ ɴᴏᴡ 🔓", url=f"https://t.me/{Var.UPDATES_CHANNEL}")
                        ]
                    ]
                ),
                
            )
            return
        except Exception:
            await bot.send_message(
                chat_id=message.chat.id,
                text="**Something Went Wrong** <b> <a href='https://t.me/The_Insomniacs_Club_Bot'>CLICK HERE FOR SUPPORT </a></b>",
                disable_web_page_preview=True)
            return
    await message.reply_text(
        text="""**⪼ ᴛʜɪs ʙᴏᴛ ᴀʟsᴏ sᴜᴘᴘᴏʀᴛs ɪɴ ᴄʜᴀɴɴᴇʟs. ᴀᴅᴅ ᴍᴇ ᴛᴏ ʏᴏᴜʀ ᴄʜᴀɴɴᴇʟ ᴀs ᴀᴅᴍɪɴ ᴀɴᴅ ɢᴇᴛ ʀᴇᴀʟ ᴛɪᴍᴇ ʟɪɴᴋs**\n\n**⪼ sᴇɴᴅ 𝟹 ғɪʟᴇs ᴘᴇʀ 𝟻 ᴍɪɴᴜᴛᴇs ᴛᴏ ᴀᴠᴏɪᴅ sᴘᴀᴍ (sᴘᴀᴍ = ʙᴀɴ)**""",
        
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(
            [
                [InlineKeyboardButton("⚡ sᴜᴘᴘᴏʀᴛ ", url="https://t.me/TheInsomniacsClub")],
                [InlineKeyboardButton("💌 ᴅᴇᴠᴇʟᴏᴘᴇʀ ", url="https://t.me/DANGER1753")]
            ]
        )
    )
