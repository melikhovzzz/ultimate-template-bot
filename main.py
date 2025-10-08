from config import token
import telebot
from random import choice
bot = telebot.TeleBot(token)

jokes = [
    "Трое неизвестных... порвали паспорт прохожему. Неизвестных стало 4 :)"
]

quotes = [
    "Жизнь - это то, что с тобой происходит, пока ты строишь планы. Джон Леннон."
]

facts = [
    " Ежедневно жители США съедают 18 гектаров пиццы."
]


# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
def send_welcome(message):
    bot.reply_to(message, """\
Hi there, I am EchoBot.
I am here to echo your kind words back to you. Just say anything nice and I'll say the exact same thing to you!\
""")


@bot.message_handler(commands=['coin'])
def coin_handler(message):
    coin = choice(["Орел", "Решка"])
    bot.reply_to(message, coin)

@bot.message_handler(commands=['joke'])
def joke_handler(message):
    joke = choice(jokes)
    bot.reply_to(message, joke)

@bot.message_handler(commands=['quote'])
def quote_handler(message):
    quote = choice(quotes)
    bot.reply_to(message, quote)

@bot.message_handler(commands=['fact'])
def fact_handler(message):
    fact = choice(facts)
    bot.reply_to(message, fact)

bot.infinity_polling()