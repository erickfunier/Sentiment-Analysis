from sklearn.linear_model import LogisticRegression

def train(tweet_train_vect, sentiment_train):
    print("Training...")
    classifier = LogisticRegression(max_iter=500)
    classifier.fit(tweet_train_vect, sentiment_train)

    return classifier