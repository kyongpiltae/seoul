# %% 
import numpy as np


# Generate a sinusoid - from scratch using numpy library only
fs = 44100 # sampling rate
amp = 0.5 # amplitude
freq = 440 # frequency in Hz
T = 1/fs # sampling period
dur = 2 # duration in seconds
phi = np.pi/2 # initual phase in radian
# time-domain signal Sinosoid 만들기
x = amp*np.sin(2*np.pi*freq*np.arange(0, dur, T)+phi) # 44100 * 2 size .wav file 

# %% 

import IPython.display as ipd
ipd.Audio(x, rate=fs, autoplay=False)

# %%
import matplotlib.pyplot as plt

dur = 0.1
xs = x[0:int(fs*dur)]
ti = np.linspace(0,dur,int(fs*dur))
plt.plot(ti,xs)
plt.title('x(t)')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.show()

# %%
nfft = 2048 # fft size  duration 
x_nfft = x[0:nfft] # snippet of x rectangular Window
X = np.fft.fft(x_nfft) # complex numbers


# %%
Xdb = 20*np.log10(np.absolute(X) + np.finfo(float).eps) # magnitude in dB scale
Xdb = list(Xdb)
fi = np.arange(0,fs,fs/nfft) # freq. resolution = fs/nfft
plt.title('Magnitude response')
plt.xlabel('frequency (Hz)')
plt.ylabel('magnitude (dB)')
plt.xlim(0,fs/2) # show only up to Nyquist limit (fs/2)
plt.plot(fi,Xdb,'o')
plt.xlim(0,1000)
plt.show()

# %%
phs = np.angle(X) # phase in radians
plt.title('Phase response')
plt.xlabel('frequency (Hz)')
plt.ylabel('phase (rad)')
plt.xlim(0,fs/2)
plt.plot(fi,phs)
plt.show()



# %%
# Frequency resolution & zero padding

fs = 44100 # sampling rate
amp = 1 # amplitude
freq = 440 # frequency in Hz
T = 1/fs # sampling period
dur = 2 # duration in seconds
phi = 0 # initual phase in radian

# time-domain signal
x = amp*np.sin(2*np.pi*freq*np.arange(0, dur, T)+phi)


# %% 
nfft1 = 1024 # fft size
x_nfft1 = x[0:nfft1] # snippet of x
X1 = np.fft.fft(x_nfft1) # complex numbers
Xdb1 = 20*np.log10(np.absolute(X1) + np.finfo(float).eps) # magnitude in dB scale
Xdb1 = list(Xdb1)

# %% 
# plot zero-padded signal
nfft2 = 8192
x_nfft2 = np.append(x_nfft1, [0] * (nfft2 - len(x_nfft1)))
X2 = np.fft.fft(x_nfft2)
Xdb2 = 20*np.log10(np.absolute(X2) + np.finfo(float).eps)
Xdb2 = list(Xdb2)


#%% 
ti = np.arange(0,dur,T)
plt.plot(ti[0:nfft1],x_nfft1)
plt.title('x_nfft1(t)')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.show()


plt.plot(ti[0:nfft2],x_nfft2)
plt.title('x_nfft2(t)')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.show()

# %%
fi = np.arange(0,fs,fs/nfft1) # freq. resolution = fs/nfft1 = 43.07 Hz
plt.title('Magnitude response')
plt.xlabel('frequency (Hz)')
plt.ylabel('magnitude (dB)')
plt.xlim(400,500)
plt.plot(fi,Xdb1,'o')
plt.show()

# %%
fi = np.arange(0,fs,fs/nfft2) # freq. resolution = fs/nfft2 = 5.38 Hz
plt.title('Magnitude response')
plt.xlabel('frequency (Hz)')
plt.ylabel('magnitude (dB)')
plt.xlim(400,500)
plt.plot(fi,Xdb2,'o')
plt.show()

# %%
# Class1 - 3 : Spectral leaking & windowing
fs = 8000 # sampling rate
amp = 1 # amplitude
freq = 440 # frequency in Hz
T = 1/fs # sampling period
dur = 2 # duration in seconds
phi = 0 # initual phase in radian

# time-domain signal
x = amp*np.sin(2*np.pi*freq*np.arange(0, dur, T)+phi)
# %% 
nfft = 1024 # fft size
x_nfft = x[0:nfft] # snippet of x
X = np.fft.fft(x_nfft) # complex numbers
Xdb = 20*np.log10(np.absolute(X) + np.finfo(float).eps) # magnitude in dB scale
Xdb = list(Xdb)

win = np.hanning(nfft) # Hann window
xw = np.multiply(x_nfft, win)
Xw = np.fft.fft(xw)
Xwdb = 20*np.log10(np.absolute(Xw) + np.finfo(float).eps) # magnitude in dB scale
Xwdb = list(Xwdb)

# %% 
ti = np.arange(0,dur,T)
plt.plot(ti[0:nfft],x_nfft)
plt.title('x_nfft(t)')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.show()

ti = np.arange(0,dur,T)
plt.plot(ti[0:nfft],xw)
plt.title('x_nfft(t)')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.show()

# %%
#  Class1 - 4 : STFT & time-frequency representation

import librosa
import librosa.display

# audio_path = 'T39-piano.wav'
# audio_path = 'T08-violin.wav'
audio_path = 'speechbeach1.wav'
# audio_path = 'public_square.wav'

audio, sr = librosa.load(audio_path, sr=None)
print('sample rate of this audio file :', sr, 'Hz')
# pd.Audio(audio, rate=sr, autoplay=False) # play audio
# %%

'''
dur = 0.1
xs = x[0:int(fs*dur)]
ti = np.linspace(0,dur,int(fs*dur))
plt.plot(ti,xs)
plt.title('x(t)')
plt.xlabel('time (seconds)')
plt.ylabel('amplitude')
plt.show()
'''

librosa.display.waveplot(audio, x_axis='time',sr=sr)
plt.show()

#%% 


n_fft = 1048

stft = librosa.stft(audio, n_fft=n_fft, hop_length=int(n_fft - 7*n_fft/8))
spectrogram, phase = librosa.magphase(stft)


# %% 
plt.figure(figsize=(18,4))
librosa.display.specshow(np.log(spectrogram + 0.001), cmap='viridis', x_axis='time', y_axis='linear',sr=sr,hop_length=int(n_fft - 7*n_fft/8))
print(np.shape(spectrogram))
plt.show()

# %%
mfcc = librosa.feature.mfcc(y=audio, sr=sr)
plt.figure(figsize=(18,4))
librosa.display.specshow(mfcc, x_axis='time',sr=sr)
plt.colorbar()
plt.title('MFCC')
plt.tight_layout()
plt.show()

# %%
plt.plot(mfcc[0,:])
plt.plot(mfcc[:3,:].T)

# %%
mfcc_delta = librosa.feature.delta(mfcc)

mfcc_deltaDelta = librosa.feature.delta(mfcc_delta)