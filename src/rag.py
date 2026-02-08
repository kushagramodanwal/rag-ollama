from collections import Counter
import math,requests,json

corpus_of_documents=[
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

def cosine_similarity(query,document):
    q=Counter(query.lower().split())
    d=Counter(document.lower().split())
    dot=sum(q[t]*d[t] for t in q.keys()&d.keys())
    q_mag=math.sqrt(sum(v*v for v in q.values()))
    d_mag=math.sqrt(sum(v*v for v in d.values()))
    return dot/(q_mag*d_mag) if q_mag*d_mag else 0

def retrieve(query,corpus):
    return max(corpus,key=lambda doc:cosine_similarity(query,doc))

user_input="i like fresh air"
relevant_document=retrieve(user_input,corpus_of_documents)

prompt=f"""You are a bot that makes recommendations for activities. Keep it under 30 words.
Recommended activity: {relevant_document}
User input: {user_input}
"""

url="http://localhost:11434/api/generate"
payload={"model":"gemma3:1b","prompt":prompt}
headers={"Content-Type":"application/json"}

response=requests.post(url,data=json.dumps(payload),headers=headers,stream=True)
output=[]
for line in response.iter_lines():
    if line:
        output.append(json.loads(line)["response"])
print("".join(output))
