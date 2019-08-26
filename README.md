Problem statement: predict and prevent natural disasters like earthquake, floods, hurricanes etc. Solution: In order to come to solve this problem we are coming up with a web application using Django that will predict the disaster and will tell about nearest safe places if the disaster occurs and what the affected people can do in order to protect themselves.

We all know that each and every disaster is unpredictable and therefore its extremely hard to predict one but our application will not only tell you about the prediction of the disaster using machine learning which is about to happen but it will also tell you the nearest safe places one can go in case of the disaster. Also, we are going to send this data to all the rescue agencies and government in order to pace up the speed of rescue missions and thus preventing a lot of damage.

We will use deep learning for prediction of the disaster which is about to happen. A CNN model will be trained and it will be noticing the changes in the parameters like rains and other visible factors etc... every few seconds.The combined predictions of weather image datasets and prediction from the frequency of floods datasets(A simple prediction model which takes the past history of floods and predicts the date of occurrence of the new flood) be fed to another reinforcement learning model as parameters and it can give a final prediction. The overall prediction can be more accurate in this case rather than using a single model.

The web application also uses Image processing in order to analyse a given area. It will be taking a snapshot of users locality and then it will implement a* algorithm or other path planning algorithms so that the users can reach the nearest safe place in the shortest way possible.

We will be using other API for getting the image of the user's location. We shall be implementing a* algorithm on it with the help of image processing to find the shortest path to the base.

Also, we will be in touch with many NGO's by giving them the live data of the users.

The whole application will be on production with the help of Azure

Thank you
