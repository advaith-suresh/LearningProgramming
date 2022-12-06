'''
Goal: to make a playable synth
1. can select between Sin, Saw etc.
2. use keyboard keys as inputs to change frequency

Made by Advaith Suresh
'''

from Signals import *
from Wave import *
import pygame.midi as midi
import pyaudio
#from midi import *

'''
# making the oscillator
squareOsc = SquareSignal(1, 2)
squareWave = Wave(5, squareOsc)

sinOsc = SinSignal(3, 2, 75)
sinWave = Wave(5, sinOsc)

sawOsc = SawSignal(1, 2, 180)
sawWave = Wave(5, sawOsc)

sum = sawWave
sum.plot()
'''



midi.init()
default_id = midi.get_default_input_id()
midi_input = midi.Input(device_id=default_id)

stream = pyaudio.PyAudio().open(
    rate=44100,
    channels=1,
    format=pyaudio.paInt16,
    output=True,
    frames_per_buffer=44100
)

def noteToFreq(note):
    a = 440 #frequency of A (coomon value is 440Hz)
    return (a / 32) * (2 ** ((note - 9) / 12))

stream.start_stream()

dict_note = {}
try:
    while True:
        if dict_note:
            for _, samples in dict_note.items():
                #print(samples)
                #print("number: ", len(dict_note))
                stream.write(samples)

        if midi_input.poll():
            event = midi_input.read(num_events=1)
            note = event[0][0][1]
            vel = event[0][0][2]
            
            if note not in dict_note:
                dict_note[note] = np.int16(Wave(44100, SawSignal(noteToFreq(note), (vel*32767)/127)).samples_y).tobytes()
                #print(noteToFreq(note))
                #print("number: ", len(dict_note))
            elif note in dict_note:
                del dict_note[note]
                #print("deleting: ", note)
                #print("number: ", len(dict_note))
            

except KeyboardInterrupt:
    print("stopping")