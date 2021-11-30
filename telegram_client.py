from telegram.ext import CommandHandler,Updater
from telegram.ext.callbackcontext import CallbackContext


#import logging     if you want logs delete these two #
#logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)

TOKEN=""#insert Token

updater = Updater(token=TOKEN, use_context=True)
dispatcher = updater.dispatcher



def main():
    start_handler = CommandHandler('start', start)
    help_handler = CommandHandler('help',help)
    dispatcher.add_handler(start_handler)
    dispatcher.add_handler(help_handler)

    #dispatcher.job_queue.run_repeating(FUNCTION_NAME,interval=60) function to do every 60 sec
    dispatcher.job_queue.run_once(start1,0)
    
    updater.start_polling()
    
def start(update, context):
    text="Start Text"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def start1(context: CallbackContext):
    text="Start Text"
    context.bot.send_message(chat_id=0, text=text)#insert id

def help(update, context):
    text="/start\n/help"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)

def Shutdown(update,context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="SHUTDOWN")
    exit() 

if __name__ == '__main__':
    main()
