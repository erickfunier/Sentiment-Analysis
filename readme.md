Train a sentiment classifier using a sentiment analysis dataset in order to interpret a text input and identify whether the text is positive or negative.<br/>
For this, two datasets obtained from Kaggle were used:<br/>

*   Sentiment140: https://www.kaggle.com/kazanova/sentiment140<br/>
    Contains 1.6M de tweets rated: 0 e 4<br/>
    The following fields will be used:<br/>
    * target: the polarity of the tweet (0 = negative, 4 = positive)<br/>
    * text: the text of review<br/>

*   IMDB movie reviews: https://www.kaggle.com/lakshmi25npathi/imdb-dataset-of-50k-movie-reviews<br/>
    Contains 50K of IMDB movie ratings rated: <i>positive</i> e <i>negative/i> <br/>
    The following fields will be used:<br/>
    * review: the text of the review<br/>
    * sentiment: the polarity of the review (<i>positive</i> ou <i>negative</i>)<br/>

The Sentiment140 dataset was used to train the model, for this, the vectorization of the data to an array of numbers with the Sklearn CountVectorizer word frequency counter was performed in the <b>logistic regression</b> which, despite being a simple model, presented a satisfactory result, this can be verified with the 2x2 confusion matrix.<br/>
The IMDB movie reviews dataset was used to test whether the model was able to rank the reviews satisfactorily.<br/>

Running the application:

<h2>Docker</h2>
* docker build -t sentiment-analysis .
* docker run --rm -ti sentiment-analysis