from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.environ.get('TOKEN')

print('bot démarrez...')


def chat_response(messages):
    user_message = str(messages).lower()
    google_link = 'https://www.google.com/'

    if user_message in ['qui es-tu', 'tu es qui', 'qui es tu', 'qui est-ce',
                        'qui es-tu ?', 'tu es qui ?', 'qui es tu ?', 'qui est-ce ?',
                        'qui es-tu?', 'tu es qui?', 'qui es tu?', 'qui est-ce?']:
        return "Je suis le Bot Créer par Abdoulaye"

    elif user_message in ['qui est abdoulaye', 'abdoulaye c\'est qui', 'c\'est qui abdoulaye',
                        'qui est abdoulaye ?', 'abdoulaye c\'est qui ?', 'c\'est qui abdoulaye ?',
                        'qui est abdoulaye?', 'abdoulaye c\'est qui?', 'c\'est qui abdoulaye?']:
        return "Abdoulaye est un homme très intelligent !"

    else:
        return f"Je n'ai pas de réponses pour cela, Redirigez vous vers Google en cliquant ici: {google_link}"


def start(update, context):
    update.message.reply_text("""
    Bienvenue je suis le bot officiel de Abdoulaye DIAKITE !
    
    Les commandes disponibles sont :
    - /github pour voir le profil GitHub
    - /linkedin pour le profil Linkedin
    - /sololearn pour le profil Sololearn
    
    Vous pouvez me poser des questions si cela vous chante !
    """)


def github(update, context):
    update.message.reply_text('https://github.com/abdoulaye151297')


def linkedin(update, context):
    update.message.reply_text('https://www.linkedin.com/in/abdoulaye-badjiri-diakite-92b9ba235/')


def sololearn(update, context):
    update.message.reply_text('https://www.sololearn.com/profile/25765142')


def message_handler(update, context):
    text = str(update.message.text)
    response = chat_response(text)

    update.message.reply_text(response)


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("github", github))
    dp.add_handler(CommandHandler("sololearn", sololearn))
    dp.add_handler(CommandHandler("linkedin", linkedin))

    dp.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
