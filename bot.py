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

# DEBUG: Print all environment variables (remove after fixing)
logger.info("Available environment variables:")
for key in os.environ.keys():
    if "TOKEN" in key or "BOT" in key:
        logger.info(f"Found: {key}")

# Get the bot token from environment variables
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")

# Also try alternative names (for debugging)
if not TOKEN:
    logger.warning("TELEGRAM_BOT_TOKEN not found, trying BOT_TOKEN...")
    TOKEN = os.environ.get("BOT_TOKEN")
if not TOKEN:
    logger.warning("BOT_TOKEN not found, trying TOKEN...")
    TOKEN = os.environ.get("TOKEN")

if not TOKEN:
    logger.error("No token found in environment variables!")
    # List all environment variables for debugging
    logger.error(f"All env vars: {list(os.environ.keys())}")
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
        logger.info("Starting bot with token: " + TOKEN[:10] + "...")  # Show first 10 chars for debugging
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        logger.info("Bot is running...")
        application.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    main()
