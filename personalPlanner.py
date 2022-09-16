'''
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Authour: Qabas Imbewa
Date of Completion: June 17 2021
File Name: personalPlanner.py
Program Description:
                    This program functions as a "personal planner". It has a purpose of providing a means of organization in the user's life. At startup, 
                    the screen begins at the "calendar" page, but the user can navigate to different pages by clicking on the appropriate line in the left
                    sidebar. 
                    
                    There are 6 distinct pages:

                    1. Calendar: The main attraction is the calendar grid that takes up a large portion of the screen. The month is set to June of 2021. The
                       The user can hover over a box - which corresponds to a date - in the calendar and a light green-coloured text box will appear. The user
                       can then type in the name of an event, and the last 11 characters will be displayed (however, there is no limit to the actual length).
                       When the enter key is pressed, the input is displayed as an event banner in the chosen date box. It also shows up on the right, as an
                       editable banner. The events on the right are arranged by date, with the earliest on top. Clicking on an event deletes it.

                    2. Task List: This page functions as a way to keep track of impending and completed tasks. At the top, immediately beneath the title, there
                       is a place to input a "focus" - or goal. The main content on this page consists of three columns. Each is named "To-do", "Being done" and
                       "done", respectively. Hovering over the space beneath each of the titles reveals an input box in which the user can type in a task. Once
                       the enter key is pressed, the task is displayed under the appropriate header. Clicking on a displayed task deletes it.

                    3. Journal: This page is a very simple text editor. In the light-gray box at the center of the screen, the user can hover and type in 
                       content. It is meant to be used as a note-taking tool. A new line is automatically formed every 115 characters, but the user can press
                       enter to create a new line at any point. As well, there is a bar at the top that allows the user to change the colour of the font and 
                       whether it is bold. The changes are applied to the entire text.

                    4. Budget: This page functions as a budget space for the user to organize their spendings. At the top, immediately below the title, is a
                       place where the user can enter their "monthly cap" - or what their budget is for that month. Below that, the total spendings are displayed,
                       (the sum of all inputted spendings), and the money left over (the budget subtracted by the amount spent). The money that is left is displayed
                       in one of three colours: red if it is negative (i.e. over budget), orange if it is under half of the budget, and green if it is above half.
                       These colours reflect level of hazard. Below that is a list of spending categories. Each category has a bar and text input box associated
                       with it. The user can hover over the text input box (located to the right of the bar) and an option to "edit" will be displayed. If clicked,
                       the user will be able to type in the amount of money that they spent in that category that month. After the enter key is pressed, the amount
                       spent, amount leftover and pie chart will update. The pie chart is located to the right of the screen, in a gray sidebar, under the title 
                       "breakdown". Each colour represents a category, and hovering over a colour will indicate which category it corresponds to.

                    5. Education: This page functions as a tool for a student to keep track of assignments, grades, and their respective weightings. At the top
                       of the page, a rectangle with the words "Add Assignment" is displayed. If clicked, the rectangle will transform into a form with three 
                       input boxes. A place to input the assignment's name, grade, and weighting. The user must input something other than a blank string in order
                       to click submit and proceed. A preview of the grade in the graph will be shown as the user adds/adjusts the grade/weighting. Once the submission
                       button is clicked, the contents of that assignment become unchangeable, but it can still be deleted. Assignments can only be deleted from the graph
                       while the user is not in the process of adding a new assignment (i.e. they pressed submit). The circles in the graph represent assignments, and hovering
                       over a circle will display the assignment's name. The circle's radius corresponds to the weighting (more significant, larger radius), and it's y
                       position on the graph with the grade. The circles are connected by lines that display an overall trend in grades. At the bottom right hand corner,
                       a circle with part of its circumference filled in (with blue) is displayed. The amount that is filled in represents the average grade, which is also
                       displayed in the center of the circle in the form of a percentage grade rounded to two decimal points.

                    6. Timeline: This page functions as a way for the user to plan out their life on a smaller scale. From 12AM one morning to 12AM the next, 
                       the timeline allows for tasks/events/notes/etc. to be placed wherever is wished. Fully flexible, the user can left click to place down
                       a corner of a rectangle, and move their mouse around until they wish to finalize the rectangle, at which point they can right click. 
                       If the user wishes to add text into the rectangle, they can right click and the rectangle will turn a paler blue, to indicate editing mode.
                       Pressing enter leaves editing mode, and the rectangle reverts back to its original colour. To delete a rectangle, simply hover and press
                       backspace on the keyboard.
                
-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
'''

from pygame import *
from pygame import display, mouse, event, font, draw, image
import calendar
from math import *
from itertools import zip_longest

page = "calendarPage"
subW = False

display.set_caption("Personal Planner")

# RELATING TO CALENDAR
positions = []
eventsDone = []
datePos = []

# RELATING TO CALENDAR

for i in range(4):
    for j in range(7):
        datePos.append((str(j)+","+str(i)))
datePos.append("0,4")
datePos.append("1,4")
dates = ["01/06", "02/06","03/06", "04/06","05/06", "06/06","07/06", "08/06","09/06", "10/06","11/06", "12/06","13/06", "14/06","15/06", "16/06","17/06", "18/06","19/06", "20/06","21/06", "22/06","23/06", "24/06","25/06", "26/06", "27/06", "28/06","29/06", "30/06"]

# general
bgColour = (19, 20, 27)
WHITE = (255, 255, 255)
LNAVY = (40, 46, 61)
LERNAVY = (60, 68, 82)
DNAVY = (31, 31, 41)
BLUE = (76, 103, 237)
LBLUE = (122, 144, 250)
GRAYBLUE = (152, 164, 184)
LGRAY = (66, 73, 89)

WIDTH, HEIGHT = 1600, 900
screen = display.set_mode((WIDTH, HEIGHT))

# FONTS
font.init()
titleFont = font.Font("MADE GoodTime Grotesk.otf", 56)
largeFont = font.Font("MADE GoodTime Grotesk.otf", 42)
widgetFont = font.Font("MADE GoodTime Grotesk.otf", 22)
midFont = font.Font("MADE GoodTime Grotesk.otf", 18)
smallFont = font.Font("MADE GoodTime Grotesk.otf", 14)
smallerFont = font.Font("MADE GoodTime Grotesk.otf", 10)
textFont = font.SysFont("Times New Roman", 16)
textFontBold = font.SysFont("Times New Roman Bold", 16)
simpleFont = font.SysFont("Avenir Next", 12)

# ICONS
calendarIcon = image.load("images//calendar.png")
educationIcon = image.load("images//education.png")
taskIcon = image.load("images//tasklist.png")
journalIcon = image.load("images//journal.png")
financesIcon = image.load("images//finances.png")
timelineIcon = image.load("images//timeline.png")

# RELATING TO JOURNAL
textColour = bgColour
add = image.load("images//add.png")
plus = image.load("images//plus.png")
plusPressed = image.load("images//addPressed.png")
gradient = image.load("images//gradient.png")

# JOURNAL TEXT OPTIONS
changeColourIcons = [image.load("images//paintBrushWhite.png"), image.load("images//paintBrushNavy.png")]

text = ""

def textBoxJournal(rect, textColour, boxColour, tFont):
    '''
    This is the large text box where the user can enter a journal entry. It automatically starts a new line every 115 characters 
    but a line break can be added by pressing enter/return on the keyboard.

    '''
    global text
    back = screen.copy()
    typing = True
    while typing:
        mx, my = mouse.get_pos()
        for evt in event.get():
            if evt.type == QUIT:
                event.post(evt)   
                return ""
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    typing = False
                    text = ""
                elif evt.key == K_BACKSPACE:
                    if len(text) > 0:
                        text = text[:-1]
                elif evt.key == K_KP_ENTER or evt.key == K_RETURN : 
                    text += " "*(115-len(lines[len(lines)-1])) # Since a new line starts every 115 characters, add spaces * whatever is remaining to current line
                elif evt.key < 256:
                    text += evt.unicode
            if not (420 <= mx <= 1320 and 230 <= my <=770):
                typing = False
            
            textArea = Rect(rect)
            draw.rect(screen,boxColour,textArea)
    
            lines = [text[i:i+115] for i in range(0, len(text), 115)] # Splits the text up into individual strings that are 115 characters long 
            # The list fills up as characters are added, not just when a multiple of 115 is reached

            for i in range(len(lines)): # displays each line of text
                textPic = tFont.render(lines[i], True, textColour)
                screen.blit(textPic, (textArea.x+13,textArea.y+15+25*(i)))

            display.flip()

    screen.blit(back,(0,0))
    return text

def textBoxEvents(x, y, posx, posy, width, height, file, boxColour, textColour, textInFrame): # pos y acts to differentiate the events and tasks (tasks are 100)
    # These are the text boxes that appear when hovering over a box in the calendar/task column
    if posy != 100:
        displayEvent(430, 230, 114, 25, LNAVY)
    if posy == 100:
        displayTask(360, 360, 340, 40, LNAVY)
    eventText = ""
    back = screen.copy()
    typing = True
    while typing:
        mx, my = mouse.get_pos() # so that the text box disappears when not hovering
        for evt in event.get():
            if evt.type == QUIT:
                event.post(evt)   
                return ""
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    typing = False
                    eventText = ""
                elif evt.key == K_BACKSPACE:
                    if len(eventText) > 0:
                        eventText = eventText[:-1]
                elif evt.key == K_KP_ENTER or evt.key == K_RETURN : 
                    typing = False
                    out = open(file, "r")
                    data = out.read()
                    position = str(posx) + "," + str(posy)
                    incidences = data.count(position)
                    print(incidences)
                    out.close()
                    if incidences < 4 and posy != 100:
                        out = open(file, "a")
                        out.write("{},{},{}\n".format(eventText, posx, posy)) # commas because names can have spaces in them 
                        out.close()
                    if incidences < 4 and posy == 100:
                        out = open(file, "a")
                        out.write("{},{}\n".format(eventText, posx))
                        out.close()
                elif evt.key < 256:
                    eventText += evt.unicode
            if not (400 + posx * 114 <= mx <= 510 + posx * 114 and 220 + posy * 114 <= my <= 320 + posy * 114) and posy != 100: # calendar
                typing = False
            if not (360 + posx*340 <= mx <= 700 + posx*340 and 270 <= my <= HEIGHT) and posy == 100: # task list
                typing = False

            textArea = Rect(x, y, width, height)
            draw.rect(screen,(0,0,0),textArea, 1, 20) 
            draw.rect(screen,boxColour,textArea, 0, 20)

            if len(eventText) == 0 and posy == 100:
                textPic = smallFont.render("Add a task...", True, textColour) # placeholder text when nothing has been typed
            elif len(eventText) == 0 and posy != 100:
                textPic = smallerFont.render("Add an event...", True, textColour)
            elif len(eventText) > textInFrame:
                textPic = smallFont.render(eventText[-textInFrame:], True, textColour) # displays the last x characters 
            else:
                textPic = smallFont.render(eventText, True, textColour) # length is less than the text in frame, so all characters can fit

            screen.blit(textPic, (textArea.x+5, textArea.y+(textArea.height - textPic.get_height())//2))
            display.flip()

    screen.blit(back,(0,0))
    return eventText

def sidebar():
    # This is the sidebar - not the widgets - that appears on the left of the screen at all times
    draw.rect(screen, LNAVY, (0, 0, 330, 900))
    draw.line(screen, LNAVY, (330, 0), (330, 900), 4)

def title():
    # This is just the title
    title = titleFont.render("Personal", True, WHITE)
    screen.blit(title, (50, 20))
    title = titleFont.render("Planner", True, WHITE)
    screen.blit(title, (50, 70))

def sideWidget():
    # These are widgets/buttons that lead to pages 
    global subW
    title()
    calendar = widgetFont.render("Calendar", True, WHITE)
    screen.blit(calendarIcon, (55, 220))
    screen.blit(calendar, (90, 220))
    taskList = widgetFont.render("Task List", True, WHITE)
    screen.blit(taskIcon, (55, 320))
    screen.blit(taskList, (90, 320))
    journal = widgetFont.render("Journal", True, (WHITE))
    screen.blit(journalIcon, (55, 420))
    screen.blit(journal, (90, 420))
    finances = widgetFont.render("Finances", True, WHITE)
    screen.blit(financesIcon, (55, 520))
    screen.blit(finances, (90, 520))
    education = widgetFont.render("Education", True, WHITE)
    screen.blit(educationIcon, (55, 620))
    screen.blit(education, (90, 620))
    timeline = widgetFont.render("Timeline", True, WHITE)
    screen.blit(timelineIcon, (55, 720))
    screen.blit(timeline, (90, 720))

def checkWidget():
    # this checks if the user is hovering and/or clicking on one of the widgets/pages. If they click, the page becomes the one they clicked on
    global page
    sidebar()
    if 50 <= mx <= 300 and 220 <= my <= 250:
        draw.rect(screen, LERNAVY, (40, 210, 250, 50), 0 , 10)
        if click:
            page = "calendarPage"
    if 50 <= mx <= 300 and 320 <= my <= 350:
        draw.rect(screen, LERNAVY, (40, 310, 250, 50), 0, 10)
        if click:
            page = "taskList"
    if 50 <= mx <= 300 and 420 <= my <= 455:
        draw.rect(screen, LERNAVY, (40, 410, 250, 50), 0, 10)
        if click:
            page = "journal"
    if 50 <= mx <= 300 and 520 <= my <= 550:
        draw.rect(screen, LERNAVY, (40, 510, 250, 50), 0, 10)
        if click:
            page = "finances"
    if 50 <= mx <= 300 and 620 <= my <= 650:
        draw.rect(screen, LERNAVY, (40, 610, 250, 50), 0, 10)
        if click:
            page = "education"
    if 50 <= mx <= 300 and 720 <= my <= 750:
        draw.rect(screen, LERNAVY, (40, 710, 250, 50), 0, 10)
        if click:
            page = "timeline"

def grid(x, y, width, height, dist):
    # calendar grid
    draw.rect(screen, bgColour, (x, y, width, height)) # so that deleted events in the calendar do not peek through 
    draw.rect(screen, bgColour, (x, y+height-114, 228, 114))
    for i in range(x, x+width, dist):
        draw.line(screen, LNAVY, (i, y), (i, y+height))
    for j in range(y, y+height+1, dist):
        draw.line(screen, LNAVY, (x, j), (x+width, j))

def calen():
    draw.rect(screen, bgColour, (340, 0, 960, 900))
    # draws the calendar w/ boxes, days, and dates
    grid(400, 220, 800, 457, 114)
    grid(400, 677, 229, 114, 114)

    calendar.setfirstweekday(1) # tuesday is the first day of june 2021
    days = calendar.weekheader(3).split()

    for i in range(len(days)): # week days
        dayPic = midFont.render(days[i], True, LNAVY)
        screen.blit(dayPic, (400+i*114, 200))

    for i in range(1, 31): # dates
        if i in range(1,8):
            dayPic = midFont.render(str(i), True, WHITE)
            screen.blit(dayPic, (404+(i-1)*114, 225))
        elif i in range(8, 15):
            dayPic = midFont.render(str(i), True, WHITE)
            screen.blit(dayPic, (404+(i-8)*114, 339))
        elif i in range(15, 22):
            dayPic = midFont.render(str(i), True, WHITE)
            screen.blit(dayPic, (404+(i-15)*114, 451))
        elif i in range(15, 29):
            dayPic = midFont.render(str(i), True, WHITE)
            screen.blit(dayPic, (404+(i-22)*114, 565))
        else:
            dayPic = midFont.render(str(i), True, WHITE)
            screen.blit(dayPic, (404+(i-29)*114, 679))


    monthPic = titleFont.render("June 2021", True, WHITE) # month/year title
    screen.blit(monthPic, (400, 120))

def calCheckHover():
    # checks if the mouse is over the calendar, in which case it will return True and program will carry on to find the exact position
    if 400 <= mx <= 1200 and 220 <= my <= 677 or 400 <= mx <= 628 and 220 <= my <= 791:
        return True
    return False

def addEvent():
    # finds the box that the mouse is hovering over and displays a text input box that will add an event at that date when the user presses enter/return on keyboard
    posx = (mx-400) // 114
    posy = (my-220) // 114
    textBoxEvents(410 + posx*114, 300 + posy*114, posx, posy, 100, 20, "text files//text.txt", (220,255,220), (0, 0, 0), 11)

def displayEvent(addX, addY, factor, Yfactor, colour): # i am not going to reuse this but it makes the code easier to understand
    # displays added events on the specified day of the month

    events = open("text files//text.txt").read().strip().split("\n")
    actualEvents = []

    for event in events:
        actualEvents.append(event.split(",")) # turns the lines in text file into a list

    positions = []
    eventsDone = []

    if len(actualEvents) > 1: # the first line would be empty but there is a placeholder in the text file that draws off screen
        for event in actualEvents:
            positions.append((event[1], event[2]))

    if len(actualEvents) > 1:
        for event in actualEvents:
            if (event[1], event[2]) not in eventsDone:
                indices = [] # so it doesn't just find the first instance (like when .index() is used)
                indices = [x for (x,y) in enumerate(positions) if y==(event[1], event[2])]
                eventsDone.append((event[1], event[2])) # to avoid duplication (if same posx, posy)
                for i in range(len(indices)):
                    eventBox = Rect(int(actualEvents[indices[i]][1])*factor + addX, int(actualEvents[indices[i]][2])*factor + addY + Yfactor*i, 80, 20) # lists the events on top of each other (max 4)
                    draw.rect(screen,colour,eventBox, 0, 20)
                    if len(actualEvents[indices[i]][0]) > 6: # 6 is the max number of lowercase characters that can fit w/ ... (if i make it based on uppercase it looks weird)
                        eventText = smallFont.render(actualEvents[indices[i]][0][:7]+"...", True, WHITE)
                        screen.blit(eventText, (eventBox.x+(eventBox.w - eventText.get_width())//2, eventBox.y))
                    else: # characters are under limit
                        eventText = smallFont.render(actualEvents[indices[i]][0], True, WHITE)
                        screen.blit(eventText, (eventBox.x+(eventBox.w - eventText.get_width())//2, eventBox.y))

def displayEditEvent(extraY, actualEvents, index, colour):
    # a single event banner (made it a function because I used it twice for hover effects)
    eventRect = Rect(1350, 140+extraY*35, 200, 30)
    draw.rect(screen, colour, eventRect, 0, 20)
    eventPic = smallFont.render(actualEvents[index][0], True, WHITE)
    screen.blit(eventPic, (1350+(eventRect.w - eventPic.get_width())//2, eventRect.y+4))

def displayEditEvents():
    # all of the event banners displayed on the right side of the screen. They are arranged in order of ascending date (earliest on top)
    # and categorized under their assigned dates

    events = open("text files//text.txt").read().strip().split("\n")
    actualEvents = []
    positions = []

    for event in events:
        actualEvents.append(event.split(","))

    if len(actualEvents) > 1: 
        for event in actualEvents:
            positions.append((event[1], event[2]))

    positionsCopy = positions.copy() # datePos contains strings but i still need a version with tuples

    for i in range(len(positions)):
        positions[i] = "".join(positions[i])
        positions[i] = positions[i][:1] + "," + positions[i][1:]

    extraY = 0 # new lines

    for date in dates: # so that it is displayed in order of date, i begin by referencing the date
        listEvents = []
        indices = []
        if datePos[dates.index(date)] in positions: # related lists. the dates correspond with the datepositions, and the date positions are in the modified (string) positions
            datePic = midFont.render(date, True, LERNAVY) #
            screen.blit(datePic, (1350, 140+extraY*35))
            for i in range(len(positions)):
                if positions[i] == datePos[dates.index(date)]:
                    listEvents.append(tuple(positions[i].split(",")))
            indices = [x for (x,y) in enumerate(positionsCopy) if y==listEvents[0]] # everything in listEvents is the same
            for index in indices:
                extraY += 1
                displayEditEvent(extraY, actualEvents, index, bgColour)
                if 1350 <= mx <= 1550 and 140+extraY*25 <= my <= 160+extraY*40:
                    displayEditEvent(extraY, actualEvents, index, LERNAVY)
                    if click:
                        removeEvent(actualEvents, index) # click on an event in the right side bar to remove it
            extraY += 1 # so that next line doesn't overlap

def eventEditBar():
    # Side bar
    draw.rect(screen, LNAVY, (1300, 0, WIDTH - 1300, HEIGHT))
    # Title
    titlePic = midFont.render("Edit Events", True, WHITE)
    screen.blit(titlePic, (1350, 100))
    # show events
    displayEditEvents()

def convertString(list1):
    # converts the contents of a tuple into a string with each item in the original tuple separated by commas
    for i in range(len(list1)):
        list1[i] = ",".join(list1[i])

def removeEvent(actualEvents, index):
    # removes an event
    file = open("text files//text.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("text files//text.txt", "w")
    convertString(actualEvents)
    for line in lines:
        if line.strip("\n") != actualEvents[index]:
            file.write(line) # rewrites every line except the one(s) with the chosen event (if same name and day, it will remove all)
    file.close()

def calendarPage(): 
    calen()
    sideWidget()
    if calCheckHover():
        addEvent()
    eventEditBar()
    displayEvent(430, 230, 114, 25, LNAVY)

focusText = ""

def textBoxFocus(x, y, width, height):
    # "today's focus" is a meaningless (i.e. it's not important to anything else in the program) text box that allows the user to type in a goal for the day
    global focusText
    displayTask(360, 360, 340, 40, LNAVY)
    back = screen.copy()
    typing = True
    while typing:
        mx, my = mouse.get_pos()
        for evt in event.get():
            if evt.type == QUIT:
                event.post(evt)   
                return ""
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    typing = False
                    focusText = ""
                elif evt.key == K_BACKSPACE:
                    if len(focusText) > 0:
                        focusText = focusText[:-1]
                elif evt.key < 256:
                    focusText += evt.unicode
            if not (360 <= mx <= 1300 and 210 <= my <= 240):
                typing = False 
            textArea = Rect(x, y, width, height)
            draw.rect(screen, bgColour, textArea)
            textPic = textFont.render(focusText, True, WHITE)
            screen.blit(textPic, textArea)
            display.flip()

    screen.blit(back,(0,0))
    return focusText

def displayFocus(x, y, width, height, focus, font):
    # displays whatever the user typed in as their focus (this was reused for the budget in finances which is why focus is a parameter)
    textArea = Rect(x, y, width, height)
    draw.rect(screen, bgColour, textArea)
    textPic = font.render(focus, True, WHITE)
    screen.blit(textPic, textArea)

def taskSetUp():
    # this is to avoid build up and distortion of text when it gets redrawn. It doesn't go over the left side bar to avoid flickering
    draw.rect(screen, bgColour, (340, 0, WIDTH-340, HEIGHT))
    # title
    title = titleFont.render("Task List", True, WHITE)
    screen.blit(title, (360, 100))

    # today's focus
    focus = smallFont.render("Today's focus:", True, WHITE)
    screen.blit(focus, (360, 210))

    # divider
    draw.line(screen, LNAVY, (360, 250), (1300, 250))

    # TO DO
    todo = widgetFont.render("To Do", True, WHITE)
    screen.blit(todo, (360, 280))
    screen.blit(add, (370+todo.get_width(), 280))
    # BEING DONE
    beingDone = widgetFont.render("Being Done", True, WHITE)
    screen.blit(beingDone, (700, 280))
    screen.blit(add, (710+beingDone.get_width(), 280))
    # DONE
    done = widgetFont.render("Done", True, WHITE)
    screen.blit(done, (1040, 280))
    screen.blit(add, (1050+done.get_width(), 280))

    if 360 <= mx <= 1300 and 210 <= my <= 240:
        textBoxFocus(480, 210, 850, 20)
    displayFocus(480, 210, 850, 20, focusText, textFont)

def checkHoverAddTask():
    # checks if mouse is over any of the "add task" areas. If true, will find the exact position
    if 360 <= mx <= 1100 and 280 <= my <= 300:
        return True
    return False
    
def addTask():
    # this gets called when the mouse is confirmed to be hovering over one of the task addition buttons. it finds column that the mouse falls over (todo, being done or done)
    posx = (mx-360)//340 # corresponds to one of the columns
    posy = 100 # y is always the same, only one row
    textBoxEvents(360 + posx*340, 310, posx, posy, 150, 30, "text files//tasks.txt", LERNAVY, WHITE, 14) # allows user to enter the task

def removeTask(actualTasks, index):
    # removes a task
    file = open("text files//tasks.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("text files//tasks.txt", "w")
    convertString(actualTasks)
    for line in lines:
        if line.strip("\n") != actualTasks[index]:
            file.write(line) 
    file.close()

def displayTask(addX, addY, factor, Yfactor, colour):
    tasks = open("text files//tasks.txt").read().strip().split("\n")
    actualTasks = []
    
    for task in tasks:
        actualTasks.append(task.split(",")) 

    positions = []
    tasksDone = []

    if len(actualTasks) > 1: 
        for task in actualTasks:
            positions.append((task[1])) # x positions (column)

    if len(actualTasks) > 1:
        for task in actualTasks:
            if task[1] not in tasksDone:
                indices = []
                indices = [x for (x,y) in enumerate(positions) if y==task[1]]
                tasksDone.append(task[1]) # to avoid repetition
                for i in range(len(indices)):
                    taskBox = Rect(int(actualTasks[indices[i]][1])*factor + addX, addY + Yfactor*i, 150, 30)
                    draw.rect(screen,colour,taskBox, 0, 20)
                    if taskBox.collidepoint(mx, my):
                        draw.rect(screen,(89, 100, 117),taskBox, 0, 20) # turns a different colour as a confirmational change when hovering
                        if click:
                            removeTask(actualTasks, indices[i])
                    if len(actualTasks[indices[i]][0]) > 12: # characters are above limit, display first 13 + ...
                        taskText = smallFont.render(actualTasks[indices[i]][0][:13]+"...", True, WHITE)
                        screen.blit(taskText, (taskBox.x+(taskBox.w - taskText.get_width())//2, taskBox.y+5))
                    else: # characters are under limit
                        taskText = smallFont.render(actualTasks[indices[i]][0], True, WHITE)
                        screen.blit(taskText, (taskBox.x+(taskBox.w - taskText.get_width())//2, taskBox.y+5))
                    
def taskList():
    taskSetUp()
    sideWidget()
    if checkHoverAddTask():
        addTask()
    displayTask(360, 360, 340, 40, LNAVY)

def displayJournalEntry(rect,textColour):
    # so that the journal entry is displayed when mouse is not hovering over text box
    lines = [text[i:i+115] for i in range(0, len(text), 115)]
    textArea = Rect(rect)
    if bold:
        tFont = textFont
    else:
        tFont = textFontBold
    for i in range(len(lines)):
        textPic = tFont.render(lines[i], True, textColour)
        screen.blit(textPic, (textArea.x+13,textArea.y+15+25*(i)))

chooseColour = False
bold = False
def textOptions():
    global chooseColour
    global bold

    mx, my = mouse.get_pos()
    journalRect = draw.rect(screen, LERNAVY, (330+(WIDTH-330-810)//2, 230, 810, 35))
    textOptionsRects = [Rect(journalRect.x+5, 235, 24, 24), Rect(journalRect.x+40, 235, 24, 24)]

    if textOptionsRects[0].collidepoint(mx, my):
        colourIndex = 1 # switches the colour to the dark (when hovering)
        if click:
            chooseColour = True
    else:
        colourIndex = 0

    if textOptionsRects[1].collidepoint(mx, my):
        if click:
            if bold:
                bold = False # every time the B is clicked, bold on/off is toggled
            else:
                bold = True
        
    # Displaying edit options (colour and bold)
    screen.blit(changeColourIcons[colourIndex], (textOptionsRects[0].x, 235))
    boldPic = midFont.render("B", True, WHITE)
    screen.blit(boldPic, (textOptionsRects[1].x, textOptionsRects[1].y))

    if chooseColour:
        choosingColour()

def choosingColour():
    # this is the "mode" in which the user can choose a colour. the colour gradient dissapears when a new colour is chosen
    global textColour
    global chooseColour
    journalRect = Rect(330+(WIDTH-330-810)//2, 230, 810, 35) # not drawing it so that the edit bar is still visible
    gradientRect = Rect(journalRect.x, 145, 79, 79)
    screen.blit(gradient, (gradientRect.x, gradientRect.y))
    if gradientRect.collidepoint(mx, my):
        if click:
            textColour = screen.get_at((mx, my))
            chooseColour = False

def journal():
    # journal page
    screen.fill((bgColour))
    title = titleFont.render("Journal", True, WHITE)
    screen.blit(title, (360, 100))
    checkWidget()
    sideWidget()
    textOptions()
    journalRect = draw.rect(screen, LGRAY, (330+(WIDTH-330-810)//2, 265, 810, 540))
    if journalRect.collidepoint(mx, my):
        if bold:
            tFont = textFont
        else:
            tFont = textFontBold
        textBoxJournal(journalRect, textColour, LGRAY, tFont)
    displayJournalEntry(journalRect, textColour) # so that text is there even when not hovering over journal textbox

def budgetingTitle():
    title = titleFont.render("Budget", True, WHITE)
    screen.blit(title, (360, 100))

def monthlyCap():
    title = midFont.render("Monthly cap:", True, WHITE)
    screen.blit(title, (360, 210))

capText = "$"
sections = ["Bills", "Food", "Entertainment", "Charity", "Transportation", "Shopping"]
colours = [(235, 64, 52), (50, 76, 240), (89, 148, 98), (126, 93, 148), (171, 97, 123), (219, 161, 114)] # colours that have an index which corresponds to a section

centerX, centerY, rad = 1350, 450, 200

def drawPieChart(colour, r, start, stop, centerX, centerY):
    poly = [(centerX, centerY)] # start at center of circle
    while start <= stop:
        poly.append((centerX+r*cos(start), centerY+r*sin(start)))
        start += pi/1800 # tenth of a degree in radians
    poly.append((centerX, centerY))
    if len(poly) > 2:
        draw.polygon(screen, colour, poly)

def pieChart():
    # This function gets the budget data from the form.txt file and represents it in a piechart
    file = open("text files//form.txt", "r")
    lines = file.readlines()
    file.close()

    data = []
    names = []
    actualLines = []

    for line in lines:
        actualLines.append(line.strip("\n").split(","))
        
    for line in actualLines:
        names.append(line[1])
        try:
            data.append(float(line[0]))
        except ValueError: # inputted non-number. 0 won't affect any further calculations
            data.append(0)
    
    summ = sum(data)
    angles = []
    for a in data:
        if summ != 0:
            angle = a/summ*(2*pi)
            angles.append(angle)

    nextStart = 0
    for i in range(len(angles)): # using indices because otherwise i would need to use .index() for the colour which acts weird when there is more than one of the same angle
        drawPieChart(colours[sections.index(names[i])], rad, nextStart, angles[i]+nextStart, centerX, centerY)
        nextStart += angles[i]

def checkColour():
    # this function checks the colour at the mouse and uses it to find out which "section" in the budget piechart the mouse is hovering over
    # and displays a box with the section's name
    colour = screen.get_at((mx, my))
    if colour in colours:
        namePic = smallFont.render(sections[colours.index(colour)], True, WHITE)
        mouseRect = (mx, my, 120, 25)
        draw.rect(screen, LNAVY, mouseRect, 0, 15)
        draw.rect(screen, LERNAVY, mouseRect, 1, 15)
        screen.blit(namePic, (mx+(120-namePic.get_width())//2, my+(25-namePic.get_height())//2))

capText = "$"
def textBoxCap(x, y, width, height):
    # this is the textbox in which the user can input their "monthly cap" or budget
    global capText
    displaySpent()
    pieChart()
    back = screen.copy()
    typing = True
    while typing:
        mx, my = mouse.get_pos()
        for evt in event.get():
            if evt.type == QUIT:
                event.post(evt)   
                return ""
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    typing = False
                    capText = ""
                elif evt.key == K_BACKSPACE:
                    capText = capText[:-1]
                elif evt.key < 256:
                    capText += evt.unicode
            if not (360 <= mx <= 1300 and 210 <= my <= 240):
                typing = False
                out = open("text files//budget.txt", "w")
                out.write(capText[1:]) # first character is $, keep that out
                out.close()
            textArea = Rect(x, y, width, height)
            draw.rect(screen, bgColour, textArea)
            textPic = midFont.render(capText, True, WHITE)
            screen.blit(textPic, textArea)
            display.flip()
    screen.blit(back,(0,0))
    return capText

def budgetBreakdown():
    title = midFont.render("Total Spent:", True, WHITE)
    screen.blit(title, (360, 250))

    title = midFont.render("Left Over:", True, WHITE)
    screen.blit(title, (360, 290))

    # sidebar
    draw.rect(screen, LNAVY, (1100, 0, WIDTH - 1100, HEIGHT))
    title = largeFont.render("Breakdown", True, WHITE)
    screen.blit(title, (1150, 50))

    # sections and bar outlines
    for i in range(len(sections)):
        sectionPic = widgetFont.render(sections[i], True, WHITE)
        draw.rect(screen, colours[i], (350, 427+50*i, sectionPic.get_width()+20, sectionPic.get_height()+6), 0, 15)
        screen.blit(sectionPic, (360, 430+50*i))
    for y in range(430, 681, 50):
        draw.rect(screen, LNAVY, (570, y, 400, 40), 1, 20)

    # DIVIDER
    draw.line(screen, LNAVY, (360, 360), (1000, 360))

def enterBudget():
    if 450 <= mx <= 1100 and 210 <= my <= 240:
        textBoxCap(510, 210, 589, 30)

rectangles = [] # spending input rectangles
for i in range(6):
    rectangles.append(Rect(1000, 440+50*i, 100, 40))

def inputSpent():
    # This function checks if the user is hovering over the area where the amount of money that was spent in each category is displayed.
    # If they are, a box with the word "edit" in it will appear. If the user clicks, they can input a new value
    # the value is meant to be a number

    for rectangle in rectangles:
        if rectangle.collidepoint(mx, my):
            mouseRect = (mx, my, 80, 15)
            editPic = smallerFont.render("Edit", True, WHITE)
            draw.rect(screen, LNAVY, mouseRect, 0, 15)
            draw.rect(screen, LERNAVY, mouseRect, 1, 15)
            screen.blit(editPic, (mx+(80-editPic.get_width())//2, my+(15-editPic.get_height())//2))
            if click:
                textBoxBudget(rectangle, sections[(rectangle.y-440)//50])

def textBoxBudget(rectangle, section):
    # This is the textbox in which the user can input a value for the amount of money spent in a category. It is found to the right of the bars.
    displaySpent()
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
                    file = open("text files//form.txt", "r")
                    lines = file.readlines()
                    file.close()
                    file = open("text files//form.txt", "w")
                    for line in lines:
                        if section not in line:
                            file.write(line)
                    file = open("text files//form.txt", "a")
                    file.write("{},{}\n".format(input, section))
                    file.close()
                elif evt.key < 256:
                    input += evt.unicode
            if not (rectangle.collidepoint(mx, my)):
                typing = False
            textArea = Rect(rectangle)
            draw.rect(screen, bgColour, textArea)
            inputPic = smallFont.render(input, True, WHITE)
            screen.blit(inputPic, (textArea.x+2, textArea.y+4))
            display.flip()
    screen.blit(back,(0,0))
    return input

rows = [0,1,2,3,4,5]

def displaySpent():
    # This function displays the amount of money that the user said they spent on each category. 
    # It also displays a bar that is filled to an amount that is proportionate to the fraction of total spending
    spendings = open("text files//form.txt", "r").read().strip().split("\n")
    spent = []
    for spending in spendings:
        spent.append(spending.split(","))

    sum = 0

    for item in spent:
        try:
            sum += int(item[0]) # total spending
        except ValueError: 
            sum += 0

    try: # in case of empty or otherwise invalid input
        budget = float(open("text files//budget.txt").read()) # budget.txt ONLY stores one line and it is whatever the user has as the budget (value gets replaced if changed, not appended)
    except:
        budget = sum # if invalid, leftOver defaults to 0 

    for i in range(len(spent)):
        spentPic = smallFont.render(spent[i][0], True, WHITE)
        Yfactor = rows[sections.index(spent[i][1])]
        screen.blit(spentPic, (1000, 440+50*Yfactor))
        try:
            percentage = float(spent[i][0]) / sum
        except (ZeroDivisionError, ValueError) as error: # either input is a non-number or sum = 0
            percentage = 0 # basically: do not fill up the bar

        # bar
        draw.rect(screen, LERNAVY, (570, 430+50*Yfactor, 400*percentage, 40), 0 , 20) # width changes to reflect fraction of total spending
    
    # TOTAL SPENT
    totalSpentPic = midFont.render("$"+str(sum), True, WHITE)
    screen.blit(totalSpentPic, (510, 250))
    # LEFT OVER
    leftOver = round(budget - sum, 2)
    if leftOver < 0:
        displayLeftOver(leftOver, (235, 125, 113)) # red if they went over budget
    elif 0 < leftOver < budget/2:
        displayLeftOver(leftOver, (237, 178, 83)) # orange if they went over half of their budget
    elif leftOver >= budget/2:
        displayLeftOver(leftOver, (147, 235, 145)) # green if they spent less than half of their budget

def displayLeftOver(leftOver, colour):
    leftOverPic = midFont.render("$"+str(leftOver), True, colour)
    screen.blit(leftOverPic, (510, 290))

def finances():
    draw.rect(screen, bgColour, (340, 0, WIDTH-340, HEIGHT))
    budgetingTitle()
    monthlyCap()
    budgetBreakdown()
    enterBudget()
    displayFocus(510, 210, 589, 30, capText, midFont)
    inputSpent()
    displaySpent()
    pieChart()
    checkColour()

assignmentRects = []
for x in range(385, 1285, 305):
    assignmentRects.append(Rect(x, 215, 280, 70))

assignmentTypes = ["text files//assignmentNames.txt", "text files//assignmentGrades.txt", "text files//assignmentWeightings.txt"]
assignmentBoxCateg = ["Assignment", "Grade", "Weight"]

def assignmentBoxEmpty():
    # when the input box is empty, display text that indicates what is supposed to go in the box (assignment, grade, weight)
    if len(makeAssignmentLists()) > 0:
        for i in range(3):
            if makeAssignmentLists()[-1][i] == "":
                categoryRect = draw.rect(screen, LNAVY, assignmentRects[i], 0, 20)
                categoryText = largeFont.render(assignmentBoxCateg[i], True, GRAYBLUE)
                screen.blit(categoryText, (categoryRect.x+(categoryRect.w - categoryText.get_width())//2, categoryRect.y+(categoryRect.h - categoryText.get_height())//2))

def textBoxAssignment(rectangle, kind):
    # This is the textbox in which the user can input one of the details about their assignment (name, grade, weight)
    # The "kind" parameter is just indicating whether it is the name, grade, or weight. It is meant to be a file.
    displayAssignments()
    sidebar()
    sideWidget()
    assignmentBoxEmpty()

    if len(makeAssignmentLists()) > 0:
        displayAssignment()
    back = screen.copy()
    assignmentText = ""
    typing = True
    while typing:
        mx, my = mouse.get_pos()
        for evt in event.get():
            if evt.type == QUIT:
                event.post(evt)   
                return ""
            if evt.type == KEYDOWN:
                if evt.key == K_ESCAPE:
                    typing = False
                    assignmentText = ""
                elif evt.key == K_BACKSPACE:
                    assignmentText = assignmentText[:-1]
                elif evt.key == K_KP_ENTER or evt.key == K_RETURN:
                    typing = False
                    try: # index errors (if empty)
                        if makeAssignmentLists()[-1][assignmentTypes.index(kind)] != None: # if user tries to add something into a position that is already filled - replace 
                            file = open(kind, "r")
                            lines = file.readlines()
                            lines[len(makeAssignmentLists())-1] = assignmentText+"\n" # the most recent submission will always be the one to replace since you can only edit before you press submit
                            out = open(kind, "w")
                            out.writelines(lines) # edited the appropriate line and now rewriting all the lines again
                            out.close()
                        else: # the position has not been filled, so just add it normally
                            out = open(kind, "a")
                            out.write(assignmentText+"\n")
                            out.close()
                    except IndexError: # initial assignment
                        out = open(kind, "a")
                        out.write(assignmentText+"\n")
                        out.close()
                elif evt.key < 256:
                    assignmentText += evt.unicode
            if not (rectangle.collidepoint(mx, my)):
                typing = False
            textArea = Rect(rectangle)
            draw.rect(screen, bgColour, textArea, 0, 10)
            textPic = midFont.render(assignmentText, True, WHITE)
            screen.blit(textPic, (textArea.x+(textArea.w - textPic.get_width())//2, textArea.y+(textArea.h - textPic.get_height())//2))
            display.flip()
    screen.blit(back,(0,0))
    return assignmentText

def displayAssignment():
    # this displays whatever the user typed in the boxes, while they are still on the "adding" screen (before they press submit) whatever is here can still be edited at this point
    for i in range(3):
        textPic = widgetFont.render(makeAssignmentLists()[-1][i], True, WHITE)
        textArea = assignmentRects[i]
        screen.blit(textPic, (textArea.x+(textArea.w - textPic.get_width())//2, textArea.y+(textArea.h - textPic.get_height())//2))

def addAssignment():
    # this is a function that sets up the "adding assignment" mode/page
    # it contains the rectangles surrounding the text boxes, the submission box, and the textbox when the user hovers over a rectangle
    global page

    # RECTANGLES SURROUNDING TEXT BOXES
    addRect = Rect(360, 200, 1100, 100)
    draw.rect(screen, LNAVY, addRect, 0, 7)
    for rect in assignmentRects:
        draw.rect(screen, LERNAVY, rect, 1, 10)
    submitRect = Rect(1315, 230, 100, 40)

    currentItem = makeAssignmentLists()[-1]

    # checks to see if any of the current submission boxes (name, grade, weight) are empty. 
    # If they are, user cannot press submit. This ensures that the circles are spaced appropriately and information is complete
    noneFlag = False
    if None in currentItem or "" in currentItem:
        noneFlag = True
    
    # SUBMISSION
    draw.rect(screen, LERNAVY, submitRect, 0, 10)
    submitPic = midFont.render("Submit", True, WHITE)
    screen.blit(submitPic, (submitRect.x+(submitRect.w - submitPic.get_width())//2, submitRect.y+(submitRect.h - submitPic.get_height())//2))
    if submitRect.collidepoint(mx, my):
        draw.rect(screen, bgColour, submitRect, 1, 10)
        if click and noneFlag == False:
            for kind in assignmentTypes:
                out = open(kind, "a")
                out.write("\n") # add a line break to the last line of every document. this allows me to start a new tuple within the list, so that the assignments are separated
                out.close()
            page = "education"

    # IF HOVER, ADD TEXT
    for assignmentRect in assignmentRects:
        if assignmentRect.collidepoint(mx, my):
            textBoxAssignment(assignmentRect, assignmentTypes[assignmentRects.index(assignmentRect)]) # not limiting additions here because i want to maintain the ability to edit

    # displays the current input in the text box
    if len(makeAssignmentLists()) > 0:
        displayAssignment()
        assignmentBoxEmpty()

def makeAssignmentLists():
    file = open("text files//assignmentNames.txt", "r")
    namesList = file.readlines()
    for i in range(len(namesList)):
        namesList[i] = namesList[i].strip("\n")
    file.close()
    file = open("text files//assignmentGrades.txt", "r")
    gradesList = file.readlines()
    for i in range(len(gradesList)):
        gradesList[i] = gradesList[i].strip("\n")
    file.close()
    file = open("text files//assignmentWeightings.txt", "r")
    weightingsList = file.readlines()
    for i in range(len(weightingsList)):
        weightingsList[i] = weightingsList[i].strip("\n")
    file.close()
    
    # each item in each of the lists is getting grouped with the item in each of the other lists with the same index
    # this keeps assignments together and makes them easy to display
    finalList = list(zip_longest(namesList, gradesList, weightingsList))
    if len(finalList) > 1:
        finalList[0] = finalList[1]
    return finalList # zip_longest so that it doesn't go with the shortest (fill extra spaces w/ None)

grades = [str(i) for i in range(0, 101, 10)]
grades = grades[::-1] # listing them from top to bottom and 100 is to be top

def displayAssignments():
    # This function draws the graph in which the assignments are displayed. The y axis corresponds to the grade on the assignment, and the radius of the circle to the weighting. 
    # If the user hovers over a circle, they can see the name of the assignment.
    # Clicking on a circle deletes that assignment.

    graphRect = Rect(390, 350, 1100, 450)
    draw.rect(screen, DNAVY, graphRect)

    for y in range(graphRect.y, graphRect.y+graphRect.h+1, 46):
        draw.line(screen, LNAVY, (graphRect.x, y), (graphRect.x+graphRect.w, y))
        index = (y-graphRect.y)//46
        gradePic = simpleFont.render(grades[index], True, LERNAVY) 
        screen.blit(gradePic, (graphRect.x-30, y-6))
    
    points = []

    for assignment in makeAssignmentLists():
        try:
            # i don't think i can get rid of the try except because it could be any invalid text, not just ""
            weighting = float(assignment[2]) / 100 
            grade = float(assignment[1])
            if grade > 100:
                grade = 100
            if weighting > 1:
                weighting = 1 # to avoid huge circles
            yCoordinate = 810-(grade/10)*46 # from bottom
            gradeRadius = weighting * 40 # 40 is the max radius
            xCoordinate = 430+(makeAssignmentLists().index(assignment))*100
            circleRect = draw.circle(screen, BLUE, (xCoordinate, yCoordinate), gradeRadius)
            points.append(circleRect.center)
            draw.lines(screen, BLUE, False, points) # connects the centers of all the circles (graph effect)
            if circleRect.collidepoint(mx, my): # displays name of assignment when hovering over circle
                assignmentNamePic = smallFont.render(assignment[0], True, WHITE)
                draw.rect(screen, LNAVY, (mx, my, assignmentNamePic.get_width()+10, 30), 0, 20)
                screen.blit(assignmentNamePic, (mx+5, my+(30-assignmentNamePic.get_height())//2))
                if click and page == "education": # cannot delete until submit is pressed
                    removeAssignments(assignment, len(points)-1)
        except ValueError:
            pass

def removeAssignments(assignment, index):
    # this function finds the line in each of the files (name, grade, weight) and deletes whatever is at the index to be deleted
    makeAssignmentLists().remove(assignment)
    for i in range(len(assignmentTypes)):
        file = open(assignmentTypes[i], "r")
        lines = file.readlines()
        lines.pop(index)
        file.close()
        file = open(assignmentTypes[i], "w")
        file.writelines(lines)
        file.close()

def checkHoverGraph():
    # this draws a line and a circle that follow the mouse 
    graphRect = Rect(390, 350, 1100, 450)
    if graphRect.collidepoint(mx, my):
        draw.line(screen, BLUE, (graphRect.x, my), (graphRect.x+graphRect.w, my))
        draw.circle(screen, BLUE, (mx, my), 5)

def checkHoverAssignment():
    # this function displays the "add assignment" box, along with the hover effects (colour change) and page.mode change when clicked
    global page
    addRect = Rect(360, 200, 1100, 100)
    draw.rect(screen, LNAVY, addRect, 0, 7)
    if addRect.collidepoint(mx, my):
        addPic = midFont.render("Add Assignment", True, LERNAVY)
        screen.blit(plus, (360+(addRect.w - addPic.get_width() - 24)//2, 200+(addRect.h - 24)//2))
        screen.blit(addPic, (855, 200+(addRect.h - 24)//2))
        if click:
            page = "adding assignment" # it's cleaner to just make it another page since it is to stay in the "adding" mode until submission
    else:
        addPic = midFont.render("Add Assignment", True, WHITE)
        screen.blit(plus, (360+(addRect.w - addPic.get_width() - 24)//2, 200+(addRect.h - 24)//2))
        screen.blit(addPic, (855, 200+(addRect.h - 24)//2))
    return False

def educationTitles():
    title = titleFont.render("Education", True, WHITE)
    screen.blit(title, (360, 100))

def education():
    screen.fill((bgColour))
    educationTitles()
    checkHoverAssignment()
    displayAssignments()
    checkHoverGraph()
    findAverage()

def addingAssignment():
    draw.rect(screen, bgColour, (360, 300, WIDTH-360, HEIGHT))
    addAssignment()
    displayAssignments()
    checkHoverGraph()

def findAverage():
    # This function finds the average of all inputted grades by summing up the weighted grades and dividing that by the sum of the weightings
    # it also calls the display function to draw the gpa circle
    weights = []
    weightedGrades = []

    # i decided to keep the try except for the same reason as above
    try:
        for i in range(1, len(makeAssignmentLists())):
            grade = float(makeAssignmentLists()[i][1])
            weight = float(makeAssignmentLists()[i][2])
            weights.append(weight)
            weightedGrades.append(grade*weight)
    except ValueError:
        pass
        
    if sum(weights) != 0:
        average = sum(weightedGrades) / sum(weights)
    else:
        average = 0
    displayGPA(average)

def displayGPA(average):
    # this function draws a partly filled in circle to represent the average grade.
    # fully white - 0% and blue - 100%
    startAngle = 0
    stopAngle = 2*pi * (average/100)
    draw.circle(screen, WHITE, (1450, 700), 120)
    drawPieChart(BLUE, 120, startAngle, stopAngle, 1450, 700)
    centerCircle = draw.circle(screen, DNAVY, (1450, 700), 80)
    averagePic = widgetFont.render(str("{:.2f}".format(average))+"%", True, WHITE)
    screen.blit(averagePic, (centerCircle.x+(centerCircle.w-averagePic.get_width())//2, centerCircle.y+(centerCircle.h - averagePic.get_height())//2))

hours = ["12 AM"]
for i in range(1, 12):
    hours.append(str(i)+" AM")
hours.append("12 PM")
for i in range(1, 12):
    hours.append(str(i)+" PM") 
hours.append("12 AM")

def drawTimeline():
    # this function sets up the timeline page. it draws the graph and the title
    title = titleFont.render("Timeline", True, WHITE)
    screen.blit(title, (360, 60))
    timelineArea = Rect(330+(WIDTH-330-1008)//2, 150, 1008, 720)
    draw.rect(screen, DNAVY, timelineArea)
    for y in range(timelineArea.y, timelineArea.y+timelineArea.h+1, 30):
        draw.line(screen, LNAVY, (timelineArea.x, y), (timelineArea.x+timelineArea.w, y))
        hourPic = simpleFont.render(hours[(y-timelineArea.y)//30], True, LERNAVY)
        screen.blit(hourPic, (timelineArea.x-50, y-6))

def timelineHover():
    # this function draws the line and circle that follow the mouse around
    timelineArea = Rect(330+(WIDTH-330-1008)//2, 150, 1008, 720)
    if timelineArea.collidepoint(mx, my):
        draw.line(screen, BLUE, (timelineArea.x, my), (timelineArea.x+timelineArea.w, my))
        draw.circle(screen, BLUE, (mx, my), 5)
        drawRect()

Imousepositions = []
finalrects = []

def textBoxTimeline(rectangle):
    # this is the text box that appears when a drawn box is right clicked
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
                    file = open("text files//timeline.txt", "a")
                    file.write("{}#{}\n".format(input, rectangle))
                    file.close()
                elif evt.key < 256:
                    input += evt.unicode
            if not (rectangle.collidepoint(mx, my)):
                typing = False
            textArea = Rect(rectangle)
            draw.rect(screen, LBLUE, textArea, 0, 10)
            inputPic = smallFont.render(input, True, WHITE)
            screen.blit(inputPic, (textArea.x+(textArea.w-inputPic.get_width())//2, textArea.y+(textArea.h-inputPic.get_height())//2))
            display.flip()
    screen.blit(back,(0,0))
    return input

def drawRect():
    # This function draws the rectangle as it is being placed. It begins by storing the intitial coordinates,
    # then adjusts the rectangle's size until the user right clicks, after which the rectangle will be placed
    # and the final rectangle will be stored in the "finalrects" list
    
    global Imousepositions # this is global because I do not want it to clear
    global finalrects

    if click and len(Imousepositions) < 1:
        initialx, initialy = mx, my
        Imousepositions.append((initialx, initialy))
    
    duringx, duringy = mx, my

    if len(Imousepositions) > 0: # aka if the rectangle is currently being scaled
        width = duringx - Imousepositions[0][0]
        height = duringy - Imousepositions[0][1]
        draw.rect(screen, BLUE, (Imousepositions[0][0], Imousepositions[0][1], width, height), 0, 10)
    
    if rightClick and len(Imousepositions) > 0: # right clicking indicates the circle is done being scaled
        initialX =  Imousepositions[0][0]
        initialY = Imousepositions[0][1]
        wid, hei = abs(mx-initialX), abs(my-initialY)
        if initialX <= mx:
            x = initialX
        if initialY <= my:
            y = initialY
        if initialX > mx:
            x = mx
        if initialY > my:
            y = my
        rect = Rect(x, y, wid, hei)
        finalrects.append(rect)
        draw.rect(screen, BLUE, rect, 0, 10)
        Imousepositions = []
    
def drawfinalRects():
    for rect in finalrects:
        draw.rect(screen, BLUE, rect, 0, 10)

def removeRects(rect):
    # this function is called when backspace is pressed over a box, and it deletes that box along with its text
    finalrects.remove(rect)
    file = open("text files//timeline.txt", "r")
    lines = file.readlines()
    file.close()
    file = open("text files//timeline.txt", "w")
    for line in lines:
        if str(rect) not in line:
            file.write(line)
    file.close()
            
def displayRects():
    # this function displays the text that was typed into the drawn text box when usser is not currently typing
    file = open("text files//timeline.txt", "r")
    lines = file.readlines()
    file.close()
    actualLines = []
    for line in lines:
        actualLines.append(line.strip("\n").strip(">").split("#<rect"))
    print(actualLines)
    for line in actualLines:
        draw.rect(screen, BLUE, eval(line[1]), 0, 15)
        textPic = smallFont.render(line[0], True, WHITE)
        rect = eval(line[1])
        screen.blit(textPic, (rect[0]+(rect[2]-textPic.get_width())//2, rect[1]+(rect[3]-textPic.get_height())//2))

def timeline():
    screen.fill((bgColour))
    drawTimeline()
    timelineHover()
    drawfinalRects()
    displayRects()

def checkPage():
    if page == "calendarPage":
        calendarPage()
    if page == "taskList":
        taskList()
    if page == "journal":
        journal()
    if page == "finances":
        finances()
    if page == "education":
        education()
    if page == "adding assignment":
        addingAssignment()
    if page == "timeline":
        timeline()

def drawScene():
    checkPage()
    checkWidget()
    sideWidget()
    display.flip()

running = True

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
                        textBoxTimeline(rect)
        if evt.type == KEYDOWN:
            if evt.key == K_BACKSPACE:
                for rect in finalrects:
                    if rect.collidepoint(mx, my):
                        removeRects(rect)
    mx, my = mouse.get_pos()
    print(mx, my)
    drawScene()

quit()


