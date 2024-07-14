# Getting Started

First clone the repository from Github and switch to the new directory:

    $ git clone git@github.com/USERNAME/{{ project_name }}.git
    $ cd {{ project_name }}
    
Activate the virtualenv for your project. For example:

    $ virtualenv {{ project_name_venv }}
    $ source project_name_venv/Scripts/activate (for windows)
    $ source project_name_venv/bin/activate (for macos)

**NOTE: Installing inside virtualenv is recommended, however you can start your project without virtualenv too.**

---

**NOTE: After that just install the local dependencies, run migrations, and start the server.**


Install project dependencies:

    $ pip install -r requirements.txt

        
Then simply apply the migrations:

    $ python manage.py migrate
    

You can now run the development server:

    $ python manage.py runserver

**NOTE: I am using Git Bash as terminal**