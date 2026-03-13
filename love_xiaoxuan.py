import turtle
import time

# ====== 初始化设置 ======
# time.sleep(10)
w = turtle.Screen()
w.title("To 小宣")
w.setup(width=1800, height=1200)
w.bgcolor("#ffebf0")  # 浪漫的浅粉色背景

t = turtle.Turtle()
t.speed(5)  # 设置画笔速度（1-10，0最快）
t.shape("turtle")

# ====== 开始绘制玫瑰花 ======
# 将画笔移动到左侧偏下的初始位置，为右侧文字留出空间
time.sleep(10)
t.penup()
t.goto(-650, 50)
t.pendown()

t.color('red', 'pink')
t.begin_fill()
t.left(90)
t.fd(200)
t.right(90)
t.circle(10, 180)
t.circle(25, 110)
t.left(50)
t.circle(60, 45)
t.circle(20, 170)
t.right(24)
t.fd(30)
t.left(10)
t.circle(30, 110)
t.fd(20)
t.left(40)
t.circle(90, 70)
t.circle(30, 150)
t.right(30)
t.fd(15)
t.circle(80, 90)
t.left(15)
t.fd(45)
t.right(165)
t.fd(20)
t.left(155)
t.circle(150, 80)
t.left(50)
t.circle(150, 90)
t.end_fill()

# 玫瑰花内部花纹
t.left(150)
t.circle(-90, 70)
t.left(20)
t.circle(75, 105)
t.setheading(60)
t.circle(80, 98)
t.circle(-90, 40)
t.left(180)
t.circle(90, 40)
t.circle(-80, 98)
t.setheading(-83)

# 绘制花枝
t.color('darkgreen')
t.pensize(3)
t.fd(30)
t.left(90)
t.fd(25)
t.left(45)

# 绘制左边叶子
t.fillcolor("green")
t.begin_fill()
t.circle(-80, 90)
t.right(90)
t.circle(-80, 90)
t.end_fill()

t.right(135)
t.fd(60)
t.left(180)
t.fd(85)
t.left(90)
t.fd(80)

# 绘制右边叶子
t.right(90)
t.right(45)
t.fillcolor("green")
t.begin_fill()
t.circle(80, 90)
t.left(90)
t.circle(80, 90)
t.end_fill()

t.left(135)
t.fd(60)
t.left(180)
t.fd(60)
t.right(90)
t.circle(200, 60)

# ====== 绘制表白文字 ======
t.penup()
t.color("#d11a2a")  # 深红色文字
# 第一句表白
t.goto(-150, 200)
t.write("Love 小宣", font=("Microsoft YaHei", 36, "bold"))
time.sleep(1)

# 浪漫情话
t.goto(-150, 100)
t.write("The world is so large, and I meet you", font=("Microsoft YaHei", 18, "normal"))
time.sleep(1)

t.goto(-150, 0)
t.write("Wanting to spend the rest of my life with you", font=("Microsoft YaHei", 18, "normal"))
time.sleep(1)
t.goto(-150, -100)
t.write("for three meals and four seasons", font=("Microsoft YaHei", 18, "normal"))
time.sleep(1)

t.goto(-150, -200)
t.write("—— love you forever, Mr Xu", font=("Microsoft YaHei", 16, "italic"))

# 隐藏画笔，并在花旁边画两颗小爱心
def draw_heart(x, y, size):
    t.goto(x, y)
    t.setheading(0)
    t.color("red", "red")
    t.begin_fill()
    t.left(140)
    t.forward(size)
    t.circle(-size/2, 200)
    t.setheading(60)
    t.circle(-size/2, 200)
    t.forward(size)
    t.end_fill()

t.goto(250, 70)
draw_heart(280, 210, 15)
draw_heart(320, 180, 10)

t.hideturtle()
w.mainloop()


# 代码参考：https://blog.csdn.net/qq_44874671/article/details/120577831