import os
import logging
from telegram import Update
from telegram.ext import Application, CommandHandler, MessageHandler, filters, ContextTypes

# Настройка логирования
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)
logger = logging.getLogger(__name__)

# Тексты песен
BANDANA_TEXT = """Помню времена, когда мне было мало
Сделал gual'у и похавал в Benihana
Пару лямов, много пармезана
Молодой Сусаноо, я Учиха после xan'а
Всё идёт по плану, на бите Montana
Голова — бандана, банде не нужна охрана
Полосы на мне, о да, я начал бегать рано
Нахуй кошельки, stack выпирает из кармана
Да, мы курим lala, да, мы курим zaza
Да, мы курим shabba и глазам пизда от газа
Миша съел xanax, Миша после xan'ов
Миша после bar'ов, слышишь, Миша после bar'ов
И на мне банда (Банда?)
Что в моём стакане? Это не простая Fanta
Она так сосёт, ей надо на шоу талантов
Но мы с ней не пара, понял после пары блантов, сука
Ты не мой partner, у меня был белый за последней партой
Да, я тот белый, сделал это, мама
Всё идёт по плану, это бандана
"""

BESY_TEXT = """Выходите, бесы, мы станцуем jersey
Отойди, я войду, и она воскреснет
Пристегнись и смотри, как тебе, Олеся?
Жопа каждой из моих подруг в AMG обвесе
Turn around, let me take my glock, я преследую цель
Твой хип-хап чисто «ха», не слышала ничё тупей
Какой ты рэпак, если хочешь выкупить мой трек?"""


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Привет! Кстати, Федя еблан"
    )


async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower().strip()

    if text == 'Бандана':
        await update.message.reply_text(BANDANA_TEXT)
    elif text == 'Бесы':
        await update.message.reply_text(BESY_TEXT)
    else:
        await update.message.reply_text(
            "Пошёл нахуй"
        )


async def error(update: Update, context: ContextTypes.DEFAULT_TYPE):
    logger.warning(f'Update {update} caused error {context.error}')


def main():
    # Получаем токен из переменных окружения
    TOKEN = os.getenv('8178786406:AAGW8d-BjnX9UjT0BpiSO3MVeeTmvxucpC0')
    if not TOKEN:
        raise ValueError("Не установлен BOT_TOKEN в переменных окружения")

    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message))
    application.add_error_handler(error)

    print("Бот запущен...")
    application.run_polling()


if __name__ == '__main__':
    main()