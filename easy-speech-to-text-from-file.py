'''
Speech to Text Recognition From an Audio File
@author: Suyash Shivaji Phatak
Date: 19/06/2020
'''

# Importing Libraries
import speech_recognition as sr

# Intitalizing a regnizor variable
r = sr.Recognizer()

# Reading Audio File and storing in a variable
with sr.AudioFile('female.wav') as source:
    audio_text = r.listen(source)

# If recognize method throws an error
try:
    ''' Using google speech recognition
    We can convert the language giving additional parameter to recognize_google function
    Refer this link https://cloud.google.com/speech-to-text/docs/languages
    for language keywords'''
    # Use this code for converting: text = r.recognize_google(audio_text, language="en-IN")
    text = r.recognize_google(audio_text)
    print('\nConverting Audio Transcipts into Text...\n')
    print(text)
except:
    print('\nRun Failed')
