
from tkinter import *
from tkinter import filedialog
from PIL import Image
import PIL.Image


import easygui


root = Tk()
root.title('Agile project')
myLabel = Label(root, text="This is a simple GUI", bg="blue", fg="white", font=("Helvetica", 16))

myLabel.pack(fill=X)

myLabelInput=Label(root, 
         text="Enter number")
myLabelInput.pack(fill=X)
e1 = Entry(root)
e1.pack(fill=X)




topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)


img1 = PhotoImage(file='img/happy.gif')
img2 = PhotoImage(file='/Users/chunsengwong/Downloads/Speech-Emotion-Recognition-master/src/img/calm.gif')
img3 = PhotoImage(file='/Users/chunsengwong/Downloads/Speech-Emotion-Recognition-master/src/img/happy.gif')
img4 = PhotoImage(file='/Users/chunsengwong/Downloads/Speech-Emotion-Recognition-master/src/img/sad.gif')

audioFile = ''
indexOfEmotion = ''
file=''
label=Label(root)
label.pack()
count = 0
anim = None
frames=0

def animation(count):
    global anim
    im2 = im[count]
    #easygui.msgbox(frames, title="simple gui")
    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))
    #i = PIL.Image.open(file)
    #i.show()

def printPrediction():
    #global indexOfEmotion
    global label
    indexOfEmotion=int(e1.get())
    global file
    file=''
    global frames
    frames=0
    global im
    im=''
    global count
    count=0
    if anim != None:
        root.after_cancel(anim)
    if indexOfEmotion == 1:
        #label.configure(image=img1)
        
        
        file='img/sad.gif'
        info = Image.open(file)
        #global frames
        frames = info.n_frames
        #global im
        im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
        
        #easygui.msgbox(file1, title="simple gui")
        
        #easygui.msgbox(frames, title="simple gui")
        #global count
        count=0
        animation(count)
    elif indexOfEmotion == 2:
        
        file='img/fearful.gif'
        info = Image.open(file)
        #global frames
        frames = info.n_frames
        #global im
        im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
        
        #easygui.msgbox(file1, title="simple gui")
        
        #easygui.msgbox(frames, title="simple gui")
        #global count
        count=0
        animation(count)
    elif indexOfEmotion == 3:
        
        file='img/surprised.gif'
        info = Image.open(file)
        #global frames
        frames = info.n_frames
        #global im
        im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
        
        #easygui.msgbox(file1, title="simple gui")
        
        #easygui.msgbox(frames, title="simple gui")
        #global count
        count=0
        animation(count)
    elif indexOfEmotion == 4:
        
        file='img/happy.gif'
        info = Image.open(file)
        
        frames = info.n_frames
        #global im
        im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
        
        #easygui.msgbox(file1, title="simple gui")
        
        #easygui.msgbox(frames, title="simple gui")
        #global count
        count=0
        animation(count)
    


def filebrowser():
    global audioFile
    global indexOfEmotion
    audioFile = filedialog.askopenfilename(initialdir="/", title="Select Your Audio File",
                                           filetypes=(("Audio Files", ".wav "), ("All Files", "*.*")))
    
    if audioFile:
        #indexOfEmotion = Predict.predictGivenFileName(audioFile)
        easygui.msgbox(audioFile, title="simple gui")
        printPrediction()

gif_label = Label(root,image="")
gif_label.pack()
browseButton = Button(bottomFrame, text="Browse", fg="red", command=filebrowser)
browseButton.pack(side=LEFT)
recordButton = Button(bottomFrame, text="Test", fg="blue", command= printPrediction)
recordButton.pack(side=LEFT)
exitButton = Button(bottomFrame, text="Exit", fg="black", command=exit)
exitButton.pack(side=LEFT)
root.mainloop()
