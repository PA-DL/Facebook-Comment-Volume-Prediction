# Facebook-Comment-Volume-Prediction

I worked on the Facebook Comment Volume Dataset. Which you can find here: https://archive.ics.uci.edu/ml/datasets/Facebook+Comment+Volume+Dataset
I made some change from the original dataset. I didn't use all the derived features and i didn't use the promote feature since none of the post were promoted. 

We had to do some data visualization on this dataset, but also try different model to find the best model tu predict how much comments a post will receive in H hours (H being a feature).

That's why you can see on my jupyter notebook two parts, the first one with data vis and the second one you can see me testing models to find out which is the best model and the best one is the Random Forest. 

We also had to create an API with Flask or Django (i used Flask). And it's why there is a folder called API with in it two python script and one pickle modle which is the model of my Randon Forest. 
