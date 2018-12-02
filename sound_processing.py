import matplotlib.pyplot as plt
from scipy.io import wavfile as wav
from scipy.fftpack import fft
import numpy as np

def main():
    samp_freq, snd = wav.read('samples/guitar_sample.wav')
    snd = snd /(2.0**15)
    #print(snd.shape[0])

    time_array = np.arange(0, snd.shape[0], 1) / samp_freq * 1000

    #fft_out = fft(data)
    #%matplotlib inline
    plt.plot(time_array, snd, color='k')
    plt.xlabel("Time(ms)")
    plt.ylabel("Amplitude")
    #plt.plot(data, fft_out)
    
    plt.show()

if __name__ == "__main__":
    main()