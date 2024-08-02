# ai-hack

## How to run the app
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
