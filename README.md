<p align="center">
  <h2 align="center">Buzzbox</h2>

  <p align="center">
    Project for Buzzbox startup
    <br />
    <br />
    <a href="https://github.com/Danielvalev/kutiika">View Demo</a>
    ·
    <a href="https://github.com/Danielvalev/kutiika/issues">Report Bug</a>
    ·
    <a href="https://github.com/Danielvalev/kutiika/issues">Request Feature</a>
  </p>
</p>



<!-- TABLE OF CONTENTS -->
<details open="open">
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
        <li><a href="#application-requirements">Application Requirements</a></li>
        <li><a href="#installation">Installation</a></li>
      </ul>
    </li>
    <li><a href="#roadmap">Roadmap</a></li>
    <li><a href="#license">License</a></li>
    <li><a href="#contact">Contact</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

### Built With

* [Python](https://www.python.org/)
* [Django](https://www.djangoproject.com/)
* [PostreSQL](https://www.postgresql.org/)
* [Bootstrap](https://getbootstrap.com)



<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these simple example steps.

### Application Requirements

1. Python 3.9.6 or newer
2. Django 3.2.9
3. Pip
4. Virtual Environment
5. Other packages listed in requirements.txt

### Installation
Make sure you have already downloaded and install python3 and pip

1. The first thing to do is to clone the repository:
 ```sh
$ git clone https://github.com/Danielvalev/buzzbox
$ cd buzzbox
`````````````

2. Create a virtual environment to install dependencies:
- For MacOS: 
 ```sh
$ python3 -m venv env 
`````````````

- For Windows:
 ```sh
C:\Users\Name\kutiika> py -m venv env
`````````````

3. Activate your Virtual Environment
- For MacOS:
 ```sh
$ source env/bin/activate
`````````````
- For Windows:
 ```sh
C:\Users\Name\kutiika> env\Scripts\activate 
`````````````

4. Install dependencies listed in the requirement.txt:
 ```sh
(env)$ pip install -r requirements.txt 
`````````````
Note the `(env)` in front of the prompt. This indicates that this terminal
session operates in a virtual environment set up by `py -m venv env`.

Once `pip` has finished downloading the dependencies:
```sh
(env)$ cd buzzbox
```

5. Run Server
```sh
(env)$ python manage.py runserver
```
Expected result: 
```
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).
January 12, 2022 - 11:14:25
Django version 3.2.9, using settings 'core.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CTRL-BREAK.
```

6. If you cannot run step 5, You may have to migrate any unapplied migrations by : 
```sh
(env)$ python manage.py makemigrations
(env)$ python manage.py migrate
```
After this run Step 5 again. 

And navigate to buzzbox homepage using `http://127.0.0.1:8000`.

#### Other syntaxes
To kill/stop the server 
> Ctrl + c

To deactivate the Virtual Environment
```sh
(env)$ deactivate
```

<!-- ROADMAP -->
## Roadmap

See the [open issues](https://github.com/Danielvalev/buzzbox/issues) for a list of proposed features (and known issues).


<!-- LICENSE -->
## License

Distributed under the MIT License. See `LICENSE` for more information.



<!-- CONTACT -->
## Contact

Daniel Valev - danielvalev89@gmail.com

Project Link: [https://github.com/Danielvalev/buzzbox](https://github.com/Danielvalev/buzzbox)

<!-- MARKDOWN LINKS & IMAGES -->
[product-screenshot]: images/screenshot.png
