# WaterSorting 水排序
A simple 'WaterSorting' game made by Pygame<br />
简单的水排序 Pygame 小游戏<br />
## How to run 使用方法<br />
Run the ‘example.py’ directly<br />
直接运行 'example.py'<br />

## How to play 玩法
一栏（竖列）色块是一支试管，色块是水<br />
点击一栏色块再点击另一栏色块，试管里的水就会移动<br />
如果点击错误，只要再次点击误点到的试管即可<br />
卡关按 'R' 键重玩<br />
保存随机关卡按 'CTRL' + 'S'

A column of color block is a test tube, and the color block is water.<br />
Click one column of color blocks and then click another column of color blocks, and the water in the test tube will move.<br />
If the click is wrong, just click the delayed test tube again.<br />
Press the' r' key to play again.<br />
Save the random level by pressing 'CTRL'+'S'

## Guides 向导

At first, the WaterSorting package has been in the downloaded source code folder.<br />
首先，WaterSorting Python 包已经在下载的源代码文件夹中

Actually, we created the 'example.py' in the same level folder of WaterSorting package.<br />
其实我们在 WaterSorting Python 包的同级文件夹中创建了 'example.py'

Import the WaterSorting python package if you want to make a custom program.<br />
如果你想自定义程序，那么就导入 WaterSorting Python 包吧！
```python
import WaterSorting
```
About how to write the code to make custom one,  we will talk about it later.<br />
关于如何编写代码，我们将在后面讨论

Let's check the 'example.py' first.<br />
我们先来看看 ’example.py‘
```python
import WaterSorting

WaterSorting.pge.playWithPyGame()
WaterSorting.pge.playWithPyGame(16)
```
The __pge__ means 'Pygame Edition',
so WaterSorting can complete the whole game process with only the __terminal or any other module__.<br />
__pge__ 意思是 'Pygame 版'，所以实际上 WaterSorting 可以只用终端或其它模块完成整个游戏过程

__playWithPygame(16)__ means a random level with difficulty level 16.<br />
playWithPygame(16) 意思是 16 级难度的随机关卡

If you run playWithPygame() with no arguments, the game will start with program own levels.<br />
如果在没有参数的情况下运行playWithPygame()，游戏将以程序自己的关卡开始

Folder Tree:<br />
文件夹树：
```
WaterSorting
│  core.py
│  levels.py
│  pge.py
│  __init__.py
└─
```
#### core.py:
The core program of the game has a class library that supports games and sandboxes.<br />
游戏的核心程序，有支持游戏与沙盒的类库
#### levels.py:
For managing levels.<br />
管理关卡的程序
#### pge.py:
Pygame-supported programs inherit the core.py class.<br />
支持 Pygame 的程序，继承了 core.py 的类
#### \_\_init__.py:
Initialization program.<br />
初始化程序
## Classes & Function 类与函数
### class core|pge.Level(Object | core.Level) (l, limit)
__param__ { l: list }<br />
The level data<br />
关卡数据<br />
__param__ { limit: int }<br />
level difficulty/height limit<br />
关卡难度/限高
### class core|pge.Levels(Level | core.Level) (levs)
__param__ { levs: list [...Level.l] }<br />
The list is full of level data<br />
关卡数据列表

### class core|pge.Generator(Level | core.Level, core.Generator) (number, limit)
__param__ { number: int }<br />
The number of test tube<br />
试管数<br />
__param__ { limit: int }<br />
level difficulty/height limit<br />
关卡难度/限高
### function core.playWithConsole(limit)
__param__ { limit: int } (Optional)<br />
level difficulty/height limit<br />
关卡难度/限高<br />
If you run playWithConsole() with no arguments, the game will start with program own levels.<br />
如果在没有参数的情况下运行 playWithConsole()，游戏将以程序自己的关卡开始
### function pge.playWithPygame(limit)
__param__ { limit: int } (Optional)<br />
level difficulty/height limit<br />
关卡难度/限高<br />
If you run playWithPygame() with no arguments, the game will start with program own levels.<br />
如果在没有参数的情况下运行 playWithPygame()，游戏将以程序自己的关卡开始<br />
## Method & Attribute 方法与属性
Simple code, no need