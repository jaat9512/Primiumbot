import time
import random
from pyrogram import Client, filters

CMD = ["/", "."]

@Client.on_message(filters.command("alive", CMD))
async def check_alive(_, message):
    await message.reply_sticker("CAACAgIAAxkBAAIw6WYC2ROIXsb04PibCs5ehGAPerx4AAKsAQACEBptInjWW-Ya5ObHHgQ")
    await asyncio.sleep(1)
    await m.delete()
    await message.reply_text("𝐇𝐞𝐲 𝐃𝐮𝐝𝐞 😎 𝐘𝐨𝐮 𝐀𝐫𝐞 𝐒𝐨 𝐋𝐮𝐜𝐤𝐲 𝐈𝐚𝐦 𝐀𝐥𝐢𝐯𝐞 𝐔𝐬𝐞 𝐓𝐡𝐢𝐬 𝐂𝐨𝐦𝐦𝐚𝐧𝐝 /start 𝐓𝐨 𝐒𝐭𝐚𝐫𝐭 𝐌𝐞 💕")
    await asyncio.sleep(1)
    await m.delete()
@Client.on_message(filters.command("ping", CMD))
async def ping(_, message):
    start_t = time.time()
    rm = await message.reply_text("...")
    end_t = time.time()
    time_taken_s = (end_t - start_t) * 1000
    await rm.edit(f"Pong!\n{time_taken_s:.3f} ms")
