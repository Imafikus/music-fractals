import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np

def main():
    samp_freq, snd = wav.read('samples/440_sine.wav')
    
    #?amplitude is mapped from -2^15 to 2^15 - 1, we want normalized amplitude
    snd = snd /(2.0**15)
    

    for s in snd[:, 0]:
        print(s)
    return
    #?snd has 2 channels and some number of sampling points
    #print(snd.shape)
    sample_points = snd.shape[0]

    #?we can calculate the time points by knowing the number
    #?of sampling points and sample frequency, because
    #?sample_points / samp_freq will give as time in ms^(-3)
    #?we want to see nice representation of miliseconds so we
    #?multiply by 10^3
    time_array = np.arange(0, sample_points, 10) / samp_freq * 1000

    #fft_out = fft(data)
    #%matplotlib inline
    plt.plot(time_array, snd, color='k')
    plt.xlabel("Time(ms)")
    plt.ylabel("Amplitude")
    #plt.plot(data, fft_out)
    
    #plt.show()

if __name__ == "__main__":
    main()