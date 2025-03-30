#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas
import numpy
import librosa


# In[ ]:


get_ipython().system('pip install librosa')


# In[ ]:


import librosa
print(librosa.__version__)


# In[5]:


import os
import pandas as pd

# Path to genres folder
base_path = 'data\genres_original'
data = []

# Loop through genres and extract file details
for genre in os.listdir(base_path):
    genre_path = os.path.join(base_path, genre)
    if os.path.isdir(genre_path):
        for file_name in os.listdir(genre_path):
            file_path = os.path.join(genre_path, file_name)
            data.append([file_name, genre, file_path])

# Create metadata DataFrame
df = pd.DataFrame(data, columns=["TrackName", "Genre", "FilePath"])
df.to_csv('data/metadata.csv', index=False)
print("✅ Metadata saved as data/metadata.csv")

