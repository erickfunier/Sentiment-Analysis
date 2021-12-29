from model.vectorize import vectorize
from model.train import train
from util.confusion_matrix import gen_confusion_matrix
from util.load_dataset import load_dataset

# sentiment 140 dataset
print("Loading dataset...")
df = load_dataset('sentiment140.csv', 
                        ['target',
                        'id',
                        'date',
                        'flag',
                        'user',
                        'text'])

print(df.head())

"""# Vectorizing

To train and assess whether the model really learned, we will do a division generating training and testing vectors, with 15% tests and 85% of the data for training 
"""
tweet_train, sentiment_train, tweet_train_vect, tweet_test_vect, sentiment_test, vector = vectorize(df)

print("tweet:", tweet_train[0])
print("sentiment:", sentiment_train[0])
print("Freq. in dataset|Freq. in current tweet\n",tweet_train_vect[0])

"""# Train
The model used was the Logistic Regression of the Sklearn library, the number of iterations was limited to 1000, which takes just under 5 minutes of execution, enough to obtain an accuracy of 80%. As a parameter for the classifier, the vectors of the sentences with the frequencies and feelings of each item were used. 

Finally, we performed the evaluation with test vectors from the same dataset. 
"""

classifier = train(tweet_train_vect, sentiment_train)

score = classifier.score(tweet_test_vect, sentiment_test)
print("Accuracy:", score)

"""# Confusion Matrix

To generate the confusion matrix, we used the confusion_matrix function from the Sklearn library, as a parameter, we inserted the test sentiment vector and the sentiment vector using the prediction with the test tweets vector, the function then returns a matrix that we can format with the dataframe inserting the row and column labels, such as 0 negative sentiment and 4 positive sentiment. In addition, for better visualization, the conversion to percentage was performed, as otherwise the correct answers would appear in relation to the total of verified tweets, which makes the visualization a little confusing. 
"""

# generate vector with predictions
sentiment_pred = classifier.predict(tweet_test_vect)

print(gen_confusion_matrix(sentiment_test, sentiment_pred, df))

"""# Tests

For the test, the IMDB reviews dataset was loaded and the first line that contained the name of the dataset columns was removed.
After that, it was necessary to treat the feelings that were previously <b>positive</b> and <b>negative</b> for <b>4</b> and <b>0</b> as per the model was trained.
After that, the vectors with reviews and feelings for classification in the model were generated, the result was satisfactory, obtaining 84% accuracy. 
"""
df_test = load_dataset('imdb-movie-reviews.csv', 
                        ['text',
                        'target'])

df_test = df_test.iloc[1: , :]

print(df_test.head())

# handling the sentiments
df_test['target'] = df_test['target'].map({'positive': 4, 'negative': 0})

print(df_test.head())

# vectorizing
review = df.text.values
sentiment2 = df.target.values

review_vect = vector.transform(review) # swap phrases in number array

# classify
score = -1
score = classifier.score(review_vect, sentiment2)

print("Accuracy:", score)