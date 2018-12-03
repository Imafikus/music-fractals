import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np
np.set_printoptions(threshold=np.inf)

SCALING_FACTOR = 200

def plot_soundwave(snd, samp_freq):
    """
    Plot a soundwave given by snd
    Sample frequency is given by samp_freq
    """

    #?amplitude is mapped from -2^15 to 2^15 - 1, we want normalized amplitude
    snd = snd /(2.0**15)
    
    #?snd has 2 channels and some number of sampling points
    #?print(snd.shape)
    sample_points = snd.shape[0]

    #?we can calculate the time points by knowing the number
    #?of sampling points and sample frequency, because
    #?sample_points / samp_freq will give as time in ms^(-3)
    #?we want to see nice representation of miliseconds so we
    #?multiply by 10^3
    time_array = np.arange(0, sample_points, 1) / samp_freq * 1000

    plt.plot(time_array, snd, color='k')
    plt.xlabel("Time(ms)")
    plt.ylabel("Amplitude")
    
    plt.show()

def main():
    samp_freq, snd = wav.read('samples/bass_sample.wav')
    
    plot_soundwave(snd, samp_freq)

    #?amplitude is mapped from -2^15 to 2^15 - 1, we want normalized amplitude
    #? for now we also want to scale it for further usage in main.py
    snd = snd /(2.0**15) * SCALING_FACTOR
        
if __name__ == "__main__":
    main()