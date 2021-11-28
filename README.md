# WaterSorting 水排序
A simple 'WaterSorting' game made by Pygame
简单的水排序 Pygame 小游戏
## How to run 使用方法
Run the ‘example.py’ directly
直接运行 'example.py'

## How to play 玩法
一栏（竖列）色块是一支试管，色块是水
点击一栏色块再点击另一栏色块，试管里的水就会移动
如果点击错误，只要再次点击误点到的试管即可
卡关按 'R' 键重玩
保存随机关卡按 'CTRL' + 'S'

A column of color block is a test tube, and the color block is water.
Click one column of color blocks and then click another column of color blocks, and the water in the test tube will move.
If the click is wrong, just click the delayed test tube again.
Close the card and press the' r' key to play again.
Save the random level by pressing' CTRL'+'S'

## Guides 向导

At first, the WaterSorting package has been in the downloaded source code folder.
首先，WaterSorting Python 包已经在下载的源代码文件夹中

Actually, we created the 'example.py' in the same level folder of WaterSorting package.
其实我们在 WaterSorting Python 包的同级文件夹中创建了 'example.py'

Import the WaterSorting python package if you want to make a custom program.
如果你想自定义程序，那么就导入 WaterSorting Python 包吧！
```python
import WaterSorting
```
About how to write the code to make custom one,  we will talk about it later.
关于如何编写代码，我们将在后面讨论

Let's check the 'example.py' first.
我们先来看看 ’example.py‘
```python
import WaterSorting

WaterSorting.pge.playWithPyGame()
WaterSorting.pge.playWithPyGame(16)
```
The __pge__ means 'Pygame Edition',
so WaterSorting can complete the whole game process with only the __terminal or any other module__.
__pge__ 意思是 'Pygame 版'，所以实际上 WaterSorting 可以只用终端或其它模块完成整个游戏过程

__playWithPygame(16)__ means a random level with difficulty level 16.
playWithPygame(16) 意思是 16 级难度的随机关卡

If you run playWithPygame() with no arguments, the game will start with program own levels.
如果在没有参数的情况下运行playWithPygame()，游戏将以程序自己的关卡开始

Folder Tree:
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
The core program of the game has a class library that supports games and sandboxes.
游戏的核心程序，有支持游戏与沙盒的类库
#### levels.py:
Procedures for managing levels
管理关卡的程序
#### pge.py:
Pygame-supported programs inherit the core.py class.
支持 Pygame 的程序，继承了 core.py 的类
#### \_\_init__.py:
初始化程序
Initialization program
## Classes & Function 类与函数
### class core|pge.Level(Object | core.Level) (l, limit)
__param__ { l: list }
The level data
关卡数据
__param__ { limit: int }
level difficulty/height limit
关卡难度/限高
### class core|pge.Levels(Level | core.Level) (levs)
__param__ { levs: list [...Level.l] }
The list is full of level data
关卡数据列表

### class core|pge.Generator(Level | core.Level, core.Generator) (number, limit)
__param__ { number: int }
The number of test tube
试管数
__param__ { limit: int }
level difficulty/height limit
关卡难度/限高
### function core.playWithConsole(limit)
__param__ { limit: int } (Optional)
level difficulty/height limit
关卡难度/限高
If you run playWithConsole() with no arguments, the game will start with program own levels.
如果在没有参数的情况下运行 playWithConsole()，游戏将以程序自己的关卡开始
### function pge.playWithPygame(limit)
__param__ { limit: int } (Optional)
level difficulty/height limit
关卡难度/限高
If you run playWithPygame() with no arguments, the game will start with program own levels.
如果在没有参数的情况下运行 playWithPygame()，游戏将以程序自己的关卡开始
## Method & Attribute 方法与属性
Simple code, no need