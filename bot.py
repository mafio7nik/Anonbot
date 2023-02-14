import telebot
from telebot import types


bot = telebot.TeleBot('5931735900:AAGC_x2hp6EZTfgz7wg2m7tPQaLNQPfMq4A');
prm = "no"
getimage = False
message1 = "message"
@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    global getimage
    global message1
    message1 = message
    if not getimage :
        if message.text == "Привет":
            bot.send_message(message.from_user.id, "Привет, чем я могу тебе помочь?")
        elif message.text == "/help":
            bot.send_message(message.from_user.id, "Напиши привет")
        else:
            bot.send_message(message.from_user.id, "Я тебя не понимаю. Напиши /help.")
    if message.text == "/generate":
        getimage = True
        genimg = "true"
        bot.send_message(message.from_user.id, "Write Prompts")
        return get_prompt(genimf = True, message = message)

def get_prompt(message, genimf = None):
    markup = types.InlineKeyboardMarkup()
    button_generate = types.InlineKeyboardMarkup("Generate image")
    markup.add(button_generate)
    bot.send_message(message.from_user.id, "", reply_markup=markup)
def get_prompts(message):
    prm = message
    bot.send_message(message.from_user.id, "сохранено")

bot.polling(none_stop=True, interval=0)