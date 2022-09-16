from pygame import *
from pygame import display, event, mouse, font, draw
from math import *

screen = display.set_mode((800, 600))

running = True
bgColour = (19, 20, 27)
WHITE = (255, 255, 255)
LNAVY = (40, 46, 61)
LERNAVY = (60, 68, 82)

# FONTS
font.init()
titleFont = font.Font("MADE GoodTime Grotesk.otf", 56)
widgetFont = font.Font("MADE GoodTime Grotesk.otf", 22)
midFont = font.Font("MADE GoodTime Grotesk.otf", 18)
smallFont = font.Font("MADE GoodTime Grotesk.otf", 14)
smallerFont = font.Font("MADE GoodTime Grotesk.otf", 10)
textFont = font.SysFont("Times New Roman", 16)


running = True

Imousepositions = []
Fmousepositions = []
finalrects = []

def textBox(rectangle):
    back = screen.copy()
    typing = True
    input = ""
    while typing:
        mx, my = mouse.get_pos()
        for evt in event.get():
            if evt.type == QUIT:
                event.post(evt)   
                return ""
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    typing = False
                    input = ""
                elif evt.key == K_BACKSPACE:
                    input = input[:-1]
                elif evt.key == K_KP_ENTER or evt.key == K_RETURN:
                    typing = False
                    file = open("timeline.txt", "a")
                    file.write("{}#{}\n".format(input, rectangle))
                    file.close()
                elif evt.key < 256:
                    input += evt.unicode
            if not (rectangle.collidepoint(mx, my)):
                typing = False
            textArea = Rect(rectangle)
            draw.rect(screen, LERNAVY, textArea, 0, 20)
            inputPic = smallFont.render(input, True, WHITE)
            screen.blit(inputPic, (textArea.x+(textArea.w-inputPic.get_width())//2, textArea.y+(textArea.h-inputPic.get_height())//2))
            display.flip()
    screen.blit(back,(0,0))
    return input

def drawRect():
    global Imousepositions
    global finalrects
    if click and len(Imousepositions) < 1:
        initialx, initialy = mx, my
        Imousepositions.append((initialx, initialy))
    duringx, duringy = mx, my

    try:
        width = duringx - Imousepositions[0][0]
        height = duringy - Imousepositions[0][1]
        draw.rect(screen, LNAVY, (Imousepositions[0][0], Imousepositions[0][1], width, height), 0, 20)
    except:
        pass

    try:
        if rightClick:
            finalx, finaly = mx, my
            rect = Rect(Imousepositions[0][0], Imousepositions[0][1], finalx-Imousepositions[0][0], finaly-Imousepositions[0][1])
            finalrects.append(rect)
            draw.rect(screen,LNAVY,rect, 0, 20)
            Imousepositions = []
    except:
        pass

def drawfinalRects():
    for rect in finalrects:
        draw.rect(screen, LNAVY, rect, 0, 20)

def removeRects(rect):
    finalrects.remove(rect)
    file = open("timeline.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("timeline.txt", "w")
    for line in lines:
        if str(rect) not in line:
            file.write(line)
    file.close()
            
def displayRects():
    file = open("timeline.txt", "r")
    lines = file.readlines()
    file.close()
    actualLines = []
    for line in lines:
        actualLines.append(line.strip("\n").strip(">").split("#<rect"))
    print(actualLines)
    for line in actualLines:
        draw.rect(screen, LNAVY, eval(line[1]), 0, 20)
        textPic = smallFont.render(line[0], True, WHITE)
        screen.blit(textPic, (eval(line[1])[0], eval(line[1])[1]))

while running:
    click = False
    rightClick = False
    for evt in event.get():
        if evt.type == QUIT:
            running = False
        if evt.type == MOUSEBUTTONDOWN:
            if evt.button == 1:
                click = True
            elif evt.button == 3:
                rightClick = True
                for rect in finalrects:
                    if rect.collidepoint(mx, my):
                        textBox(rect)
        if evt.type == KEYDOWN:
            if evt.key == K_BACKSPACE:
                for rect in finalrects:
                    removeRects(rect)


    screen.fill((bgColour))
    mx, my = mouse.get_pos()
    mb = mouse.get_pressed()
    
    drawRect()
    drawfinalRects()
    displayRects()
    display.flip()

quit()