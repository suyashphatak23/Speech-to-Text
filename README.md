<a href="https://python.org"><img src="https://www.python.org/static/community_logos/python-logo-master-v3-TM.png" title="Python" width="500px" height="200px" alt="Python"></a>

<a href="https://cloud.google.com/speech-to-text"><img src="https://andrestephens.org/wp-content/uploads/2018/11/gcp-speech.png" title="Google Speech API" width="500px" height="300px" alt="Google Speech API"></a>

<a href="https://pypi.org/project/PyAudio/"><img src="https://i.pinimg.com/originals/fd/35/68/fd3568921ab43120e710df86f3de00f0.png" title="Pyaudio" width="500px" height="200px" alt="Pyaudio"></a>

# Easy Speech to Text Recognition

In this project, I have used google cloud speech api service for converting speech to text in python program. I have created 2 seperate file such as one file containing conversion from a audio file of extension .wav and one file containing direct speech from microphone. In this project, I have also tried to convert text into different languages such as marathi. In this project, I have observerd that accuracy of speeh to text api is around 70-90% according to the noise level in the speech. I refered this project from website *towardsdatascience.com*.

[![Build Status](http://img.shields.io/travis/badges/badgerbadgerbadger.svg?style=flat-square)](https://travis-ci.org/badges/badgerbadgerbadger)
[![Coverage Status](http://img.shields.io/coveralls/badges/badgerbadgerbadger.svg?style=flat-square)](https://coveralls.io/r/badges/badgerbadgerbadger)

**Note:<br> 1. The speech to text file needs network or data connection. <br>
        2. Audio file supported by speech recognition are  *wav, AIFF, AIFF-C, FLAC*.**

# Outputs

### 1. Audio File
I have used **<a href="https://github.com/suyashphatak23/Speech-to-Text/blob/master/female.wav">female.wav</a>** file in this output.
<img src="https://github.com/suyashphatak23/Speech-to-Text/blob/master/Outputs/outputfile.JPG" title="Audio File" width="1200px" height="500px" alt="Audio File Output">

### 2. Microphone File
I talked **how are you** and it returned correctly.

<img src="https://github.com/suyashphatak23/Speech-to-Text/blob/master/Outputs/outputmicrophone.JPG" title="Microphone File" width="1200px" height="500px" alt="Microphone File Output">

### 3. Microphone File with other language
I talked **how are you** in *marathi* and it returned correctly.

<img src="https://github.com/suyashphatak23/Speech-to-Text/blob/master/Outputs/outputmarathi.JPG" title="Microphone File in Marathi" width="1200px" height="500px" alt="Microphone File Output in Marathi">

# Clone

***Clone this repo to your local machine using*** **https://github.com/suyashphatak23/Speech-to-Text**

# Setup

1. > Open **Command Prompt**

2. > Install **PyAudio** and **SpeechRecognition** python-libray in your local machine by using following commands:

```shell
> pip install PyAudio
> pip install SpeechRecognition
```

3. > Run the code in **python3 shell**

4. > If you want to change the audio file just change the file name in the code and note that it should be in the same directory of the code.

# License

[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0)

**[GNU license](https://opensource.org/licenses/gpl-license)**
