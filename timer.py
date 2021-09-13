import pygame, time, sys
p = list(map(int, ''.join(sys.argv[1:]).split(':')))
s = p.pop()
if p: s += p.pop()*60
if p: s += p.pop()*3600
time.sleep(s)
pygame.mixer.init(11025)
pygame.mixer.Sound('ringin.wav').play(1)
time.sleep(10)





