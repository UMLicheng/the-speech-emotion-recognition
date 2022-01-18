#!/usr/bin/env python
# coding: utf-8

# In[1]:


import speech_recognition as sr


# In[39]:


speech1 = "C:/Users/Dell/Downloads/DTWSpeech-master/sounds/Aishsad.wav"
speech2 = "C:/Users/Dell/Downloads/DTWSpeech-master/sounds/Aishscary.wav"
speech3 = "C:/Users/Dell/Downloads/DTWSpeech-master/sounds/AishSurprise.wav"
speech4 = "C:/Users/Dell/Downloads/DTWSpeech-master/sounds/HappyAish.wav"


# In[40]:


# initialize the recognizer
r = sr.Recognizer()


# In[41]:


with sr.AudioFile(speech1) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text1 = r.recognize_google(audio_data)
    
with sr.AudioFile(speech2) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text2 = r.recognize_google(audio_data)
    
with sr.AudioFile(speech3) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text3 = r.recognize_google(audio_data)
    
with sr.AudioFile(speech4) as source:
    # listen for the data (load audio to memory)
    audio_data = r.record(source)
    # recognize (convert from speech to text)
    text4 = r.recognize_google(audio_data)
    
print("Speech1 :",text1)
print("Speech2 :",text2)
print("Speech3 :",text3)
print("Speech4 :",text4)


# In[42]:


import text2emotion as myText


# In[43]:


myText.get_emotion(text1)


# In[44]:


myText.get_emotion(text2)


# In[45]:


myText.get_emotion(text3)


# In[46]:


myText.get_emotion(text4)


# In[ ]:




