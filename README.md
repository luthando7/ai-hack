# ai-hack

## Terraplan

This application is Machine learning application that analyses soil data.
Taking soil data from multple soil sensors we train the neural network. After the training, we are able to get the network to tell us which crops will grow best on different types of soil. This can help farmers make the most of their soil and reduce crop failure

On this iteration, we use 7 features to train our model and use those 7 features to predict crops suitable for the soil environment.
We currently have 3 outcomes corn, soybean and wheat.

The prediction is a tensor which has weightings.
```
PREDICTION tensor([2.2442, 3.7262, 3.8062])
```

The first value on the array is the weighting of corn, then soybean and then wheat respectively.
The one that gets a high score wins and becomes the suggestion.

In the example above though, we see that there is not a huge gap between soybean and wheat and so a feature would be to rank these for a person. Giving them a way to understand what they are looking at. 

## How to run the app
```sh
# Linux, Mac:
python -m venv venv
source venv/bin/activate

# Windows
venv\Scripts\activate 

# Insall dependancies
pip install -r requirements.txt

# Optional
python manage.py migrate

# Running the application
cd terraplan
python manage.py runserver
```
The site will be on http://127.0.0.1:8000

## Video presentation

https://youtu.be/Im7Nd_LdA5c
