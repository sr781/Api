# Build your own API Project
A project which will build an API which can add, read, edit and delete data in a database. This database will consist of student information and a nested address table.

# Resources

</br>

# Student Data


## Post ```/api/students```

### Parameters
No Parameters

### Request Body
 ```
{
    "age": 23,
    "city": "Guildford",
    "english_grade": 8,
    "gender": "male",
    "languages_grade": 7,
    "lat": "52.11",
    "long": "11.23",
    "maths_grade": 6,
    "name": "Joe Bloggs",
    "nationality": "British",
    "sciences_grade": 6
}
 ```
### Cookies
No cookies

### Success Response
#### HTTP Status 201

 ```
{
    "data": {
        "age": 23,
        "city": "Guildford",
        "english_grade": 8,
        "gender": "male",
        "languages_grade": 7,
        "lat": "52.11",
        "long": "11.23",
        "maths_grade": 6,
        "name": "Joe Bloggs",
        "nationality": "British",
        "sciences_grade": 6
    },
    "msg": "New student has been created",
    "status_code": 201
}
 ```
<br/>

### Error Response

#### HTTP Status 400 Missing Field

 ```
{
    "msg": "Please check to make sure the following fields have been added: <name>, <nationality>, <city><lat>, <long>, <gender>, <age>, <english_grade>, <maths_grade>, <sciences_grade>, <languages_grade>",
    "status_code": 400
}
 ```


## Get ```/api/students ```

### Parameters
No Parameters

### Request Body
No request body

### Cookies
No cookies

### Success Response
#### HTTP Status 200
 ```
{
    "data": [
        {
            "address_data": [
                {
                    "city": "Guildford",
                    "country": "United Kingdom",
                    "house_name": "Janet",
                    "id": 1,
                    "number": 9,
                    "road": "Sunshine drive",
                    "state": "Surrey",
                    "student_id": 1,
                    "zipcode": "GU1 1AA"
                }
            ],
            "age": 23,
            "city": "Guildford",
            "english_grade": 8,
            "gender": "male",
            "languages_grade": 7,
            "lat": "52.11",
            "long": "11.23",
            "maths_grade": 6,
            "name": "Joe Bloggs",
            "nationality": "British",
            "sciences_grade": 6
        }
    ],
    "status": 200
}
 ```
 ------------

#### HTTP Status 200 No Results Found
 ```
 {
    "msg": "No results",
    "status": 200
}
  ```
 ------------
## Get ```/api/students/<int:student_id> ```

### Parameters
Where ``` /<int:student_id>``` is the ID of the student

### Request Body
No request body

### Cookies
No cookies

### Success Response
#### HTTP Status 200
 ```
{
    "data": {
        "address_data": [
            {
                "city": "Guildford",
                "country": "United Kingdom",
                "house_name": "Janet",
                "id": 1,
                "number": 9,
                "road": "Sunshine drive",
                "state": "Surrey",
                "student_id": 1,
                "zipcode": "GU1 1AA"
            }
        ],
        "age": 23,
        "city": "Guildford",
        "english_grade": 8,
        "gender": "male",
        "languages_grade": 7,
        "lat": "52.11",
        "long": "11.23",
        "maths_grade": 6,
        "name": "Joe Bloggs",
        "nationality": "British",
        "sciences_grade": 6
    },
    "status": 200
}
 ```

#### HTTP Status 200 Student Not Found
 ```
{
    "msg": "Student with the id 2 was not found ",
    "status": 200
}
 ```
## Patch ```/api/students/<int:student_id>```

### Parameters
Where ```<int:student_id>``` is a student id

### Request Body
 ```
{
    "age": 28,
    "city": "London",
    "languages_grade": 4
}
 ```
### Cookies
No cookies

### Success Response
#### HTTP Status 200

 ```
{
    "data": {
        "address_data": [],
        "age": 28,
        "city": "London",
        "english_grade": 8,
        "gender": "male",
        "languages_grade": 4,
        "lat": "52.11",
        "long": "11.23",
        "maths_grade": 6,
        "name": "Joe Bloggs",
        "nationality": "British",
        "sciences_grade": 6
    },
    "msg": "Student with ID 1 updated",
    "status": 200
}
 ```
<br/>

#### HTTP Status 200 Student ID Does Not Exist
 ```
{
    "msg": "Student with the id 5 was not found ",
    "status": 200
}
 ```

### Error Response

#### HTTP Status 400 Updating Column That Does Not Exist

 ```
{
    "msg": "Error referencing columns. Please check to make sure the following fields have been added: <name>, <nationality>, <city> <lat>, <long>, <gender>, <age>, <english_grade>, <maths_grade>, <sciences_grade>, <languages_grade>",
    "status": 400
}
 ```
  ------------
## Delete ```/api/students/<int:student_id>```

### Parameters
Where ```<int:student_id>``` is a student id

### Request Body
 ```

 ```
### Cookies
No cookies

### Success Response
#### HTTP Status 201

 ```

 ```
<br/>

### Error Response

#### HTTP Status 400 Missing Field

 ```

 ```
 
 

 
 
