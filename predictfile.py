# Installing machine learning and NLP libraries
import tensorflow as tf


from transformers import DistilBertTokenizerFast
from transformers import TFDistilBertForSequenceClassification


import warnings
warnings.filterwarnings('ignore', category=DeprecationWarning)  # Ignoring warnings

#  A function that predicts label (positive or negative) when user inputs according to the parameters of the TFDistilBertForSequenceClassification model
def predict_label(client_review):    
    # Initializing a tokenizer
    tokenizer = DistilBertTokenizerFast.from_pretrained('distilbert-base-uncased-finetuned-sst-2-english')
    # Loading the saved re-trained, pre-trained DistilBert NLP model
    loaded_model = TFDistilBertForSequenceClassification.from_pretrained('./tdb_sentiment')

    # Predicting on unseen/new data
    predict_input = tokenizer.encode(client_review,
                                    truncation=True, 
                                    padding=True, 
                                    return_tensors='tf')
    tf_output = loaded_model.predict(predict_input)[0]
    tf_prediction = tf.nn.softmax(tf_output, axis=1)  # Activation set to softmax for Sparse Categorical Entropy loss
    labels = ['Negative','Positive']
    label = tf.argmax(tf_prediction, axis=1)
    label = label.numpy()
    
    # Returning prediction of label (postive or negative)
    return labels[label[0]]
