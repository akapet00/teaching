%% modulate data using QAM and display results in a scatter plot
k = 4;                          % number of bits
M = 2^k;                        % order of QAM -> 16QAM
x = (0:M-1)';                   % input data
y = qammod(x, M);
scatterplot(y)
title('16-QAM')

%% normalize QAM signal by average power
k = 5;
M = 2^k;
x = randi([0 M-1], 1000, 1);    % 1000 random integers
y = qammod(x, M, 'UnitAveragePower', true);
avgPower = mean(abs(y).^2);
scatterplot(y)
title('64-QAM, Average Power = 1 W')

%% binary ordering
M = 16;
d = (0:M-1);
symorder = 'bin';
qammod(d, M, 'PlotConstellation', true);
qammod(d, M, symorder, 'PlotConstellation', true);

%% bit as inputs
k = 6;
M = 2^k;
d = (0:M-1);
y = transpose(de2bi(d, k));
symorder = 'bin';
xmap = qammod(y, M, symorder, ...
    'InputType', 'bit', ...
    'PlotConstellation', true);

%% noisy channel 
k = 5;
M = 2^k;
% generate binary data sequence
% the number of rows, N, in the input must be an integer multiple of
% the number of bits per symbol, k
x = randi([0 1], 1000*k, 1);
% modulate the signal using bit inputs, set it to have unit average power
tx = qammod(x, M, 'InputType', 'bit', ...
    'UnitAveragePower', true);
% pass the signal through a noisy channel
rx = awgn(tx, 25);
% plot the constellation diagram
cd = comm.ConstellationDiagram( ...
    'ShowReferenceConstellation', false);
cd(rx)

%% demodulation
% set the modulation order as 64, and determine the number of bits/symbol
M = 64;
k = log2(M);
% generate a sequence of random bits considering the number of bits/symbol
x = randi([0 1], 10*k, 1);
% modulate the input data using a binary symbol mapping and
% set the modulator to output fixed-point data;
% the numeric data type is signed with a 16-bit word length and
% a 10-bit fraction length
y = qammod(x, M, 'bin', ...
    'InputType', 'bit', ...
    'OutputDataType', numerictype(1,16,10));
% demodulate the modulated signal
z = qamdemod(y, M, 'bin', 'OutputType', 'bit');
s = isequal(x, boolean(z))