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

# Get the bot token from environment variables
TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
if not TOKEN:
    raise ValueError("TELEGRAM_BOT_TOKEN environment variable not set.")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a welcome message when the /start command is issued."""
    await update.message.reply_text(
        "🤖 Welcome to ForexBot!\n\n"
        "I'm your Forex analysis assistant. Here are my commands:\n"
        "/start - Show this message\n"
        "/help - Get help\n"
        "/news - Get latest Forex news (coming soon)\n"
        "/analyze - Analyze currency pairs (coming soon)"
    )

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a help message when the /help command is issued."""
    await update.message.reply_text(
        "📊 Available Commands:\n\n"
        "/start - Welcome message\n"
        "/help - Show this help menu\n\n"
        "🔧 More features coming soon!"
    )

def main() -> None:
    """Start the bot."""
    try:
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        logger.info("Bot is starting...")
        application.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    main()
