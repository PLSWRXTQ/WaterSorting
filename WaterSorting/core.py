from . import levels
import pickle
from copy import deepcopy

COLORS = ((0,0,0),(0,0,255),(0,255,0),(0,255,255),(255,0,0),(255,0,255),(255,255,0),(0,0,127),(0,127,0),(0,127,127),(127,0,0),(127,0,127),(127,127,0),(127,127,127),(0,127,255),(0,255,127),(127,255,0),(127,255,127),(127,255,255),(255,0,127),(255,127,0),(255,127,127),(255,127,255),(255,255,127))

class Level:
    def __init__(self, l, limit):
        self.l = l
        self.backup = deepcopy(l)
        self.limit = limit
    def start(self):
        while not self.isover():
            self.disp()
            self.move(*self.inputf())
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
        self.printf('你赢了')
    def end(self):
        pass
    def listen(self, msg):
        i = input(msg)
        if i == 'restart':
            self.restart()
        elif i == 'save':
            try:
                self.save(input('输出路径 '))
            except:
                self.printf('保存失败')
        try:
            return int(i)
        except ValueError:
            self.printf('输入错误')
    def inputf(self):
        return self.listen('从序号 '), self.listen('到序号 ')
    def printf(self, msg):
        print(msg)
    def disp(self):
        self.printf('\n'.join([f'试管 {i+1} {self.l[i]}' for i in range(len(self.l))]))
    def move(self, a, b, r=False):
        try:
            try:
                if len(self.l[b-1])+1 > self.limit:
                    raise Exception('试管溢出')
                if self.l[b-1][-1:] and self.l[a-1][-1:] and self.l[b-1][-1:] != self.l[a-1][-1:]:
                    raise Exception('颜色相同才能倒入')
                if self.l[b-1] or self.l[a-1]:
                    self.l[b-1].append(self.l[a-1].pop())
                self.move(a, b, True)
            except Exception as err:
                if not r:
                    raise err
        except IndexError:
            self.printf('试管序号超出范围')
        except Exception as err:
            self.printf(err.args[0])
    def restart(self):
        self.l = deepcopy(self.backup)
        self.disp()
        self.printf('已重置')
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
    def save(self, uri):
        with open(uri, 'wb') as f:
            pickle.dump(self.levs, f)

class Generator(Level):
    def __init__(self, width, limit):
        super().__init__([[] for _ in range(width)], limit)
    def start(self):
        while True:
            self.disp()
            self.add()
    def add(self):
        try:
            a, b = self.inputf()
            if len(self.l[a-1])+1 > self.limit:
                raise Exception('试管溢出')
            self.l[a-1].append(b)
        except IndexError:
            self.printf('试管序号超出范围')
        except Exception as err:
            self.printf(err.args[0])
    def inputf(self):
        return self.listen('试管序号 '), self.listen('液体颜色 ')

def playWithConsole(limit=None):
    if limit:
        Level(levels.getRandom(limit), limit).start()
    else:
        Levels(levels.lst).start()