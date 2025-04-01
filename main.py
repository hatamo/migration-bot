from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text("سلام! به ربات مشاوره مهاجرتی خوش اومدی 👋")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))

app.run_polling()
