import pandas as pd

def Vocabulary(csv_path=None,Level=5):
	source = csv_path
	df = pd.read_csv(source)[pd.read_csv(source)['Levels'] == Level]
	    # Randomly select one row from the DataFrame
	random_row = df.sample(n=1)
	return {
    		'word' : random_row["Words"].to_string(index=False),
    		'meaning' :  random_row["Meanings"].to_string(index=False),
    		'character' : random_row["Characters"].to_string(index=False),
    		'spelling' : random_row["Spellings"].to_string(index=False),
    		'level' : random_row["Levels"].to_string(index=False)
    			}

def main():
	print(Vocabulary("vocabulary.csv",4))
if __name__ == '__main__':
	main()

		