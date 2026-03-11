from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Токен твоего бота
TOKEN = "8562012302:AAF9CWM4P-MxoV9_W-bF_AIK9fllyzrCX1Y"

# Текст сообщения
TEXT = """Чтобы получить 50 звёзд вы должны написать @Arslan2016m
1 сообщение — 30 звёзд оплата.
Это делается добровольно и вы не обязаны это делать.

Пригласи друга по ссылке в бота и вы получите в 2 раза больше,
вы это тоже не обязаны.

Ссылка на бота: http://t.me/bespaltozvezd_bot
"""

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(TEXT)

# Создание и запуск бота
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.run_polling()
