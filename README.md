# SANOJ DODDAPANENI

## Project 2 - Cuisine Predictor

**Introduction -** In this project, we have a dataset in the form of JSON which is yummly.json which consists of cusines and its ingredients which has a particular id associated to it. In this case, we need to read the JSON file given and should apply modeling to it using several libraries and the final output my predict a cuisine based on the ingredients provided by the user in command line. We use python and command line tools in this project.

**Sources -**  
*__For wget library to download json file -__* https://pypi.org/project/wget/  
*__For reading json file -__* https://www.programiz.com/python-programming/json  
*__Dataframe ingredients to string -__* https://datascience.stackexchange.com/questions/103926/multi-label-classification-deep-learning  
*__Tfidf Vectorization -__* https://stackoverflow.com/questions/47557417/understanding-text-feature-extraction-tfidfvectorizer-in-python-scikit-learn  
*__Logistic Regression and its functions -__* https://scikit-learn.org/stable/modules/generated/sklearn.linear_model.LogisticRegression.html. 
*__MutlinomialNB and ints functions -__* https://scikit-learn.org/stable/modules/generated/sklearn.naive_bayes.MultinomialNB.html  
*__NearestNeighbors -__* https://scikit-learn.org/stable/modules/neighbors.html  

**Installation Directories -** In this project, we use the packages json, pandas, sklearn, sys, os and wget. These packages can be installed using the command below replacing [package_name] with the package that is to be installed. These packages will be imported according to requirement.  
```pipenv install [package_name]```

**Project Description -**

In the project, we use wget module and use wget.download to download the yummly.json file to the main directory. The json file will be downloaded if it does not exists and will skip the code if the file already exists.

**read_input() -** In this function, we read the json file that is existing in the directory and then convert it to the dataframe for data using pandas module. This returns the values data read and dataframe for furthe processing in next function.

**processing() -** In this function, we first first collect the dataframe that is returned from the read_input function and then storing the dataframe into a list of ingredients.  

Now, TfidfVectorizer is used with ngram_range=(1,3) and stored in tfidf variable.  
This tfidf vectorizer is used to fit_transform the dataframe of list of ingredients where the data is converted into vectors for further processing.  
Now, from the main data read, we are appending the cuisines and storing in the variable y for prediction.  

After, having the data lists, we then use LogisticRegression or MultinomialNB model to train the lists according and then fitting them into the model for further predictions.  

Here, we need to use LogisticRegression with Max_iter of 1000 to avoid Max_iter warning and to predict the resutls with high accuracy.  
Alternatively, we can use MutlinomialNB model but, this model gives less accorate resutls but are faster compared to LogisticRegression.  

_Code for both the models are written in the processing function and Mutlinomial is commented in code to not be considered as system resources are plenty for our computing._  

After performing the model and fitting the data, we take any number of ingredients from the user from commandline and then we transform those input ingredients into vectors using transform function if tfidf.  
This vectors are used to predict the cuisine and the score from the model using predict  and predict_proba function of LogisticRegression of MultinomialNB according to the preferences.

Once all the processing is done we then print the output of prediction and prediction probability using json loads and dumps function from json library.

Now, we also need to find user provided number of nearest cuisines and then print the data ids and scores of those cuisines.  
Here, we use NearestNeighbors library to find the number of nearest neighbors according to the user input in commandline for --N.  

Then we print the --N number of nearest neighbors in loop using json dumps function.

At the end, we use sys.argv to read the number for --N and each ingredient for --ingredient and append it to variable called userinput.  
Then, these values are collected and are passed to the processing function accoridngly for prediction to be successful.

We use the command below to run the program -  
```pipenv run python project2.py --N 5 --ingredients 'chicken' --ingredients 'broth' --ingredients 'onion'```

I have used ingredients as chicken, broth and onion to predict the cuisine. These can be replaced to predict any other cuisine according to the ingredients that once want to specify.

Please be informed that it could take 3-7 minutes to run the program using LogisticRegression model which is defaulted in the code.

If computing resources and faster processing is to be kept in mind, the MultinomialNB code should be used by removing the comments for MultinomialNB lines in code and comment the LogisticRegression model to use the MultinomialNB model accordingly.

After running the code with the command mentioned above, the output will be printed as below -  
<img width="339" alt="image" src="https://user-images.githubusercontent.com/31980486/163660609-89e10d10-183a-4096-a758-2a7e62ac6db0.png">

**Test Cases -**

Here, we have created a new directory called tests and then created a file called test_code.py which contains different functions of test cases for each function and code in project2.py. Each test case in the file is explained below accordingly.

Firstly, we import the packages sys to execute test file for all the directories of the project and provide the path accordingly and then import project2.py within the folder and then finally we should import package pytest to run testcases accordingly. Pyest modules works on pytest framework and can be installed using the command below -  
```pipenv install pytest command```

**test_yummly() -** In this function of test case, we check if the yummly.json file exists in the main directory which is used for processing the code.  

**test_processing() -** In this test case, we check for the processing function which contains code for modeling and prediction and to print the prediction and nearest neighbors accoridngly. If the function is existing in the project2.py, then the test case is passed accordingly.

**test_readinput() -** In this test case, we check for the read_input() function which contains code for reading and converting the data into dataframe accoridngly. If the function is existing in the project2.py, then the test case is passed accordingly.

**test_mainexists() -** In this function, we check if the code for arguments exist in the code and if user is able to pass --N and --ingredients accordingly to modeling, prediction and nearest neighbors.

**test_dataframe() -** In this function, we check if the dataframe exists for the main function which stores the read input data returned by the read_input() function.

**test_userinput() -** Here, we check if the user provided ingredients are collected for prediction and modeling.

Here, Test cases can be executed using below command -  
```pipenv run python -m pytest```

Once the command is passed, it will show the execution of test cases as below -  
<img width="1435" alt="image" src="https://user-images.githubusercontent.com/31980486/163660892-11f00e4c-268f-4ea2-83c0-ebe2ec29b79b.png">

**Possible Bugs -** 

In this code, the output of predicted cuisines is printed correctly in JSON format. The output values such as id and score of nearest neighbors is printed correctly but the format has been changed a little as seen in the output screenshot above.

At the end, these files are added, committed and pushed into git hub using git commands accordingly for each file.
