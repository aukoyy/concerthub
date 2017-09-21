![concerthub Logo](https://www.ntnu.no/documents/10310/1272645483/PhD-award-NTNU.jpg/aa8b5a76-c9ce-4876-a116-5b1d4323a240?t=1483311043529)

# concerthub

concerthub is the place to be for local and big band to run your gig at gløs


## Set up on Linux

Install and configure PostgreSQL. (Drive > Team Isbjørn > Tech docs > Auk_PostgreSQL)

Make sure to have virtualenv and pip installed

Go to your preferred code / github folder

```
$ virtualenv -p python3 it1901
$ cd it1901
$ source bin/activate
$ mkdir src
$ cd src
```
Remember det dot (".") at the end of following command. It copies all files to current folder,
 as opposed to a new folder with all the files. 
```
$ git clone '[repo link]' .
```
Install all the dependencies:
```
$ pip install -r requirements.txt
```

You may now test the server
```
$ python manage.py runserver
``` 

To get the models and admin up and running, run 
```
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py createsuperuser
```
127.0.0.1:8000/admin should now work


## Set up on Windows
 - **Install Linux**
 - *Follow above steps*
 
 
Install and configure PostgreSQL. (Drive > Team Isbjørn > Tech docs > Auk_PostgreSQL)

Make sure to have python 3.5 or above, virtualenv and pip installed

Go to your preferred code / github folder

```
> virtualenv it1901
> cd it1901/Scripts
> activate
> cd ..
> mkdir src
> cd src
```
Remember det dot (".") at the end of following command. It copies all files to current folder,
 as opposed to a now folder with all the files. 
```
> git clone '[repo link]' .
```
Install all the dependencies:
```
> pip install -r requirements.txt
```

You may now test the server
```
> python manage.py runserver
``` 

To get the models and admin up and running, make sure you installed and configured 
the database, then run 
```
> python manage.py makemigrations
> python manage.py migrate
> python manage.py createsuperuser
```
127.0.0.1:8000/admin should now work









