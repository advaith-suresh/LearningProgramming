import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# class to store the values from the oscillator
class Wave:
    def __init__(self, seconds, signal=0, sample_rate = 44100): 
        self._num_frames = seconds * sample_rate
        self._sample_rate = sample_rate
        
        #arrays
        self._samples_t = np.array(range(0, int(self._num_frames), 1))/self._num_frames
        if not isinstance(signal, int): # handwavy way of checking if we need a signal or not
            signal = iter(signal)
            self.samples_y = np.array([next(signal) for i in range(self._num_frames)])

    def __add__(self, wave2):
        if self._num_frames != wave2._num_frames:
            raise ValueError
        elif self._sample_rate != wave2._sample_rate:
            raise ValueError
        else:
            new_wave = Wave(self._num_frames/self._sample_rate) # to convert back to seconds
            new_wave.samples_y = self.samples_y + wave2.samples_y
            return new_wave
    
    # plotting the values 
    def plot(self):
        plt.plot(self._samples_t, self.samples_y)
        plt.show()

    # converting to wav file
    def convert_to_wav(self, filename="default.wav", vol=0.1):
        wav = np.int16(self.samples_y * vol * (2**15 - 1))
        wavfile.write(filename, self._sample_rate, wav)
