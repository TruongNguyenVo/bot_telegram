from telegram import InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler
import models
import sys
import random
def help_bot(update,context):
    text = f'/nvocab : new vocabulary \n/qvocab : quiz vocabulary \n/n5vocab : test jlpt for n5 vocabulary'
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
def quiz_jlpt_vocabulary(update,context):
    quiz = models.jlpt_n5_vocabulary()
    quiz['question']
    quiz['right_answer']
    quiz['answer_1']
    quiz['answer_2']
    quiz['answer_3']
    quiz['explain']
    quiz['meaning']

    context.chat_data['right_answer'] = quiz['right_answer']
    explain = f"{quiz['explain']} \nMeaning : {quiz['meaning']}"
    context.chat_data['explain'] = explain
    context.chat_data['type'] = 'quiz_n5_vocab'

    choices = [quiz['right_answer'],quiz['answer_1'],quiz['answer_2'],quiz['answer_3']]
    random.shuffle(choices)
    #setting radio button
    keyboard = [
        [InlineKeyboardButton(f"{choices[0]}", callback_data=f'{choices[0]}')],
        [InlineKeyboardButton(f"{choices[1]}", callback_data=f'{choices[1]}')],
        [InlineKeyboardButton(f"{choices[2]}", callback_data=f'{choices[2]}')],
        [InlineKeyboardButton(f"{choices[3]}", callback_data=f'{choices[3]}')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    question = f"Question : {quiz['question']}: "
    context.bot.send_message(chat_id=update.effective_chat.id, text=question, reply_markup=reply_markup)
    # Clear previous selected_option data
    context.user_data.pop('selected_option', None)



def quiz_vocab_bot(update, context):
    # get 4 vocab
    datas = []
    for count in range(0,4):
        datas.append(models.get_vocabulary())
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
    context.chat_data['type'] = 'quizvocab'

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
    question = f"{vocab_1} is meaning: "
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
        if (context.chat_data['type']  == "quizvocab"):
            continue_button = InlineKeyboardButton("Continue", callback_data='continue_quizvocab')
            reply_markup = InlineKeyboardMarkup([[continue_button]])
            context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)
        else:
            continue_button = InlineKeyboardButton("Continue", callback_data='contiue_n5_vocabuly')
            reply_markup = InlineKeyboardMarkup([[continue_button]])
            context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)
        
    elif choice == 'continue_quizvocab':
        print("quiz vocab")
        quiz_vocab_bot(update, context)
    elif choice == 'contiue_n5_vocabuly':   
        quiz_jlpt_vocabulary(update,context)  
        print("quiz n5")   
    else:
        context.bot.send_message(chat_id=query.message.chat_id, text=f"Wrong!")
        query.message.reply_text(f"Explain:\n{explain}")
        
        explanation_text = "Are you want to continue?"
        if (context.chat_data['type']  == "quizvocab"):
            continue_button = InlineKeyboardButton("Continue", callback_data='continue_quizvocab')
            reply_markup = InlineKeyboardMarkup([[continue_button]])
            context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)
        else:
            continue_button = InlineKeyboardButton("Continue", callback_data='contiue_n5_vocabuly')
            reply_markup = InlineKeyboardMarkup([[continue_button]])
            context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)
        

def new_vocab_bot(update, context):
    data = models.get_vocabulary()
    text = f"Word : {data['word']} \nMeaning : {data['meaning']} \nCharacter : {data['character']} \nSpelling : {data['spelling']} \nLevel : {data['level']}"
    context.bot.send_message(chat_id=update.effective_chat.id, text=text)
def start_bot(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello, my boss!")
def end_bot(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Goodbye, my boss!")
    global updater
    updater.stop()
    sys.exit() #stop script

def main():

    # Create an instance of the Updater and pass your bot token
    token_api = "6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y"
    updater = Updater(token=token_api, use_context=True)
    print("Start Bot")

    # Get the dispatcher to register handlers
    dispatcher = updater.dispatcher

    # Register the command handler
    statement_start = "start"
    dispatcher.add_handler(CommandHandler(statement_start, start_bot))
    
    statement_help = "help"
    dispatcher.add_handler(CommandHandler(statement_help, help_bot))

    statement_new_vocab = "nvocab"
    dispatcher.add_handler(CommandHandler(statement_new_vocab, new_vocab_bot))

    statement_jlpt_n5_vocab = "n5vocab"
    dispatcher.add_handler(CommandHandler(statement_jlpt_n5_vocab , quiz_jlpt_vocabulary))
    
    statement_end = "end"
    dispatcher.add_handler(CommandHandler(statement_end, end_bot))

    statement_quiz_vocab = "qvocab"
    dispatcher.add_handler(CommandHandler(statement_quiz_vocab, quiz_vocab_bot))
    
    dispatcher.add_handler(CallbackQueryHandler(button_quiz_bot))

    # Start the bot
    updater.start_polling()


if __name__ == '__main__':
    main()