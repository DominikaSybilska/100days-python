<h3>Final Project: Escaping the Maze<h3>
<hr>
  <h5>The main goal of this day was to understand:</h5>
<ul>
  <li>Defining and Calling Python Functions</li>
  <li>Indentation in Python</li>
  <li>While Loops</li>
</ul>
  
It was done by resolving simple problems that are offered by https://reeborg.ca/
<br>
 <p>Look below to one of the levels – Escape the Maze.
The robot was spawned at a random place with a random position. You have to build the algorithm to achieve the goal every time. The code was simple easy:</p>
<br>

```python
def turn_right():
    turn_left()
    turn_left()
    turn_left()

while front_is_clear():
    move()
turn_left()   

while at_goal() == False:
    if right_is_clear() == True:
        turn_right()
        move()
    elif front_is_clear() == True:
        move()
    else:
        turn_left()
```
<img src="https://user-images.githubusercontent.com/98851253/154312745-8abc5397-27b7-4a1d-b29c-3a1527280868.gif"/>

