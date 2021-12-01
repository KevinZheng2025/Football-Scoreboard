from tkinter import *
from tkinter import colorchooser
import time

##Create TK window, set Name
root = Tk()                                 ##create TK window
root.title("Football Scoreboard")           ##set window name
root.attributes('-topmost',True)            ##set the window to always be on top
root.resizable(width=False, height=False)   ##lock window resizeing so window crop will work right in OBS

##Declare Variable
homePt = 0
homeColor = {}
home_name = "Home"
awayPt = 0
awayColor = {}
away_name = "Away"
minute = StringVar()
second = StringVar()
doTicks = False
global down
down = "1st"
downNum = 1
distance = 10
distanceName = down, '&' , str(distance)


# setting the default value as 0
minute.set("00")
second.set("00")

##Function to Stop Ticking
def stop():
    global doTicks
    doTicks = False

##sends time to canvas text
def submitTime():
    root.update()
    canvas.itemconfig(timeText, text=(minute.get() + ':' + second.get()))

##Function that Submit and Start Tick
def start():
    try:
        # the input provided by the user is
        # stored in here :temp
        temp = int(minute.get()) * 60 + int(second.get())
    except:
        print("Please input the right value")

    global doTicks
    doTicks = True


    while (temp > -1) and doTicks:
        ##secLabel.config(text=second.get())
        ##minLabel.config(text=minute.get())
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        if mins > 60:
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)


        # using format () method to store the value up to
        # two decimal places

        minute.set("{0:2d}".format(mins))
        second.set('{:0>2}'.format(secs))
        canvas.itemconfig(timeText, text=(minute.get() + ':' + second.get()))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()


        time.sleep(1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"


        # after every one sec the value of temp will be decremented
        # by one
        temp -= 1

##open up colorpicker and sends output from that to array
##  and uses array to set canvas BG color
def hmColor():
  global homeColor
  homeColor['rgb'], homeColor['hex'] = colorchooser.askcolor()
  print(homeColor)
  canvas.itemconfig(homeCanvas, outline=homeColor['hex'], fill=homeColor['hex'])

##just uses config to update home name using input from entry
def submitHomeName():
    canvas.itemconfig(homeNameText, text=home_name.get())

##takes in a parameter and adds that to homePt varable and updates it with config
def addHomePoint(point):
  global homePt
  homePt = homePt + point
  canvas.itemconfig(homeScoreText, text=homePt)

##Same as home
def awColor():
  global awayColor
  awayColor['rgb'], awayColor['hex'] = colorchooser.askcolor()
  canvas.itemconfig(awayCanvas, outline=awayColor['hex'], fill=awayColor['hex'])

##Same as home
def submitAwayName():
    canvas.itemconfig(awayNameText, text=away_name.get())

##Same as home
def addAwayPoint(point):
  global awayPt
  awayPt = awayPt + point
  print(awayPt)
  canvas.itemconfig(awayScoreText, text=awayPt)

##takes in a parameter from button and uses that number to decide what to set the Period
##  canvas text and configs it
def period(userPeriod):
    if userPeriod == 1:
        canvas.itemconfig(periodText, text="1st")
    elif userPeriod == 2:
        canvas.itemconfig(periodText, text="2nd")
    elif userPeriod == 3:
        canvas.itemconfig(periodText, text="3rd")
    elif userPeriod == 4:
        canvas.itemconfig(periodText, text="4th")
    elif userPeriod == 5:
        canvas.itemconfig(periodText, text="OT")
    elif userPeriod == 6:
        canvas.itemconfig(periodText, text="2 OT")
    elif userPeriod == 7:
        canvas.itemconfig(periodText, text="Half")

##takes in parameter from button and uses that number to show what Down it is
def down(userDown):
    global downNum
    if userDown == 1:
        canvas.itemconfig(downText, text="1st Down")
        downNum = 1
    elif userDown == 2:
        canvas.itemconfig(downText, text="2nd Down")
        downNum = 2
    elif userDown == 3:
        canvas.itemconfig(downText, text="3rd Down")
        downNum = 3
    elif userDown == 4:
        canvas.itemconfig(downText, text="4th Down")
        downNum = 4

## uses the varaiable downNum from function down and using that will set
##  which down it is and also takes the number from entry and concatnate
##  it so that it shows down and distance
def submitDownDist():
    downtext = ""
    if downNum == 1:
        downtext = "1st"
    elif downNum == 2:
        downtext = "2nd"
    elif downNum == 3:
        downtext = "3rd"
    elif downNum == 4:
        downtext = "4th"
    userDistance = downtext, '&', distance_num.get()
    canvas.itemconfig(downText, text=userDistance)

##if there is a number in the distance_num entry it will take that number and
##  add 1 to it and then delete the number in the entry and insert the new one
def addDownDist():
    userDownDist = int(distance_num.get())
    tempNum = userDownDist + 1
    distance_num.delete(0, END)
    distance_num.insert(0, tempNum)

##if there is a number in the distance_num entry it will take that number and
##  subtract 1 to it and then delete the number in the entry and insert the new one
def subtDownDist():
    userDownDist = int(distance_num.get())
    tempNum = userDownDist - 1
    distance_num.delete(0, END)
    distance_num.insert(0, tempNum)

##just updates the downText canvas so it says 1st & 10
def resetDownDist():
    canvas.itemconfig(downText, text = "1st & 10")

##updates the Canvas text with 1st & 10 and inserts 'GL' into the distance_num entry
def GlDownDist():
    distance_num.delete(0, END)
    distance_num.insert(0, "GL")
    downtext = "1st"
    userDistance = downtext, '&', distance_num.get()
    canvas.itemconfig(downText, text=userDistance)

## update the downText so it says nothing thus 'hiding' it
def HideDownDist():
    canvas.itemconfig(downText, text='')

canvas = Canvas(root, height=50, width=660,bg="#00b140")
canvas2 = Canvas(root, height=1, width=1000)
homeCanvas = canvas.create_rectangle(30, 10, 210, 40, outline="#cecece", fill="#cecece")
homeScoreBGCanvas = canvas.create_rectangle(172, 12, 208, 38, outline="#141414", fill="#141414")
homeScoreText = canvas.create_text(189,25, text=homePt, font=('Ariel', 15), fill="white")
homeNameText = canvas.create_text(35, 25, text=home_name, font=('Arial', 15),anchor="w")
awayCanvas = canvas.create_rectangle(210, 10, 390, 40, outline="#cecece", fill="#cecece")
awayScoreBGCanvas = canvas.create_rectangle(352, 12, 388, 38, outline="#141414", fill="#141414")
awayScoreText = canvas.create_text(369,25, text=awayPt, font=('Ariel', 15), fill="white")
awayNameText = canvas.create_text(215, 25, text=away_name, font=('Arial', 15),anchor="w")
periodBGCanvas = canvas.create_rectangle(390, 10, 430, 40, outline="#1d1d1d", fill="#1d1d1d")
periodText = canvas.create_text(410,26, text="1st", font=('Ariel', 13), fill="gold")
downBGCanvas = canvas.create_rectangle(430,10, 530, 40, outline="#cecece", fill="#cecece")
downText = canvas.create_text(480,25, text=distanceName, font=('Ariel', 15))
timeBGCanvas = canvas.create_rectangle(530,10,630,40, outline="#1d1d1d", fill="#1d1d1d")
timeText = canvas.create_text(580,25, text = (minute.get() + ':' + second.get()),font=('Ariel', 20), fill="white")
canvas.grid(row=0, column=0, columnspan=8)
canvas2.grid(row=7, column=0, columnspan=8)

home_name = Entry(root)
home_name.grid(row=2, column=0, columnspan=2)

away_name = Entry(root)
away_name.grid(row=2, column=3, columnspan=2)

distance_num = Entry(root, width=3, font=("Arial", 18))
distance_num.insert(0,10)
distance_num.grid(row=4, column=5, padx=2, pady=2)

minuteEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=minute)
minuteEntry.grid(row=3, column=6, sticky = "e", padx= 2, pady= 2)

secondEntry = Entry(root, width=3, font=("Arial", 18, ""),textvariable=second)
secondEntry.grid(row=3, column=7, sticky = "w", padx= 2, pady= 2)



submitTime_btn = Button(root, text='Submit', bd='5',command=submitTime)
submitTime_btn.grid(row=5, column=6, columnspan=2)

submitHomeName_btn = Button(root, text="Submit", bd='5',command=submitHomeName)
submitHomeName_btn.grid(row=2, column=2)

submitAwayName_btn = Button(root, text="Submit", bd='5',command=submitAwayName)
submitAwayName_btn.grid(row=2, column=5)

submitDownDist_btn = Button(root, text="Submit", bd='5', command=submitDownDist)
submitDownDist_btn.grid(row=4, column=5,columnspan=2)

start_btn = Button(root, text='Start', bd='5',command=start)
start_btn.grid(row=4, column=6, sticky = "e", padx= 2)

stop_btn = Button(root, text='Stop', bd='5',command=stop)
stop_btn.grid(row=4, column=7, sticky = "w", padx= 2)

hmColorPicker = Button(root, text = "Color",bd='5', command=hmColor)
hmColorPicker.grid(row=2, column=2, sticky="e")

awColorPicker = Button(root, text = "Color",bd='5', command=awColor)
awColorPicker.grid(row=2, column=5, sticky="e")



homeTdButton = Button(root, text = "+6", command=lambda: addHomePoint(6))
homeTdButton.grid(row=3, column=0, sticky="e")

homeMinusTdButton = Button(root, text = "-6", command=lambda: addHomePoint(-6))
homeMinusTdButton.grid(row=3, column=0)

homeFGButton = Button(root, text = "+3", command=lambda: addHomePoint(3))
homeFGButton.grid(row=4, column=0, sticky="e")

homeMinusFGButton = Button(root, text = "-3", command=lambda: addHomePoint(-3))
homeMinusFGButton.grid(row=4, column=0)

home2Button = Button(root, text = "+2", command=lambda: addHomePoint(2))
home2Button.grid(row=5, column=0, sticky="e")

homeMinus2Button = Button(root, text = "-2", command=lambda: addHomePoint(-2))
homeMinus2Button.grid(row=5, column=0)

home1Button = Button(root, text = "+1", command=lambda: addHomePoint(1))
home1Button.grid(row=6, column=0, sticky="e")

homeMinus1Button = Button(root, text = "-1", command=lambda: addHomePoint(-1))
homeMinus1Button.grid(row=6, column=0)

##AwayScoreButton
awayTdButton = Button(root, text = "+6", command=lambda: addAwayPoint(6))
awayTdButton.grid(row=3, column=3, sticky="e")

awayMinusTdButton = Button(root, text = "-6", command=lambda: addAwayPoint(-6))
awayMinusTdButton.grid(row=3, column=3)

awayFGButton = Button(root, text = "+3", command=lambda: addAwayPoint(3))
awayFGButton.grid(row=4, column=3, sticky="e")

awayMinusFGButton = Button(root, text = "-3", command=lambda: addAwayPoint(-3))
awayMinusFGButton.grid(row=4, column=3)

away2Button = Button(root, text = "+2", command=lambda: addAwayPoint(2))
away2Button.grid(row=5, column=3, sticky="e")

awayMinus2Button = Button(root, text = "-2", command=lambda: addAwayPoint(-2))
awayMinus2Button.grid(row=5, column=3)

away1Button = Button(root, text = "+1", command=lambda: addAwayPoint(1))
away1Button.grid(row=6, column=3, sticky="e")

awayMinus1Button = Button(root, text = "-1", command=lambda: addAwayPoint(-1))
awayMinus1Button.grid(row=6, column=3)

##Period button
Period1Button = Button(root, text = "1st", command=lambda: period(1))
Period1Button.grid(row=3, column=1, sticky='e', padx = 3)

Period2Button = Button(root, text = "2nd", command=lambda: period(2))
Period2Button.grid(row=3, column=2, sticky='w', padx = 3)

PeriodHalfButton = Button(root, text = "Half", command=lambda: period(7))
PeriodHalfButton.grid(row=4, column=1, columnspan = 2)

Period3Button = Button(root, text = "3rd", command=lambda: period(3))
Period3Button.grid(row=5, column=1, sticky='e', padx = 3)

Period4Button = Button(root, text = "4th", command=lambda: period(4))
Period4Button.grid(row=5, column=2, sticky='w', padx = 3)

PeriodOtButton = Button(root, text = "OT", command=lambda: period(5))
PeriodOtButton.grid(row=6, column=1, sticky='e', padx = 3)

Period2OtButton = Button(root, text = "2OT", command=lambda: period(6))
Period2OtButton.grid(row=6, column=2, sticky='w', padx = 3)

##Down Button
Down1Button = Button(root, text = "1st Down", command=lambda: down(1))
Down1Button.grid(row=3, column=4, ipadx = 2, sticky='e')
Down2Button = Button(root, text = "2nd Down", command=lambda: down(2))
Down2Button.grid(row=4, column=4, sticky='e')
Down3Button = Button(root, text = "3rd Down", command=lambda: down(3))
Down3Button.grid(row=5, column=4, ipadx = 2, sticky='e')
Down4Button = Button(root, text = "4th Down", command=lambda: down(4))
Down4Button.grid(row=6, column=4, ipadx = 2, sticky='e')

addDist_btn= Button(root, text = "+", command=addDownDist)
addDist_btn.grid(row=3,column=5)

subtDist_btn= Button(root, text = "-", command=subtDownDist)
subtDist_btn.grid(row=5,column=5)

resetDist_btn = Button(root,text = "1st & 10", command = resetDownDist)
resetDist_btn.grid(row=6,column=5)

GlDist_btn = Button(root,text = "1st & GL", command = GlDownDist)
GlDist_btn.grid(row=6,column=5, columnspan = 2)

HideDist_btn = Button(root,text = "Hide", command = HideDownDist)
HideDist_btn.grid(row=5,column=5, columnspan = 2)


root.mainloop()
