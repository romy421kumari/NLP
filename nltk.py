
# coding: utf-8

# ## NLTK library

# In[17]:


import nltk


# In[18]:


a=['romy','romy','and','and','romy','in','the','all','about','in','the']


# In[19]:


f=nltk.FreqDist(a)
type(f)


# In[20]:


f


# In[21]:


for i,v in f.items():
    print(str(i)+':'+ str(v))


# In[22]:


import nltk
nltk.download('stopwords')


# In[23]:


from nltk.corpus import stopwords
stopwords.words('english')


# In[24]:


# tokenize
from nltk.tokenize import word_tokenize
nltk.download('punkt')


# In[25]:


#tokenize words
string="This is the string that need to be tokenize and then presented into lists as tokens"
word_tokens=word_tokenize(string)
word_tokens


# In[26]:


stop_words=stopwords.words('english')
filter=[]
for w in word_tokens:
    if w not in stop_words:
        filter.append(w)


# In[27]:


print(filter)


# In[28]:


#tokenize sentence
from nltk.tokenize import sent_tokenize


# In[29]:


sentence="Hii Romy, How are you? Hope you are doing well. Today is a good day."
sent_tokenize(sentence)


# In[30]:


import nltk
from nltk.corpus import wordnet
nltk.download('wordnet')
nltk.download('omw')


# In[31]:


# get synonym of words
wrd=wordnet.synsets('happy')
print(wrd[1].definition())
wrd[0].examples()


# In[32]:


#get antonyms
antonyms=[]
for syn in wordnet.synsets("happy"):
    for l in syn.lemmas():
        if l.antonyms():
            antonyms.append(l.antonyms()[0].name())


# In[33]:


antonyms


# # Stemming

# In[34]:


# stemming means removing affixes from words and returning the root word
from nltk.stem import PorterStemmer
var=PorterStemmer()
var.stem("working")


# In[35]:


#SnowballStemmer support many languages
from nltk.stem import SnowballStemmer
var1=SnowballStemmer("english")
print(SnowballStemmer.languages)


# # Lemmatizing

# In[36]:


# Lemmatizing is similar to stemming but lemmatizing return real word
# example for word increase
from nltk.stem import WordNetLemmatizer
var2=WordNetLemmatizer()
print("After Lemmatizing : ", var2.lemmatize("increase"))
print("After stemming : ", var1.stem("increase"))


# In[37]:


var2.lemmatize("playing") # returning the same word because default part of speech is noun


# In[38]:


# to get the verb 
print("Verb: ",var2.lemmatize("playing", pos='v') )#verb
print("Adjective: ",var2.lemmatize("playing", pos='a')) #adjective
print("Noun: ",var2.lemmatize("playing", pos='n')) #noun
print("Adverb: ",var2.lemmatize("playing", pos='r')) #verb

