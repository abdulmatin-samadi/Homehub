HomeHub — Real Estate Platform for Uzbekistan

HomeHub is a Django-based real estate platform designed for users in Uzbekistan. Users can create property listings, search and filter properties, save favorites, leave reviews, and communicate with property owners.

Features

* User registration, login, and profile management
* Property listing creation, editing, viewing, and deletion
* Property search and filtering
* Favorites
* Property reviews
* Messaging between users
* Personal dashboard
* Django administration panel
* REST API built with Django REST Framework
* Optional map coordinates using OpenStreetMap

Technologies

* Python
* Django
* Django REST Framework
* SQLite
* HTML and CSS
* Pillow

Project Structure

The project contains the following Django applications:

Application	Purpose
pages	Homepage
users	User accounts and profiles
properties	Property listings and search
favorites	Saved properties
reviews	Property reviews
chat	User messaging
dashboard	Personal dashboard
payments	Premium listing payment management
api	REST API

Installation

1. Clone the repository

git clone https://github.com/abdulmatin-samadi/Homehub.git
cd Homehub

2. Create and activate a virtual environment

python3 -m venv venv
source venv/bin/activate

On Windows:

venv\Scripts\activate

3. Install dependencies

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

4. Apply database migrations

python3 manage.py migrate

5. Create an administrator account

python3 manage.py createsuperuser

6. Run the development server

python3 manage.py runserver

Open http://127.0.0.1:8000/ in your browser.

Main URLs

URL	Description
/	Homepage
/users/	User accounts
/elonlar/	Property listings
/sevimlilar/	Favorite properties
/sharhlar/	Reviews
/xabarlar/	Messages
/dashboard/	Personal dashboard
/api/properties/	Property REST API
/admin/	Administration panel

Testing

Run the automated tests with:

python3 manage.py test

The project includes tests for the property model’s string representation and absolute URL generation.

Implementation Notes

* The project uses a custom user model, users.User.
* Property owners can manage their own listings.
* Property listings support optional geographic coordinates.
* Messaging uses regular page requests rather than WebSockets.
* The payment system currently supports administrative approval; a live Payme or Click payment gateway is not integrated.
* The application uses SQLite by default.

Future Improvements

* Real-time messaging
* Payment gateway integration
* Additional automated tests
* Production deployment and security configuration