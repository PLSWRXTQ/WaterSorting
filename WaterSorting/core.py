from . import levels
import pickle
from copy import deepcopy

COLORS = ((0,0,0),(0,0,255),(0,255,0),(0,255,255),(255,0,0),(255,0,255),(255,255,0),(0,0,127),(0,127,0),(0,127,127),(127,0,0),(127,0,127),(127,127,0),(127,127,127),(0,127,255),(0,255,127),(127,255,0),(127,255,127),(127,255,255),(255,0,127),(255,127,0),(255,127,127),(255,127,255),(255,255,127))
LISTEN_MSG = ['从序号 ', '到序号 ', '输出路径 ', '试管序号 ', '液体颜色 ']
SAY_MSG = ['输入错误', '你赢了', '保存失败', '试管', '试管溢出', '颜色相同才能倒入', '试管序号超出范围', '已重置']

class Level:
    def __init__(self, l, limit):
        self.l = l
        self.backup = deepcopy(l)
        self.limit = limit
    def start(self):
        while not self.isover():
            self.disp()
            try:
                self.move(int(self.listen(0)), int(self.listen(1)))
            except ValueError:
                self.say(0)
        else:
            self.disp()
        self.over()
    def isover(self):
        m = []
        for i in self.l:
            if i:
                e = i[0]
                if e in m:
                    return False
                for j in i:
                    if j != e:
                        return False
                m.append(e)
        return True
    def over(self):
        self.say(1)
    def end(self):
        pass
    def listen(self, msg):
        i = input(LISTEN_MSG[msg])
        if i == 'restart':
            self.restart()
        elif i == 'save':
            try:
                self.save(self.listen(2))
            except:
                self.say(2)
        return i
    def say(self, msg):
        if isinstance(msg, int):
            print(SAY_MSG[msg])
        else:
            print(msg)
    def disp(self):
        self.say('\n'.join([f'{SAY_MSG[3]} {i+1} {self.l[i]}' for i in range(len(self.l))]))
    def move(self, a, b, r=False):
        try:
            try:
                if len(self.l[b-1])+1 > self.limit:
                    raise Exception(4)
                if self.l[b-1][-1:] and self.l[a-1][-1:] and self.l[b-1][-1:] != self.l[a-1][-1:]:
                    raise Exception(5)
                if self.l[b-1] or self.l[a-1]:
                    self.l[b-1].append(self.l[a-1].pop())
                self.move(a, b, True)
            except Exception as err:
                if not r:
                    raise err
        except IndexError:
            self.say(6)
        except Exception as err:
            self.say(err.args[0])
    def restart(self):
        self.l = deepcopy(self.backup)
        self.disp()
        self.say(7)
    def save(self, uri):
        with open(uri, 'wb') as f:
            pickle.dump((self.l, self.limit), f)

class Levels(Level):
    def __init__(self, levs):
        self.level = 0
        self.levs = levs
        super().__init__(*self.levs[self.level])
    def over(self):
        super().over()
        self.level += 1
        if self.level < len(self.levs):
            super().__init__(*self.levs[self.level])
            self.start()
        else:
            self.end()

class Generator(Level):
    def __init__(self, number, limit):
        super().__init__([[] for _ in range(number)], limit)
    def start(self):
        while True:
            self.disp()
            self.add()
    def listen(self, msg):
        i = super().listen(msg)
        if i == 'd':
            self.delete(int(self.listen(3)))
        else:
            return i
    def add(self):
        try:
            a, b = int(self.listen(3)), int(self.listen(4))
            if len(self.l[a-1])+1 > self.limit:
                raise Exception(4)
            self.l[a-1].append(b)
        except ValueError:
            pass
        except IndexError:
            self.say(6)
        except Exception as err:
            self.say(err.args[0])
    def delete(self, i):
        try:
            self.l[i-1].pop()
        except IndexError:
            self.say(6)

def playWithConsole(limit=None):
    if limit:
        Level(levels.getRandom(limit), limit).start()
    else:
        Levels(levels.lst).start()