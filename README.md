# New York Taxi Fare Prediction

The New York taxi industry is a significant contributor to the city's transportation system, and it is crucial to ensure that passengers are charged a fair price for their rides. In this project, we aim to predict the taxi fare for a given set of latitude and longitude coordinates. The distance between the coordinates needs to be calculated, but as the coordinates are given in degrees and the distance is measured in meters, we use the Haversine formula to compute the distance accurately
![vidar-nordli-mathisen-ZYDhBqxJnJ8-unsplash](https://user-images.githubusercontent.com/120264399/233767973-a6125723-863a-4e9e-b385-a93d48bcf3aa.jpg)


To provide additional insights into the data, we perform some analysis on the dataset, including determining which year had the highest number of passengers and which month taxi drivers collected the most revenue. This information can be valuable to taxi companies and city officials to understand the trends in the taxi industry and make informed decisions.

We train two machine learning models, decision tree and random forest, on the dataset to predict the fare accurately. These models take into account factors such as the distance traveled, pickup and dropoff locations, time of day, and day of the week. The trained models provide accurate fare predictions, which can be used to ensure passengers are charged appropriately for their rides.

We have also developed a Flask app that can accept post requests and return the fare prediction based on the provided coordinates. This app can be easily integrated into any other system, making it easier for users to access the fare prediction service. The app's next step is to dockerize it, making it more portable and easier to deploy, and then host it on the cloud for even greater accessibility.

In summary, this project provides a valuable service to both passengers and taxi companies by accurately predicting taxi fares based on latitude and longitude coordinates. With the additional analysis and machine learning models, it provides valuable insights into the taxi industry's trends and helps ensure a fair price for passengers.
