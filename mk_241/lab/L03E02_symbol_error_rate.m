% The example generates a random digital signal, modulates it, adds noise,
% demodulates the noisy signal, and computes the symbol error rate.
% The noisy, modulated data is plotted in a constellation diagram.
% Numerical results and plot may vary due to the random input data.

% Set alphabet size for 16-QAM
M = 16;
x = randi([0 M-1],5000,1);

% Initialize constellation diagram
cpts = qammod(0:M-1,M);
constDiag = comm.ConstellationDiagram('ReferenceConstellation',cpts, ...
    'XLimits',[-4 4],'YLimits',[-4 4]);

% Apply 16-QAM modulation
y = qammod(x,M);

% Transmit signal through an AWGN channel with SNR set to 15 and SIGPOWER
% defined as 'measured'
ynoisy = awgn(y,15,'measured');

% Demodulate ynoisy to recover the message
z = qamdemod(ynoisy,M);

% Check the symbol error rate
[num,rt] = symerr(x,z);

% Create constellation diagram from noisy data. The signal reference
% constellation has 16 precisely located points but the transmitted symbols
% with the noise added causes the scatter plot to have a small cluster of
% points scattered around each reference constellation point.
constDiag(ynoisy)