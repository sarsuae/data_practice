import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import random
from random import randint
from faker import Faker

# Instantiate Faker class
fake = Faker()

# Set constants
NUM_ROWS = 100

# Generate fake data for each column
timestamps = [fake.date_time_this_year() for _ in range(NUM_ROWS)]
post_texts = [fake.text(max_nb_chars=randint(20, 200)) for _ in range(NUM_ROWS)]
likes = [randint(0, 500) for _ in range(NUM_ROWS)]
shares = [randint(0, 100) for _ in range(NUM_ROWS)]

# Create dataframe
data = {'timestamp': timestamps, 'post_text': post_texts, 'likes': likes, 'shares': shares}
df = pd.DataFrame(data)

# Convert timestamps to pandas datetime format
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Create a new column for post length
df['post_length'] = df['post_text'].str.len()

# Basic data exploration
print(df.describe())

# Visualise data
sns.set_theme(style="whitegrid")
fig, axs = plt.subplots(2, figsize=(10, 12))

# Assign color based on condition
df['like_category'] = ['high' if x > 400 else 'low' for x in df['likes']]

# Plot 1: Post length vs Number of likes
axs[0].set_title('Post length vs Number of likes', fontsize=15)
sns.scatterplot(x=df['post_length'], y=df['likes'], hue=df['like_category'], ax=axs[0])
axs[0].set_xlabel('Post length', fontsize=12)
axs[0].set_ylabel('Number of likes', fontsize=12)

# More complex data exploration
# Here we're grouping by the hour of the post and calculating the mean number of likes
df['hour'] = df['timestamp'].dt.hour
hourly_likes = df.groupby('hour')['likes'].mean()

# Plot 2: Average number of likes by hour of the day
axs[1].set_title('Average number of likes by hour of the day', fontsize=15)
hourly_likes.plot(kind='bar', color='skyblue', ax=axs[1])
axs[1].set_xlabel('Hour of the day', fontsize=12)
axs[1].set_ylabel('Average number of likes', fontsize=12)

plt.tight_layout()
plt.show()