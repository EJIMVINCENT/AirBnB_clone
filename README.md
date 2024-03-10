# AirBnB_clone

AirBnB clone built using the Python language and Flask framework, it's a team project aim to clone [AirBnB](https://https://www.airbnb.com/)

## Resources

**Read or watch:**

* cmd module
* packages concept page
* uuid module
* datetime
* unittest module
* args/kwargs
* Python test cheatsheet

## The Console
The console is a command interpreter to manage objects abstraction between objects and how they are stored. This means: from the console code (the command interpreter itself) and from the front-end and RestAPI are built.

**The console will perform the following tasks:**

- create your data model
- manage (create, update, destroy, etc) objects via a console / command interpreter
- store and persist objects to a file (JSON file)

## Web static

- learn HTML/CSS
- create the HTML of your application
- create template of each object

## MySQL storage

- replace the file storage by a Database storage
- map your models to a table in database by using an O.R.M.

## Files and Directories

- models directory contain all classes used for the entire project. A class, called “model” in a OOP project is the representation of an object/instance.
- tests directory contain all unit tests.
- console.py file is the entry point of our command interpreter.
- models/base_model.py file is the base class of all our models. It contains common elements:
    * attributes: id, created_at and updated_at
    * methods: save() and to_json()
- models/engine directory contain all storage classes (using the same prototype). For the moment you will have only one: file_storage.py.

### File Storage == JSON serialization
- convert an instance to Python built in serializable data structure (list, dict, number and string) - for us it will be the method my_instance.to_json() to retrieve a dictionary
- convert this data structure to a string (JSON format, but it can be YAML, XML, CSV…) - for us it will be a my_string = JSON.dumps(my_dict)
- write this string to a file on disk

And the process of deserialization?

**The same but in the other way:**

- read a string from a file on disk
- convert this string to a data structure. This string is a JSON representation, so it’s easy to convert - for us it will be a my_dict = JSON.loads(my_string)
- convert this data structure to instance - for us it will be a my_instance = MyObject(my_dict)

### *args, **kwargs
- *args is a Tuple that contains all arguments
- *kwargs is a dictionary that contains all arguments by key/value

### Installation/Cloning
git clone https://github.com/EJIMVINCENT/AirBnB_clone.git

**change to the AirBnb directory and run the command:**
./console.py

#### Execution

**In interractive mode**

> $ ./console.py
> (hbnb) help

> Documented commands (type help <topic>):
========================================
> EOF  help  quit

> (hbnb)
> (hbnb)
> (hbnb) quit
> $

**in Non-interactive mode**

> $ echo "help" | ./console.py
> (hbnb)

> Documented commands (type help <topic>):
========================================
> EOF  help  quit
>(hbnb)
>> $
> $ cat test_help
> help
> $
>> $ cat test_help | ./console.py
>  (hbnb)

> Documented commands (type help <topic>):
========================================
>> EOF  help  quit
> (hbnb)
> $

### Data Diagram
[![Data diagram](/https://camo.githubusercontent.com/f214d0102e583bf74caae88a5e3de8d24358baec288a25301a7a2b7a038965d9/68747470733a2f2f692e696d6775722e636f6d2f49375655524e522e6a7067)]

### Authors

* [Chiamaka Emeti](https://github.com/chiamablessing)

* [Ejim Onyedikachi Vincent](https://github.com/EJIMVINCENT)