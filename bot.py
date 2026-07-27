import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Get token from environment
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Fallback for testing (REMOVE AFTER FIXING ENV VARIABLE)
if not TOKEN:
    logger.warning("TELEGRAM_BOT_TOKEN not found in environment!")
    # Only use this for testing - replace with your actual token
    # TOKEN = "YOUR_BOT_TOKEN_HERE"
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "🤖 Welcome to ForexBot!\n\n"
        "I'm your Forex analysis assistant.\n"
        "Send /help to see available commands."
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "📊 Available Commands:\n\n"
        "/start - Welcome message\n"
        "/help - Show this help menu\n\n"
        "🔧 More features coming soon!"
    )

def main() -> None:
    try:
        logger.info("Bot is starting with Python version...")
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        logger.info("Bot is running successfully!")
        application.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    main()
