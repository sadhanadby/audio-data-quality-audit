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

# Load the metadata and features data
metadata_path = 'data/metadata_fixed.csv'
features_path = 'data/features_30_sec.csv'

metadata_df = pd.read_csv(metadata_path)
features_df = pd.read_csv(features_path)

# Rename 'TrackName' to 'filename' for consistency
metadata_df = metadata_df.rename(columns={'TrackName': 'filename'})

# Calculate duration using the formula: Duration (seconds) = Length / 22050
features_df['duration'] = features_df['length'] / 22050

# Select only necessary columns for merging
features_selected_df = features_df[['filename', 'duration']]

# Merge the two dataframes using 'filename' as the key
merged_df = pd.merge(metadata_df, features_selected_df, on='filename', how='left')

# Save the updated data to a new CSV
merged_df.to_csv(r'data/metadata_with_duration.csv', index=False)

print("metadata_with_duration.csv created successfully!")

# Load the dataset
file_path = "data/features_30_sec.csv"
df = pd.read_csv(file_path)

# Select the required columns
columns_needed = ["filename", "tempo", "length", "rms_mean", "zero_crossing_rate_mean", "spectral_bandwidth_mean",
                  "mfcc1_mean","mfcc2_mean", "mfcc3_mean","mfcc4_mean","mfcc5_mean",
                  "mfcc6_mean","mfcc7_mean","mfcc8_mean","mfcc9_mean","mfcc10_mean","mfcc11_mean",
                  "mfcc12_mean","mfcc13_mean","mfcc14_mean","mfcc15_mean","mfcc16_mean","mfcc17_mean",
                  "mfcc18_mean","mfcc19_mean","mfcc20_mean", "spectral_centroid_mean", "chroma_stft_mean", "label"]

metadata = df[columns_needed]

# Save to CSV
metadata.to_csv(r'data/metadata_with_more_features.csv', index=False)

# Show first few rows to verify
metadata.head()

