## Use This Template For A New Project

* **Goal**: Learn To Make A Simple Rock Paper Scissors Game

___

**Expected Output**: A Question Asking What You Pick, Assigning That To A String, Picking The Computers Choice, Picking Who Is The Winner   
<br>
<br>
**Skills Learned**: For Loops, Functions, If Statements, Return
<br>
<br>
**Extra Info**: Your Code May Not Be The Same As The Solution Given
___

**Hints (Add Hints Here)**:
<br>

<details>
  <summary>For Loop & User Input</summary>

  <br>
  How To Use A Loop Loop, And Take User Input<br>


  ```python

  list = ["Name", "Age", "Height"]
  x = 1

  for i in list:
    print(f"{x}. " + i)
    x = x + 1

  pick = input("Enter Your Pick: ")
  ```

</details>

<details>
  <summary>Assign Value To String</summary>

  <br>
  Use A Function To Assign The Value<br>


  ```python

  answer = int(input("Enter A Value: "))

  def check(value):
    if answer == 1:
      return "Correct"
    elif answer == 2:
      return "Wrong"
    elif answer == 3:
      return "Wrong"

  output = check(answer)
  print(output)
  ```

</details>

<details>
  <summary>Use If Statements</summary>

  <br>
  Use If Statements<br>


  ```python

  pick1 = "Yes"
  pick2 = "No"

  if pick1 == "Yes" and pick2 == "No":
    print("Correct")

  elif pick1 == "No" and pick2 == "No":
    print("Wrong")

  elif pick1 == "No" and pick2 == "Yes":
    print("Wrong")

  else:
    print("Invalid")
  
  ```

</details>
