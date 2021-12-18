from tkinter import *
from tkinter import colorchooser
from tkinter import ttk
from tkinter import filedialog
from threading import *
import time
import pickle

##Version 2.5
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
score.geometry('1280x43')
score.resizable(width=False, height=False)  ##lock window resizeing so window crop will work right in OBS

##Declare Variable
homePt = 0
homeColor = {}
homeName = "Home" 
awayPt = 0
awayColor = {}
awayName = "Away"
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
homeColor['hex']="#cecece"
awayColor['hex']="#cecece"
holderTime = 0
hmImage= PhotoImage(file="")
awImage= PhotoImage(file="")
isMini = False
font17 = 17
font23 = 23
font25 = 25
hmImagePath = ''
awImagePath = ''
colorIcon= PhotoImage(file='image/color.png')
pictureIcon = PhotoImage(file='image/picture.png')
folderIcon = PhotoImage(file='image/folder.png')
saveIcon = PhotoImage(file='image/save.png')

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
    global homeName
    homeName = home_name.get()
    canvas.itemconfig(homeNameText, text=homeName)

##takes in a parameter and adds that to homePt varable and updates it with config
def addHomePoint(point):
  global homePt
  homePt = homePt + point
  if homePt<100:
      canvas.itemconfig(homeScoreText, font=('Arial Black', 23))
  elif homePt>99:
      canvas.itemconfig(homeScoreText, font=('Arial Black', 17))
  if homePt < 0:
      homePt=0
  HomePointLabel.configure(text=homePt)
  if point < 6:
    canvas.itemconfig(homeScoreText, text=homePt)
  else:
    TDAnimation('home')

def homeImage():
    global hmImage
    global hmImagePath
    root.filename = filedialog.askopenfilename(initialdir = "/Pictures",title = "Select a File",filetypes = (("png files", "*.png*"),("all files","*.*")))
    hmImagePath=(root.filename)
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
        if homeTO == 3:
            canvas.itemconfig(hmTO1, fill='white')
        elif homeTO == 2:
            canvas.itemconfig(hmTO2, fill='white')
        elif homeTO == 1:
            canvas.itemconfig(hmTO3, fill='white')


def takehomeTO():
    global homeTO
    if homeTO >0:
        homeTO -= 1
        HomeTOLabel.configure(text=homeTO)
        if homeTO == 2:
            canvas.itemconfig(hmTO1, fill='black')
        elif homeTO == 1:
            canvas.itemconfig(hmTO2, fill='black')
        elif homeTO == 0:
            canvas.itemconfig(hmTO3, fill='black')

##Same as home
def awColor():
  global awayColor
  awayColor['rgb'], awayColor['hex'] = colorchooser.askcolor()
  canvas.itemconfig(awayCanvas, outline=awayColor['hex'], fill=awayColor['hex'])
  canvas.itemconfig(awayPossession, outline=awayColor['hex'], fill=awayColor['hex'])

##Same as home
def submitAwayName():
    global awayName
    awayName = away_name.get()
    canvas.itemconfig(awayNameText, text=awayName)

##Same as home
def addAwayPoint(point):
    global awayPt
    awayPt = awayPt + point
    if awayPt<100:
        canvas.itemconfig(awayScoreText, font=('Arial Black', 23))
    elif awayPt>99:
        canvas.itemconfig(awayScoreText, font=('Arial Black', 17))
    if awayPt < 0:
        awayPt=0
    AwayPointLabel.configure(text=awayPt)
    if point < 6:
        canvas.itemconfig(awayScoreText, text=awayPt)
    else:
        TDAnimation('away')

def awayImage():
    global awImage
    global awImagePath
    root.filename = filedialog.askopenfilename(initialdir = "/Pictures",title = "Select a File",filetypes = (("png files", "*.png*"),("all files","*.*")))
    awImagePath=(root.filename)
    awImage= PhotoImage(master=canvas, file=root.filename)
    oldHeight = awImage.height()
    scale_h = (int)(oldHeight/40)
    awImage= awImage.subsample(scale_h)
    canvas.itemconfig(awLogo, image=awImage)

def addawayTO():
    global awayTO
    if awayTO<3:
        awayTO += 1
        AwayTOLabel.configure(text=awayTO)
        if awayTO == 3:
            canvas.itemconfig(awTO1, fill='white')
        elif awayTO == 2:
            canvas.itemconfig(awTO2, fill='white')
        elif awayTO == 1:
            canvas.itemconfig(awTO3, fill='white')
        ##global awTOi
        ##global awTOj
        ##awTOi -= 12
        ##awTOj -= 12
        ##canvas.create_oval(712,awTOi,720,awTOj, fill='white')


def takeawayTO():
    global awayTO
    if awayTO >0:
        awayTO -= 1
        AwayTOLabel.configure(text=awayTO)
        if awayTO == 2:
            canvas.itemconfig(awTO1, fill='black')
        elif awayTO == 1:
            canvas.itemconfig(awTO2, fill='black')
        elif awayTO == 0:
            canvas.itemconfig(awTO3, fill='black')

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
    distance_num.delete(0, END)
    distance_num.insert(0, 10)
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

def mini():
    global isMini
    global font17
    global font23
    global font25
    if isMini == False:
        isMini = True
        for i in range (0,100,1):
            time.sleep(.0001)
            canvas.coords(timeBGCanvas, 1060+(.40*i), 0+(.2*i),1220,40)
            canvas.move(timeText,.2, .1)
            if i % 12==0:
                font23 -= 1
                canvas.itemconfig(timeText,font=('Ariel Black',str(font23),'bold'))
            if i % 14==0:
                font25 -= 1
                canvas.itemconfig(downText,font=('Ariel',str(font23), 'bold'))
            if i % 20==0:
                font17 -= 1
                canvas.itemconfig(periodText,font=('Ariel', str(font17),'bold'))
            canvas.coords(downBGCanvas, 860+i*2,0,1060+(1.62*i),40-(.2*i))
            canvas.coords(periodBGCanvas,780+i*2.81, 0+(.2*i), 860+i*2.5,40)
            canvas.move(downText,1.8,-.1)
            canvas.move(periodText,2.6,.1)
            canvas.coords(blankCanvas,780+i*2.81,0,1220,40)
            canvas.move(awayCanvas,5.2,0)
            canvas.move(awayGrad,5.2,0)
            canvas.move(awayNameText,5.83,0)
            canvas.move(awLogo,2.8,0)
            canvas.move(awTO1,2.8,0)
            canvas.move(awTO2,2.8,0)
            canvas.move(awTO3,2.8,0)
            canvas.move(awayScoreBGCanvas,2.8,0)
            canvas.move(awayScoreText,2.8,0)
            canvas.move(homeCanvas,7.6,0)
            canvas.move(homeGrad,7.6,0)
            canvas.move(homeNameText,8.23,0)
            canvas.move(hmLogo,5.2,0)
            canvas.move(hmTO1,5.2,0)
            canvas.move(hmTO2,5.2,0)
            canvas.move(hmTO3,5.2,0)
            canvas.move(homeScoreBGCanvas,5.2,0)
            canvas.move(homeScoreText,5.2,0)
            canvas.move(GreenLeft,7.6,0)
            canvas.update()
            
def full():
    global isMini
    global font17
    global font23
    global font25
    if isMini:
        isMini = False
        for i in range (0,100,1):
            time.sleep(.0001)
            canvas.coords(timeBGCanvas, 1099.6-(.40*i), 19.8-(.2*i),1220,40)
            canvas.move(timeText,-.2, -.1)
            if i % 12==0:
                font23 += 1
                canvas.itemconfig(timeText,font=('Ariel Black',str(font23),'bold'))
            if i % 14==0:
                font25 += 1
                canvas.itemconfig(downText,font=('Ariel',str(font23), 'bold'))
            if i % 20==0:
                font17 += 1
                canvas.itemconfig(periodText,font=('Ariel', str(font17),'bold'))
            canvas.coords(downBGCanvas, 1058-i*2,0,1220.38-(1.62*i),20.2+(.2*i))
            canvas.coords(periodBGCanvas,1058.19-i*2.81, 19.8-(.2*i), 1107.5-i*2.5,40)
            canvas.coords(blankCanvas,1058.19-i*2.81,0,1220,40)
            canvas.move(downText,-1.8,+.1)
            canvas.move(periodText,-2.6,-.1)
            canvas.move(awayCanvas,-5.2,0)
            canvas.move(awayGrad,-5.2,0)
            canvas.move(awayNameText,-5.83,0)
            canvas.move(awLogo,-2.8,0)
            canvas.move(awTO1,-2.8,0)
            canvas.move(awTO2,-2.8,0)
            canvas.move(awTO3,-2.8,0)
            canvas.move(awayScoreBGCanvas,-2.8,0)
            canvas.move(awayScoreText,-2.8,0)
            canvas.move(homeCanvas,-7.6,0)
            canvas.move(homeGrad,-7.6,0)
            canvas.move(homeNameText,-8.23,0)
            canvas.move(hmLogo,-5.2,0)
            canvas.move(hmTO1,-5.2,0)
            canvas.move(hmTO2,-5.2,0)
            canvas.move(hmTO3,-5.2,0)
            canvas.move(homeScoreBGCanvas,-5.2,0)
            canvas.move(homeScoreText,-5.2,0)
            canvas.move(GreenLeft,-7.6,0)
            canvas.update()

def save():
    global homeColor
    global homeName
    global hmImagePath
    global awayColor
    global awayName
    global awImagePath
    global templateName
    x=[homeColor,homeName,hmImagePath,awayColor,awayName,awImagePath]
    savePath = 'saved_games/' + str(templateName.get()) + '.txt'
    with open (savePath, 'wb') as f:
        pickle.dump(x, f)

def load():
    global homeColor
    global homeName
    global hmImagePath
    global awayColor
    global awayName
    global awImagePath
    global hmImage
    global awImage
    root.filename = filedialog.askopenfilename(initialdir = "saved_games",title = "Select a File",filetypes = (("txt files", "*.txt*"),("all files","*.*")))
    with open (root.filename, 'rb') as f:
        x=pickle.load(f)
    homeColor=x[0]
    homeName=x[1]
    hmImagePath=x[2]
    awayColor=x[3]
    awayName=x[4]
    awImagePath=x[5]
    canvas.itemconfig(homeCanvas, outline=homeColor['hex'], fill=homeColor['hex'])
    canvas.itemconfig(homePossession, outline=homeColor['hex'], fill=homeColor['hex'])
    canvas.itemconfig(homeNameText, text=homeName)
    home_name.delete(0, END)
    home_name.insert(0,homeName)
    hmImage= PhotoImage(master=canvas, file=hmImagePath)
    oldHeight = hmImage.height()
    scale_h = (int)(oldHeight/40)
    hmImage= hmImage.subsample(scale_h)
    canvas.itemconfig(hmLogo, image=hmImage)
    canvas.itemconfig(awayCanvas, outline=awayColor['hex'], fill=awayColor['hex'])
    canvas.itemconfig(awayPossession, outline=awayColor['hex'], fill=awayColor['hex'])
    canvas.itemconfig(awayNameText, text=awayName)
    away_name.delete(0, END)
    away_name.insert(0,awayName)
    awImage= PhotoImage(master=canvas, file=awImagePath)
    oldHeight = awImage.height()
    scale_h = (int)(oldHeight/40)
    awImage= awImage.subsample(scale_h)
    canvas.itemconfig(awLogo, image=awImage)

def TDAnimation(team):
    global homePt
    global awayPt
    if team == 'home':
        canvas.itemconfig(TDUpperL,outline=homeColor['hex'], fill=homeColor['hex'])
        canvas.itemconfig(TDUpperR,outline=homeColor['hex'], fill=homeColor['hex'])
        canvas.itemconfig(TDCanvasL,outline=homeColor['hex'], fill=homeColor['hex'])
        canvas.itemconfig(TDCanvasR,outline=homeColor['hex'], fill=homeColor['hex'])
    else:
        canvas.itemconfig(TDUpperL,outline=awayColor['hex'], fill=awayColor['hex'])
        canvas.itemconfig(TDUpperR,outline=awayColor['hex'], fill=awayColor['hex'])
        canvas.itemconfig(TDCanvasL,outline=awayColor['hex'], fill=awayColor['hex'])
        canvas.itemconfig(TDCanvasR,outline=awayColor['hex'], fill=awayColor['hex'])
    
    for i in range (130): 
        if i < 20:
            canvas.coords(TDUpperL, 640-i*12,0,640,43)
            canvas.coords(TDUpperR, 640,0,640+i*12,43)
            canvas.update()
            time.sleep(.01)
        if i == 20:
            canvas.coords(TDBGL,850,0)
            canvas.coords(TDBGR,430,0)
            canvas.coords(T,640,20)
            canvas.coords(O,640,20)
            canvas.coords(U,640,20)
            canvas.coords(C,640,20)
            canvas.coords(H,640,20)
            canvas.coords(D,640,20)
            canvas.coords(O2,640,20)
            canvas.coords(W,640,20)
            canvas.coords(N,640,20)
        if i == 35:
            canvas.coords(TDCanvasL, 200,0,700,43)
            canvas.coords(TDCanvasR, 580,0,1080,43)
        if i>20 and i<50:
            canvas.move(TDBGL,-7,0)
            canvas.move(TDBGR,7,0)
            canvas.move(TDCanvasL,-10,0)
            canvas.move(TDCanvasR,10,0)
            canvas.move(TDUpperL,-20,0)
            canvas.move(TDUpperR,20,0)
            canvas.move(T,-6,0)
            canvas.move(O,-4.66,0)
            canvas.move(U,-3.33,0)
            canvas.move(C,-2,0)
            canvas.move(H,-.66,0)
            canvas.move(D,1,0)
            canvas.move(O2,2.33,0)
            canvas.move(W,3.83,0)
            canvas.move(N,5.33,0)
            canvas.update()
            time.sleep(.01)
        if i == 50:
            canvas.itemconfig(homeScoreText, text=homePt)
            canvas.itemconfig(awayScoreText, text=awayPt)
        if i>50 and i<100:
            canvas.move(T,-2.5,0)
            canvas.move(O,-2,0)
            canvas.move(U,-1.5,0)
            canvas.move(C,-1,0)
            canvas.move(H,-.5,0)
            canvas.move(D,.5,0)
            canvas.move(O2,1,0)
            canvas.move(W,1.5,0)
            canvas.move(N,2,0)
            canvas.update()
            time.sleep(.01)
        if i>100:
            canvas.move(TDBGL,-21,0)
            canvas.move(TDBGR,21,0)
            canvas.move(TDCanvasL,-21,0)
            canvas.move(TDCanvasR,21,0)
            canvas.move(T,-21,0)
            canvas.move(O,-21,0)
            canvas.move(U,-21,0)
            canvas.move(C,-21,0)
            canvas.move(H,-21,0)
            canvas.move(D,21,0)
            canvas.move(O2,21,0)
            canvas.move(W,21,0)
            canvas.move(N,21,0)
            canvas.update()
            time.sleep(.01)
            

def Close():
    score.destroy()
    root.destroy()

##Copied somewhere from Internet Not sure how it works but it works
def scrollwheel(event):
    setupCanvas.yview_scroll(int(-1*(event.delta/120)), "units")

notebook = ttk.Notebook(root)
notebook.pack(expand=True)

canvas = Canvas(score, height=43, width=1280,bg="#00ff00",highlightthickness=0)
canvasBG = PhotoImage(master=canvas, file='image/CanvasBG.png')
imageTDBGL= PhotoImage(master=canvas, file='image/TDBGL.png')
imageTDBGR= PhotoImage(master=canvas, file='image/TDBGR.png')
iT= PhotoImage(master=canvas, file='image/T.png')
iO= PhotoImage(master=canvas, file='image/O.png')
iU= PhotoImage(master=canvas, file='image/U.png')
iC= PhotoImage(master=canvas, file='image/C.png')
iH= PhotoImage(master=canvas, file='image/H.png')
iD= PhotoImage(master=canvas, file='image/D.png')
iW= PhotoImage(master=canvas, file='image/W.png')
iN= PhotoImage(master=canvas, file='image/N.png')
##Logo = PhotoImage(master=canvas, file='image/save.png')
homeCanvas = canvas.create_rectangle(60, 0, 420, 40, outline="#cecece", fill="#cecece")
homeGrad = canvas.create_image(60,0,image=canvasBG,anchor='nw')
homeNameText = canvas.create_text(65, 20, text=homeName, font=('Arial Black', 25),fill='white',anchor="w")
hmLogo=canvas.create_image(330,20,image="")
homeScoreBGCanvas = canvas.create_rectangle(368, 0, 420, 40, outline="#141414", fill="#141414")
homeScoreText = canvas.create_text(394,20, text=homePt, font=('Arial Black', 23), fill="white")
awayCanvas = canvas.create_rectangle(420, 0, 780, 40, outline="#cecece", fill="#cecece")
awayGrad = canvas.create_image(420,0,image=canvasBG,anchor='nw')
awayNameText = canvas.create_text(425, 20, text=awayName, font=('Arial Black', 25),fill='white',anchor="w")
awLogo=canvas.create_image(690,20,image="")
awayScoreBGCanvas = canvas.create_rectangle(728, 0, 780, 40, outline="#141414", fill="#141414")
awayScoreText = canvas.create_text(754,20, text=awayPt, font=('Arial Black', 23), fill="white")
blankCanvas = canvas.create_rectangle(780,0,1220,40, fill="#1d1d1d", outline="#1d1d1d")
downBGCanvas = canvas.create_rectangle(860,0, 1060, 40, outline="#cecece", fill="#cecece")
downText = canvas.create_text(960,20, text=distanceName, font=('Ariel', str(font25),'bold'))
timeBGCanvas = canvas.create_rectangle(1060,0,1220,40, outline="#1d1d1d", fill="#1d1d1d")
timeText = canvas.create_text(1140,20, text = (minute.get() + ':' + second.get()),font=('Arial Black', str(font23)), fill="white")
periodBGCanvas = canvas.create_rectangle(780, 0, 860, 40, outline="#1d1d1d", fill="#1d1d1d")
periodText = canvas.create_text(820,20, text="1st", font=('Ariel', str(font17),'bold'), fill="gold")
hmTO1=canvas.create_oval(352,4,360,12, fill='white')
hmTO2=canvas.create_oval(352,16,360,24, fill='white')
hmTO3=canvas.create_oval(352,28,360,36, fill='white')
awTO1=canvas.create_oval(712,4,720,12, fill='white')
awTO2=canvas.create_oval(712,16,720,24, fill='white')
awTO3=canvas.create_oval(712,28,720,36, fill='white')
possessionLine = canvas.create_rectangle(60,40,1220,43, outline="black", fill="black")
homePossession = canvas.create_polygon(0,0,0,0,0,0, outline=homeColor['hex'], fill=homeColor['hex'])
awayPossession = canvas.create_polygon(0,0,0,0,0,0, outline=awayColor['hex'], fill=awayColor['hex'])
TDCanvasL = canvas.create_rectangle(0,0,0,43,outline="", fill="")
TDCanvasR = canvas.create_rectangle(0,0,0,43,outline="", fill="")
TDBGL = canvas.create_image(850,70,image=imageTDBGL,anchor='ne')
TDBGR = canvas.create_image(430,70,image=imageTDBGR,anchor='nw')
TDUpperL = canvas.create_rectangle(0,0,0,43,outline="", fill="")
TDUpperR= canvas.create_rectangle(0,0,0,43,outline="", fill="")
T = canvas.create_image(0,20, image=iT)
O = canvas.create_image(0,20, image=iO)
U = canvas.create_image(0,20, image=iU)
C = canvas.create_image(0,20, image=iC)
H = canvas.create_image(0,20, image=iH)
D = canvas.create_image(0,20, image=iD)
O2 = canvas.create_image(0,20, image=iO)
W = canvas.create_image(0,20, image=iW)
N = canvas.create_image(0,20, image=iN)
GreenRight = canvas.create_rectangle(1220,0,1280,43,outline="#00ff00", fill="#00ff00")
GreenLeft = canvas.create_rectangle(-1000,0,60,43,outline="#00ff00", fill="#00ff00")
canvas.pack()

##set up frames to be added to notebook
controllNotebook = Frame(root, bg="#404040", width=950, height=320)
controllNotebook.pack(fill='both', expand=True)

setupNotebook = Frame(root,bg="#404040", width=950, height=320)
setupNotebook.pack(fill='both', expand=True)

setupCanvas = Canvas(setupNotebook, bg="#404040")
setupCanvas.pack(side='left',fill='both', expand=True)

scroll = Scrollbar(setupNotebook, orient=VERTICAL, command= setupCanvas.yview)
scroll.pack(side=RIGHT,fill=Y)

setupCanvas.configure(yscrollcommand=scroll.set)
setupCanvas.bind('<Configure>', lambda e: setupCanvas.configure(scrollregion=setupCanvas.bbox("all")))

setupFrame = Frame(setupCanvas, bg="#404040")
setupCanvas.create_window((0,0), window=setupFrame, anchor= NW)

##set up frames
homeFrame= Frame(controllNotebook, bg="#949494", width=300, height=160, borderwidth=0,highlightthickness=0)
homeFrame.place(x=20,y=20)

awayFrame= Frame(controllNotebook, bg="#949494", width=300, height=160, borderwidth=0,highlightthickness=0)
awayFrame.place(x=630,y=20)

downFrame= Frame(controllNotebook, bg="#696969", width=270, height=160, borderwidth=0,highlightthickness=0)
downFrame.place(x=340,y=20)

bottomFrame= Frame(controllNotebook, bg="#696969", width=910, height=100, borderwidth=0,highlightthickness=0)
bottomFrame.place(x=20,y=200)

homeSetupFrame= Frame(setupFrame, bg="#949494", width=890, height=180)
homeSetupFrame.grid(row=0,column=0,padx=20,pady=20)

awaySetupFrame= Frame(setupFrame, bg="#949494", width=890, height=180)
awaySetupFrame.grid(row=1,column=0,padx=20,pady=20)

templateSetupFrame= Frame(setupFrame, bg="#949494", width=890, height=180)
templateSetupFrame.grid(row=2,column=0,padx=20,pady=20)

##Home Setup Frame Items
home_name = Entry(homeSetupFrame, width=12, font=("Arial", 12))
home_name.insert(0,"Home")
home_name.place(x=170, y= 47)

submitHomeName_btn = Button(homeSetupFrame, text="Submit",command=submitHomeName)
submitHomeName_btn.place(x=300,y=46)

hmColorPicker = Button(homeSetupFrame,width=30, height=30,image = colorIcon, command=hmColor)
hmColorPicker.place(x=170,y=86)

hmLogoPicker = Button(homeSetupFrame,width=30, height=30,image = pictureIcon, command = homeImage)
hmLogoPicker.place(x=170,y=133)

Label(homeSetupFrame, bg="#949494", fg='black', text="Home Team Setup",font=('Ariel', 17)).place(x=5,y=2)
Label(homeSetupFrame, bg="#949494", fg='black', text="Enter Home Name:",font=('Ariel', 12)).place(x=30,y=45)
Label(homeSetupFrame, bg="#949494", fg='black', text="Home Team Color:",font=('Ariel', 12)).place(x=30,y=90)
Label(homeSetupFrame, bg="#949494", fg='black', text="Home Team Logo:",font=('Ariel', 12)).place(x=32,y=135)

##Home Frame Items
##Home Point Button
Label(homeFrame, bg="#949494", fg="black", text="HOME",font=('Ariel Black', 23,'bold')).place(x=100,y=-3)
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

##Home Time Out Buttons
homeTOLLabel = Label(homeFrame, bg="#949494", fg="white", text="T.O.L.",font=('Ariel', 12))
homeTOLLabel.place(x=200,y=30)
HomeTOLabel=Label(homeFrame, height=0, width=3, bg="black", fg="#e08d3e", text=homeTO, font=('Ariel', 15))
HomeTOLabel.place(x=200,y=87)
homeTOMinus_btn = Button(homeFrame, text = "-",width='2', command=takehomeTO)
homeTOMinus_btn.place(x=209,y=120)
homeTOAdd_btn = Button(homeFrame, text = "+",width='2', command=addhomeTO)
homeTOAdd_btn.place(x=209,y=57)

##Away Setup Frame Items
away_name = Entry(awaySetupFrame, width=12, font=("Arial", 12))
away_name.insert(0,"Away")
away_name.place(x=170, y= 47)

submitAwayName_btn = Button(awaySetupFrame, text="Submit",command=submitAwayName)
submitAwayName_btn.place(x=300,y=46)

awColorPicker = Button(awaySetupFrame,width=30, height=30,image = colorIcon, command=awColor)
awColorPicker.place(x=170,y=86)

awLogoPicker = Button(awaySetupFrame,width=30, height=30,image = pictureIcon, command = awayImage)
awLogoPicker.place(x=170,y=133)

Label(awaySetupFrame, bg="#949494", fg='black', text="Away Team Setup",font=('Ariel', 17)).place(x=5,y=2)
Label(awaySetupFrame, bg="#949494", fg='black', text="Enter Away Name:",font=('Ariel', 12)).place(x=30,y=45)
Label(awaySetupFrame, bg="#949494", fg='black', text="Away Team Color:",font=('Ariel', 12)).place(x=30,y=90)
Label(awaySetupFrame, bg="#949494", fg='black', text="Away Team Logo:",font=('Ariel', 12)).place(x=32,y=135)

##Away Frame Items
##Away Point Button
Label(awayFrame, bg="#949494", fg="black", text="AWAY",font=('Ariel Black', 23,'bold')).place(x=100,y=-3)
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
AwayPointLabel= Label(awayFrame, height=0, width=11, bg="black", fg="#e08d3e", text=awayPt, font=('Ariel', 15))
AwayPointLabel.place(x=20,y=87)

##Away Time Out Buttons
awayTOLLabel = Label(awayFrame, bg="#949494", fg="white", text="T.O.L.",font=('Ariel', 12))
awayTOLLabel.place(x=200,y=30)
AwayTOLabel=Label(awayFrame, height=0, width=3, bg="black", fg="#e08d3e", text=homeTO, font=('Ariel', 15))
AwayTOLabel.place(x=200,y=87)
awayTOMinus_btn = Button(awayFrame, width='2', text = "-", command=takeawayTO)
awayTOMinus_btn.place(x=209,y=120)
awayTOAdd_btn = Button(awayFrame, width='2', text = "+", command=addawayTO)
awayTOAdd_btn.place(x=209,y=57)

##Bottom Frame Items
##Time Items
minuteEntry = Entry(bottomFrame, width=3, font=("Arial", 18, ""),textvariable=minute)
minuteEntry.place(x=305,y=30)
secondEntry = Entry(bottomFrame, width=3, font=("Arial", 18, ""),textvariable=second)
secondEntry.place(x=355,y=30)
submitTime_btn = Button(bottomFrame, text='Submit', bd='5',command=submitTime)
submitTime_btn.place(x=405,y=30)
start_btn = Button(bottomFrame, text='Start', bd='5',command=start)
start_btn.place(x=305,y=65)
stop_btn = Button(bottomFrame, text='Stop', bd='5',command=stop)
stop_btn.place(x=355,y=65)
timeLabel = Label(bottomFrame, bg="#696969", fg="white", text="Game Clock",font=('Ariel', 15))
timeLabel.place(x=325,y=0)

##Period Items
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

##Possesion Items
PossessionLabel= Label(bottomFrame, bg="#696969", fg="white", text="Possession",font=('Ariel', 15))
PossessionLabel.place(x=580,y=0)
homePossession_btn=Button(bottomFrame, height=2, width=8,text = "Home", command = lambda: possession(1))
homePossession_btn.place(x=520,y=30)
noPossession_btn= Button(bottomFrame, height=2, width=8,text = "None", command = lambda: possession(0))
noPossession_btn.place(x=600,y=30)
awayPossession_btn=Button(bottomFrame, height=2, width=8,text = "Away", command = lambda: possession(2))
awayPossession_btn.place(x=680,y=30)

##Board View Items
mini_btn = Button(bottomFrame, height=2, width=8, text='Mini', bd='5',command=TDAnimation)
mini_btn.place(x=800,y=3)

full_btn = Button(bottomFrame, height=2, width=8, text='Full', bd='5',command=full)
full_btn.place(x=800,y=52)

##Down Frame Items
##Down Items
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

##Template Setup Frame Items
Label(templateSetupFrame, bg="#949494", fg='black', text="Template",font=('Ariel', 17)).place(x=5,y=2)
Label(templateSetupFrame, bg="#949494", fg='black', text="Enter Template Name:",font=('Ariel', 12)).place(x=30,y=45)
Label(templateSetupFrame, bg="#949494", fg='black', text="Load Template:",font=('Ariel', 12)).place(x=77,y=90)
templateName = Entry(templateSetupFrame, width=12, font=("Arial", 12))
templateName.place(x=190,y=47)
save_btn=Button(templateSetupFrame,width=30, height=30,image = saveIcon,command=save)
save_btn.place(x=310,y=42)
load_btn=Button(templateSetupFrame,width=30, height=30,image = folderIcon, command = load)
load_btn.place(x=195,y=87)

##Takes the frames and add them to the notebook
notebook.add(controllNotebook, text="Control")
notebook.add(setupNotebook, text='Setup')

##When the root window close button id click it execute the rootCLose Function
score.protocol("WM_DELETE_WINDOW", Close)
root.protocol("WM_DELETE_WINDOW", Close)

##Binds Mouse Wheel to scrollwheel Command
root.bind("<MouseWheel>", scrollwheel)

root.mainloop()
score.mainloop()
