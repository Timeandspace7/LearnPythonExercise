
# brief: 随机策略，碰到墙壁后，随机转向
# date : 2019.12.14
# by   : udality

import turtle
import random
import vacuumsetup

# fun  : vacuumTrutle
# brief: 画出一条白色的线，意思为清除干净。
def vacuumTurtle():
    # Create a vacuum turtle.
    t = turtle.Turtle()
    t.width(10); t.speed(0)
    t.color("white")
    return t

# fun  : nearWall
# brief: 靠近墙壁则返回 True .  
def nearWall(t):
    # Is the turtle near a wall?
    x, y = t.pos()
    bounds = 100 - t.width() * 2/3
    print(bounds)
    return not (-bounds < x < bounds
            and -bounds < y < bounds)
    

# fun  : cleanRoom
# brief: 随机移动清扫屋子，当碰到墙壁时，随机转向。
def cleanRoom():
    t = vacuumTurtle()
    # Write your code here!
    t.forward(5)
    for count in range(5000):
        t.forward(5)
        if nearWall(t):
            t.back(5)
            angle= 180 + random.randint(-50,50)
            t.right(angle)
            


# Don't remove this function call!
cleanRoom()


