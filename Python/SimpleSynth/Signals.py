from abc import ABC, abstractmethod
import math

# parent class
class Signal(ABC):
    def __init__(self, freq, ampl=1, phase = 0, sample_rate = 44100):
        #these will stay fixed
        self._freq = freq
        self._time_period = 1/freq
        self._ampl = ampl
        self._phase = math.pi*(phase/180) #phase in degrees
        self._sample_rate = sample_rate

        #these will change to allow for modulation
        self._f = freq
        self._a = ampl
        self._p = math.pi*(phase/180)
        self.frame = 0
        
    @property
    def init_freq(self):
        return self._freq
    
    @property
    def init_ampl(self):
        return self._ampl
    
    @property
    def init_phase(self):
        return self._phase

    #we now interact with _f with the property freq of the class
    @property
    def freq(self):
        return self._f
    
    @freq.setter
    def freq(self, freq):
        self._f = freq
        self._step = (2*math.pi*self._f)/self._sample_rate
    
    #we now interact with _a with the property ampl of the class
    @property
    def ampl(self):
        return self._a
    
    @ampl.setter
    def ampl(self, ampl):
        self._a = ampl

    #we now interact with _p with the property phase of the class
    @property
    def phase(self):
        return self._p
    
    @phase.setter
    def phase(self, phase):
        self._p = phase

    @abstractmethod
    def _initialize_signal(self):
        pass

    def __iter__(self):
        self.freq = self._freq
        self.ampl = self._ampl
        self.phase = self._phase
        self._initialize_signal()
        return self
    
    @abstractmethod
    def __next__(self):
        pass



# child classes

# class implementing sin wave
class SinSignal(Signal):
    def _initialize_signal(self):
        self._i = 0

    def __next__(self):
        val = math.sin(self._i + self._p)
        self._i += self._step
        return self._a * val


# class implementing square wave
class SquareSignal(Signal):
    def __init__(self, freq, ampl, duty = 0.5, phase=0, sample_rate=44100):
        super().__init__(freq, ampl, phase, sample_rate)
        self._duty = duty

    def _initialize_signal(self):
        self._i = 0

    def __next__(self):
        phase = self._i + self._p
        self._i += self._step

        if (phase - (phase//(2*math.pi))*2*math.pi) <= self._duty*2*math.pi:
            return self.ampl
        else:
            return -self.ampl 

#class implementing saw wave
class SawSignal(Signal):
    def _initialize_signal(self):
        self._i = 0

    def __next__(self):
        phase = self._i + self._p
        self._i += self._step 
        mod_phase = phase - (phase//(2*math.pi))*2*math.pi

        y = 2*self._a*self._f*mod_phase/(2*math.pi*self.freq) - self.ampl
        return y