import soundfile as sf
import numpy as np
import matplotlib.pyplot as plt
import math
from scipy.signal import freqz

data,samplerate=sf.read('timilai.wav')
fs=samplerate
ddt=np.fft.fft(data)
plt.plot(ddt.real)
for i in range(0,len(data)):
        ddt[i]+2
    
plt.show()
plt.plot(ddt.real)
iddt=np.fft.ifft(ddt)
plt.show()
sf.write('cleanMusic.wav',iddt.real,samplerate)