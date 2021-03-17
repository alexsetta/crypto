from telegram.ext import *
import config, responses
import logging

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
logger = logging.getLogger(__name__)

def start_command(update, context):
    update.message.reply_text(f"Olá {update.message.from_user['first_name']} Seja bem vindo ao bot [alexsetta], digite /help para ver os comandos disponíveis")

def help_command(update, context):
    update.message.reply_text(responses.help())

def handle_message(update, context):
	txt = str(update.message.text).lower()
	logger.info(txt)
	response = responses.sample_responses(txt)
	logger.info(response)
	update.message.reply_text(response)

def error(update, context):
    print(f"Update: {update} caused error: {context.error}")

def main():
    updater = Updater(config.TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start_command))
    dp.add_handler(CommandHandler("help", help_command))
    dp.add_handler(MessageHandler(Filters.text, handle_message))
    dp.add_error_handler(error)

    updater.start_polling()
    updater.idle()

main()