import logging
from datetime import datetime,time
import asyncio
from telegram import ForceReply,Update,InputMediaPhoto
from telegram.ext import Application,CommandHandler,ContextTypes,MessageHandler,filters
group_id = "@baraholkakish" #Tagul Grupului daca e privat place like INT
with open("D:/xampp/htdocs/python/NikGroupSpamer/x.txt","r",encoding='utf-8') as file:
        txt =file.read()




async def run( context:ContextTypes.DEFAULT_TYPE):
   
    # List of media group photo ,used to send some picures
    media_group = [
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/1.jpg', 'rb')),
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/2.jpg', 'rb')),
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/3.jpg', 'rb')),
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/4.jpg', 'rb')),
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/5.jpg', 'rb')),
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/6.jpg', 'rb')),
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/7.jpg', 'rb')), 
        InputMediaPhoto(open('D:/xampp/htdocs/python/NikGroupSpamer/photo/8.jpg', 'rb'))     
    ]
   
    try:
        # Functia raspunde pentru trimiterea
        await context.bot.send_media_group(chat_id=group_id, media=media_group) and await context.bot.send_message(chat_id=group_id, text =txt)
    except Exception as e:
        print(f"An error occurred: {e}")




async def start(update:Update,cotext:ContextTypes.DEFAULT_TYPE)->None:
    await update.message.reply_text("Команды Будуть")

    

    

def main()->None:
    application = Application.builder().token("<TOKEN").build()
    print("starting...")
    application.add_handler(CommandHandler("start",start))
    #application.add_handler(CommandHandler("run",run))
    application.job_queue.run_repeating(run,interval=3600,first=0,)
    
    # Run the bot until the user presses Ctrl-C
    application.run_polling(allowed_updates=Update.ALL_TYPES)
    

if __name__ == "__main__":
    main()

