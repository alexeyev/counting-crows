# coding: utf-8

import configparser
import logging
import camera
import telebot

logger = logging.getLogger("counting-crops")
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler("everything.log")
fh.setLevel(logging.DEBUG)
logger.addHandler(fh)

parser = configparser.ConfigParser()
parser.read("configs/bot_config.ini")
ACCESS_KEY = parser["telegram"]["key"]

bot = telebot.TeleBot(ACCESS_KEY, num_threads=4)
content_types = "audio, sticker, video, video_note, location, contact, new_chat_members, " \
                "left_chat_member, new_chat_title, new_chat_photo, delete_chat_photo, group_chat_created, " \
                "supergroup_chat_created, channel_chat_created, migrate_to_chat_id, migrate_from_chat_id, " \
                "pinned_message, document, photo, text".split(", ")


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    logger.debug(message)
    bot.reply_to(message, "Привет, это бот, который докладывает обстановку. Ещё в процессе разработки. "
                          "Используйте команду /bang.")


@bot.message_handler(commands=["bang"])
def process_bang(message):
    logger.debug(message)
    username = message.from_user.username
    date = message.date
    prefix = "data/%d_%d_%s" % (date, message.message_id, username)
    image = camera.shoot(prefix)
    bot.send_photo(message.chat.id, image, caption="""¯\\_(ツ)_/¯""")


@bot.message_handler(content_types=["voice"])
def handle_voice(message):
    logger.debug(message)
    bot.reply_to(message, "Не очень удобно сейчас слушать голосовые, давайте лучше командами.")


@bot.message_handler(content_types=content_types)
def handle_other(message):
    logger.debug(message)
    bot.reply_to(message, "Увы, бот воспринимает только команды, начинающиеся на \"/\".")


bot.polling()
