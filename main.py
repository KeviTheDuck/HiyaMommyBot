from telegram.ext import Updater, CommandHandler , CallbackContext
from telegram import Update
import anime_images_api
from keep_alive import keep_alive
from decouple import config


BOT_TOKEN = config('TOKEN')
culture = anime_images_api.Anime_Images()

bot_help= """
    Hello, I am your Hiya Mommy. 
    Commands:
            SFW(Safe for work):
                /hugs    : Hug media     
                /kiss    : Kiss media
                /pat     : Head pat media
                /cuddle  : Cuddle media
                /kill    : Kill media (mostly kawaii)
                /wink    : Wink media

            NSFW(Not Safe For Work)
                /bonkers : Boob media (mommy bonkers)
                /hentai  : Hentai media
    Extras:
        /hiya : Acts like Hiya 

 """


#URLS
def get_sfw(flag):
   sfw = culture.get_sfw(flag)
   return sfw

def get_nsfw(flag):
   nsfw = culture.get_nsfw(flag)
   return nsfw

#Commands
#----NSFW----
def bonkers(update: Update, context: CallbackContext):
    url = get_nsfw(flag="boobs")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def hentai(update: Update, context: CallbackContext):
    url = get_nsfw(flag="hentai")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

#----SFW----
def hugs(update: Update, context: CallbackContext):
    url = get_sfw(flag="hug")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def kiss(update: Update, context: CallbackContext):
    url = get_sfw(flag="kiss")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def cuddle(update: Update, context: CallbackContext):
    url = get_sfw(flag="cuddle")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def wink(update: Update, context: CallbackContext):
    url = get_sfw(flag="wink")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def kill(update: Update, context: CallbackContext):
    url = get_sfw(flag="kill")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def pat(update: Update, context: CallbackContext):
    url = get_sfw(flag="pat")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

def slap(update: Update, context: CallbackContext):
    url = get_sfw(flag="slap")
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo=url)

#EXTRAS
def help(update: Update, context: CallbackContext):
    context.bot.send_message(chat_id=update.effective_chat.id , text=bot_help)

def hiya(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_photo(chat_id=chat_id, photo="http://0x0.st/o8Kn.png")



#BOT
def error_handler(update: Update, context: CallbackContext):
    chat_id = update.message.chat_id
    context.bot.send_message(chat_id=chat_id, text="Please try the command again")
def main():
    updater = Updater(BOT_TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler('bonkers',bonkers))
    dp.add_handler(CommandHandler('hentai',hentai))
    
    dp.add_handler(CommandHandler('hugs',hugs))
    dp.add_handler(CommandHandler('kiss',kiss))
    dp.add_handler(CommandHandler('pat',pat))  
    dp.add_handler(CommandHandler('kill',kill))
    dp.add_handler(CommandHandler('wink',wink))
    dp.add_handler(CommandHandler('cuddle', cuddle))
    dp.add_handler(CommandHandler('slap', slap))
    
    dp.add_handler(CommandHandler('hiya',hiya))
    dp.add_handler(CommandHandler('help',help))
    
    dp.add_error_handler(error_handler)
    updater.start_polling()
    updater.idle()

keep_alive()
    
if __name__ == '__main__':
    main()


