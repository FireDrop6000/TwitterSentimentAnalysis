import matplotlib.pyplot as plt
import pandas as pd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("credentials.json")

firebase_admin.initialize_app(cred)

db = firestore.client()
users = list(db.collection('SentimentAnalysis').stream())

users_dict = list(map(lambda x: x.to_dict(), users))
df = pd.DataFrame(users_dict)

colors = ['red', 'blue', 'green']
# explode = (0.05, 0.05, 0.05) 

df.groupby(['Sentiment'])['Sentiment'].count().plot.pie(y = 'count', autopct='%1.0f%%', colors=colors)
plt.show()
