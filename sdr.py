from pylab import *
import matplotlib.pyplot as plt
from rtlsdr import *
#import scipy.signal as signal
#import sk_dsp_comm.sigsys as ss
#import sk_dsp_comm.rtlsdr_helper as sdr
#import sk_dsp_comm.fir_design_helper as fir_d
#import sk_dsp_comm.digitalcom as dc

sdr = RtlSdr()

def plot(freq):
    ''' Frequency: MHz'''
    # configure device
    sdr.sample_rate = 2.4e6
    sdr.center_freq = freq * 1e6 - 1e6 #1227.60 * 1e6
    sdr.gain = 4

    samples = sdr.read_samples(256*1024)
    offsets = np.convolve(np.real(samples), np.ones(1024), 'valid') / 1024
    offsets = np.pad(offsets, (len(samples) - len(offsets), 0), mode='constant', constant_values=offsets[0])
    samples = samples - offsets.astype(complex)

    #offsets = np.mean(np.real(samples)
    #samples = samples - complex(np.mean(np.real(samples)), 0)

    # PSD = (np.abs(np.fft.fft(samples))/len(samples))**2
    # PSD_log = 10.0 * np.log10(PSD)
    # PSD_shifted = np.fft.fftshift(PSD_log)
    #
    # f = np.linspace(sdr.center_freq - sdr.sample_rate/2, sdr.center_freq + sdr.sample_rate/2, len(samples)) # lazy method
    # plt.plot(f, PSD_shifted)
    # plt.show()

    # psdsk,freqs = ss.my_psd(samples, NFFT=1024, Fs=sdr.sample_rate)
    #
    # plt.plot(freqs + sdr.center_freq, psdsk)
    # plt.show()

    # use matplotlib to estimate and plot the PSD
    plt.psd(samples, NFFT=1024, Fs=sdr.sample_rate/1e6, Fc=sdr.center_freq/1e6)
    plt.xlabel('Frequency (MHz)')
    plt.ylabel('Relative power (dB)')
    return


plt.ion()
fig = plt.figure()
fig.set_figwidth(15)

while True:
    plt.subplot(1, 3, 1)
    plot(100)
    plt.subplot(1, 3, 2)
    plot(1575.42)
    plt.subplot(1, 3, 3)
    plot(1227.60)
    fig.canvas.draw()
    time.sleep(0.4)
    fig.clear()

