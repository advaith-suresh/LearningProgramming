'''
Goal: to make a playable synth
1. can select between Sin, Saw etc.
2. use keyboard keys as inputs to change frequency

Made by Advaith Suresh
'''

from Signals import *
from Wave import *

# making the oscillator
squareOsc = SquareSignal(1, 2)
squareWave = Wave(5, squareOsc)

sinOsc = SinSignal(3, 2, 75)
sinWave = Wave(5, sinOsc)

sawOsc = SawSignal(7, 2, 180)
sawWave = Wave(5, sawOsc)

sum = (sinWave + squareWave) + sawWave
sum.plot()
