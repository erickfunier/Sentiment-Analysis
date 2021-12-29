from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split

def vectorize(df):
    print("Vectorizing...")
    tweet = df.text.values
    sentiment = df.target.values
    tweet_train, tweet_test, sentiment_train, sentiment_test = train_test_split(tweet, sentiment, test_size=0.15, random_state=32)

    # count words with CountVectorizer and transform the vectors in your frequency in the dataset

    vector = CountVectorizer()
    vector.fit(tweet_train)

    tweet_train_vect = vector.transform(tweet_train)
    tweet_test_vect = vector.transform(tweet_test)

    return tweet_train, sentiment_train, tweet_train_vect, tweet_test_vect, sentiment_test, vector