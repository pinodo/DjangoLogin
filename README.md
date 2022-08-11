<div id="top"></div>

<div align="center">
<h3 align="center">Django Login</h3>

  <p align="center">
    Django Login Implementation
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li>
      <a href="#getting-started">Getting Started</a>
      <ul>
        <li><a href="#prerequisite">Prerequisite</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
  </ol>
</details>

<!-- ABOUT THE PROJECT -->
## About The Project
This project aims to know the basic django structure from installation to the basic use and structure. <br />
Moreover, for the further use when I create a new project, this project could be a milestone.

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)

<!-- GETTING STARTED -->
## Getting Started

This is an example of how you may give instructions on setting up your project locally.
To get a local copy up and running follow these simple example steps.

### Prerequisite
1. Install the latest version of python and django

### Installation
1. Make a virtual environment in cmd
   ```sh
   i) py -3 -m venv {envname}
    ```
   ```sh
   ii) cd {envname}/Scripts
   ```
   ```sh
   iii) activate
   ```
   Then now you can see your virtual environment as a bracket as
   ```sh
   ({appname})Users\...
   ```
2. Install django
   ```
   pip install django
   ```   
3. Create a new django project in a root file
   ```sh
   django-admin startproject {projectname}
   ```
4. Create an app in the project file
   ```sh
   cd {projectname}
   ```
   ```sh
   python manage.py startapp {appname}
   ```
5. Go to project file and work on
   ```sh
   cd {projectname}
   ```
Total File Structure<br />
```hash
.
└── {filename}
    ├── {envname}
    └── {projectname} (work on in here)
        └── {appname}
            └── ...
        └── {projectname}
            └── ...
```

*** Connect to PostgreSQL ***
1. Install PostgreSQL
2. Install libraries
   ```sh
   pip install psycopg2
   pip install Pillow
   ```
3. Migrate them to the project
   ```sh
   python manage.py makemigrations
   python manage.py migrate
   ```

<!-- └── -->
<p align="right">(<a href="#top">back to top</a>)</p>


