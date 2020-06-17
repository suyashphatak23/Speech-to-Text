'''
Speech to Text Recognition From Microphone
@author: Suyash Shivaji Phatak
Date: 19/06/2020
'''

# Importing Libraries
import speech_recognition as sr

# Intitalizing a regnizor variable
r = sr.Recognizer()

# Reading from micorphone as source
# listening and storing in variable
with sr.Microphone() as source:
    print('\nTalk\n')
    audio_text = r.listen(source)
    print('\nTime Over Thanks!!!\n')

# Error handeling
try:
    ''' Using google speech recognition
    We can convert the language giving additional parameter to recognize_google function
    Refer this link https://cloud.google.com/speech-to-text/docs/languages
    for language keywords'''
    # Use this code for converting: print('\nText: '+ r.recognize_google(audio_text, language="mr-IN"))
    
    print('\nText: '+ r.recognize_google(audio_text))
except:
    print('\nSorry, I did not get that !!!')
