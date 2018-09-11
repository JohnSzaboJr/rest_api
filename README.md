# rest_api
A RESTful API implementation in Django/Python

A database of cities in JSON format.

* **Setup**

pip install django

pip install djangoframework

pip install Pillow

python manage.py runserver

* **URL**

GET : /Cities/ or /Cities/[id]

POST: /Newcity/

* **Method:**

`GET` | `POST` | `DELETE` | `PUT`

* **URL Params:**

**Optional:**
 
`id=[integer]`

* **Data Params**

**Example:**

{

    name: [string, required, format: starting with uppercase, can only contain letters, space and hyphen]
    
    population: [integer, required]
    
    photo: [image file, limit: 150kb]
    
}

* **Success Response:**

**Code:** 200 (OK) or 201 (Created)

* **Error Response:**

**Code:** 400 (Bad Request) or 201 (Not Found)

* **Sample Calls:**

curl -X GET http://127.0.0.1:8000/Cities/

curl --user test -d '{"name":"Shanghai", "population":"24115000"}' \
-H "Content-Type: application/json" -X POST http://127.0.0.1:8000/Cities/
