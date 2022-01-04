# from time import time
# import speech_recognition as sr
#
#
# def interpretcommand():
#     if int(time() % 8) == 0:
#         # get audio from the microphone
#         r = sr.Recognizer()
#         with sr.Microphone() as source:
#             print("Tell a command:")  # supported commands are start the game, return to menu and quit the game.
#             audio = r.listen(source)
#
#         try:
#             speech = r.recognize_google(audio)
#             print("You have said " + speech)
#             return speech
#
#         except sr.UnknownValueError:
#             print("Could not understand audio")
#             return
#
#         except sr.RequestError as e:
#             print("Could not request results; {0}".format(e))
#             return
#
