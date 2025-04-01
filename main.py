from telegram import Update, ReplyKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, ContextTypes, filters

import os

BOT_TOKEN = os.getenv("BOT_TOKEN")

# دسته‌ها
categories = {
    "🎨 اقامت هنرمندی": "بررسی شرایط شما برای دریافت اقامت هنرمندی در اتریش",
    "🎓 ویزای دانشجویی": "راهنمایی در مورد پذیرش، مدارک و مراحل ویزای دانشجویی اتریش",
    "👨‍💼 ویزای جستجوی کار": "بررسی شرایط شما برای دریافت ویزای Job Seeker اتریش",
    "💰 خودحمایتی / تمکن مالی": "مشاوره درباره اقامت خودحمایتی برای افراد با تمکن مالی",
    "👨‍👩‍👧 الحاق همراهان": "بررسی شرایط پیوستن همراهان (همسر/فرزند) به متقاضی اصلی"
}

keyboard = ReplyKeyboardMarkup(
    [[key] for key in categories.keys()],
    resize_keyboard=True
)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "سلام! 👋\nلطفاً یکی از دسته‌های مشاوره‌ای زیر رو انتخاب کن:",
        reply_markup=keyboard
    )

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    if text in categories:
        await update.message.reply_text(
            "💬 *مشاوره اولیه 60 دقیقه‌ای*\n"
            "💸 مبلغ: ۱,۰۰۰,۰۰۰ تومان\n"
            f"📄 {categories[text]}\n\n"
            "لطفاً روش پرداخت را انتخاب کنید:\n"
            "💳 پرداخت آنلاین (زرین‌پال)\n"
            "🏦 ارسال فیش بانکی",
            parse_mode="Markdown"
        )
    else:
        await update.message.reply_text("لطفاً یکی از گزینه‌های منو را انتخاب کن.")

app = ApplicationBuilder().token(BOT_TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
app.run_polling()
