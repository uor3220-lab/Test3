from telegram.ext import ApplicationBuilder, CommandHandler
from config import BOT_TOKEN
from database import load_db
from payments import bkash, nagad, binance
from admin import admin, addbalance, users

async def start(update, context):
    await update.message.reply_text("🤖 Bot started")

app = ApplicationBuilder().token(8481040153:AAEGvSLjZRhaapftjsKuuuALNvzWfuJT8Zs).build()
app.add_handler(CommandHandler("start", start))

print("Bot running...")
app.run_polling()
