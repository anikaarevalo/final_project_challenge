# 👍final_project_challenge🤗
*An individual project culminating my experience in the AI Ops training at BeCode (Ghent)*


## Description ##
*Necessity is the mother of invention*. This rings true with the impending **arrival of Amazon.BE** as a shake-up in the online Belgian retail market is certainly underway. Although trite yet equally true, there is opportunity in the inevitable crisis ensuing from the American e-commerce monolith crushing existing competition. ***In the shoes of a locally-based, Belgian small business owner possessing an online retail outlet, how can they shore up on capital and muscle up on their business operations?*** The simple yet elegant solution lies in **enhancing customer experience—but with AI becoming mainstream, this solution can be high-tech, too.** 


## Methodology ## 
My approach to this use case took form and direction by answering the following **three key questions**:

1. ***Who needs help?*** 

Amazon is in fact coming very soon to cater specifically to the Belgian market, so instinctively I thought of **Belgium-based online retailers** who will benefit from a simple, efficient and reliable app to track customer sentiment that informs their digital marketing strategy.  

2. ***Where is the relevant data abundant and obtainable?***

I acquired the dataset needed for developing a machine learning solution from **Tensor Flow's data base.**  Following the instructions of the project, i.e. leveraging 'Sentiment Analysis' as a NLP capability to determine over-all sentiment of Amazon product reviews, I downloaded the **Amazon US Personal Care Appliances customer review data which contains roughly 85,000 data points. 

3. ***What are the latest free and open-source software to accomplish the task?***

I was given the wonderful opportunity of building the use case so I chose 'Natural Language Processing' (NLP) to be able to access and deploy a deep learning model for the first time. I had been intrigued by BERT, the state-of-the-art general-purpose NLP model developed by Google, and the transformer technique behind it. As an advocate of free and open-source software, I decided to give **distilBERT** (a lighter yet powerful version of BERT from the HuggingFace🤗 library) a try. Reduced in size by 40%, distilBERT retains 97% of BERT's language understanding capabilities but at 60% faster—hence I was convinced.  


## The App ##
This is a **handy yet effective software that analyses customer product reviews on the web in order to gauge over-all consumer satisfaction**. At this stage of the product cycle development, it is a proof of concept for clients who are open to leveraging AI and ML technologies when it comes to improving their customer support strategy based on customer feedback evaluation. 


## Installation ##
In the repository you can find the **requirements.txt** file. Make sure that these are installed. 


## Usage ##
- To access the app, go to the **app.py** file. When you run the code, you will receive a http address that you can open in your preferred browser. (See C & D visualisations.) Paste a sample customer review in the text box as instructed. When you press the button to process the text, the software will return a result of either 'Positive👍' (meaning a positive rating) or a 'Negative👎' (meaning a negative rating) label.

- The file **Trans_DistilBERT_Sentiment_Model_for_Amazon_Personal_Care_Appliances.ipynb** is where the actual model was created. (See A & B visualisations.) The model is already trained and can be found in the **'test' folder**. 

- The file **LDA_Mallet_Sentiment_Model_for_Amazon_Personal_Care_Appliances.ipynb** in the **'test' folder** is an early attempt to extract topic-keyword relationships based on a topic modelling NLP capability. It does not, as of now, contribute to the actual preprocessing of the data and development of the app.


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

07 days

20/06/2022 - 28/06/2022

(Delivery deadline: 30/06/2022)

## Personal situation ##
This machine leaning softare is a minimum viable product (MVP) and would indeed benefit from further optimisation. Although I am impressed by the computational power of the model to accurately predict customer sentiment, this app can be further developed in the following ways:
- Upgrading the app to perform a **fine-grain sentiment analysis** that takes a 'neutral' position into consideration. 
- Developing a second pipeline that can be integrated into the base pipeline in order to extract keywords. (Come see in the file **LDA_Mallet_Sentiment_Model_for_Amazon_Personal_Care_Appliances.ipynb** inside the **'test' folder**).
- Massive pre-trained machine learning models run the risk of overfitting (ie 'overgeneralising' from the initial dataset to unseen yet relevant data), so for those who want to take my app for a spin, let me know if it indeed does! Thank you! 😊  
