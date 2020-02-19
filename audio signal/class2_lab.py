
# %% 
import IPython.display as ipd
# import numpy as np
import librosa
import librosa.display
from matplotlib import pyplot as plt
import librosa
import librosa.display
import matplotlib.pyplot as plt
import numpy as np
import IPython.display as ipd
import scipy

import numpy as np
def sinewave(amp,freq,phs,dur,fs):
    T = 1 / fs
    y = amp * np.sin(2 * np.pi * freq * np.arange(0, dur, T) + phs)
    return y




'''
a. Generate a sequence of sinusoids whose frequencies move from C4 to C5 in a diatonic scale, that is, C4-D4-E4-F4-G4-A4-B4-C5. Each note should be 0.5 second long

'''
fs = 8000
### from https://pages.mtu.edu/~suits/notefreqs.html
### f0_list = []
audio_c4c5 = []

# %% 


freq_list = [261.63,293.66, 329.63, 349.23, 392.00, 440.00, 493.88, 523.25]
for freq in freq_list:
    audio_c4c5.extend(sinewave(0.5,freq,0, 0.5, fs))

audio_c4c5 = np.asarray(audio_c4c5)
ipd.display(ipd.Audio(audio_c4c5, rate=fs, autoplay=True))
    
# %% 
sr = fs
n_fft = int(np.power(2, np.ceil(np.log2(np.abs(int(sr*0.1))))))

spec, phase = librosa.magphase(librosa.stft(audio_c4c5, n_fft=n_fft, win_length = n_fft, hop_length = int(n_fft - 7*n_fft/8), window='hann'))

nframe = len(spec[0])
plt.figure(figsize=(18,4))
plt.title("STFT")
librosa.display.specshow(np.log(spec + 0.001), cmap='viridis', x_axis='time', y_axis='linear',hop_length = int(n_fft - 7*n_fft/8),sr=sr)
#plt.ylim(0,1000)
plt.show()

# %%
audio = audio_c4c5
C = np.abs(librosa.cqt(y=audio,fmin=30, sr=sr))
plt.figure(figsize=(18,4))
librosa.display.specshow(librosa.amplitude_to_db(C, ref=np.max), sr=sr, x_axis='time', y_axis='cqt_note')

# librosa.display.specshow(20*np.log10(C), sr=sr, x_axis='time', y_axis='cqt_note')

plt.colorbar(format='%+2.0f dB')
plt.title('Constant-Q power spectrum')
plt.tight_layout()
plt.show()

# %%
'''
a. For the same sequence in the previous problem, compute and plot the chromagram.It is consistent with your expectation?
b. Download prelude_cmaj_short_11k.wav from the class homepage. Compute and plot the chromagram. By visual inspection, try to estimate the chord sequence (Hint: there are three different kinds of chords, each repeating twice like A-A-B-B-C-C-A-A).
'''
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
audio, sr = librosa.load('prelude_cmaj_short_11k.wav', sr=None)
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
print(*chord,sep='-')
print('Expected chord : CEGCEGCE-CEGCEGCE-CDADFCAD-CDADFCAD-FBDGDFBD-FBDGDFBD-CEGCEGCE-CEGCEGCE')

# %%
