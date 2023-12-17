from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import requests, json
import random
def get_vocabulary():
    url = "https://jlpt-vocab-api.vercel.app/api/words/random"
    response = requests.get(url).json()
    return {
    'word' : response['word'],
    'meaning' : response['meaning'],
    'character' : response['furigana'],
    'spelling' : response['romaji'],
    'level' : response['level']
    }

def quiz_bot(update, context):
    # get 4 vocab
    datas = []
    for count in range(0,4):
        datas.append(get_vocabulary())
    # take word 1 is quiz
    vocab_1 = datas[0]["word"]
    meaning_1 = datas[0]['meaning']
    character_1 = datas[0]['character']
    spelling_1 = datas[0]['spelling']
    level_1 = datas[0]['level']
       
    #right answer for quiz
    context.chat_data['right_answer'] = meaning_1
    explain = f'Word : {vocab_1} \nMeaning : {meaning_1} \nCharacter : {character_1} \nSpelling : {spelling_1} \nLevel : {level_1}'
    context.chat_data['explain'] = explain

    vocab_2 = datas[1]["word"]
    meaning_2 = datas[1]['meaning'] 
    
    vocab_3 = datas[2]["word"]
    meaning_3 = datas[2]['meaning'] 
    
    vocab_4 = datas[3]["word"]
    meaning_4 = datas[3]['meaning']

    meanings = [meaning_1,meaning_2,meaning_3,meaning_4]
    random.shuffle(meanings)
    #setting radio button
    keyboard = [
        [InlineKeyboardButton(f"{meanings[0]}", callback_data=f'{meanings[0]}')],
        [InlineKeyboardButton(f"{meanings[1]}", callback_data=f'{meanings[1]}')],
        [InlineKeyboardButton(f"{meanings[2]}", callback_data=f'{meanings[2]}')],
        [InlineKeyboardButton(f"{meanings[3]}", callback_data=f'{meanings[3]}')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    question = f"{vocab_1} {'(' + spelling_1 + ')'} is meaning: "
    context.bot.send_message(chat_id=update.effective_chat.id, text=question, reply_markup=reply_markup)
    # Clear previous selected_option data
    context.user_data.pop('selected_option', None)


    # update.message.reply_text(question, reply_markup=reply_markup)

def button_quiz_bot(update, context):
    query = update.callback_query
    choice = query.data
    query.answer()
    right_answer = context.chat_data['right_answer']
    explain = context.chat_data['explain']
    if choice == right_answer:
        context.bot.send_message(chat_id=query.message.chat_id, text=f"Right! Congratulations.")
        query.message.reply_text(f"Explain:\n{explain}")

        explanation_text = "Are you want to continue?"
        continue_button = InlineKeyboardButton("Continue", callback_data='continue')
        reply_markup = InlineKeyboardMarkup([[continue_button]])
        context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)
    elif choice == 'continue':
        quiz_bot(update, context)        
    else:
        context.bot.send_message(chat_id=query.message.chat_id, text=f"Wrong!")
        query.message.reply_text(f"Explain:\n{explain}")
        
        explanation_text = "Are you want to continue?"
        continue_button = InlineKeyboardButton("Continue", callback_data='continue')
        reply_markup = InlineKeyboardMarkup([[continue_button]])
        context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)


def vocab_bot(update, context):
    data = get_vocabulary()
    text = f"Word : {data['word']} \nMeaning : {data['meaning']} \nCharacter : {data['character']} \nSpelling : {data['spelling']} \nLevel : {data['level']}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
def start_bot(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, my boss!")
def end_bot(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Goodbye, my boss!")
    global updater
    updater.stop()

def main():

    # Create an instance of the Updater and pass your bot token
    token_api = "6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y"
    updater = Updater(token=token_api, use_context=True)

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler
    statement_start = "start"
    dispatcher.add_handler(CommandHandler(statement_start, start_bot))
    
    statement_vocab = "vocab"
    dispatcher.add_handler(CommandHandler(statement_vocab, vocab_bot))
    
    statement_end = "end"
    dispatcher.add_handler(CommandHandler(statement_end, end_bot))

    statement_quiz = "quiz"
    dispatcher.add_handler(CommandHandler("quiz", quiz_bot))
    dispatcher.add_handler(CallbackQueryHandler(button_quiz_bot))

    # Start the bot
    updater.start_polling()


if __name__ == '__main__':
    main()