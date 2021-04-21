from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
from newsapi import NewsApiClient

newsapi = NewsApiClient(api_key='ac1090254ef54229bac8a6a1a300b2a7')
TOKEN = "1525707127:AAHRkcH0iBcgmBsPnh3IQsxViLO7Js9JaYY"
privet = ['Приветик!', 'Здравствуй', 'Хай', 'Привет)', 'Вечер в хату', 'Hello',
          'Привет', 'Ку-ку', 'Здарова', 'Хеллоу', 'Хелоу']
cool = ['Класс', 'Вау', 'Кул', 'Прекрас', 'Супер', 'Крут', 'Отлично',
        'Замечательн', 'Молодец', 'Молодэ']


def echo(update, context):
    lol = update.message.text
    if 'расскажи' in lol.lower():
        del lol['расскажи']
        print('с')
        update.message.reply_text('Секунду')
        top_headlines = newsapi.get_everything(q=f'{lol.lower()}', language='ru')
        title = top_headlines["articles"][0]["title"]
        description = top_headlines["articles"][0]["description"]
        update.message.reply_text(title, '\n', description)



def start(update, context):
    update.message.reply_text(
        "Привет! Я Олежа - твой помощник в мире новостей!")


def help(update, context):
    update.message.reply_text(
        "Я пока не умею помогать... Я только ваше эхо.")


def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher
    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))

    text_handler = MessageHandler(Filters.text, echo)

    dp.add_handler(text_handler)
    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()
