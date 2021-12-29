<h1 align="center">
Sentiment Analysis
</h1>
<p align="center">
  <a href="https://github.com/erickfunier">
    <img alt="Made by Erick Santos" src="https://img.shields.io/badge/made%20by-Erick%20Santos-lightgrey">
  </a>
</p>
<p>
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
</p>
Running the application:

### Docker 
    
- `docker build -t sentiment-analysis .`
- `docker run --rm -ti sentiment-analysis`
  
### Execution results

```docker run --rm -ti sentiment-analysis
Loading dataset...
   target          id                          date      flag             user                                               text
0       0  1467810369  Mon Apr 06 22:19:45 PDT 2009  NO_QUERY  _TheSpecialOne_  @switchfoot http://twitpic.com/2y1zl - Awww, t...
1       0  1467810672  Mon Apr 06 22:19:49 PDT 2009  NO_QUERY    scotthamilton  is upset that he can't update his Facebook by ...
2       0  1467810917  Mon Apr 06 22:19:53 PDT 2009  NO_QUERY         mattycus  @Kenichan I dived many times for the ball. Man...
3       0  1467811184  Mon Apr 06 22:19:57 PDT 2009  NO_QUERY          ElleCTF    my whole body feels itchy and like its on fire
4       0  1467811193  Mon Apr 06 22:19:57 PDT 2009  NO_QUERY           Karoli  @nationwideclass no, it's not behaving at all....
Vectorizing...
tweet: @mandelak  I guess my local printer is lousy.
sentiment: 0
Freq. in dataset|Freq. in current tweet
   (0, 234226)  1
  (0, 267751)   1
  (0, 336267)   1
  (0, 339499)   1
  (0, 350289)   1
  (0, 388197)   1
  (0, 441594)   1
Training...      
/usr/local/lib/python3.10/site-packages/sklearn/linear_model/_logistic.py:814: ConvergenceWarning: lbfgs failed to converge (status=1):
STOP: TOTAL NO. of ITERATIONS REACHED LIMIT.

Increase the number of iterations (max_iter) or scale the data as shown in:
    https://scikit-learn.org/stable/modules/preprocessing.html
Please also refer to the documentation for alternative solver options:
    https://scikit-learn.org/stable/modules/linear_model.html#logistic-regression
  n_iter_i = _check_optimize_result(
Accuracy: 0.8005916666666667
Generating confusion matrix...
          0         4
0  0.808434  0.206907
4  0.191566  0.793093
                                                text    target
1  One of the other reviewers has mentioned that ...  positive
2  A wonderful little production. <br /><br />The...  positive
3  I thought this was a wonderful way to spend ti...  positive
4  Basically there's a family where a little boy ...  negative
5  Petter Mattei's "Love in the Time of Money" is...  positive
                                                text  target
1  One of the other reviewers has mentioned that ...       4
2  A wonderful little production. <br /><br />The...       4
3  I thought this was a wonderful way to spend ti...       4
4  Basically there's a family where a little boy ...       0
5  Petter Mattei's "Love in the Time of Money" is...       4
Accuracy: 0.846171875
