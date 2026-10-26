HomeHub — Real Estate Platform for Uzbekistan

Video Demo: https://youtu.be/22drCo_vUZs

Description

HomeHub is a Django-based real estate web application designed for users in Uzbekistan. The main purpose of this project is to provide a platform where users can explore property listings, publish their own properties, save their favorite listings, leave reviews, and communicate with other users.

The project was developed as my CS50x Final Project. It brings several real estate-related features together in one web application and demonstrates my understanding of Python, Django, database models, user authentication, CRUD operations, URL routing, templates, and automated testing.

HomeHub is designed to make property management more convenient for users. Property owners can publish information about properties, including titles, descriptions, prices, locations, areas, and the number of rooms. Other users can browse available listings and find properties that match their needs.

The application uses Django for its backend functionality, Django REST Framework for API development, SQLite as its default database, and HTML and CSS for its web interface.

Features

User Authentication and Profiles

* User registration and login.
* User profile management.
* Authentication for accessing user-specific features.

Property Management

* Create property listings.
* View property details.
* Edit existing listings.
* Delete listings owned by the current user.
* Store information such as title, description, price, address, location, area, and number of rooms.

Property Search and Filtering

* Browse available property listings.
* Search for properties.
* Filter listings using the available search criteria.

Favorites

* Save interesting properties to a favorites list.
* View saved properties later.

Reviews

* Leave reviews using the available review functionality.
* View reviews associated with properties.

Messaging

* Communicate with other users through the messaging functionality.
* Send and view messages using regular page requests.

Dashboard and Administration

* Access a personal dashboard.
* Manage application data through Django’s administration panel.
* Manage users and property-related records according to administrative permissions.

REST API

The project includes an API built with Django REST Framework. The API provides endpoints for accessing property-related data according to the application’s configuration and permissions.

Geographic Information

Property listings support optional geographic coordinates. These coordinates can be used for future map-based functionality with OpenStreetMap.

Technologies Used

* Python — programming language.
* Django — web framework and backend development.
* Django REST Framework — REST API development.
* SQLite — default database.
* HTML — page structure.
* CSS — styling and layout.
* Pillow — image processing and image-field support.

Project Structure

The project is organized into separate Django applications, with each application responsible for a specific part of the platform.

Application	Purpose
pages	Homepage and general pages
users	User accounts, authentication, and profiles
properties	Property listings and search
favorites	Favorite property management
reviews	Property reviews
chat	User messaging
dashboard	Personal dashboard
payments	Premium listing payment management
api	REST API endpoints
homehub	Main Django project configuration

The project also contains manage.py, requirements.txt, templates, static files, and database configuration.

Installation and Setup

Follow these steps to run HomeHub locally.

1. Clone the Repository

git clone https://github.com/abdulmatin-samadi/Homehub.git
cd Homehub

2. Create a Virtual Environment

python3 -m venv venv

3. Activate the Virtual Environment

On macOS or Linux:

source venv/bin/activate

On Windows:

venv\Scripts\activate

4. Install Dependencies

python3 -m pip install --upgrade pip
python3 -m pip install -r requirements.txt

5. Apply Database Migrations

python3 manage.py migrate

6. Create an Administrator Account

python3 manage.py createsuperuser

Follow the prompts to create the administrator account.

7. Run the Development Server

python3 manage.py runserver

Open the following address in your browser:

http://127.0.0.1:8000/

Main URLs

The following routes are provided by the application:

URL	Description
/	Homepage
/users/	User account functionality
/elonlar/	Property listings
/sevimlilar/	Favorite properties
/sharhlar/	Reviews
/xabarlar/	Messages
/dashboard/	Personal dashboard
/api/properties/	Property REST API
/admin/	Django administration panel

Some routes may require authentication or particular permissions.

Testing

The project includes automated tests for the property model.

To run the tests, execute:

python3 manage.py test

The current test suite checks:

* Whether the property’s string representation returns its title.
* Whether the property’s absolute URL points to the expected detail page.

The tests passed successfully in the development environment.

Django’s system check can also be run with:

python3 manage.py check

The system check reported no issues in the development environment.

Implementation Notes

* The project uses a custom user model, users.User.
* Property owners can manage their own listings.
* Property listings support optional geographic coordinates.
* Messaging uses regular HTTP page requests rather than WebSockets.
* The payment system supports administrative approval; a live Payme or Click payment gateway is not integrated.
* SQLite is the default database for local development.
* The project is organized into multiple Django applications to separate responsibilities and make the codebase easier to maintain.

Future Improvements

Possible future improvements include:

* Real-time messaging using WebSockets.
* Integration with online payment providers such as Payme or Click.
* Additional automated tests for application features and user permissions.
* Improved property search and filtering.
* Expanded map functionality using OpenStreetMap.
* Production deployment with appropriate security settings.
* Improved accessibility and responsive design.
* Additional API endpoints and documentation.

What I Learned

Developing HomeHub helped me improve my understanding of Python and Django. I gained practical experience with database models, user authentication, URL routing, templates, CRUD operations, application organization, and automated testing.

I also learned how different components of a web application work together to provide functionality to users. Building this project gave me an opportunity to apply concepts learned during CS50x to a larger application.

Author

Name: Abdulmatin Samadi
GitHub: abdulmatin-samadi
Location: Tashkent, Uzbekistan

Acknowledgments

Thanks to Harvard University’s CS50 team for providing the CS50x course and learning resources that supported my development as a programmer.

