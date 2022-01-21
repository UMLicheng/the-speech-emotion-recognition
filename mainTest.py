import librosa
from librosa import feature
#from dtw import dtw
import soundfile,time
import os, glob, pickle

import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neural_network import MLPClassifier
from sklearn.metrics import accuracy_score

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
        #print(result)
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
#observedEmotions=['sad', 'fearful', 'surprised', 'happy']
observedEmotions=['sad', 'fearful', 'disgust', 'happy']
#Load data and extract features
def loadData(test_size=0.2):
    x,y=[],[]
    for file in glob.glob("archive/Actor_*/*.wav"):
        fileName=os.path.basename(file)
        emotion=emotions[fileName.split("-")[2]]
        #print(fileName)
        if emotion not in observedEmotions:
            continue
        feature=extractFeature(file,mfcc=True, chroma=True, mel=True)
        x.append(feature)
        y.append(emotion)
    return train_test_split(np.array(x), y, test_size=test_size, random_state=9)

file="archive/Actor_05/03-01-04-01-02-02-05.wav"
feature=extractFeature(file,mfcc=True, chroma=True, mel=True)
x_train,x_test,y_train,y_test=loadData(test_size=0.25)
#print(x_train)
#print(x_test)
#print(y_train)
#print(y_test)
#print((x_train.shape[0], x_test.shape[0]))

#print(f'Features extracted:{x_train.shape[1]}')

model=MLPClassifier(alpha=0.01, batch_size=256, epsilon=1e-08, hidden_layer_sizes=(300,),learning_rate='adaptive', max_iter=500)

model.fit(x_train, y_train)

y_pred=model.predict(x_test)
y_pre=model.predict([feature])

print(y_pre)

#accuracy= accuracy_score(y_true=y_test, y_pred=y_pred)

#print("Accurancy: {:.2f}%".format(accuracy*100))
#print(y_pred)