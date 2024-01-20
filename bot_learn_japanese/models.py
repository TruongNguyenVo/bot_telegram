import random
import pandas as pd
pd.set_option('display.max_colwidth', None)
pd.set_option('display.max_columns', None)
def get_vocabulary(level=5):
    file_path = "vocabulary.csv"  # Replace with the actual file path
    df = pd.read_csv(file_path)[pd.read_csv(file_path)['Levels'] == level]

    # Randomly select one row from the DataFrame
    random_row = df.sample(n=1)

    # Print the randomly selected row
    return {
    'word' : random_row["Words"].to_string(index=False),
    'meaning' :  random_row["Meanings"].to_string(index=False),
    'character' : random_row["Characters"].to_string(index=False),
    'spelling' : random_row["Spellings"].to_string(index=False),
    'level' : random_row["Levels"].to_string(index=False)
    }
def jlpt_n5_vocabulary():
    file_path = "dethi n5\\questions_n5_vocabulary.csv"
    df = pd.read_csv(file_path)
    random_row = df.sample(n=1)
    return {
    'question' : random_row['Question'].to_string(index=False),
    'right_answer' : random_row['RightAnswer'].to_string(index=False),
    'answer_1' : random_row['Answer_1'].to_string(index=False),
    'answer_2' : random_row['Answer_2'].to_string(index=False),
    'answer_3' : random_row['Answer_3'].to_string(index=False),
    'explain' : random_row['Explain'].to_string(index=False),
    'meaning' : format_meaning_vocabulary_n5(random_row['Meaning'].to_string(index=False))

    }
def format_meaning_vocabulary_n5(text=None):
    if(text == "NaN"):
        return None
    else:
        right_format_text = text.replace("|", "\n")
        return right_format_text
