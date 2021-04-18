from telegram.ext import Updater, MessageHandler, Filters
from telegram.ext import CallbackContext, CommandHandler
import random

TOKEN = "1525707127:AAHRkcH0iBcgmBsPnh3IQsxViLO7Js9JaYY"
privet = ['Приветик!', 'Здравствуй', 'Хай', 'Привет)', 'Вечер в хату', 'Hello',
          'Привет', 'Ку-ку', 'Здарова', 'Хеллоу', 'Хелоу']
cool = ['Класс', 'Вау', 'Кул', 'Прекрас', 'Супер', 'Крут', 'Отлично',
        'Замечательн', 'Молодец', 'Молодэ']


def echo(update, context):
    lol = update.message.text
    if 'расскажи' in lol.lower() and 'фильм' in lol.lower():
        # КИНОПОИСК В ДЕЙСТВИИ
        update.message.reply_text('Классный фильм, что могу сказать')
    if 'расскажи' in lol.lower() and 'сериал' in lol.lower():
        # КИНОПОИСК В ДЕЙСТВИИ
        update.message.reply_text('Классный сериал, что могу сказать')
    for j in cool:
        if j.lower() in lol.lower() and 'фильм' not in lol.lower() and \
                'сериал' not in lol.lower():
            update.message.reply_text(
                random.choice(['Спасибо', 'Благодарю', 'Няя']))
    if 'найди' in lol.lower():
        update.message.reply_text('Введи название фильма или сериала')
        # КИНОПОИСК В ДЕЙСТВИИ
        update.message.reply_text('Вот что мне удалось найти')
    if 'посоветуй' in lol.lower():
        if 'фильм' in lol.lower():
            update.message.reply_text('Фильм тебе надо, да?')
        elif 'сериал' in lol.lower():
            update.message.reply_text('Сериальчик')
        else:
            update.message.reply_text('Фильм или сериал?')
    for i in privet:
        if i.lower() in lol.lower():
            update.message.reply_text(random.choice(privet))


def start(update, context):
    update.message.reply_text(
        "Привет! Я Олежа - твой помощник в мире фильмов и сериалов! Напиши мне"
        " 'Посоветуй'")


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
