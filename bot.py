import os
import logging
import asyncio
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# បើកប្រព័ន្ធកត់ត្រាការងារ (Logging)
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# ទាញយក Token ពី Environment Variables របស់ Render
TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

# --- ពាក្យបញ្ជា /start ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    # បង្កើតប៊ូតុងតំណភ្ជាប់នៅពីក្រោមសារ
    keyboard = [
        [InlineKeyboardButton("🌐 ចូលលេងកម្សាន្តទីនេះ", url="https://t.me/WIN365KH1BOT?start=telegram")]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # សារស្វាគមន៍ដែលអ្នកចង់បាន
    welcome_msg = (
        "សូមស្វាគមន៍មកវេបសាយធំបំផុត ងាយស្រួលលេង📲 "
        "និងគួរឱ្យទុកចិត្តបំផុតនៅកម្ពុជា🔥សេវាកម្ម២៤ម៉ោង!"
    )
    
    if update.message:
        await update.message.reply_text(welcome_msg, reply_markup=reply_markup)

async def run_bot() -> None:
    if not TOKEN:
        logger.error("រកមិនឃើញ TELEGRAM_BOT_TOKEN នៅក្នុង Environment Variables ទេ!")
        return

    # កសាងកម្មវិធីបូត
    application = Application.builder().token(TOKEN).build()

    # បន្ថែម Command Handler សម្រាប់ /start
    application.add_handler(CommandHandler("start", start))

    # ចាប់ផ្តើមដំណើរការបូត
    logger.info("កំពុងចាប់ផ្តើមដំណើរការបូត...")
    await application.initialize()
    await application.start()
    
    # រក្សាបូតឱ្យដំណើរការជាប្រចាំ
    await application.updater.start_polling()
    
    stop_signal = asyncio.Event()
    await stop_signal.wait()

def main() -> None:
    try:
        asyncio.run(run_bot())
    except KeyboardInterrupt:
        logger.info("បូតត្រូវបានបញ្ឈប់។")

if __name__ == "__main__":
    main()
