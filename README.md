# ai-hack

## Terraplan

This application is Machine learning application that analyses soil data.
Taking soil data from multple soil sensors we train the neural network. After the training, we are able to get the network to tell us which crops will grow best on different types of soil. This can help farmers make the most of their soil and reduce crop failure

## How to run the app
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
