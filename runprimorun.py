# -*- coding: utf-8 -*-
import telebot

from utils import myglobals
from control import channelMgr
from control import phraseMgr
from control import putasMgr
from control import funnyChat

bot = telebot.TeleBot(myglobals.TOKEN)


@bot.message_handler(commands=['start'])
def send_start(message):
    channelMgr.Check2Save(message.chat.id)
    bot.reply_to(message, "Que puta vida, hoy amaneci sarcastico!!")
    myglobals.START = True


@bot.message_handler(commands=['stop'])
def send_stop(message):
    bot.reply_to(message, "Vaya, que sorpresa...")
    myglobals.START = False


@bot.message_handler(commands=['help'])
def send_help(message):
    myhelp = "Su mama de todos. Blah!!"
    myhelp += "\n/start inicio frases a peticion"
    myhelp += "\n/stop paro frases a peticion"
    myhelp += "\n/phrase digo una frase"
    myhelp += "\n/addphrase [phrase] agrego una frase asi que cuidado!! No acentos chavos"
    myhelp += "\n/delphrase [num] elimino una frase mas cuidado!!"
    myhelp += "\n/numphrases te digo cuantas hay..."
    myhelp += "\nHey!! intenta esto <@elprimobot putas>"
    myhelp += "\addputa [@puta]"
    myhelp += "\addputasphrase [phrase]"
    bot.reply_to(message, myhelp)


@bot.message_handler(commands=['phrase'])
def send_phrase(message):
    if myglobals.PHRASES:
        if  myglobals.START:
            randomANDphrase = phraseMgr.getRandomAndPhrase()
            bot.reply_to(message, "[" + str(randomANDphrase['random'] + 1) + "]" + randomANDphrase['phrase'])
        else:
            bot.reply_to(message, "No Estoy Activo... Pudranse Todos!!")


@bot.message_handler(commands=['numphrases'])
def count_phrases(message):
    if myglobals.PHRASES:
        bot.reply_to(message, "Ah!! como joden... son un total de [" + str(len(myglobals.PHRASES)) + "]")


@bot.message_handler(commands=['addphrase'])
def add_phrase(message):
    if phraseMgr.addPhraseAndUpdate(message):
        bot.reply_to(message, "Y una vez mas #lavidaapesta ... Listo El Deploy Chavos!!")
    else:
        bot.reply_to(message, "Sean serios...e s     s i n      a c e n t o s!!")


@bot.message_handler(commands=['delphrase'])
def del_phrase(message):
    if phraseMgr.delPhraseAndUpdate(message):
        bot.reply_to(message, "Esta frase eliminada es lo mas positivo del dia de hoy...")
    else:
        bot.reply_to(message, "Chavos tomense la vida en serio, si es numero manden un numero...")


@bot.message_handler(commands=['addputa'])
def add_putas(message):
    if putasMgr.addPutasAndUpdate(message):
        bot.reply_to(message, "Pero dejad que las putas se acerquen a mí!!")
    else:
        bot.reply_to(message, "Sean serios...@ e s     s i n      a c e n t o s!!")


@bot.message_handler(commands=['addputasphrase'])
def add_putas_phrase(message):
    if putasMgr.addPutasPhraseAndUpdate(message):
        bot.reply_to(message, "En serio? Es lo mejor que puedes escribir?")
    else:
        bot.reply_to(message, "Sean serios...@ e s     s i n      a c e n t o s!!")


@bot.inline_handler(lambda query: query.query == 'putas')
def query_text(inline_query):
    try:
        r1 = telebot.types.InlineQueryResultArticle('1', 'Random Puta Guess Who', telebot.types.InputTextMessageContent('-random-'))
        bot.answer_inline_query(inline_query.id, [r1])
    except Exception as e:
        print(e)


@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, funnyChat.mywhores(message.text))

channelMgr.loadChannels()
channelMgr.sayHello2Channels(bot)
phraseMgr.loadPhrases()
putasMgr.loadPutas()
putasMgr.loadPutasPhrases
bot.polling()