from telegram.ext import Updater, CommandHandler
import requests, json
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

    # Start the bot
    updater.start_polling()


if __name__ == '__main__':
    main()