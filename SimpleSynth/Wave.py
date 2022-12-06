import numpy as np
import matplotlib.pyplot as plt
from scipy.io import wavfile

# class to store the values from the oscillator
class Wave:
    def __init__(self, num_frames, signal=0, sample_rate = 44100): 
        self._num_frames = num_frames
        self._sample_rate = sample_rate
        self._signal = signal
        
        self.set_samples()
    
    @property
    def num_frames(self):
        return self._num_frames
    
    @num_frames.setter
    def num_frames(self, numbers):
        self._num_frames = numbers
        self.set_samples()

    @property
    def samples_y(self):
        return self._samples_y

    def set_samples(self):
        #making time array for plotting
        self._samples_t = np.array(range(0, int(self._num_frames), 1))/self._sample_rate

        if not isinstance(self._signal, int): # handwavy way of checking if we need a signal or not
            signal = iter(self._signal)
            self._samples_y = np.array([next(self._signal) for i in range(self._num_frames)])

    def __add__(self, wave2):
        if self._num_frames != wave2.num_frames:
            raise ValueError
        elif self._sample_rate != wave2._sample_rate:
            raise ValueError
        else:
            new_wave = Wave(self._num_frames/self._sample_rate) # to convert back to seconds
            new_wave._samples_y = self._samples_y + wave2.samples_y
            return new_wave

    # plotting the values 
    def plot(self):
        plt.plot(self._samples_t, self.samples_y)
        plt.show()

    # converting to wav file
    def convert_to_wav(self, filename="default.wav", vol=0.1):
        wav = np.int16(self.samples_y * vol * (2**15 - 1))
        wavfile.write(filename, self._sample_rate, wav)
