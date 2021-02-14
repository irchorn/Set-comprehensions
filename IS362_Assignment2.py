#!/usr/bin/env python
# coding: utf-8

# # Set comprehensions
# 

# In[33]:


## Pull out unique words from the sentence.
sentence = 'As people spend more time indoors, a mountain of scientific research says spending time in nature is critical to health and increases longevity.'
print(sentence)


# <font color= 'purple'>
# *Make sentence lowercase and remove the comma and the period.
# *Use split function to separate the sentence into list of words.
# *Generate a set of urepeated words. </font>

# In[5]:


words = sentence.lower().replace('.', '').replace(',', '').split()
sent_words = {word for word in words}
print(sent_words)


# In[8]:


# Pull out of the sentence words that have more than 7 letters
sent_words = {word for word in words if len(word) >= 7}
print (sent_words)


# [Python methods](https://www.w3schools.com/python/ref_string_find.asp)

# In[20]:


#Leave out words that start with "s".
sent_words = {word.find('s') if word[0] == 's' else word for word in words}
print(sent_words)


# In[ ]:




