# the_gallery

Its an application  let you view some of my picture in my gallery

## Getting Started

**Open your terminal type this:**

* Clone this repository

    ```

    $ git clone https://github.com/JeromeMberia/the_gallery.git
    ```

* Creating a virtual environment

    ```

    $ sudo apt-get install python3-venv
    $ python3 -m venv virtual
    ```

* Activating the virtual environment

    ```

    $ . virtual/bin/activate
    ```

* Installing all dependencies

    ```

    $ pip install -r requirements.txt
    ```

## Prerequisites

  **you must have python if follow this steps:**

* Install  python
  
    ```

    $ sudo add-apt-repository ppa:jonathonf/python-3.8
    $ sudo apt-get update
    $ sudo apt-get install python3.8
    ```

  * Confirm Installation

      ```

      $ python3

      Python 3.8.2 (default, Apr 27 2020, 15:53:34)
      [GCC 9.3.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>>
      ```

  * To exit the interface type *exit()* in interface

      ```

      jerome@jerome-HP-EliteBook-840-G3:~$ python3
      Python 3.8.2 (default, Apr 27 2020, 15:53:34)
      [GCC 9.3.0] on linux
      Type "help", "copyright", "credits" or "license" for more information.
      >>>exit()
      ```

* Install  python

    ```

    $ sudo apt-get install python3-pip
    ```

**Setting up a database for PostgreSQL**

## Run it

* Create a file named .env
  
* In that file type the code below:

    ```

    source virtual/bin/activate

    export DB_NAME='< the database name >'
    export DB_USER='username of your database'
    export DB_PASSWORD='password of your database'
    export SECRET_KEY='< your secert key >'
    export DEBUG=True 
    ```

* Then you go to your terminal and type this to run this application

    ```

    $ . .env
    $ python3 manage.py runserver
    ```

## Built With

* HTML & CSS
* Bootstrap-4
* Python
* Django

## Support and contact details

For ways on how to improve the app contact me via jeromemberia@gmail.com.

## Known Bugs

The image doesn't display it's own modal.
 

## Link to the deployed site

[Live site](https://the--gallery.herokuapp.com/)

## Authors

[Jerome Mberia](https://github.com/JeromeMberia)

### License

This project is licensed under the MIT License - see the [LICENSE.md](https://github.com/JeromeMberia/the_gallery/blob/master/LICENSE)) file for details

Copyright (c) 2020 [Jerome Mberia](https://github.com/JeromeMberia)