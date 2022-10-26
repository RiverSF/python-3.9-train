from turtle import *

# 设置笔刷宽度:
width(4)
speed(2)

penup()
setpos(-150, 150)
pendown()

# 何 丿:
right(125)
forward(80)
penup()
forward(-40)
pendown()

# 何 丨:
pencolor('red')
left(35)
forward(100)

# 何 一:
pencolor('orange')
penup()
left(90)
forward(20)

pencolor('yellow')
left(90)
forward(100)
pendown()
right(90)
forward(100)
forward(-20)

pencolor('green')
right(90)
forward(100)

pencolor('cyan')
right(135)
forward(15)

pencolor('blue')
penup()
forward(80)
pendown()
right(135)
forward(35)

pencolor('purple')
right(90)
forward(35)

pencolor('gray')
right(90)
forward(35)

pencolor('pink')
right(90)
forward(35)

# 李
penup()
right(90)
forward(200)
left(90)
forward(38)
right(90)
pendown()

# 木
pencolor('pink')
forward(80)
forward(-40)
left(90)
forward(20)
forward(-60)
forward(40)
left(135)
forward(70)
forward(-70)
left(90)
forward(70)
forward(-5)

# 子
penup()
right(135)
forward(65)
pendown()
forward(-40)

left(45)
forward(30)
left(60)
forward(40)

right(130)
forward(20)
penup()
forward(60)
left(28)
forward(-30)
pendown()
forward(-70)

penup()
forward(-20)
# 调用done()使得窗口等待被关闭，否则将立刻关闭窗口:
done()