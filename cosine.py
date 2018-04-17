import re, math
from main import *
from collections import Counter
from start import *
WORD = re.compile(r'\w+')

def get_cosine(vec1, vec2):
     intersection = set(vec1.keys()) & set(vec2.keys())
     numerator = sum([vec1[x] * vec2[x] for x in intersection])

     sum1 = sum([vec1[x]**2 for x in vec1.keys()])
     sum2 = sum([vec2[x]**2 for x in vec2.keys()])
     denominator = math.sqrt(sum1) * math.sqrt(sum2)

     if not denominator:
        return 0.0
     else:
        return float(numerator) / denominator

def text_to_vector(text):
     words = WORD.findall(text)
     return Counter(words)

text1 = summaries1
text2 = summaries2
text3 = summaries3

vector1 = text_to_vector(text1)
vector2 = text_to_vector(text2)
vector3 = text_to_vector(text3)

cosinea = get_cosine(vector1, vector2)
print 'Cosine12:', cosinea
if cosinea > 0.5:
     result12 = summaries1 + summaries2
     print Summarize("",result12)
cosineb = get_cosine(vector2, vector3)
print 'Cosine23:', cosineb
if cosineb > 0.5:
    result23 = summaries3 + summaries2
    print Summarize("",result23)
cosinec = get_cosine(vector1, vector3)
print 'Cosine13:', cosinec
if cosinec > 0.5:
    result13 = summaries1 + summaries3
    print Summarize("",result13)
