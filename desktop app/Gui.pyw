from tkinter import *
from tkinter import filedialog
from PIL import Image


import easygui
# my function can be used as follows: indexOfEmotion = Predict.predictGivenFileName(filename) filename is a string
# with full file location "D//abc//1.wav"   ranges from 1 to 8

root = Tk()
root.title('Agile project')
myLabel = Label(root, text="This is a simple GUI", bg="blue", fg="white", font=("Helvetica", 16))
#myLabel2 = Label(root, text="You Think You Will Die Alone!", fg="#CCCC00", bg="white", font=("Helvetica", 16))
#myLabel3 = Label(root, text="We Got You Covered", fg="white", bg="black", font=("Helvetica", 16))
#myLabel4 = Label(root, text="Just Talk To US :)", fg="black", bg="green", font=("Helvetica", 16))
myLabel.pack(fill=X)
#myLabel2.pack(fill=X)
#myLabel3.pack(fill=X)
#myLabel4.pack(fill=X)
myLabelInput=Label(root, 
         text="First Name")
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

    gif_label.configure(image=im2)
    count += 1
    if count == frames:
        count = 0
    anim = root.after(50,lambda :animation(count))

def printPrediction():
    #global indexOfEmotion
    global label
    indexOfEmotion=int(e1.get())
    if indexOfEmotion == 1:
        #label.configure(image=img1)
        
        global file
        file='img/happy.gif'
        info = Image.open(file)
        global frames
        frames = info.n_frames
        global im
        im = [PhotoImage(file=file,format=f"gif -index {i}") for i in range(frames)]
        
        #easygui.msgbox(file1, title="simple gui")
        
        easygui.msgbox(frames, title="simple gui")
        global count
        count=0
        animation(count)
    elif indexOfEmotion == 2:
        label.configure(image=img2)
    elif indexOfEmotion == 3:
        label.configure(image=img3)
    elif indexOfEmotion == 4:
        label .configure(image=img4)
    


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
