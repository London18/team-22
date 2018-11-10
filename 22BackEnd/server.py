
from pymongo import MongoClient
from stop_words import get_stop_words
import nltk
import pprint

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client['test']
collection = db['customer']
customer = db.customer

# pprint.pprint(customer.find_one())

qndict = customer.find_one()

### Parser Function ###

stop_words = set(get_stop_words('english'))


def myKeyWordParser(myString):
    myStringLowered = myString.lower()   
    word_tokens = nltk.tokenize.RegexpTokenizer('\\b\\w*[a-zA-Z]\\w+\\b').tokenize(myStringLowered)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


### End of Parser Function ####

def checkOccurrences(parsed_input):
    possible_questions = []
    for qn in qndict:
        input_ = qndict[qn]
        if qn == '_id':
            continue

        question_parsed = myKeyWordParser(input_['question'])
        counter = 0

        for myKeyWord in parsed_input:
            if myKeyWord in question_parsed:
                counter += 1
                if myKeyWord not in input_['keywords']:
                        input_['keywords'].append(myKeyWord)

        possible_questions.append((input_['question'], counter, input_['links']))
        
    pprint.pprint(possible_questions)
    pprint.pprint(qndict)
    

####### Parsing of user Question #######

input_1 = 'do you share data'
parsed_input = myKeyWordParser(input_1)
# input_2 = "Why do you not like my details?"
# parsed_input2 = myKeyWordParser(input_2)
####### End of Parsing  user question ########

checkOccurrences(parsed_input)
# checkOccurrences(parsed_input2)