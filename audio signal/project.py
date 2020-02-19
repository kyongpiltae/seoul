
# %% 
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import IPython.display as ipd
import scipy
import glob
import librosa
import IPython.display as ipd
import librosa.display

# %% 
# read files
speech_mnist = glob.glob('./speech_mnist/*.wav')

X, fs = librosa.load(speech_mnist[0], sr=None)

print('file name : ' + speech_mnist[0])
print('sampling rate : ' + (str)(fs))
# ipd.Audio(X, rate=fs, autoplay=False)
sr = fs
audio = X 
# %%
plt.figure(figsize=(18,4))
librosa.display.waveplot(audio, sr)
plt.show()


# %% 
# plot , mel, mfcc , f0:pitch 

n_fft = int(np.power(2, np.ceil(np.log2(np.abs(int(sr*0.1))))))
spec, phase = librosa.magphase(librosa.stft(audio, n_fft=n_fft, win_length = n_fft, hop_length = int(n_fft - 7*n_fft/8), window='hann'))

nframe = len(spec[0])
plt.figure(figsize=(18,4))
plt.title("STFT")
librosa.display.specshow(np.log(spec + 0.001), cmap='viridis', x_axis='time', y_axis='linear',hop_length = int(n_fft - 7*n_fft/8),sr=sr)
plt.show()

# %% 
# compute spectral centroid (SC) and spectral spread (SS)
fi = np.linspace(0,int(sr/2),int(n_fft/2))
ti = np.linspace(0,len(audio)/sr,nframe)
print(ti[-1])
sc = []
ss = []

for i in range(0,nframe):
  X = spec[:-1,i]
  sc.append(np.sum(np.multiply(fi,np.power(np.abs(X),2)))/np.sum(np.power(np.abs(X),2)))
  ss.append(np.sqrt(np.sum(np.power(np.subtract(fi,sc[i]),2)*np.power(np.abs(X),2))/np.sum(np.power(np.abs(X),2))))
# %%
C = np.abs(librosa.cqt(y=audio,fmin=30, sr=sr))
plt.figure(figsize=(18,4))
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max), sr=sr, x_axis='time', y_axis='cqt_note')

# librosa.display.specshow(20*np.log10(C), sr=sr, x_axis='time', y_axis='cqt_note')

plt.colorbar(format='%+2.0f dB')
plt.title('Constant-Q power spectrum')
plt.tight_layout()
plt.show()

# %%
pitch_class = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
chromagram = librosa.feature.chroma_cqt(y=audio,fmin=30, sr=sr)
plt.figure(figsize=(18,4))
librosa.display.specshow(chromagram, y_axis='chroma', x_axis='time',sr=sr)
plt.colorbar()
plt.title('Chromagram')
plt.tight_layout()
plt.show()
chord = []
prev_c = np.argmax(chroma[:,0])
chord.append(pitch_class[prev_c])
for c in np.argmax(chroma,axis=0).tolist():
    if prev_c == c:
        prev_c = c
        continue
    prev_c = c 
    chord.append(pitch_class[c])
print(*chord[1:-1],sep='-')
print('The result is not consistent with the real value (CDEFGABC)')

# %%
