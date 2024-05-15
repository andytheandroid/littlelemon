# LittleLemon


By Carlos Torres Sanchez

LittleLemon is a project in Django that provides APIs for managing menus, menu items, and bookings.

## Getting Started

1. **Clone the Repository:**

url: https://github.com/andytheandroid/littlelemon


2. **Create a Virtual Environment:**

in your project folder in a terminal(cmd in windows) use this command

 ```
python -m venv venv source venv/bin/activate
```


3. **Install Dependencies using pip(make sure you have python properly configured):**

Dependencies to install:

- django
- djangorestframework
- pymysql
- Insomnia,Postman or any other API testing tool
- Mysql server
- A mysql client of your choice


4. **Database Setup:**
- Configure your database settings in `settings.py`.
- Run migrations:
  ```
  python manage.py makemigrations
  python manage.py migrate
  ```

5. **Create Superuser that will be used to access django admin**

```
  python manage.py createsuperuser


  ```


6. **Run the Development Server by default it will run on port 8000:**

```
  python manage.py runserver


  ```


7. **The menu and booking endpoints to test are on the url patterns array in the urls.py file on the littlemon module:**

Example endpoint


http://localhost:8000/menu-items/items


The menu and booking endpoints are secured so you need to authenticate using a token, to get a token you must have credentials(other that the super user) registered on django admin, once that you have completed that step call this endpoint with your credentials(as json)

Endpoint to get a token:

http://localhost:8000/api-token-auth/


With the token generated from the above endpoint, put it on the Bearer token section of the Auth tab of insomnia, it should be able to retrieve the data from the apis to test