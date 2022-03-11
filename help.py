import telebot
import urllib.request
import datetime

token = '***'
bot = telebot.TeleBot(token)


@bot.message_handler(content_types=["text", "sticker", "pinned_message", "photo", "audio"])
def get_text_messages(message):
    if message.text == "/search":
        bot.send_message(message.chat.id, "Отправь изображение обложки учебника")
        bot.register_next_step_handler(message, get_image)
    elif message.text == "/help":
        bot.send_message(message.chat.id, "Напиши /search")


def get_image(message):
    # print(message)
    # print(message.json['photo'])
    # print(message.json['photo'][1]['file_id'])
    image = message.json['photo'][1]['file_id']
    bot.send_photo(message.chat.id, image)
    res = bot.get_file(image)
    file_type_temp = res.file_path.split(".")
    file_type = file_type_temp[1]
    urllib.request.urlretrieve("https://api.telegram.org/file/bot" + token + "/" + res.file_path, 'local_' + " " + file_type)
    print(res)


bot.infinity_polling()