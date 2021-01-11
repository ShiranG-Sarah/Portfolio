The code predicted whether a shelter animal has a positive (adoption, returned to original owner) or negative 
(euthanized, transferred to other shelter)outcome based on information on the animal.

This code conducted linear regression and logistic regression. 

Since linear regression predicts continuous target, we set the binary target to 1 and 0. 
Then we consider results of linear regression that are less than 0.5 as 0, greater than 0.5 as 1.

This code also includes data preprocessing and pre-analysis.
