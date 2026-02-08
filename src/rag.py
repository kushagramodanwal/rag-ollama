

corpus_of_documents = [
    "Take a leisurely walk in the park and enjoy the fresh air.",
    "Visit a local museum and discover something new.",
    "Attend a live music concert and feel the rhythm.",
    "Go for a hike and admire the natural scenery.",
    "Have a picnic with friends and share some laughs.",
    "Explore a new cuisine by dining at an ethnic restaurant.",
    "Take a yoga class and stretch your body and mind.",
    "Join a local sports league and enjoy some friendly competition.",
    "Attend a workshop or lecture on a topic you're interested in.",
    "Visit an amusement park and ride the roller coasters."
]

corpus_of_documents


user_query="i am an indian and i live in india"

document="india is a country for the indians and for eveyone"

from collections import Counter
import math

query_tokens=user_query.lower().split(" ")

query_tokens

document_tokens=document.lower().split(" ")

document_tokens

query_counter=Counter(query_tokens)

query_counter

document_counter=Counter(document_tokens)

document_counter

lst=[]
for token in query_counter.keys():
    lst.append(query_counter[token])

user_query="i am an indian and i live in india"
document="india is a country for the indians and for eveyone"

#sentence vector
lst

for tokens in query_counter.keys() & document_counter.keys():
    print(tokens)

mylist=[]
for tokens in query_counter.keys() & document_counter.keys():
    mylist.append(query_counter[tokens]*document_counter[tokens])

mylist

dot_prod=sum(mylist)

query_magnitude = math.sqrt(sum(query_counter[token] ** 2 for token in query_counter))
    

query_magnitude

document_magnitude = math.sqrt(sum(document_counter[token] ** 2 for token in document_counter))

document_magnitude

similarity=(dot_prod)/(query_magnitude*document_magnitude)

similarity

user_query="is yoga good for health"
document="yoga is very good for living healthy lifesytle."

def cosine_similarity(query, document):
    # Tokenize and convert to lowercase
    query_tokens = query.lower().split(" ")
    document_tokens = document.lower().split(" ")

    # Create Counters for query and document
    query_counter = Counter(query_tokens)
    document_counter = Counter(document_tokens)

    # Calculate dot product
    dot_product = sum(query_counter[token] * document_counter[token] for token in query_counter.keys() & document_counter.keys())

    # Calculate magnitudes
    query_magnitude = math.sqrt(sum(query_counter[token] ** 2 for token in query_counter))
    document_magnitude = math.sqrt(sum(document_counter[token] ** 2 for token in document_counter))

    # Calculate cosine similarity
    similarity = dot_product / (query_magnitude * document_magnitude) if query_magnitude * document_magnitude != 0 else 0

    return similarity

cosine_similarity(user_query,document)

def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = cosine_similarity(query, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]

corpus_of_documents

user_input="i like fresh air."

relevant_document=return_response(query,corpus_of_documents)

user_input="i like to do yoga"

relevant_document=return_response(user_input,corpus_of_documents)

relevant_document

# how you can configure llm in your local system
# LLAMA2
#hugging face(we are not going to use this one)

# augument this response by using llama2 model

import requests
import json
full_response = []

full_response = []
prompt = """
You are a bot that makes recommendations for activities. You answer in very short sentences and do not include extra information.
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""

url = 'http://localhost:11434/api/generate'


data = {
    "model": "llama2",
    "prompt": prompt.format(user_input=user_input, relevant_document=relevant_document)
}

headers = {'Content-Type': 'application/json'}

response = requests.post(url, data=json.dumps(data), headers=headers, stream=True)


try:
    for line in response.iter_lines():
        # filter out keep-alive new lines
        if line:
            decoded_line = json.loads(line.decode('utf-8'))
            # print(decoded_line['response'])  # uncomment to results, token by token
            full_response.append(decoded_line['response'])
finally:
    response.close()
    
    
print(''.join(full_response))