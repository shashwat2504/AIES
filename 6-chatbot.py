pip install nltk
pip install newspaper3k


from newspaper import Article
import random
import string
import nltk
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np
import warnings

warnings.filterwarnings('ignore')



nltk.download('punkt', quiet=True)

article = Article('https://www.mayoclinic.org/diseases-conditions/chronic-kidney-disease/symptoms-causes/syc-20354521')
article.download()
article.parse()
article.nlp()

corpus = article.text

print(corpus)


text = corpus
sentence_list = nltk.sent_tokenize(text)

print(sentence_list)


def bot_response(user_input):
    user_input = user_input.lower()
    sentence_list.append(user_input)

    bot_response = ''

    cm = CountVectorizer().fit_transform(sentence_list)
    similarity_scores = cosine_similarity(cm[-1], cm)
    similarity_scores_list = similarity_scores.flatten()

    index = index_sort(similarity_scores_list)
    index = index[1:]

    response_flag = 0
    j = 0

    for i in range(len(index)):
        if similarity_scores_list[index[i]] > 0.0:
            bot_response = bot_response + ' ' + sentence_list[index[i]]
            response_flag = 1
            j = j + 1

        if j > 2:
            break

    if response_flag == 0:
        bot_response = bot_response + " " + "I apologize, I don't understand."

    sentence_list.remove(user_input)

    return bot_response




def index_sort(list_var):
    length = len(list_var)
    list_index = list(range(0, length))

    for i in range(length):
        for j in range(length):
            if list_var[list_index[i]] > list_var[list_index[j]]:
                list_index[i], list_index[j] = list_index[j], list_index[i]

    return list_index



def greeting_response(text):
    text = text.lower()

    bot_greetings = ['hi', 'hey', 'hello', 'hola']
    user_greetings = ['hi', 'hey', 'hello', 'hola', 'greetings']

    for word in text.split():
        if word in user_greetings:
            return random.choice(bot_greetings)




print("Doc Bot: I am doc bot for your services for short time i will answer your questions")

exit_list = ['exit', 'see you later', 'bye', 'quit', 'break']

while True:
    user_input = input()

    if user_input.lower() in exit_list:
        print("Doc Bot: Chat with you later!")
        break

    else:
        if greeting_response(user_input) is not None:
            print('Doc Bot: ' + greeting_response(user_input))

        else:
            print('Doc Bot: ' + bot_response(user_input))













# import nltk
# from newspaper import Article
# from nltk.tokenize import sent_tokenize, word_tokenize
# from nltk.corpus import stopwords

# nltk.download('punkt')
# nltk.download('punkt_tab')
# nltk.download('stopwords')

# # Get article
# article = Article('https://en.wikipedia.org/wiki/Influenza')
# article.download()
# article.parse()

# sentences = sent_tokenize(article.text)
# stop_words = set(stopwords.words('english'))

# # Find answer
# def get_answer(question):
#     q = set(word_tokenize(question.lower())) - stop_words
#     best, score = "", 0

#     for s in sentences:
#         words = set(word_tokenize(s.lower())) - stop_words
#         count = len(q & words)

#         if count > score:
#             best, score = s, count

#     return best

# # Chatbot
# print("Chatbot ready! Type bye to exit.")

# while True:
#     user = input("You: ").lower()

#     if user in ['bye', 'exit', 'quit']:
#         print("Bot: Goodbye!")
#         break

#     elif user in ['hi', 'hello', 'hey']:
#         print("Bot: Hello! Ask me about influenza.")

#     else:
#         answer = get_answer(user)
#         print("Bot:", answer if answer else "No answer found.")
