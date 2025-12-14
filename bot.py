import telebot
from config import TOKEN
from logic import DatabaseManager, hide_img

bot = telebot.TeleBot(TOKEN)
manager = DatabaseManager("database/prizes.db")

@bot.message_handler(commands=['start'])
def start(message):
    manager.add_user(message.chat.id, message.chat.username)
    prize_id, img = manager.get_random_prize()
    hide_img(img)

    with open(f'hidden_img/{img}', 'rb') as photo:
        bot.send_photo(message.chat.id, photo, caption="Нажми «Получить»")

    manager.mark_prize_used(prize_id)
    manager.add_winner(message.chat.id, prize_id)

bot.polling()
