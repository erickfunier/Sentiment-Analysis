import pandas as pd

from sklearn.metrics import confusion_matrix

def gen_confusion_matrix(sentiment_test, sentiment_pred, df):
    print("Generating confusion matrix...")
    matrix = confusion_matrix(sentiment_test, sentiment_pred, labels=df.target.unique())
    df_matrix = pd.DataFrame(matrix, index=df.target.unique(), columns=df.target.unique())

    # converter a matriz para porcentagem
    for i in df_matrix:
        df_matrix[i] /= df_matrix[i].sum()
    
    return(df_matrix)