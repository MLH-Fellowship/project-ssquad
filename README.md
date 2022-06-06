# The SSquad Portfolio

The portfolio website of Sebastian and Sally from pod 15 of the MLH summer 2022 batch.

# Inspiration
Our portfolio name, the SSquad, was inspired from the fact that both of our names start with an "s" and we make a fun programming squad.

# What it does
Clicking on the photos that appear after you scroll down from the initial landing page leads to a page introducing each member of the SSquad. Each page consists of full-screen sections describing the respective member's previous work experience, hobbies, education, and where they've traveled before. Each section can also be accessed from the navigation bar at the top of any page on the website.

# How we built it
For remote collaboration, we used Discord, Github, and Zoom. Each web page was structured with HTML and styled with CSS. Python and Flask was used to re-route between pages and sections. Jinja was used to create a template for additional work experience, hobbies, and education.

# Challenges we ran into
Neither of us were familiar with Jinja so it took some time to read its documentation and incorporate it into our HTML code. It had also been a while since either of us had used HTML and CSS extensively so re-learning how to use both languages also required reading documentation and watching tutorials.

# Accomplishments that we're proud of
We're proud of completing the Github, portfolio, and Flask tasks as a team in incremental steps and carefully managing the time we had until the deadline. We're also proud of learning Jinja and becoming re-acquainted with HTML and CSS.

# What we learned
* Github
    * how to create issues, branches for each issue, and pull requests
* HTML
    * how to structure a web page in an organized manner
* CSS
    * how to style HTML including centering, shaping, spacing, and coloring elements.

# What's next for The SSquad
We hope to use the Github best practices and technologies we learned while building this portfolio for more exciting projects in the future.



## Installation

Make sure you have python3 and pip installed

Create and activate virtual environment using virtualenv
```bash
$ python -m venv python3-virtualenv
$ source python3-virtualenv/bin/activate
```

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install all dependencies!

```bash
pip install -r requirements.txt
```

## Usage

Create a .env file using the example.env template (make a copy using the variables inside of the template)

Start flask development server
```bash
$ export FLASK_ENV=development
$ flask run
```

You should get a response like this in the terminal:
```
❯ flask run
 * Environment: development
 * Debug mode: on
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
```

You'll now be able to access the website at `localhost:5000` or `127.0.0.1:5000` in the browser! 

*Note: The portfolio site will only work on your local machine while you have it running inside of your terminal. We'll go through how to host it in the cloud in the next few weeks!* 

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.
