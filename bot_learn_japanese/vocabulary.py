'''
file lấy dữ liệu về các từ 
'''
import requests
import json
def get():
	'''
	api
	https://jlpt-vocab-api.vercel.app/api/words/random
	'''
	url = "https://jlpt-vocab-api.vercel.app/api/words/random"
	response = requests.get(url).json()
	'''
	data respone 
	{'word': 'ふざける', 
	'meaning': 
	'to romp, to gambol, to frolic, to joke', 
	'furigana': '', 
	'romaji': 'fuzakeru', 
	'level': 2}
	'''

	return response['word']
print(get())

		
