# Generated from: 15_RAG_ImplemFromSractch_OLlama_Llama2.ipynb
# Converted at: 2026-02-08T15:35:24.085Z
# Next step (optional): refactor into modules & generate tests with RunCell
# Quick start: pip install runcell

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

user_query="I am an indian and i live in india"

document="india is a country for the indians and for everyone"

from collections import Counter
import math



query_tokens = user_query.lower().split(" ")
query_tokens

document_tokens = document.lower().split(" ")
document_tokens

query_counter=Counter(query_tokens)
query_counter

document_counter=Counter(document_tokens)
document_counter

lst=[]

for token in query_counter.keys():
    lst.append(query_counter[token])


# sentence vector 
# instead of using sentence level similarity we are using word level similarity below
lst

mylist=[]
for tokens in query_counter.keys() & document_counter.keys():
    mylist.append(query_counter[tokens]*document_counter[tokens])


mylist

dot_product =sum(mylist) # now this is a dot b


query_magnitude = math.sqrt(sum(query_counter[token] ** 2 for token in query_counter))


document_magnitude = math.sqrt(sum(document_counter[token] ** 2 for token in document_counter))


similarity = (dot_product)/(query_magnitude*document_magnitude)
similarity

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

user_input="i like fresh air"


relevant_document=return_response(user_input,corpus_of_documents)


# how you can configure llm in your local system

# LLAMA2

# we can also use hugging face but in this we will use Ollama

# this is generic response but i want to augment this response by using llama 2 model


import requests
import json
full_response = []




full_response = []
prompt = """
You are a bot that makes recommendations for activities.keep it short to 30 words
This is the recommended activity: {relevant_document}
The user input is: {user_input}
Compile a recommendation to the user based on the recommended activity and the user input.
"""

url = 'http://localhost:11434/api/generate'


data = {
    "model": "gemma3:1b",
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