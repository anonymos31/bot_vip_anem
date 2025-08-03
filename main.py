from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import os

# ✅ التوكن من متغيرات البيئة
TOKEN = os.getenv("TOKEN")

# ✅ رسالة ترحيب عند الضغط على "ابدأ"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 مرحبًا بك!\n\n"
        "📥 هذا البوت مخصص فقط لاستقبال الرسائل من التطبيق.\n"
        "❌ البوت لا يقدم أي خدمة مباشرة ولا يستقبل أوامر.\n\n"
        "✅ تأكد من شراء التطبيق وتفعيله حتى يعمل البوت معك بشكل صحيح.\n\n"
        "📩 للاستفسار: @Elbahi_anas"
    )

# 🟢 تشغيل البوت
if __name__ == '__main__':
    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    print("✅ البوت شغال على Railway ...")
    app.run_polling()
