# Text preprocessing steps
## 1) Removing stop words and extra unuseful text
These are the most common words in any language and do not add much information to the text. Examples of a few stop words in English are “the”, “a”, “an”, “so”, and “what”. They are moreover, removing spaces, and punctuations. 
## 2) Tokenization
It is a way of separating a piece of text into smaller units called tokens.
## 3) Stemming 
It is the process of reducing a word to its stem. This is important since Arabic has several variants of a single term.
## 4) TF-IDF 
It is a text vectorizer that transforms text into a vector form. It is a combination of term frequency and inverse document frequency. Term frequency is the number of times a word I appears in a document j divided by the total number of words in the document. 

# Implementing models
## 1) Main function creation
Data Splitting: Splits the data into training and testing sets.
Model Training: Trains the machine learning model.
Prediction: Makes predictions on the test data.
Evaluation: Computes performance metrics for the predictions.
Cross-Validation: Assesses model accuracy using cross-validation.

## 2) Disscuing results and metrics
I tried the following models which are random forest, logistic regression, SGD, and multinomial naïve Bayes.
The SGD classifier has the highest accuracy and general results in metrics, so I will discuss its results.

## 3) SGD classifier
![SGDClassifier](https://github.com/Ammar-Ehab/Wide-Bot-Intern-Tasks/assets/67014583/6ca4623f-b752-402c-9dc1-572ffb690575)
