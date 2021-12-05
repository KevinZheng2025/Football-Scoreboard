from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter import filedialog
import time

##Version 2.2
##Creator Kevin Zheng

##Create TK window, set Name
root = Tk()                                 ##create TK window
root.title("Football Scoreboard Control")           ##set window name
root.attributes('-topmost',True)            ##set the window to always be on top
##root.geometry('950x320')
root.configure(background="#404040")

score = Tk()
score.title("Football Scoreboard")
score.configure(background="#00b140")
score.resizable(width=False, height=False)  ##lock window resizeing so window crop will work right in OBS

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
homeTO = 3
awayTO = 3
hmTOi=4
hmTOj=12
awTOi=4
awTOj=12
awayColor['hex']="#cecece"
homeColor['hex']="#cecece"
holderTime = 0
hmImage= PhotoImage(file="")
awImage= PhotoImage(file="")

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
    global holderTime

    while (temp > -1) and doTicks:
        ##secLabel.config(text=second.get())
        ##minLabel.config(text=minute.get())
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins, secs = divmod(temp, 60)

        # using format () method to store the value up to
        # two decimal places

        minute.set("{0:2d}".format(mins))
        second.set('{:0>2}'.format(secs))
        canvas.itemconfig(timeText, text=(minute.get() + ':' + second.get()))

        # updating the GUI window after decrementing the
        # temp value every time
        root.update()


        time.sleep(.1)

        # when temp value = 0; then a messagebox pop's up
        # with a message:"Time's up"

        # after every one sec the value of temp will be decremented
        # by one
        if holderTime == 10:
            temp -= 1
            holderTime = 0
        
        holderTime += 1
        
        

##open up colorpicker and sends output from that to array
##  and uses array to set canvas BG color
def hmColor():
  global homeColor
  homeColor['rgb'], homeColor['hex'] = colorchooser.askcolor()
  canvas.itemconfig(homeCanvas, outline=homeColor['hex'], fill=homeColor['hex'])
  canvas.itemconfig(homePossession, outline=homeColor['hex'], fill=homeColor['hex'])

##just uses config to update home name using input from entry
def submitHomeName():
    canvas.itemconfig(homeNameText, text=home_name.get())

##takes in a parameter and adds that to homePt varable and updates it with config
def addHomePoint(point):
  global homePt
  homePt = homePt + point
  if homePt<100:
      canvas.itemconfig(homeScoreText, font=('Arial Black', 23))
  elif homePt>99:
      canvas.itemconfig(homeScoreText, font=('Arial Black', 17))
  canvas.itemconfig(homeScoreText, text=homePt)
  HomePointLabel.configure(text=homePt)

def homeImage():
    global hmImage
    root.filename = filedialog.askopenfilename(initialdir = "/Pictures",title = "Select a File",filetypes = (("png files", "*.png*"),("all files","*.*")))
    hmImage= PhotoImage(master=canvas, file=root.filename)
    oldHeight = hmImage.height()
    scale_h = (int)(oldHeight/40)
    hmImage= hmImage.subsample(scale_h)
    canvas.itemconfig(hmLogo, image=hmImage)

def addhomeTO():
    global homeTO
    if homeTO<3:
        homeTO += 1
        HomeTOLabel.configure(text=homeTO)
        global hmTOi
        global hmTOj
        hmTOi -= 12
        hmTOj -= 12
        canvas.create_oval(352,hmTOi,360,hmTOj, fill='white')


def takehomeTO():
    global homeTO
    if homeTO >0:
        homeTO -= 1
        HomeTOLabel.configure(text=homeTO)
        global hmTOi
        global hmTOj
        canvas.create_oval(352,hmTOi,360,hmTOj, fill='black')
        hmTOi += 12
        hmTOj += 12


##Same as home
def awColor():
  global awayColor
  awayColor['rgb'], awayColor['hex'] = colorchooser.askcolor()
  canvas.itemconfig(awayCanvas, outline=awayColor['hex'], fill=awayColor['hex'])
  canvas.itemconfig(awayPossession, outline=awayColor['hex'], fill=awayColor['hex'])

##Same as home
def submitAwayName():
    canvas.itemconfig(awayNameText, text=away_name.get())

##Same as home
def addAwayPoint(point):
  global awayPt
  awayPt = awayPt + point
  if awayPt<100:
      canvas.itemconfig(awayScoreText, font=('Arial Black', 23))
  elif awayPt>99:
      canvas.itemconfig(awayScoreText, font=('Arial Black', 17))
  canvas.itemconfig(awayScoreText, text=awayPt)
  AwayScoreLabel.configure(text=awayPt)

def awayImage():
    global awImage
    root.filename = filedialog.askopenfilename(initialdir = "/Pictures",title = "Select a File",filetypes = (("png files", "*.png*"),("all files","*.*")))
    awImage= PhotoImage(master=canvas, file=root.filename)
    oldHeight = awImage.height()
    scale_h = (int)(oldHeight/40)
    awImage= awImage.subsample(scale_h)
    canvas.itemconfig(awLogo, image=awImage)

def addawayTO():
    global awayTO
    if awayTO<3:
        awayTO += 1
        AwayTOLabel.configure(text=homeTO)
        global awTOi
        global awTOj
        awTOi -= 12
        awTOj -= 12
        canvas.create_oval(712,awTOi,720,awTOj, fill='white')


def takeawayTO():
    global awayTO
    if awayTO >0:
        awayTO -= 1
        AwayTOLabel.configure(text=awayTO)
        global awTOi
        global awTOj
        canvas.create_oval(712,awTOi,720,awTOj, fill='black')
        awTOi += 12
        awTOj += 12

##takes in a parameter from button and uses that number to decide what to set the Period
##  canvas text and configs it
def period(userPeriod):
    if userPeriod == 0:
        canvas.itemconfig(periodText, text="")
    elif userPeriod == 1:
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
        canvas.itemconfig(periodText, text="3 OT")
    elif userPeriod == 8:
        canvas.itemconfig(periodText, text="4 OT")
    elif userPeriod == 9:
        canvas.itemconfig(periodText, text="5 OT")
    elif userPeriod == 10:
        canvas.itemconfig(periodText, text="Half")
    elif userPeriod == 11:
        canvas.itemconfig(periodText, text="Final")

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

def Quit():
    root.destroy()
    score.destroy()

def possession(userNum):
    global awayColor
    if userNum==0:
        canvas.itemconfig(possessionLine,outline="black",fill="black")
        canvas.coords(awayPossession,0,0,0,0,0,0)
        canvas.coords(homePossession,0,0,0,0,0,0)
        
    elif userNum==1:
        ##homePossession = canvas.create_polygon(380,43,410,43,395,35, outline=homeColor['hex'], fill=homeColor['hex'])
        canvas.coords(awayPossession,0,0,0,0,0,0)
        canvas.coords(homePossession,380,43,410,43,395,35)
        canvas.itemconfig(possessionLine, outline=homeColor['hex'], fill=homeColor['hex'])
    elif userNum==2:
        ##awayPossession = canvas.create_polygon(740,43,770,43,755,35, outline=awayColor['hex'], fill=awayColor['hex'])
        canvas.coords(homePossession,0,0,0,0,0,0)
        canvas.coords(awayPossession,740,43,770,43,755,35)
        canvas.itemconfig(possessionLine, outline=awayColor['hex'], fill=awayColor['hex'])

notebook = ttk.Notebook(root)
notebook.pack(expand=True)

canvas = Canvas(score, height=43, width=1280,bg="#00ff00",highlightthickness=0)
canvas2 = Canvas(root, height=1, width=1000)
homeCanvas = canvas.create_rectangle(60, 0, 420, 40, outline="#cecece", fill="#cecece")
hmLogo=canvas.create_image(330,20,image="")
homeScoreBGCanvas = canvas.create_rectangle(368, 2, 420, 40, outline="#141414", fill="#141414")
homeScoreText = canvas.create_text(394,20, text=homePt, font=('Arial Black', 23), fill="white")
homeNameText = canvas.create_text(65, 20, text=home_name, font=('Arial Black', 25),anchor="w")
awayCanvas = canvas.create_rectangle(420, 0, 780, 40, outline="#cecece", fill="#cecece")
awLogo=canvas.create_image(690,20,image="")
awayScoreBGCanvas = canvas.create_rectangle(728, 2, 780, 40, outline="#141414", fill="#141414")
awayScoreText = canvas.create_text(754,20, text=awayPt, font=('Arial Black', 23), fill="white")
awayNameText = canvas.create_text(425, 20, text=away_name, font=('Arial Black', 25),anchor="w")
periodBGCanvas = canvas.create_rectangle(780, 0, 860, 40, outline="#1d1d1d", fill="#1d1d1d")
periodText = canvas.create_text(820,20, text="1st", font=('Ariel', 17,'bold'), fill="gold")
downBGCanvas = canvas.create_rectangle(860,0, 1060, 40, outline="#cecece", fill="#cecece")
downText = canvas.create_text(960,20, text=distanceName, font=('Ariel', 25,'bold'))
timeBGCanvas = canvas.create_rectangle(1060,0,1220,40, outline="#1d1d1d", fill="#1d1d1d")
timeText = canvas.create_text(1140,20, text = (minute.get() + ':' + second.get()),font=('Arial Black', 23), fill="white")
canvas.create_oval(352,4,360,12, fill='white')
canvas.create_oval(352,16,360,24, fill='white')
canvas.create_oval(352,28,360,36, fill='white')
canvas.create_oval(712,4,720,12, fill='white')
canvas.create_oval(712,16,720,24, fill='white')
canvas.create_oval(712,28,720,36, fill='white')
possessionLine = canvas.create_rectangle(60,40,1220,43, outline="black", fill="black")
homePossession = canvas.create_polygon(0,0,0,0,0,0, outline=homeColor['hex'], fill=homeColor['hex'])
awayPossession = canvas.create_polygon(0,0,0,0,0,0, outline=awayColor['hex'], fill=awayColor['hex'])
canvas.pack()

controllNotebook = Frame(root, bg="#404040", width=950, height=320)
controllNotebook.pack(fill='both', expand=True)

homeFrame= Frame(controllNotebook, bg="#949494", width=300, height=160, borderwidth=0,highlightthickness=0)
homeFrame.place(x=20,y=20)

awayFrame= Frame(controllNotebook, bg="#949494", width=300, height=160, borderwidth=0,highlightthickness=0)
awayFrame.place(x=630,y=20)

downFrame= Frame(controllNotebook, bg="#696969", width=270, height=160, borderwidth=0,highlightthickness=0)
downFrame.place(x=340,y=20)

bottomFrame= Frame(controllNotebook, bg="#696969", width=910, height=100, borderwidth=0,highlightthickness=0)
bottomFrame.place(x=20,y=200)

home_name = Entry(homeFrame, width=12, font=("Arial", 12))
home_name.insert(0,"Home")
home_name.place(x=5, y= 5)

away_name = Entry(awayFrame, width=12, font=("Arial", 12))
away_name.insert(0,"Away")
away_name.place(x=5, y= 5)

minuteEntry = Entry(bottomFrame, width=3, font=("Arial", 18, ""),textvariable=minute)
minuteEntry.place(x=405,y=30)

secondEntry = Entry(bottomFrame, width=3, font=("Arial", 18, ""),textvariable=second)
secondEntry.place(x=455,y=30)


timeLabel = Label(bottomFrame, bg="#696969", fg="white", text="Game Clock",font=('Ariel', 15))
timeLabel.place(x=395,y=0)

submitTime_btn = Button(bottomFrame, text='Submit', bd='5',command=submitTime)
submitTime_btn.place(x=505,y=30)

submitHomeName_btn = Button(homeFrame, text="Submit", bd='5',command=submitHomeName)
submitHomeName_btn.place(x=130,y=2)

submitAwayName_btn = Button(awayFrame, text="Submit", bd='5',command=submitAwayName)
submitAwayName_btn.place(x=130,y=2)

start_btn = Button(bottomFrame, text='Start', bd='5',command=start)
start_btn.place(x=405,y=65)

stop_btn = Button(bottomFrame, text='Stop', bd='5',command=stop)
stop_btn.place(x=455,y=65)

hmColorPicker = Button(homeFrame, text = "Color", command=hmColor)
hmColorPicker.place(x=200,y=2)

hmLogoPicker = Button(homeFrame, text = "Logo", command = homeImage)
hmLogoPicker.place(x=250,y=2)

awColorPicker = Button(awayFrame, text = "Color", command=awColor)
awColorPicker.place(x=200,y=2)

awLogoPicker = Button(awayFrame, text = "Logo", command = awayImage)
awLogoPicker.place(x=250,y=2)

##Home Point Button
homeScoreLabel = Label(homeFrame, bg="#949494", fg="white", text="Score",font=('Ariel', 12))
homeScoreLabel.place(x=60,y=30)
homeTdButton = Button(homeFrame,width='2', text = "+6", command=lambda: addHomePoint(6))
homeTdButton.place(x=125,y=57)
homeMinusTdButton = Button(homeFrame,width='2', text = "-6", command=lambda: addHomePoint(-6))
homeMinusTdButton.place(x=125,y=120)
homeFGButton = Button(homeFrame,width='2', text = "+3", command=lambda: addHomePoint(3))
homeFGButton.place(x=90,y=57)
homeMinusFGButton = Button(homeFrame,width='2', text = "-3", command=lambda: addHomePoint(-3))
homeMinusFGButton.place(x=90,y=120)
home2Button = Button(homeFrame,width='2', text = "+2", command=lambda: addHomePoint(2))
home2Button.place(x=55,y=57)
homeMinus2Button = Button(homeFrame,width='2', text = "-2", command=lambda: addHomePoint(-2))
homeMinus2Button.place(x=55,y=120)
home1Button = Button(homeFrame,width='2', text = "+1", command=lambda: addHomePoint(1))
home1Button.place(x=20,y=57)
homeMinus1Button = Button(homeFrame,width='2', text = "-1", command=lambda: addHomePoint(-1))
homeMinus1Button.place(x=20,y=120)
HomePointLabel= Label(homeFrame, height=0, width=11, bg="black", fg="#e08d3e", text=homePt, font=('Ariel', 15))
HomePointLabel.place(x=20,y=87)

homeTOLLabel = Label(homeFrame, bg="#949494", fg="white", text="T.O.L.",font=('Ariel', 12))
homeTOLLabel.place(x=200,y=30)
HomeTOLabel=Label(homeFrame, height=0, width=3, bg="black", fg="#e08d3e", text=homeTO, font=('Ariel', 15))
HomeTOLabel.place(x=200,y=87)
homeTOMinus_btn = Button(homeFrame, text = "-",width='2', command=takehomeTO)
homeTOMinus_btn.place(x=209,y=120)
homeTOAdd_btn = Button(homeFrame, text = "+",width='2', command=addhomeTO)
homeTOAdd_btn.place(x=209,y=57)

##Away Point Button
awayScoreLabel = Label(awayFrame, bg="#949494", fg="white", text="Score",font=('Ariel', 12))
awayScoreLabel.place(x=60,y=30)
awayTdButton = Button(awayFrame,width='2', text = "+6", command=lambda: addAwayPoint(6))
awayTdButton.place(x=125,y=57)
awayMinusTdButton = Button(awayFrame,width='2', text = "-6", command=lambda: addAwayPoint(-6))
awayMinusTdButton.place(x=125,y=120)
awayFGButton = Button(awayFrame,width='2', text = "+3", command=lambda: addAwayPoint(3))
awayFGButton.place(x=90,y=57)
awayMinusFGButton = Button(awayFrame,width='2', text = "-3", command=lambda: addAwayPoint(-3))
awayMinusFGButton.place(x=90,y=120)
away2Button = Button(awayFrame,width='2', text = "+2", command=lambda: addAwayPoint(2))
away2Button.place(x=55,y=57)
awayMinus2Button = Button(awayFrame,width='2', text = "-2", command=lambda: addAwayPoint(-2))
awayMinus2Button.place(x=55,y=120)
away1Button = Button(awayFrame,width='2', text = "+1", command=lambda: addAwayPoint(1))
away1Button.place(x=20,y=57)
awayMinus1Button = Button(awayFrame,width='2', text = "-1", command=lambda: addAwayPoint(-1))
awayMinus1Button.place(x=20,y=120)
AwayScoreLabel= Label(awayFrame, height=0, width=11, bg="black", fg="#e08d3e", text=awayPt, font=('Ariel', 15))
AwayScoreLabel.place(x=20,y=87)

awayTOLLabel = Label(awayFrame, bg="#949494", fg="white", text="T.O.L.",font=('Ariel', 12))
awayTOLLabel.place(x=200,y=30)
AwayTOLabel=Label(awayFrame, height=0, width=3, bg="black", fg="#e08d3e", text=homeTO, font=('Ariel', 15))
AwayTOLabel.place(x=200,y=87)
awayTOMinus_btn = Button(awayFrame, width='2', text = "-", command=takeawayTO)
awayTOMinus_btn.place(x=209,y=120)
awayTOAdd_btn = Button(awayFrame, width='2', text = "+", command=addawayTO)
awayTOAdd_btn.place(x=209,y=57)

##Period button
periodLabel= Label(bottomFrame, bg="#696969", fg="white", text="Period",font=('Ariel', 15))
periodLabel.place(x=120,y=0)
Period1Button = Button(bottomFrame,width=3, text = "1st", command=lambda: period(1))
Period1Button.place(x=20,y=30)
Period2Button = Button(bottomFrame,width=3, text = "2nd", command=lambda: period(2))
Period2Button.place(x=60,y=30)
PeriodHalfButton = Button(bottomFrame,width=3, text = "Half", command=lambda: period(10))
PeriodHalfButton.place(x=100,y=30)
Period3Button = Button(bottomFrame, text = "3rd", command=lambda: period(3))
Period3Button.place(x=140,y=30)
Period4Button = Button(bottomFrame,width=3, text = "4th", command=lambda: period(4))
Period4Button.place(x=180,y=30)
PeriodFinalButton = Button(bottomFrame,width=4, text = "Final", command=lambda: period(11))
PeriodFinalButton.place(x=220,y=30)
PeriodOtButton = Button(bottomFrame,width=3, text = "OT", command=lambda: period(5))
PeriodOtButton.place(x=20,y=65)
Period2OtButton = Button(bottomFrame,width=3, text = "2OT", command=lambda: period(6))
Period2OtButton.place(x=60,y=65)
Period3OtButton = Button(bottomFrame,width=3, text = "3OT", command=lambda: period(7))
Period3OtButton.place(x=100,y=65)
Period4OtButton = Button(bottomFrame,width=3, text = "4OT", command=lambda: period(8))
Period4OtButton.place(x=140,y=65)
Period5OtButton = Button(bottomFrame,width=3, text = "5OT", command=lambda: period(9))
Period5OtButton.place(x=180,y=65)
PeriodHideButton = Button(bottomFrame,width=4, text = "Hide", command=lambda: period(0))
PeriodHideButton.place(x=220,y=65)

##Down Button
Down1Button = Button(downFrame, text = "1st Down", width=8, command=lambda: down(1))
Down1Button.place(x=10,y=20)
Down2Button = Button(downFrame, text = "2nd Down", width=8, command=lambda: down(2))
Down2Button.place(x=10,y=55)
Down3Button = Button(downFrame, text = "3rd Down", width=8, command=lambda: down(3))
Down3Button.place(x=10,y=90)
Down4Button = Button(downFrame, text = "4th Down", width=8, command=lambda: down(4))
Down4Button.place(x=10,y=125)

to_goLabel= Label(downFrame, bg="#696969", fg="white", text="To Go",font=('Ariel', 15))
to_goLabel.place(x=100,y=0)

distance_num = Entry(downFrame, width=3, font=("Arial", 18))
distance_num.insert(0,10)
distance_num.place(x=110,y=60)

addDist_btn= Button(downFrame, width=2, text = "+", command=addDownDist)
addDist_btn.place(x=120,y=30)

subtDist_btn= Button(downFrame, width=2, text = "-", command=subtDownDist)
subtDist_btn.place(x=120,y=95)

submitDownDist_btn = Button(downFrame, text="Submit", bd='5', command=submitDownDist)
submitDownDist_btn.place(x=105,y=125)

resetDist_btn = Button(downFrame, height=1, width=8, text = "1st & 10", command = resetDownDist)
resetDist_btn.place(x=195,y=40)

GlDist_btn = Button(downFrame, height=1, width=8,text = "1st & GL", command = GlDownDist)
GlDist_btn.place(x=195,y=80)

HideDist_btn = Button(downFrame, height=1, width=8,text = "Hide", command = HideDownDist)
HideDist_btn.place(x=195,y=120)

Quit_btn = Button(bottomFrame, text = "Quit", command=Quit)
Quit_btn.place(x=870,y=70)


PossessionLabel= Label(bottomFrame, bg="#696969", fg="white", text="Possession",font=('Ariel', 15))
PossessionLabel.place(x=680,y=0)
homePossession_btn=Button(bottomFrame, height=2, width=8,text = "Home", command = lambda: possession(1))
homePossession_btn.place(x=620,y=30)
noPossession_btn= Button(bottomFrame, height=2, width=8,text = "None", command = lambda: possession(0))
noPossession_btn.place(x=700,y=30)
awayPossession_btn=Button(bottomFrame, height=2, width=8,text = "Away", command = lambda: possession(2))
awayPossession_btn.place(x=780,y=30)

notebook.add(controllNotebook, text="Control")

root.mainloop()
score.mainloop()
