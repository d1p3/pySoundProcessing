#subplot(nrows, ncols, plot_number)
import soundfile as sf
import matplotlib.pyplot as plt
from scipy.signal import freqz
import numpy as np
import math
soundfile,samplerate=sf.read("")
fs=samplerate
half_soundfile=np.array([])
ddt=np.fft.fft(soundfile)

fig1,(ax1,ax2)=plt.subplots(1,2)
ax1.set_title("time domain")
#plt.subplot(1,2,1)
ax1.plot(soundfile)
ax2.set_title("frequency domain")
#plt.subplot(1,2,2)
ax2.plot(abs(ddt.real)[0:int(len(soundfile)/2)])

#lowpass filter
fc=3500
L=101
M=L-1
ft=fc/fs
wn=np.array([])
new_wn=np.array([])
window=np.array([])
for n in range(0,L):
    window=np.append(window,0.54-0.46*math.cos(2*math.pi*n/M))
    if(n!=M/2):
        wn=np.append(wn,math.sin((2*math.pi*ft*(n-(M/2))))/(math.pi*(n-(M/2))))
    elif(n==(M/2)):
        wn=np.append(wn,2*ft)
for i in range(0,L):
    new_wn=np.append(new_wn,wn[i]*window[i])
soundfile1=np.convolve(soundfile,new_wn)
fig1,(ax1,ax2)=plt.subplots(nrows=1,ncols=2)
#plt.subplot(1,2,1)
ax1.set_title("time domain")
ax1.plot(soundfile1)
ax2.set_title("frequency domain")
ddt1=np.fft.fft(soundfile1)
#plt.subplot(1,2,2)

ax2.plot(abs(ddt1.real)[0:int(len(soundfile1)/2)])
sf.write("laurelLow.wav",soundfile1,fs)

#highpass filter

wn2=np.array([])
new_wn2=np.array([])
window2=np.array([])
for n in range (0,L):
    window2=np.append(window2,0.54-0.46*math.cos(2*math.pi*n/M))
    if(n!=M/2):
        wn2=np.append(wn2,-math.sin((2*math.pi*ft*(n-(M/2))))/(math.pi*(n-(M/2))))
    if(n==M/2):
        wn2=np.append(wn2,1-2*ft)
for i in range(0,L):
    new_wn2=np.append(new_wn2,wn2[i]*window2[i])
soundfile2=np.convolve(soundfile,new_wn2)
fig1,(ax1,ax2)=plt.subplots(nrows=1,ncols=2)
ax1.set_title("time domain")
ax1.plot(soundfile2)
ax2.set_title("frequency domain")
ddt2=np.fft.fft(soundfile2)
ax2.plot(abs(ddt2.real)[0:int(len(soundfile2)/2)])
sf.write("laurelHigh.wav",soundfile2,fs)
