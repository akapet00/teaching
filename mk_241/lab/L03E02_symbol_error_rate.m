% The example generates a random digital signal, modulates it, adds noise,
% demodulates the noisy signal, and computes the symbol error rate.
% The noisy, modulated data is plotted in a constellation diagram.
% Numerical results and plot may vary due to the random input data.

% Set alphabet size for 16-QAM
M = 16;
x = randi([0 M-1], 5000, 1);
% initialize constellation diagram
c = qammod(0:M-1, M);
cd = comm.ConstellationDiagram('ReferenceConstellation', c, ...
    'XLimits', [-4 4], ...
    'YLimits', [-4 4]);
% apply 16-QAM modulation
tx= qammod(x, M);

% pass the signal through an AWGN channel with 
% the SNR set to 15 and
% the parameter SIGPOWER defined as 'measured'
rx = awgn(tx, 15, 'measured');

% demodulate the modeulated signal to recover the message
z = qamdemod(rx, M);

% Check the symbol error rate
[num, rt] = symerr(x, z);

% create constellation diagram from noisy data;
% note that the signal reference constellation has 16 precisely located
% points, but the transmitted symbols with the noise added causes the
% scatter plot to have a small cluster of points scattered around each
% reference constellation point
cd(rx)