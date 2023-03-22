fs = 100;
t = (0:1/fs:100)';
fc = 10; 
x = sin(2*pi*t);
ydouble = ammod(x,fc,fs);
ysingle = ssbmod(x,fc,fs);

sadsb = spectrumAnalyzer( ...
    SampleRate=fs, ...
    PlotAsTwoSidedSpectrum=false);
sadsb(ydouble)

sassb = spectrumAnalyzer( ...
    SampleRate=fs, ...
    PlotAsTwoSidedSpectrum=false)
sassb(ysingle)