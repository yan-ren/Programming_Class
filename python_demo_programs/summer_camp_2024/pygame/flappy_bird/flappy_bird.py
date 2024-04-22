import pgzrun  # 导入游戏库
import random  # 导入随机库
WIDTH = 350   # 设置窗口的宽度
HEIGHT = 600  # 设置窗口的高度

background = Actor('background')  # 导入背景图片
bird = Actor('bird')  # 导入小鸟图片
bird.x = 50           # 设置小鸟的x坐标
bird.y = HEIGHT/2     # 设置小鸟的y坐标
bar_up = Actor('bar_up')    # 导入障碍物上半部分图片
bar_up.x = 300              # 设置障碍物上半部分的x坐标
bar_up.y = 0           # 设置障碍物上半部分的y坐标
bar_down = Actor('bar_down')    # 导入障碍物下半部分图片
bar_down.x = 300                # 设置障碍物下半部分的x坐标
bar_down.y = 600             # 设置障碍物下半部分的y坐标
score = 0     # 游戏得分
speed = 1     # 游戏速度，即障碍物向左移动的速度

def draw():   # 绘制模块，每帧重复执行
    background.draw()  # 绘制背景
    bar_up.draw()         # 绘制障碍物上半部分
    bar_down.draw()         # 绘制障碍物下半部分
    bird.draw()        # 绘制小鸟
    screen.draw.text(str(score), (30, 30),
                     fontsize=50, color='green')

def update():  # 更新模块，每帧重复操作
    global score,speed
    bird.y = bird.y + 2  # 小鸟y坐标增加，即缓慢下落
    bar_up.x = bar_up.x - speed   # 障碍物上半部分缓慢向左移动
    bar_down.x = bar_down.x - speed   # 障碍物上半部分缓慢向左移动
    # 当障碍物移动到最左边时，可以让其在右边重新出现
    if bar_up.x < 0:
        bar_up.x = WIDTH
        bar_down.x = WIDTH
        bar_up.y = random.randint(-200, 200)  # 障碍物上半部分上下随机出现
        bar_down.y = 600 + bar_up.y   # 上、下部分的障碍物中间空挡大小固定
        score = score + 1  # 得分加1
        if (score % 5 == 0): # 如果得分增加了5分，就让游戏速度增加
            speed = speed + 1

    # 如果小鸟碰到障碍物上半部分或下半部分，游戏失败
    if bird.colliderect(bar_up) or bird.colliderect(bar_down) or bird.y < 0 or bird.y > HEIGHT:
        print('游戏失败')
        # 把得分清零、速度设为1，小鸟、障碍物的位置重新归位
        score = 0
        speed = 1
        bird.x = 50            # 设置小鸟的x坐标
        bird.y = HEIGHT/2      # 设置小鸟的y坐标
        bar_up.x = WIDTH       # 设置障碍物上半部分的x坐标
        bar_up.y = 0           # 设置障碍物上半部分的y坐标
        bar_down.x = WIDTH     # 设置障碍物下半部分的x坐标
        bar_down.y = 600       # 设置障碍物下半部分的y坐标

def on_mouse_down():  # 当鼠标点击时运行
    bird.y = bird.y - 100  # 小鸟y坐标减少，即上升一段距离

pgzrun.go()   # 开始执行游戏