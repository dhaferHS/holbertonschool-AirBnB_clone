# AirBnB_clone

![hbnb_logo](https://user-images.githubusercontent.com/69083631/176741018-39fdad26-a09d-4b84-acb9-60a450571814.png)

## Concept
```
- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)
```


* A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
* A database or files that store data (data = objects)
* An API (Application programming interface) that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


## Step 1: Write a command interpreter to manage your AirBnB objects

 * To implement the parent class "BaseModel".
 * To create a simple flow of serialization/deserialization:(the process of turning some object into a data format that can be restored later) Instance <-> Dictionary <-> JSON string <-> file
 * To create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
 * To create the first abstracted storage engine of the project: File storage
 * To create all unittests to validate all the classes and storage engine
 

### What’s a command interpreter?

 * Create a new object (ex: a new User or a new Place)
 * Retrieve an object from a file, a database etc…
 * Do operations on objects (count, compute stats, etc…)
 * Update attributes of an object
 * Destroy an object

### __Resources__

* cmd module
* Packages concept page
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet

### __General__

* __How to create a Python package ?__

First, we create a directory and give it a package name, preferably related to its operation. Then we put the classes and the required functions in it. Finally we create an `__init__.py` file inside the directory, to let Python know that the directory is a package.

* __How to create a command interpreter in Python using the `cmd` module ?__
```
1. import cmd
2. create class HBNBCommand(cmd.Cmd)
3. set the prompt as "(hbnb) "
4. create the commands with module "def do_ANYTHING"
5. At the end of the file,
if __name__ == '__main__':
    HBNBCommand().cmdloop()
```
* __What is Unit testing and how to implement it in a large project ?__
```
1. to use the unittest module
2. import unittest
```
* __How to serialize and deserialize a Class ?__

What is serialize and deserialize a Class?
```
<class 'BaseModel'> -> to_dict() -> <class 'dict'> -> <class 'BaseModel'>
```

1. we can recreate a BaseModel from another one by using a dictionary representation
2. Convert the dictionary representation to a JSON string in order to reading for us, like humains.

3. Simple Python data structure:
```
{ '12': { 'numbers': [1, 2, 3], 'name': "John" } }
```
4. JSON string representation: 
```
'{ "12": { "numbers": [1, 2, 3], "name": "John" } }'
```
5. Serialization : Instance -> Json File<br>
Using "dump" for making a file Json
6. Deserialization : Json File -> Instance<br>
Using "load" for making a file Python

* __How to write and read a JSON file ?__
```
1. import json
2. Create a dictionary object
3. Open the dictionary object file
4. Using "dump" for creating a Json file to write as Json data type
5. Open the file Json
6. Using "load" for creating the dictionary file to read as Python data type
```
* __How to manage `datetime` ?__<br>
The datetime module supplies classes for manipulating dates and times
1. from datetime import datetime : A combination of a date and a time. Attributes: year, month, day, hour, minute, second, microsecond, and tzinfo
2. To initialize the instance attributes ("created_at" and "updated_at") as `datetime.now()`
```
datetime.datetime(2017, 9, 28, 21, 5, 54, 119434)

```
3. isoformat() : DATE and TIME -> String
```
   isoformat() = Return a string representing the date in ISO 8601 format, YYYY-MM-DD:
   
   ex) 
   import datetime

   dt = datetime.datetime(2018, 12, 31, 5, 0, 30, 1000)
   print(d)
   # 2018-12-31 05:00:30.001000

   print(type(d))
   # <class 'datetime.datetime'>
   
   print(d.isoformat())
   # 2018-12-31T05:00:30.001000
   
   print(type(d.isoformat()))
   # <class 'str'>
   
```
4. fromisoformat() : String -> DATE and TIME
```
ex)
import datetime

s = '2018-12-31T05:00:30.001000'
dt = datetime.datetime.fromisoformat(s)

print(dt)
# 2018-12-31 05:00:30.001000

print(type(dt))
# <class 'datetime.datetime'>

print(datetime.datetime.fromisoformat('2018-12-31x05:00:30.001000'))
# 2018-12-31 05:00:30.001000

# print(datetime.datetime.fromisoformat('2018-12-31xx05:00:30.001000'))
# ValueError: Invalid isoformat string: '2018-12-31xx05:00:30.001000'

```

5. To be converted from string to date time object:
```
   strptime() = String to date and time conversion

  ex) datetime.datetime(2017, 9, 28, 21, 5, 54, 119572)
  -> datetime.strptime("%Y-%m-%dT%H:%M:%S.%f")
  ->'2017-09-28T21:05:54.119572'
  
```

* __What is an `UUID` ?__
```
When you want a unique ID, you should call uuid1() or uuid4().<br>
uuid1(): may compromise privacy since it creates a UUID containing the computer’s network address<br>
uuid4(): creates a random UUID<br>
str(uuid) returns a string in the form 12345678-1234-5678-1234-567812345678 where the 32 hexadecimal digits represent the UUID
```

* __What is `*args` and how to use it ?__
```
We can pass a variable number of arguments to a function by using `*args` and `**kwargs` in our code.<br>
In Python, the single-asterisk form of `*args` can be used as a parameter to send a non-keyworded variable-length argument list to functions.
Accepts multiple arguments as a tuple.
```
* __What is `**kwargs` and how to use it ?__
```
The double asterisk form of `**kwargs` is used to pass a keyworded, variable-length argument dictionary to a function.
Like `*args`, `**kwargs` can take however many arguments you would like to supply to it.<br>
However, `**kwargs` differs from *args in that you will need to assign keywords.<br>
When we use `**kwargs` as a parameter, we don’t need to know how many arguments we would eventually like to pass to a function.<br>
Accepts multiple keyword arguments as a dictionary
```

* __How to handle named arguments in a function ?__


## Requirements
### Python Scripts
* Allowed editors: vi, vim, emacs
* All your files will be interpreted/compiled on Ubuntu 20.04 LTS using python3 (version 3.8.5)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/python3`
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should use the pycodestyle (version 2.8.*)
* All your files must be executable
* The length of your files will be tested using wc
* All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
* All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
* All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)' and python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
* A documentation is not a simple word, it’s a real sentence explaining what’s the purpose of the module, class or method (the length of it will be verified)

### Python Unit Tests
* Allowed editors: vi, vim, emacs
* All your files should end with a new line
* All your test files should be inside a folder tests
* You have to use the unittest module
* All your test files should be python files (extension: .py)
* All your test files and folders should start by test_
* Your file organization in the tests folder should be the same as your project
* e.g., For `models/base_model.py`, unit tests must be in: `tests/test_models/test_base_model.py`
* e.g., For `models/user.py`, unit tests must be in: `tests/test_models/test_user.py`
* All your tests should be executed by using this command: `python3 -m unittest discover tests`
* You can also test file by file by using this command: `python3 -m unittest tests/test_models/test_base_model.py`
* All your modules should have a documentation `(python3 -c 'print(__import__("my_module").__doc__)')`
* All your classes should have a documentation `(python3 -c 'print(__import__("my_module").MyClass.__doc__)')`
* All your functions (inside and outside a class) should have a documentation `(python3 -c 'print(__import__("my_module").my_function.__doc__)'` and `python3 -c 'print(__import__("my_module").MyClass.my_function.__doc__)')`
* We strongly encourage you to work together on test cases, so that you don’t miss any edge case

## Execution

Your shell should work like this in interactive mode: :

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```
But also in non-interactive mode: (like the Shell project in C) :

```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```
All tests should also pass in non-interactive mode: $ echo "python3 -m unittest discover tests" | bash

## STEP 1: The Console
![flowchart_the_console](https://user-images.githubusercontent.com/69083631/176741298-c3505293-486d-4b5d-a31f-b120f9ee8ed3.png)

### Console : the command interpreter
prompt : (hbnb)

| COMMAND                                                |                 DESCRIPTION                  |
|--------------------------------------------------------|----------------------------------------------|
| quit                                                   | To exit the console                          |
| EOF                                                    | To exit the console by EOF                   |
| Empty Line + ENTER                                     | Nothing                                      |
| help                                                   | Display the help documentation.              |
| create + class name                                        | Creates an object and print the ID           |
| show + class name + id                                      | To show the informations of the object       |
| destroy + class name + id                                   | To delete an object                          |
| all + class name                                            | To show all the instances of a class         |
| update + class name + id + attribute name + attribute value | To update the attribute of a class         |
| class name + "." + all | To show all the instances of a class         |
| class name + "." + count | To count number of the instances of a class        |
| class name + "." + show + id | To show the informations of the object        |
| class name + "." + destroy + id | To delete an object        |
| class name + "." + update + id + attribute name + attribute value | To update an instance based on his ID |

### Some examples of the command interpreter
show:
![image](https://user-images.githubusercontent.com/98317357/177001366-bf3efca3-0a7e-4721-9b30-dd59797806d6.png)

destroy:
![image](https://user-images.githubusercontent.com/98317357/177001454-ce5114c3-29e2-4cf5-b5b9-735eca47150d.png)

all:
![image](https://user-images.githubusercontent.com/98317357/177001493-71ef1108-9b1d-4d09-914f-5c5bed5fb868.png)

city:
![image](https://user-images.githubusercontent.com/98317357/177001612-735440c2-ab0a-4919-ba91-f7e68736a76d.png)

count:
![image](https://user-images.githubusercontent.com/98317357/177001679-e97a4217-2b91-455f-931f-3be2ad6c5bc8.png)

### More Classes

| CLASSE                                                |                 Attributes                 |
|--------------------------------------------------------|----------------------------------------------|
| State                                                   | name                          |
| City                                                    | state_id<br>name                   |
| Amenity                                   | name                                      |
| Place                                                  | city_id<br>user_id<br>name<br>description<br>number_rooms<br>number_bathrooms<br>max_guest<br> price_by_night<br>latitude<br>longitude<br>amenity_ids             |
| Review                                      | place_id<br>user_id<br>text           |

## :couple: About us ##
This is one of Holberton School tunisia projects was made  in the 9 october 2022!!<br>
If you have a question or a comment, please contact me.<br>
Dhafer Hamza Sfaxi <5037@holbertonstudents.com>