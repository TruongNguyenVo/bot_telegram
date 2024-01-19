token = "6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y"

# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# # Define the function to handle the /start command
# def start(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Option 1", callback_data='1')],
#         [InlineKeyboardButton("Option 2", callback_data='2')],
#         [InlineKeyboardButton("Option 3", callback_data='3')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Please select an option:', reply_markup=reply_markup)

# # Define the function to handle button presses
# def button(update, context):
#     query = update.callback_query
#     option = query.data
#     query.answer()
#     context.bot.send_message(chat_id=query.message.chat_id, text=f"You selected option {option}")
#     updater.stop()
# # Create an instance of the Updater and pass your bot token
# updater = Updater(token="6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y", use_context=True)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # Register the command handler
# dispatcher.add_handler(CommandHandler("start", start))

# # Register the callback query handler
# dispatcher.add_handler(CallbackQueryHandler(button))

# # Start the bot
# updater.start_polling()
#-------------------------------------------------------------------

# import random

# my_list = [1, 2, 3, 4]

# # Randomly select an element from the list
# for i in range(1,5):
# 	random_element = random.choice(my_list)
# 	my_list.remove(random_element)
# 	print("Randomly selected element:", random_element)

#-------------------------------------------------------------------
# import random

# my_list = [1, 2, 3, 4]

# # Shuffle the elements in the list
# random.shuffle(my_list)

# print("Shuffled list:", my_list[0])

#-----------------------------------------------------------------------
# one = 1
# two = ''
# print(f"this is {one} and {'(' + two + ')'} ")
#--------------------------------------------------------------------
# list = [1,2,3,4]
# for i in range(0,len(list)):
# 	print(list[i])
# ------------------------------------------------------------
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# # Define the function to handle the /start command
# def start(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Option 1", callback_data='1')],
#         [InlineKeyboardButton("Option 2", callback_data='2')],
#         [InlineKeyboardButton("Option 3", callback_data='nguyen')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)

#     # Store additional data in context for later use
#     context.chat_data['additional_data'] = 'This is additional data'

#     update.message.reply_text('Please select an option:', reply_markup=reply_markup)

# # Define the function to handle button presses
# def button(update, context):
#     query = update.callback_query
#     selected_option = query.data
#     query.answer()

#     # Retrieve additional data from context
#     additional_data = context.chat_data['additional_data']

#     # Store the selected option in user's data
#     context.user_data['selected_option'] = selected_option

#     # Update the message with the selected option and additional data
#     query.edit_message_text(text=f"You selected option {selected_option}")
#     query.message.reply_text(f"Additional data: {additional_data}")
#     updater.stop()

# # Create an instance of the Updater and pass your bot token
# updater = Updater(token="6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y", use_context=True)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # Register the command handler
# dispatcher.add_handler(CommandHandler("start", start))

# # Register the callback query handler
# dispatcher.add_handler(CallbackQueryHandler(button))

# # Start the bot
# updater.start_polling()

#------------------------------------------------------
# import requests
# import random
# def get_vocabulary():
#     url = "https://jlpt-vocab-api.vercel.app/api/words/random"
#     response = requests.get(url).json()
#     return {
#     'word' : response['word'],
#     'meaning' : response['meaning'],
#     'character' : response['furigana'],
#     'spelling' : response['romaji'],
#     'level' : response['level']
#     }
# datas = []
# for count in range(0,4):
#     datas.append(get_vocabulary())
# # take word 1 is quiz
# vocab_1 = datas[0]["word"]
# meaning_1 = datas[0]['meaning']
# character_1 = datas[0]['character']
# spelling_1 = datas[0]['spelling']
# level_1 = datas[0]['level']
   
# vocab_2 = datas[1]["word"]
# meaning_2 = datas[1]['meaning'] 
    
# vocab_3 = datas[2]["word"]
# meaning_3 = datas[2]['meaning'] 
    
# vocab_4 = datas[3]["word"]
# meaning_4 = datas[3]['meaning']

# print(datas[3]['meaning'])

# meanings = [meaning_1,meaning_2,meaning_3,meaning_4]
# print(meanings)
# random.shuffle(meanings)
# print(meanings)
#-------------------------------------------------------------------
# from telegram import ReplyKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# # Define the function to handle the /start command
# def start(update, context):
#     update.message.reply_text("Please enter your statement:")

# # Define the function to handle user messages
# def handle_message(update, context):
#     user_message = update.message.text

#     # Process the user's statement here
#     # ...

#     # Reply with the completion message and the "Continue" button
#     reply_markup = ReplyKeyboardMarkup([['Continue']])
#     update.message.reply_text("Statement completed!", reply_markup=reply_markup)

# # Define the function to handle the "Continue" button
# def handle_continue(update, context):
#     update.message.reply_text("You clicked Continue!")

# # Create an instance of the Updater and pass your bot token
# updater = Updater(token="6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y", use_context=True)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # Register the command handler
# dispatcher.add_handler(CommandHandler("start", start))

# # Register the message handler
# dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))

# # Register the handler for the "Continue" button
# dispatcher.add_handler(MessageHandler(Filters.regex('^(Continue)$'), handle_continue))

# # Start the bot
# updater.start_polling()
#------------------------------------------------------------------
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# # Define the function to handle the /start command
# def start(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Option 1", callback_data='1')],
#         [InlineKeyboardButton("Option 2", callback_data='2')],
#         [InlineKeyboardButton("Option 3", callback_data='3')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     update.message.reply_text('Please select an option:', reply_markup=reply_markup)

# # Define the function to handle button presses
# def button(update, context):
#     query = update.callback_query
#     selected_option = query.data
#     query.answer()

#     if selected_option == '1':
#         explanation_text = "This is an explanation for Option 1."
#         continue_button = InlineKeyboardButton("Continue", callback_data='continue')
#         reply_markup = InlineKeyboardMarkup([[continue_button]])
#         query.edit_message_text(text=explanation_text, reply_markup=reply_markup)
#     elif selected_option == 'continue':
#         query.edit_message_text(text="You clicked Continue!")

# # Create an instance of the Updater and pass your bot token
# updater = Updater(token="6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y", use_context=True)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # Register the command handler
# dispatcher.add_handler(CommandHandler("start", start))

# # Register the callback query handler
# dispatcher.add_handler(CallbackQueryHandler(button))

# # Start the bot
# updater.start_polling()
#-----------------------------------------------------------------------
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# # Define the function to handle the /start command
# def start(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Option 1", callback_data='1')],
#         [InlineKeyboardButton("Option 2", callback_data='2')],
#         [InlineKeyboardButton("Option 3", callback_data='3')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     context.bot.send_message(chat_id=update.effective_chat.id, text=f"You selected option {selected_option}")
#     update.message.reply_text('Please select an option:', reply_markup=reply_markup)
#     # Clear previous selected_option data
#     context.user_data.pop('selected_option', None)

# # Define the function to handle button presses
# def button(update, context):
#     query = update.callback_query
#     selected_option = query.data
#     query.answer()

#     if selected_option == '1':
#         explanation_text = "This is an explanation for Option 1."
#         continue_button = InlineKeyboardButton("Continue", callback_data='continue')
#         reply_markup = InlineKeyboardMarkup([[continue_button]])
#         context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)
#         context.user_data['selected_option'] = '1'
#     elif selected_option == 'continue':
#         if 'selected_option' in context.user_data:
#             start(update, context)
#         else:
#             context.bot.send_message(chat_id=update.effective_chat.id, text='No option selected. Please select an option:')

#     else:
#         context.bot.send_message(chat_id=update.effective_chat.id, text=f"You selected option {selected_option}")

# # Create an instance of the Updater and pass your bot token
# updater = Updater(token="6529100020:AAG894nsmLa_vB6Igk-UvEPWnvlsycaz91Y", use_context=True)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # Register the command handler
# dispatcher.add_handler(CommandHandler("start", start))

# # Register the callback query handler
# dispatcher.add_handler(CallbackQueryHandler(button))

# # Start the bot
# updater.start_polling()

#-----------------------------------------------------------
# from telegram import InlineKeyboardButton, InlineKeyboardMarkup
# from telegram.ext import Updater, CommandHandler, CallbackQueryHandler

# # Define the function to handle the /start command
# def start(update, context):
#     keyboard = [
#         [InlineKeyboardButton("Option 1", callback_data='1')],
#         [InlineKeyboardButton("Option 2", callback_data='2')],
#         [InlineKeyboardButton("Option 3", callback_data='3')]
#     ]
#     reply_markup = InlineKeyboardMarkup(keyboard)
#     context.bot.send_message(chat_id=update.effective_chat.id, text='Please select an option:', reply_markup=reply_markup)
#     # Clear previous selected_option data
#     context.user_data.pop('selected_option', None)

# # Define the function to handle button presses
# def button(update, context):
#     query = update.callback_query
#     selected_option = query.data
#     query.answer()

#     if selected_option == '1':
#         explanation_text = "This is an explanation for Option 1."
#         continue_button = InlineKeyboardButton("Continue", callback_data='continue')
#         reply_markup = InlineKeyboardMarkup([[continue_button]])
#         context.bot.send_message(chat_id=query.message.chat_id, text=explanation_text, reply_markup=reply_markup)
#         context.user_data['selected_option'] = '1'
#     elif selected_option == 'continue':
#         if 'selected_option' in context.user_data:
#             start(update, context)
#         else:
#             context.bot.send_message(chat_id=update.effective_chat.id, text='No option selected. Please select an option:')
#     else:
#         context.bot.send_message(chat_id=update.effective_chat.id, text=f"You selected option {selected_option}")

# # Create an instance of the Updater and pass your bot token
# updater = Updater(token=token, use_context=True)

# # Get the dispatcher to register handlers
# dispatcher = updater.dispatcher

# # Register the command handler
# dispatcher.add_handler(CommandHandler("start", start))

# # Register the callback query handler
# dispatcher.add_handler(CallbackQueryHandler(button))

# # Start the bot
# updater.start_polling()
#-----------------------------------------------------------------
# import telegram

# print(telegram.__version__)
#-------------------------------------------------------
# import requests
# import json
# def main():
# 	url = "https://jlpt-vocab-api.vercel.app//api/words/all"
# 	response = requests.get(url).json()
# 	# Open the file in write mode
# 	file_path = "vocabulary.txt"  # Replace with the actual file path
# 	file = open(file_path, "w",encoding="utf-8")


# 	# Write content to the file
# 	file.write(str(response))

# 	# Close the file
# 	file.close()
# 	print("done")
# main()
#--------------------------------------------------
# import pandas as pd
# file_path = "vocabulary.txt"  # Replace with the actual file path
# file = open(file_path, "r", encoding = 'utf-8')

# # Read the contents of the file
# content = file.read()

# # Close the file
# file.close()

# # Print the file content
# datas = eval(content)
# words = []
# meanings = []
# characters = []
# spellings = []
# levels = []

# for data in datas:
# 	words.append(data['word'])
# 	meanings.append(data['meaning'])
# 	characters.append(data['furigana'])
# 	spellings.append(data['romaji'])
# 	levels.append(data['level'])


# data = {
#     "Words": words,
#     "Meanings": meanings,
#     "Characters": characters,
#     "Spellings" : spellings,
#     "Levels" : levels
# }

# # Create a DataFrame from the dictionary
# df = pd.DataFrame(data)

# # File path to save the CSV file
# file_path = "vocabulary.csv"  # Replace with the actual file path

# # Save the DataFrame as a CSV file
# df.to_csv(file_path, index=False)

# print("CSV file saved successfully.")
#-----------------------------------------------------
# import pandas as pd

# # File path of the CSV file
# file_path = "vocabulary.csv"  # Replace with the actual file path

# # Read the CSV file into a DataFrame
# df = pd.read_csv(file_path)[pd.read_csv(file_path)['Levels'] == 5]

# # Randomly select one row from the DataFrame
# random_row = df.sample(n=1)



# # Print the randomly selected row
# text = random_row
# print(text)
# ----------------------------------------
