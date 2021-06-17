## Make A Flask App

* **Goal**: Make A Flask App With 4 Routes, Homepage, User Page, User
& Password Page, And A Variables Page (If You Do Not Understand, Just Make A Basic Flask Project)

___

**Expected Output**: (Google Doc: Info There)[https://docs.google.com/document/d/1cBqoqFzbug92yPLVc5yay2nKnyPq5QB7p4oCkli1kWQ/edit?usp=sharing]
<br>
<br>
**Skills Learned**: Flask, Jinja, HTML, Variables, Functions, Return

___

**Hints (Add Hints Here)**:
<br>

<details>
  <summary>Start A Flask App</summary>

  <br>
  How To Start A Flask App `pip install flask`<br>


  ```python
  from flask import Flask

  app = Flask(__name__)

  @app.route('/')
  def index():
    return f"""<h1> Hey! </h1>"""

  ```

</details>

<details>
  <summary>Use Variables In Flask</summary>

  <br>
  How To Use Variables In Flask (Jinja)<br>


  ```python
  from flask import Flask, render_template

  app = Flask(__name__)

  @app.route('/')
  def index():
    myVar = "GitHub"
    return render_template('index.html', myVar = myVar)

    # How To Use In HTML File:
    <!DOCTYPE html>
    <html lang="en" dir="ltr">
      <head>
        <meta charset="utf-8">
        <title>Home Page</title>
      </head>
      <body>
         <h1>{{ myVar }}</h1>
      </body>
    </html>

  ```

</details>

<details>
  <summary>How To Make Extentions</summary>

  <br>
  How To Make Extentions (Variables)<br>


  ```python
  from flask import Flask

  app = Flask(__name__)

  @app.route('/<user>')
  def index(user):
    if user == "GitHub":
      return f"""<h1> Hey GitHub! </h1>"""
    else:
      return f"""Hey! You Don't Have Access Here!"""

  ```
  
</details>
