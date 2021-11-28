from . import core, levels
import pygame, time
from pygame.locals import *
from tkinter import Tk
from tkinter import filedialog
from os import _exit

class Level(core.Level):
    def __init__(self, width=512, height=512, margin=6, fps=60, *level_args, **level_kwargs):
        super().__init__(*level_args, **level_kwargs)
        self.fps = fps
        self.width = width
        self.height = height
        self.margin = margin
        pygame.init()
        pygame.display.set_caption("水排序 Aleph Edition - Alpha")
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.event.pump()
    def start(self):
        self.blockw = (self.width-(len(self.l)+1)*self.margin)//len(self.l)
        self.blockh = (self.height-2*self.margin)//self.limit
        super().start()
    def end(self):
        pygame.quit()
    def listen(self, msg):
        while True:
            for e in pygame.event.get():
                i = self.filter(e)
                if i:
                    return i
    def filter(self, e):
        if e.type == pygame.QUIT:
            self.end()
        elif e.type == pygame.MOUSEBUTTONDOWN:
            ypos = e.pos[0]
            for i in range(len(self.l)):
                if ypos in range(self.margin+(self.blockw+self.margin)*i, self.margin+(self.blockw+self.margin)*i+self.blockw+1):
                    return i+1
        elif e.type == pygame.KEYDOWN:
            if e.key == pygame.K_r:
                self.restart()
            else:
                keys = pygame.key.get_pressed()
                if (keys[pygame.K_LCTRL] or keys[pygame.K_RCTRL]) and keys[pygame.K_s]:
                    Tk().withdraw()
                    fp = filedialog.asksaveasfilename(initialfile=levels.getMD5((self.l, self.limit))+'.pkl', defaultextension='.pkl', filetypes=[('Python Pickle File', '*.pkl')])
                    try:
                        self.save(fp)
                    except:
                        self.say(2)
    def say(self, msg):
        font = pygame.font.SysFont('SimHei', 50)
        text = font.render(core.SAY_MSG[msg], 1, (127,127,127))
        textpos = text.get_rect()
        textpos.center = self.screen.get_rect().center
        self.screen.blit(text, textpos)
        pygame.display.update()
        time.sleep(1)
        self.disp()
    def disp(self):
        self.screen.fill(pygame.Color(255,255,255))
        for i in range(len(self.l)):
            for j in range(len(self.l[i])):
                pygame.draw.rect(self.screen, pygame.Color(*core.COLORS[self.l[i][j]-1]), Rect(self.margin+(self.blockw+self.margin)*i, (self.height-self.margin-self.blockh)-self.blockh*j, self.blockw, self.blockh))
        pygame.display.update()
        pygame.event.pump()

class Levels(Level, core.Levels):
    def __init__(self, levs):
        super().__init__(levs=levs)

class Generator(Level, core.Generator):
    def __init__(self, number, limit):
        super().__init__(number=number, limit=limit)
        self.incc = False
    def listen(self, msg):
        coind = 0
        while True:
            for e in pygame.event.get():
                i = self.filter(e)
                if e.type == pygame.MOUSEBUTTONDOWN:
                    if e.button == 1:
                        if msg == 4:
                            self.incc = False
                            return coind+1
                        elif i:
                            self.incc = True
                            return i
                    elif e.button == 3:
                        if self.incc:
                            coind += 1
                        else:
                            self.delete(i)
                            self.disp()

def playWithPyGame(limit=None):
    try:
        if limit:
            Level(l=levels.getRandom(limit), limit=limit).start()
        else:
            Levels(levs=levels.lst).start()
    except: pass