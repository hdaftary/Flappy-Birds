import pygame
import flappy
from thread import callback
import speech_recognition as sr
import sys

if __name__ == '__main__':
    if len(sys.argv) == 3 and sys.argv[2] == "False":
        r = sr.Recognizer()
        m = sr.Microphone()
        with m as source:
            r.adjust_for_ambient_noise(source)  # we only need to calibrate once, before we start listening

        # start listening in the background (note that we don't have to do this inside a `with` statement)
        stop_listening = r.listen_in_background(m, callback)

    pygame.init()  # initialize pygame
    pygame.display.set_caption('Flappy Birds For Handicapped People')
    flappy.play_game()

