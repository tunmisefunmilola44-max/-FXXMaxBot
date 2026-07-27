import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", 
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# 🔥 TEMPORARY - Hardcode your token here for testing
# DELETE THIS AFTER TESTING AND USE ENVIRONMENT VARIABLES
TOKEN = "YOUR_BOT_TOKEN_HERE"  # Replace with your actual token from @BotFather

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
        logger.info("Bot is starting...")
        application = Application.builder().token(TOKEN).build()
        application.add_handler(CommandHandler("start", start))
        application.add_handler(CommandHandler("help", help_command))
        logger.info("Bot is running!")
        application.run_polling()
    except Exception as e:
        logger.error(f"Failed to start bot: {e}")
        raise

if __name__ == "__main__":
    main()
