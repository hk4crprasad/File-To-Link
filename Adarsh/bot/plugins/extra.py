from Adarsh.bot import StreamBot
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from pyrogram import filters
import time
import shutil, psutil
from utils_bot import *
from Adarsh import StartTime

        
    
@StreamBot.on_message(filters.command('stats') & filters.private)
async def stats(bot, update):
  currentTime = readable_time((time.time() - StartTime))
  total, used, free = shutil.disk_usage('.')
  total = get_readable_file_size(total)
  used = get_readable_file_size(used)
  free = get_readable_file_size(free)
  sent = get_readable_file_size(psutil.net_io_counters().bytes_sent)
  recv = get_readable_file_size(psutil.net_io_counters().bytes_recv)
  cpuUsage = psutil.cpu_percent(interval=0.5)
  memory = psutil.virtual_memory().percent
  disk = psutil.disk_usage('/').percent
  botstats = f'<b>Bot Uptime:</b> {currentTime}\n' \
            f'<b>💿 Total disk space💿:</b> {total}\n' \
            f'<b>✅ Used ✅:</b> {used}  ' \
            f'<b>⚜️ Free ⚜️:</b> {free}\n\n' \
            f'📊 Data Usage 📊\n<b>Upload:</b> {sent}\n' \
            f'<b>⬇️ Down ⬇️:</b> {recv}\n\n' \
            f'<b>🖥️ CPU 🖥️:</b> {cpuUsage}% ' \
            f'<b>💾 RAM 💾:</b> {memory}% ' \
            f'<b>📀 Disk 📀:</b> {disk}%'
  await update.reply_text(botstats)
