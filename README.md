# Build your own API Project
A python project which will build an API which can add, read, edit and delete data in a database stored in mysql . This database will consist of student information and a nested address table. Postman is used to test the API by sending reqeusts. 



 
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
 
  ------------
  
  <br/>
    <br/>
  
 # Address Data
 
 ## Post ```/api/addresses```

### Parameters
No Parameters

### Request Body
 ```
{
    "city": "London",
    "country": "United Kingdom",
    "house_name": "Janet",
    "number": 9,
    "road": "Sunshine drive",
    "state": "Islington",
    "student_id": 1,
    "zipcode": "SW1 1AA"
}
 ```
### Cookies
No cookies

### Success Response
#### HTTP Status 201

 ```
{
    "data": {
        "city": "London",
        "country": "United Kingdom",
        "house_name": "Janet",
        "number": 9,
        "road": "Sunshine drive",
        "state": "Islington",
        "student_id": 1,
        "zipcode": "SW1 1AA"
    },
    "msg": "New address data created for a student",
    "status": 201
}
 ```
<br/>

### Error Response


#### HTTP Status 400 Corresponding Student Not Found

 ```
{
    "msg": "Student not found",
    "status": 400
}
 ```
 
 #### HTTP Status 400 Missing Fields

 ```
{
    "msg": "Please specify the fields, <student_id>, <number>, <house_name>, <road>, <city>, <state><country>, <zipcode> for address",
    "status": 400
}
 ```
 
   ------------
 
 ## Get ```/api/students/<int:address_id>```

### Parameters
Where ```<int:address_id>``` is the address ID (not to be confused with the student id which is a foreign key that links to the primary key called 'id' in the students table)

### Request Body
No requests

### Cookies
No cookies

### Success Response
#### HTTP Status 200

 ```
{
    "data": {
        "city": "London",
        "country": "United Kingdom",
        "house_name": "Janet",
        "id": 1,
        "number": 9,
        "road": "Sunshine drive",
        "state": "Islington",
        "student_id": 1,
        "zipcode": "SW1 1AA"
    },
    "status": 200
}
 ```
<br/>
#### HTTP Status 200 Address Not Found

 ```
{
    "msg": "Address with the id 5 was not found ",
    "status": 200
}
 ```
  ------------
  
## Patch ```/api/addresses/<int:address_id>```

### Parameters
Where ```<int:address_id>``` is the id of the address to be updated

### Request Body
 ```
{
    "house_name": "Bob",
    "road": "Cresent drive",
    "state": "Islington"
}
 ```
### Cookies
No cookies

### Success Response
#### HTTP Status 200

 ```
{
    "data": {
        "city": "London",
        "country": "United Kingdom",
        "house_name": "Bob",
        "id": 1,
        "number": 9,
        "road": "Cresent drive",
        "state": "Islington",
        "student_id": 1,
        "zipcode": "SW1 1AA"
    },
    "msg": "Address with ID 1 updated",
    "status": 200
}
 ```
 
 ##### Table nested within the Student table
 
  ```
 {
    "data": [
        {
            "address_data": [
                {
                    "city": "London",
                    "country": "United Kingdom",
                    "house_name": "Bob",
                    "id": 1,
                    "number": 9,
                    "road": "Cresent drive",
                    "state": "Islington",
                    "student_id": 1,
                    "zipcode": "SW1 1AA"
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
<br/>

#### HTTP Status 200 Address ID Does Not Exist
 ```
{
    "msg": "Address with the id 15 was not found ",
    "status": 200
}
 ```

### Error Response

#### HTTP Status 400 Updating Column That Does Not Exist

 ```
{
    "msg": "Error referencing columns, <student_id>, <number>, <house_name>, <road>, <city>, <state>",
    "status": 400
}
 ```
  ------------
 ## Delete ```/api/students/<int:address_id>```

### Parameters
Where ```<int:address_id>``` is the corresponding address id

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
