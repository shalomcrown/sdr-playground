#SDR
This is a set of programs to work with RTL-SDR.

## sdr.py
Requires Pylab instead of Numpy/Maptplotlib, Pyrtlsdr for working with the SDR

The sdr.py program simply samples three fequencies a few times every second, and plots power 
spectra

In the plots, the center frequency is 1MHz less than the requested frequency. 
This is because I can't get rid of the DC spike.

The three frequencies are 100 MHz, 1575.42 MHz (L1) and 1227.60 MHz (L2)
