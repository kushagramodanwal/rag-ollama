#!/usr/bin/env python
# coding: utf-8

# In[63]:


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


# In[64]:


corpus_of_documents


# In[65]:


user_query="I am an indian and i live in india"


# In[66]:


document="india is a country for the indians and for everyone"


# In[67]:


from collections import Counter
import math



# In[68]:


query_tokens = user_query.lower().split(" ")
query_tokens


# In[69]:


document_tokens = document.lower().split(" ")
document_tokens


# In[70]:


query_counter=Counter(query_tokens)
query_counter


# In[71]:


document_counter=Counter(document_tokens)
document_counter


# In[72]:


lst=[]

for token in query_counter.keys():
    lst.append(query_counter[token])


# In[73]:


# sentence vector 
# instead of using sentence level similarity we are using word level similarity below
lst


# In[74]:


mylist=[]
for tokens in query_counter.keys() & document_counter.keys():
    mylist.append(query_counter[tokens]*document_counter[tokens])


# In[75]:


mylist


# In[76]:


dot_product =sum(mylist) # now this is a dot b


# In[77]:


query_magnitude = math.sqrt(sum(query_counter[token] ** 2 for token in query_counter))


# In[78]:


document_magnitude = math.sqrt(sum(document_counter[token] ** 2 for token in document_counter))


# In[79]:


similarity = (dot_product)/(query_magnitude*document_magnitude)
similarity


# In[80]:


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


# In[81]:


cosine_similarity(user_query,document)


# In[82]:


def return_response(query, corpus):
    similarities = []
    for doc in corpus:
        similarity = cosine_similarity(query, doc)
        similarities.append(similarity)
    return corpus_of_documents[similarities.index(max(similarities))]


# In[83]:


corpus_of_documents


# In[94]:


user_input="i like fresh air"


# In[95]:


relevant_document=return_response(user_input,corpus_of_documents)


# In[96]:


# how you can configure llm in your local system

# LLAMA2

# we can also use hugging face but in this we will use Ollama

# this is generic response but i want to augment this response by using llama 2 model


# In[97]:


import requests
import json
full_response = []




# In[100]:


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


# In[ ]:




