import requests
from telegram import Update, Bot
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from typing import Final
import asyncio

TOKEN: Final = 'your_token_here'
BOT_USERNAME: Final = '@banana_banana_bbbot'

# Initialize the Updater
app = ApplicationBuilder().token(TOKEN).build()
bot = Bot(token=TOKEN)

# Commands
async def start_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text='Hello! Thanks for chatting with me!')

async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text='Please type something so I can respond!')

async def custom_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(text='This is a custom command!')

# Responses
def handle_respond(text):
    processed = text.lower()
    if 'hello' in processed:
        return 'Hey There!'
    if 'how are you' in processed:
        return 'I am good!'
    if 'i love python' in processed:
        return 'Remember to subscribe'
    return 'I do not understand what you wrote...'

# Message Handling
async def handle_message(update, context):
    message_type = update.message.chat.type
    text = update.message.text
    print(f'User({update.message.chat.id}) in {message_type}: "{text}"')
    if message_type == 'group':
        if BOT_USERNAME in text:
            new_text = text.replace(BOT_USERNAME, '').strip()
            response = handle_respond(new_text)
            await context.bot.send_message(chat_id=update.effective_chat.id, text=response)
        else:
            return
    else:
        response = handle_respond(text)
        await context.bot.send_message(chat_id=update.effective_chat.id, text=response)

def error(update, context):
    print(f'Update {update} caused error {context.error}')

# Initialize the bot and command handlers

async def send_initial_messages(bot, user_ids, message):
    for user_id in user_ids:
        try:
            await bot.send_message(chat_id=user_id, text=message)
        except Exception as e:
            print(f"Failed to send message to {user_id}: {str(e)}")

# async def main():
#     await send_initial_messages(bot, user_ids, message)
#     await app.run_polling()

import asyncio

async def main():
    user_ids = ['969257303', '351304736']
    message = 'Hello! This is a test message from your Telegram bot.'
    bot.sendMessage(chat_id=user_ids, text=message)
    
    # Add handlers before starting the polling
    app.add_handler(CommandHandler("start", start_command))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(CommandHandler("custom", custom_command))
    
    # Start polling
    await app.run_polling()

if __name__ == '__main__':
    print('Starting bot...')
    asyncio.run(main())



