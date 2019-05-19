# Voice-Imposing-Deep-Learning-Hackathon

This  whole project is for our course CS 671, by Dr Aditya Nigam. and build under a 40hrs hackathon.
Title - Voice Imposing
Problem Statement is - Given a human voice, we will convert its speech/audio into target person voice-style.

Network division - Whole network is divided into 2 modules first Voice to text and second Text to Target persons voice.
Module-1 : Voice to text, For this we have used deepspeech pre-trained network and by its trained module we can convert audio(.wav format) to text.

To download the Module 1, use this command from the command line:

while [ $? -ne 0 ]; do LC_ALL=C wget --continue -O deepspeech.tar.gz  https://github.com/mozilla/DeepSpeech/releases/download/v0.4.1/deepspeech-0.4.1-models.tar.gz; done

Module-2 : The Encoder-Decoder network which takes a test as input and outputs final audio as target persons style.

After this we have created a script to create a end-to-end pipeline which takes as input audio and gives an audio output, but for script to work system needs to connect to IIT Mandi Wifi.
