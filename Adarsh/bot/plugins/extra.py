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
            f'<b>ð¿ Total disk spaceð¿:</b> {total}\n' \
            f'<b>â Used â:</b> {used}  ' \
            f'<b>âï¸ Free âï¸:</b> {free}\n\n' \
            f'ð Data Usage ð\n<b>Upload:</b> {sent}\n' \
            f'<b>â¬ï¸ Down â¬ï¸:</b> {recv}\n\n' \
            f'<b>ð¥ï¸ CPU ð¥ï¸:</b> {cpuUsage}% ' \
            f'<b>ð¾ RAM ð¾:</b> {memory}% ' \
            f'<b>ð Disk ð:</b> {disk}%'
  await update.reply_text(botstats)
