import telebot
from telebot import types

bot = telebot.TeleBot('5464599994:AAFQYI1epbWDM_SC72H13c2L7rhIVajBg00')

@bot.message_handler(commands=["start"])
def main(message):
    keyboard = types.InlineKeyboardMarkup()
    url_btn = types.InlineKeyboardButton(text="Queen", url="https://sefon.pro/artist/3251-queen/")
    url_btn2 = types.InlineKeyboardButton(text="The Beatles", url="https://sefon.pro/artist/28429-the-beatles/")
    url_btn3 = types.InlineKeyboardButton(text="AC-DC", url="https://sefon.pro/artist/10904-ac-dc/")
    url_btn4 = types.InlineKeyboardButton(text="Pink Floyd", url="https://sefon.pro/artist/1182-pink-floyd/")
    url_btn5 = types.InlineKeyboardButton(text="Depeche Mode", url="https://sefon.pro/artist/3325-depeche-mode/")
    url_btn6 = types.InlineKeyboardButton(text="Kiss", url="https://sefon.pro/artist/10895-kiss/")
    url_btn7 = types.InlineKeyboardButton(text="Whitesnake", url="https://sefon.pro/artist/1161-whitesnake/")
    url_btn8 = types.InlineKeyboardButton(text="Deep Purple", url="https://sefon.pro/artist/6149-deep-purple/")
    url_btn9 = types.InlineKeyboardButton(text="Elvis Presley", url="https://sefon.pro/artist/7035-elvis-presley/")
    url_btn1 = types.InlineKeyboardButton(text="Guns'n'roses", url="https://sefon.pro/artist/1197-guns-n-roses/")
    keyboard.add(url_btn, url_btn1, url_btn2, url_btn3, url_btn4, url_btn5, url_btn6, url_btn7, url_btn8, url_btn9)

    bot.send_message(message.chat.id, "Выбери что-то для души)", reply_markup=keyboard)

if __name__ == '__main__':

    bot.polling(none_stop=True)