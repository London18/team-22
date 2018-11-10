
from pymongo import MongoClient
from stop_words import get_stop_words
import nltk
import pprint

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client['MYDB']
collection = db['customer']
customer = db.customer

# pprint.pprint(customer.find_one())

qndict = customer.find_one()

### Parser Function ###

stop_words = set(get_stop_words('english'))


def myKeyWordParser(myString):
    word_tokens = nltk.tokenize.RegexpTokenizer('\\b\\w*[a-zA-Z]\\w+\\b').tokenize(myString)
    filtered_sentence = []
    for w in word_tokens:
        if w not in stop_words:
            filtered_sentence.append(w)
    return filtered_sentence


### End of Parser Function ####

####### Parsing of user Question #######

input_1 = 'do you share data'.lower()
parsed_input = myKeyWordParser(input_1)


####### End of Parsing  user question ########

def checkOccurrences(parsed_input):
    possible_questions = []
    for qn in qndict:
        input_ = qndict[qn]
        if qn == '_id':
            continue

        question_parsed = myKeyWordParser(input_['question'].lower())
        counter = 0
        for keyword in parsed_input:
            if keyword in question_parsed:
                counter += 1
                print(counter)
            # if keyword not in input_['keywords']:
            #     input_['keywords'].append(keyword)
            possible_questions.append((input_['question'], counter, input_['links']))
    print(possible_questions)


checkOccurrences(parsed_input)