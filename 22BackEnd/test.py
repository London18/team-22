from pymongo import MongoClient
from stop_words import get_stop_words
import nltk
import pprint

client = MongoClient()
client = MongoClient('localhost', 27017)

db = client['test']
customer = db.customer

qndict = customer.find_one()
qndictOld = qndict.copy()

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


storeMyAwnsers = []
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
        #change question to awnser for actual output
        possible_questions.append((input_['answer'], counter, input_['links']))
    storeMyAwnsers.append(sorted(possible_questions, reverse = True, key = lambda x: x[1]))
    

#     customer.replace_one({ },qndict)    

    

####### Parsing of user Question #######
input_1 = 'do xvkjk xckjvnxckvnxckl xcvkjncklvdlkf share data you xcnbvjhl, be careful'
input_2 = "Why do you not like my details?"
parsed_input = myKeyWordParser(input_1)
parsed_input2 = myKeyWordParser(input_2)
####### End of Parsing  user question ########

checkOccurrences(parsed_input)
checkOccurrences(parsed_input2)

counter = 1
for eachAnswer in storeMyAwnsers:
        
        print("The {}st answer is................... ".format(counter))
        print(eachAnswer[0])
        counter += 1

# pprint.pprint(storeMyAwnsers)
