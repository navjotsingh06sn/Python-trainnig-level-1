# google collab + python + scikit-learn
# Machine Learning :- meachine learnings  means teaching a computer to learn from predictions and data...
# It is a subset of AI.
# Ml learns patterns automatically...

# ML is of three types:-

# 1. Supervised Learning:- In this type of learning, the model is trained on labeled data, 
# where the input data is paired with the correct output. 
# The model learns to make predictions based on this training data. 

# types of supervised learning:-

# regresssion 
# classification 

# e.g:- Netflix, spam detection , face recoginition 

# Advantages:- highly accurrate with sufficient labeled data , used for prediction and classification tasks, easy to understand and implement.

# classification:- it is the process of predicting which category or class an item belongs to...
# eg:- spam or not spam, cat or dog..

# regression:- it is the process of predicting a continuous numerical value based on past data....
# eg:- predicting the house price, area , and no of rooms.... 

# types of regression:-

# linear regression :-Linear Regression is a machine learning method used to predict a value by finding the relationship between two or more variables.

# import pandas as pd
# data={
#     "Study_Hours":[1,2,3,4,5,6,7,8],
#     "Result":[0,0,0,0,1,1,1,1]
# }
# df = pd.DataFrame(data)
# print(df)

# logistic regression:-Logistic Regression is a supervised machine learning algorithm used to classify data into categories such as Yes/No, True/False, or 0/1.

# from sklearn.linear_model import LogisticRegression
# x= df[["Study_Hours"]]
# y= df["Result"]
# model = LogisticRegression()
# model.fit(x,y)
# print("Model Trained Successfully")

# predicition= model.predict([[6]]).  #after training the model we can use it to make predictions on new data.
# print("prediction",predicition)
# otput:- prediction [1]

# decision tree:-A Decision Tree predicts an answer by splitting data into branches based on questions.
# random forest:-Random Forest combines multiple decision trees to make better and more reliable predictions.
# k-nearest neighbors(KNN):-KNN predicts something based on the majority of its nearest similar examples.
# support vector machines(SVM):-SVM separates data into classes by drawing the best possible dividing line between them.

 


