
import logging
from datetime import datetime,time
import asyncio

from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters
chat_ids = set()
# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
# set higher logging level for httpx to avoid all GET and POST requests being logged
logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


# Define a few command handlers. These usually take the two arguments update and
# context.
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /start is issued."""
    chat_id = update.effective_chat.id
    chat_ids.add(chat_id)
    user = update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Send a message when the command /help is issued."""
    await update.message.reply_text("Help!")


async def echo(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Echo the user message."""
    await update.message.reply_text("lezbuha")

async def hi(update:Update, context:ContextTypes.DEFAULT_TYPE)-> None:
    user =update.effective_user
    await update.message.reply_html(
        rf"Hi {user.mention_html()}!!!",
       
    )

async def WAYD(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Just hanging out, you?")

async def time_based(context:ContextTypes.DEFAULT_TYPE)->None:
    now =datetime.now().time()
    target_time = time(20,00)
    if now.hour == target_time.hour and now.minute ==target_time.minute:
        for chat_id in chat_ids:
            await context.bot.send_message(chat_id=chat_id, text="Good Afternoon Dear!")



async def time_mornignf(context:ContextTypes.DEFAULT_TYPE)->None:

    now= datetime.now().time()
    target_time=time(00,56)
    if now.hour==target_time.hour and now.minute==target_time.minute:
        for chat_id in chat_ids:
            await context.bot.send_message(chat_id=chat_id, text="Good Morning!")
            await context.bot.send_photo(chat_id=chat_id, photo='https://i.redd.it/2me05y8squh61.png')
                
async def nudes(update:Update,context:ContextTypes.DEFAULT_TYPE)->None:
    for chat_id in chat_ids:
        await context.bot.send_photo(chat_id=chat_id, photo='https://wimg.rule34.xxx//images/5132/b34e24b09bd3fda1d0789905710a1a20.jpeg?9844504')
        await context.bot.send_photo(chat_id=chat_id, photo='https://rule34.xxx//samples/6918/sample_ff17a50f5787fa3c6a6128712ee41083.jpg?9649972')

async def send_message(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    group_id = -4140864453  # Group ID as an integer
    try:
        await context.bot.send_message(chat_id=group_id, text="Hello, group!")
    except Exception as e:
        print(f"An error occurred: {e}")
def main() -> None:
    
    """Start the bot."""
    # Create the Application and pass it your bot's token.
    application = Application.builder().token("7129202708:AAE18ol9D32DgPSPv2zXDypk3loi25bD-y0").build()
   
    # on different commands - answer in Telegram
    application.add_handler(CommandHandler("start", start))
    #application.add_handler(CommandHandler("help", help_command))

    # on non command i.e message - echo the message on Telegram
    application.add_handler(MessageHandler(filters.Regex("You are") & ~filters.COMMAND, echo))
    application.add_handler(MessageHandler(filters.Regex("nudes"),nudes))
    application.add_handler(MessageHandler(filters.Regex("mess"),send_message))

    application.add_handler(MessageHandler(filters.Regex("Hi Abigail!" and "Hi"),hi)) #saing Hi to bot 
    application.add_handler(MessageHandler(filters.Regex("what are you doing?" and "What are you doing"),WAYD))
    application.job_queue.run_repeating(time_based, interval=60, first=1)
    application.job_queue.run_repeating(time_mornignf,interval=60,first=1)
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    


if __name__ == "__main__":
    main()