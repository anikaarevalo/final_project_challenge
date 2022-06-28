# 👍final_project_challenge
*An individual project culminating my experience in the AI Ops training at BeCode (Ghent)*


## Description ##


## The App ##
This is a **handy yet effective software that analyses customer product reviews on the web in order to gauge over-all consumer satisfaction**. At this stage of the product cycle development, it is a proof of concept for clients who are open to leveraging AI and ML technologies when it comes to improving their customer support strategy based on customer feedback evaluation. 


## Installation ##
In the repository you can find the **requirements.txt** file. Make sure that these are installed. 


## Usage ##


- To access the app, go to the **app.py** file. When you run the code, you will receive a http address that you can open in your preferred browser. (See C & D visualisations.) Paste a sample customer review in the text box as instructed. When you press the button to process the text, the software will return a result of either 'Positive👍' (meaning a positive rating) or a 'Negative👎' (meaning a negative rating) label.

- The file **Trans_DistilBERT_Sentiment_Model_for_Amazon_Personal_Care_Appliances.ipynb** is where the actual model was created. (See A & B visualisations.) The model is already trained and can be **found in the 'test' folder**. 


## Data Sources ##


- The **Tensorflow database** for the [Amazon US Personal Care Appliances data set](https://www.tensorflow.org/datasets/catalog/amazon_us_reviews) 
- **Research material on Natural Language Processing (NLP) models** and available libraries were sourced from the following:
  - [Amazon Product Review Sentiment Analysis Using BERT](https://www.analyticsvidhya.com/blog/2021/06/amazon-product-review-sentiment-analysis-using-bert/https://github.com/yashinaniya/NLP_Projects/blob/main/Amazon_product_sentiment_analysis.ipynb)
  - [DistilBERT](https://huggingface.co/docs/transformers/main/model_doc/distilbert)
  - [BERT 101 🤗 State Of The Art NLP Model Explained](https://huggingface.co/blog/bert-101)
  

## Visuals ## 


                      A. Model training: TFDistilBertForSequenceClassification
<img width="650" alt="pipeline 2022-04-21 at 15 49 28" src="https://github.com/anikaarevalo/final_project_challenge/blob/0d9c67a1a05cf218902244d1e7fb05a968bacaa2/assets/VI.model_training.png">


                      B. Plotting the results of model training: High accuracy, low loss
<img width="1000" alt="pipeline 2022-04-21 at 15 49 28" src="https://github.com/anikaarevalo/final_project_challenge/blob/0d9c67a1a05cf218902244d1e7fb05a968bacaa2/assets/plot_distilBERT_retrained.png">

                      C. Customer review rating App: The user interface
<img width="650" alt="pipeline 2022-04-21 at 15 49 28" src="https://github.com/anikaarevalo/final_project_challenge/blob/eae5a493701ed30c7149193e7cc913980f4f4b44/assets/positive_review.png">


                      D. Customer review rating app: A sample output
<img width="650" alt="pipeline 2022-04-21 at 15 49 28" src="https://github.com/anikaarevalo/final_project_challenge/blob/6459bdcf78ea268157a19a59138e636adb11b490/assets/positive_output.png">

                  
## Contributor

⚛️**Anika Arevalo (Jr. AI Data Scientist, BeCode in Ghent)**

https://www.linkedin.com/in/anika-arevalo/

## Timeline ##

09 days

20/06/2022 - 30/06/2022

## Personal situation ##
  
  
