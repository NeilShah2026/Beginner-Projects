## Make A Passoword Generator

* **Goal**: Use The Random And String Module To Randomly Pick Letters And Numbers And Make A Password

___ 

**Expected Output**: 4 Letters (Both Capital/Lowercase), 3 Numbers, 1 Special Character
<br>
<br>
**Skills Learned**: Basic Usage Of Random Module, Basic ASCII Characters Usage, For Loops, Lists

___

**Hints (Only Use If Needed)**:
<br>

<details>
  <summary>To Pick A Letter</summary>
  
  <br>
  Make Sure To Use The Random & String Packages

  ```python
  import random
  import string
  
  # `string.ascii_letters` Is A List of Letters
  # To Pick A Letter:
  letter = random.choice(string.ascii_letters)
  ```
  
</details>

<details>
  <summary>To Pick A Number</summary>
  
  <br>
  Make Sure To Use The Random Package

  ```python
  import random

  # To Pick A Number
  number = random.randint(1, 10)
  ```
  
</details>

<details>
  <summary>Use A For Loop & Append</summary>
  
  <br>

  ```python
  
  # Make A String
  string = "github"
  
  # Make The For Loop & Empty List
  
  list = []
  for i in string:
    # Append Each Letter To A List
    list.append(i)
  ```
  
</details>

<details>
  <summary>Shuffle List And Combine</summary>
  
  <br>

  ```python
  import random
  
  # Make A String
  list = ["g", "i", "t", "h", "u", "b"]
  
  # Shuffle The List
  new_list = random.shuffle(list)
  
  # Join The List
  final_password = "".join(pass_list)
  
  ```
  
</details>
