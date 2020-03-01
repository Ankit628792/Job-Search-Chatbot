pip install nltk

pip install newspaper3k


from newspaper import Article
import random
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
import numpy as np
import warnings

warnings.filterwarnings('ignore')

nltk.download('punkt', quiet=True)
nltk.download('wordnet', quiet=True)

article = Article('https://www.themuse.com/advice/the-9-best-things-you-can-read-before-you-start-your-new-job')
article.download()
article.parse()
article.nlp()
corpus = article.text


print(corpus)

text = corpus
sent_tokens = nltk.sent_tokenize(text) 


print(sent_tokens)

remove_punct_dict = dict(  ( ord(punct),None) for punct in string.punctuation)


print(string.punctuation)


print(remove_punct_dict)

def LemNormalize(text):
  return nltk.word_tokenize(text.lower().translate(remove_punct_dict))

#Print the tokenization text
print(LemNormalize(text))

GREETING_INPUTS = ["hi", "hello", "hola", "greetings", "wassup", "hey"]

#Greeting responses back to the user
GREETING_RESPONSES=["howdy", "hi", "hey", "what's good", "hello", "hey there"]

#Function to return a random greeting response to a users greeting
def greeting(sentence):
  #if the user's input is a greeting, then return a randomly chosen greeting response
  for word in sentence.split():
    if word.lower() in GREETING_INPUTS:
      return random.choice(GREETING_RESPONSES)

def response(user_response):
  

  user_response = user_response.lower()

  

  
  robo_response = ''


  sent_tokens.append(user_response)

 


  TfidfVec = TfidfVectorizer(tokenizer = LemNormalize, stop_words='english')


  tfidf = TfidfVec.fit_transform(sent_tokens)
  



  vals = cosine_similarity(tfidf[-1], tfidf)

 

  idx = vals.argsort()[0][-2]

 
  flat = vals.flatten()

  
  flat.sort()


  score = flat[-2]

  if(score == 0):
    robo_response = robo_response+"I apologize, I don't understand."
  else:
    robo_response = robo_response+sent_tokens[idx]
  
 
  sent_tokens.remove(user_response)
  
  return robo_response

flag = True
print("JobSearch: I am Job Searchng Bot or JobBot for short. I will help to fnd the new job . If you want to exit, type Bye!")
while(flag == True):
  user_response = input()
  user_response = user_response.lower()
  if(user_response != 'bye'):
    if(user_response == 'thanks' or user_response =='thank you'):
      flag=False
      print("JobSearch: You are welcome !")
    else:
      if(greeting(user_response) != None):
        print("JobSearch: "+greeting(user_response))
      else:
        print("JobSearch: "+response(user_response))       
  else:
    flag = False
    print("JobSearch: Chat with you later !")
