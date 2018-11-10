from pymongo import MongoClient

from stop_words import get_stop_words
import nltk

import pprint

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client['MYDB']
collection = db['customer']
customer = db.customer

pprint.pprint(customer.find_one())
qndict = customer.find_one()

### Parser Function ###
stop_words = set(get_stop_words('english'))
def myKeywordParser(myString):
	word_tokens = nltk.word_tokenize(myString)
  filtered_Sentence = []
  for w in word_tokens:
		if w not in stop_words:
			filtered_sentence.append(w)
	return filtered_sentence

####### Parsing of user Question #######
input_1 = "do you share data"
parsed_input = myKeyWorldParser(input_1)
####### End of Parsing  user question ########

question_filter = []

for qn in qndict:
    input_ = qndict[qn]

    if qn == '_id':
        continue
    
    question_filter.append(myKeywordParser(input_))

print(question_filter)
