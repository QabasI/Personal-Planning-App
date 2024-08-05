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
