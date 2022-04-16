# Importing necessry libraries
# Json library to read and write data
# Pandas library for dataframes
# LogisticRegression for training and fitting the data
# MutlinomialNB for training and fitting the data for faster processing
# NearestNeighbors library for finsing the nearest cuisines for the ingredients mentioned
# TfidfVectorier for vectorizing X fitting and user input
# Sys library for arguments
# Os library to check existing json file
# Wget Library for downloading yummly file if not existing

import json
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.neighbors import NearestNeighbors
import sys
import os
import wget

# Downloading yummly.json if not existing in the current required folder
# Source - https://pypi.org/project/wget/
if not os.path.exists('yummly.json'):
    wget.download('https://oudatalab.com/cs5293sp22/projects/yummly.json')

# Reading data from yummly.json
# Source - https://www.programiz.com/python-programming/json
def read_input():
    with open('yummly.json') as datafile:
        data = json.load(datafile)
    df = pd.DataFrame(data)
    return df, data

# Processing and Prediction function
def processing(df, data, inputs, userN):
# Source - https://datascience.stackexchange.com/questions/103926/multi-label-classification-deep-learning
    df['ingredients'] = [', '.join(map(str, i)) for i in df['ingredients']]

# Source - https://stackoverflow.com/questions/47557417/understanding-text-feature-extraction-tfidfvectorizer-in-python-scikit-learn
    tfidf= TfidfVectorizer(ngram_range=(1,3))
# X Fitting for ingredients in the data frame for fitting in Logistic regression
    X = tfidf.fit_transform(df['ingredients'])

# y fitting for cuisine in json file to list to fit in Logistic regression
    y = []
    for i in data :
        y = y + [i['cuisine']]

# Logistic regression and fitting X and y
# Source - https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html
    clf = LogisticRegression(max_iter = 10000)
    clf.fit(X, y)

# MiltinomialNB and fitting X and y (faster processing and less accurate results)
# Scource - https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html
    '''clf = MultinomialNB()
    clf.fit(X, y)'''

# Taking input from the user in the main function
# Declared userinput variable as list globally to be called as arguments in this function
# Transforming user input for prediction
    userinputvalues = tfidf.transform(inputs)
# Prediction using .predict() function of Linear Regression model
    prediction = clf.predict(userinputvalues)
# Score Prediction using .predict_proba() function of Linear Regression model
    predictionscore = clf.predict_proba(userinputvalues)[0]

# Printing the output of predicted cuisine
    cuisinejson = '{"Cuisine": "%s", "Score": "%f"}' %(prediction[0], predictionscore[0]*100)
    finalcuisinejson = json.loads(cuisinejson)
    print(json.dumps(finalcuisinejson, indent = 4, sort_keys = True))

# Nearest cuisine prediction for ingredients given
# Source - https://scikit-learn.org/stable/modules/neighbors.html
    ndata=NearestNeighbors(n_neighbors=userN)
    ndata.fit(X,y)
    nid, nscore = ndata.kneighbors(userinputvalues,int(userN))

# Printing the predicted nearest cuisines
    print('{\n    "closest:" [\n')
    for i in range(len(nscore[0])):
        finalnearcuisine = '  { "id": "%d", "score": "%f" },' %(df.id[nscore[0][i]],nid[0][i])
        finalnearcuisine = finalnearcuisine.replace('\"', '')
        print(json.dumps(finalnearcuisine, indent=4, separators=(', ','{ ')))
    print("\n    ]\n}")

# Main function using sys library
arg_ls = sys.argv
# Declaring final main variables to be passed for arguments
files=pd.DataFrame()
cuisines=[]
userinput = []
output = ''

for i in range(len(arg_ls)):
    if arg_ls[i] == 'project2.py':
        for j in range(len(arg_ls)):
            if arg_ls[j] == '--N':
                N = arg_ls[j+1]
            if arg_ls[j] == '--ingredients':
                userinput.append(arg_ls[j+1])
# Calling read_input function
        files, cuisines = read_input()
# Calling processing function
        processing(files, cuisines, userinput, N)

#----------------------------------------------END OF THE CODE----------------------------------------------
