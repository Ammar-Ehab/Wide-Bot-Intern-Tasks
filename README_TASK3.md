# Text preprocessing steps
## 1) Removing stop words and extra unuseful text
These are the most common words in any language and do not add much information to the text. Examples of a few stop words in English are “the”, “a”, “an”, “so”, and “what”. They are moreover, removing spaces, and punctuations. 
## 2) Tokenization
It is a way of separating a piece of text into smaller units called tokens.
## 3) Stemming 
It is the process of reducing a word to its stem. This is important since Arabic has several variants of a single term.
## 4) TF-IDF 
It is a text vectorizer that transforms text into a vector form. It is a combination of term frequency and inverse document frequency. Term frequency is the number of times a word I appears in a document j divided by the total number of words in the document. 

# Model Implementation
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

As shown in the following photo, we can conclude that our model struggles the most with classes: -
### Class 2(Societe): 
The precision, recall, and F1-score are relatively lower compared to other classes. This suggests that the model has difficulty correctly identifying instances belonging to class 2.
### Class 5(Orbites): 
Similarly, the precision, recall, and F1-score for class 5 are relatively lower compared to other classes, indicating that the model struggles to correctly classify instances in class 5.
### Class 7(Marocains-du-monde): 
While the precision and recall are decent for class 7, the F1-score is slightly lower, suggesting that the model may face challenges in precisely capturing instances of class 7.

However, we are predicting “sport(1)”, “art-et-culture(10)”, “medias(6)”, “tamazight(0)” with high accuracy.


![SGDClassifier](https://github.com/Ammar-Ehab/Wide-Bot-Intern-Tasks/assets/67014583/6ca4623f-b752-402c-9dc1-572ffb690575)
