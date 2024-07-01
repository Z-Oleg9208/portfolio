#!/usr/bin/env python
# coding: utf-8

# In[4]:


import numpy as np


# In[8]:


import pandas as pd
from sentence_transformers import SentenceTransformer, util

def predict(test, model = SentenceTransformer('sentence-transformers/LaBSE')):
    
    test = test.copy()
    school_id = np.load('school_id.npy')
    corpus = np.load('corpus.npy')
    
    query = model.encode(test.name.values)
    
    search_result = util.semantic_search(query, corpus, top_k=5)
    
    
    predict_ind = [row[0]['corpus_id'] for row in search_result]
    test['predict_id'] = school_id[predict_ind]
    top_5 = [[row[x]['corpus_id'] for x in range(5)] for row in search_result]
    test['top_5_id'] = [[school_id[row[x]]for x in range(5)] for row in top_5]
    
    try:
        score = {
            'top':round((test.school_id == test.predict_id).mean(), 2),
            'top_5':round((test.apply(lambda x: x['school_id'] in  x['top_5_id'], axis=1)).mean(), 2)
        }
    except:
        score = None
    
    
    return score, test


# In[10]:


patch = input('Введите путь к тестовому файлу:')
test = pd.read_csv(patch)
score, test = predict(test)

print('accuracy для top и top_5 результатов модели: ', score)
test.head()

