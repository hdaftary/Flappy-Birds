import speech_recognition as sr

# this is called from the background thread
from constant import set_speech


def callback(recognizer, audio):
    # received audio data, now we'll recognize it using Google Speech Recognition
    try:
        speech = recognizer.recognize_google(audio)
        print("You have said " + speech)
        set_speech(speech)

    except sr.UnknownValueError:
        print("Could not understand audio")

    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))
