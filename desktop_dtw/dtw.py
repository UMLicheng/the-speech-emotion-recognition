import librosa
import soundfile
import os, glob
import sys
import numpy as np

def extractFeature (fileName, mfcc, chroma, mel ):
    with soundfile.SoundFile(fileName) as soundFile:
        X=soundFile.read(dtype="float32")
        sampleRate=soundFile.samplerate
        if chroma:
            stft=np.abs(librosa.stft(X))
        result=np.array([])
        if mfcc:
            mfccs=np.mean(librosa.feature.mfcc(y=X, sr=sampleRate, n_mfcc=40).T, axis=0)
            result=np.hstack((result, mfccs))

        if chroma:
            chroma=np.mean(librosa.feature.chroma_stft(S=stft, sr=sampleRate).T, axis=0)
            result=np.hstack((result, chroma))

        if mel:
            mel=np.mean(librosa.feature.melspectrogram(X, sr=sampleRate).T,axis=0)
            result=np.hstack((result, mel))
    return result

emotions={
    '01':'neutral',
    '02':'calm',
    '03':'happy',
    '04':'sad',
    '05':'angry',
    '06':'fearful',
    '07':'disgust',
    '08':'surprised'
}

#observe the emotion
observedEmotions=['sad', 'fearful', 'surprised', 'happy']
#Load data and extract features
def loadData():
    x,y=[],[]
    for file in glob.glob("archive/Actor_*/*.wav"):
        fileName=os.path.basename(file)
        emotion=emotions[fileName.split("-")[2]]
        if emotion not in observedEmotions:
            continue
        feature=extractFeature(file,mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return np.array(x), y

#sad:03-01-04-01-01-01-05
file="archive/Actor_05/03-01-04-01-01-02-05.wav"
feature=extractFeature(file, mfcc=True, chroma=True, mel=True)
x,y=loadData()
best_cost = sys.maxsize
index = -1
for i in range(len(x)):
    D, wp = librosa.sequence.dtw(feature, x[i])
    cost = D[wp[-1, 0], wp[-1, 1]]
    print(cost)
    if cost < best_cost and cost != 0:
        best_cost = cost
        index = i
print(best_cost)
print(y[index])