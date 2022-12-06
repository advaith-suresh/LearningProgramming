import pygame.midi as midi
import pyaudio

'''
class midi:
    def __init__(self):
        midi.init()
        default_id = midi.get_default_input_id()
        self.midi_input = midi.Input(device_id=default_id)

    def get_input(self):
        try:
            while True:
                if self.midi_input.poll():
                    data = self.midi_input.read(num_events=1)
                    print(data)
        except KeyboardInterrupt:
            print("stopping")
'''


midi.init()
default_id = midi.get_default_input_id()
midi_input = midi.Input(device_id=default_id)

stream = pyaudio.PyAudio().open(
    rate=44100,
    channels=1,
    format=pyaudio.paInt16,
    output=True,
    frames_per_buffer=256
)

stream.start_stream()

try:
    while True:
        if midi_input.poll():
            data = midi_input.read(num_events=1)
            
            

except KeyboardInterrupt:
    print("stopping")
