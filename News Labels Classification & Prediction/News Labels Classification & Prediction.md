This code used [fetch_20newsgroups dataset](https://scikit-learn.org/stable/modules/generated/sklearn.datasets.fetch_20newsgroups.html). 
Then split the whole dataset into two parts, training data (70%) and test data (30%).

Then prepared all the features we need for Bag of words, Word weight (tfidf), and Word2vek approaches

Next step, we used Multinomial Naive Bayes (MNB) and Support Vector Machines (SVM) to classify and predict the label of news.
To evaluate the models, we used Accuracy, Precision, Recall, and F1 Score features.

Lastly, to improve the model performance, we adjusted the metric argument of KNeighborsClassifier to 'cosine'
