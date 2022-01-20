import librosa
from librosa import feature
import soundfile
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
            result=np.hstack((result,mel))
    return result
