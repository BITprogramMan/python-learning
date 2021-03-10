import turtle as t

# def main():
# 	t.goto(150, 0)
# 	for i in range(100):
# 		t.left(160)
# 		t.fd(200)
# 		t.left(270)
# 		t.fd(210)
# import turtle
#
# turtle.speed(0)
# turtle.color('red')
# turtle.bgcolor('black')
# turtle.ht()
#
#
# def ss(N):
#     turtle.circle(N)
#     turtle.left(5)
#     if N<1:
#         return
#     N-=5
#     turtle.fd(8)
#     ss(N)
#
#
# def main():
#     for i in range(1, 13):
#         turtle.up()
#         turtle.home()
#         turtle.left(30*i)
#         turtle.fd(150)
#         turtle.down()
#         ss(180)

def main():
	t.pensize(2)  # 画线宽度
	t.bgcolor("black")  # 设置背景颜色
	colors = ["red", "yellow", "blue", "purple"]  # 颜色列表
	t.tracer(True)  # 是否显示轨迹

	for x in range(400):
		t.forward(2 * x)  # 前进
		t.color(colors[x % 4])  # 设置当前画笔颜色
		t.left(92)  # 右转角度

	#t.done()  # 加上这一句可以使画图结束之后不立即关闭窗口

if __name__=='__main__':
	main()