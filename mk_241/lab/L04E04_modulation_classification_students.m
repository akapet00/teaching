%% Modulation Classification with Deep Learning

% This excercise uses a convolutional neural network (CNN) to classify
% modulated signals in three steps:
% 1. You generate synthetic, channel-impaired waveforms;
% 2. Using this generated waveforms as training data, you train a CNN for
%    classification purposes;
% 3. You test CNN with software-defined radio (SDR) hardware and
% over-the-air signals.

%% Predict Modulation Type Using CNN

% The trained CNN should be able to recognize 8 digital and 3 analog
% modulation types: BPSK, BPSK, 8-PSK, 16-QAM, 64-QAM, PAM4, GFSK, CPFSK,
% B-FM, DSB-AM, SSB-AM.
% Your first task is to create a 'modulationTypes' categorical variable and
% fill it with names of each modulation type to be classified:
modulationTypes = ...;

% Now, load the trained network 'trainedModulationClassificationNetwork':
...

% Check the properties of the network by typing 'trainedNet' in the Command
% Window in Matlab. How many layers does the network contain? How many
% channel-impaired samples does it take as its input?
n_samples = ...;

% Visualize the schematic of the network by using predifend functionality
% 'plot'. What is the type of the 'trainedNet' and what are its core
% properties?

% The following task is to generate several PAM4 frames that are impaired
% with Rician multipath fading, center frequency and sampling time drift,
% and AWGN. Use following function to generate synthetic signals to test
% the CNN. Then use the CNN to predict the modulation type of the frames.
rng(123456)  % state of the random number generator
d = randi([0 3], n_samples, 1);  % random bits
syms = ...;  % apply PAM4 modulation

filterCoeffs = rcosdesign(0.35,4,8);  % square-root raised cosine filter
tx = filter(filterCoeffs,1,upsample(syms,8));  % pulse shape the symbols

% Define the channel where SNR is 30 dB, carrier frequency is 902 MHz,
% sample rate is is 200 thousands samples per unit time. Maximal offset
% should be set to 5.
SNR = ...;
maxOffset = ...;
fc = ...;
fs = ...;

% apply Rician multipath channel
multipathChannel = comm.RicianChannel(...
  'SampleRate', fs, ...
  'PathDelays', [0 1.8 3.4] / 200e3, ...
  'AveragePathGains', [0 -2 -10], ...
  'KFactor', 4, ...
  'MaximumDopplerShift', 4);

% apply phase/frequency shift due to clock offset
frequencyShifter = comm.PhaseFrequencyOffset('SampleRate', fs);

% apply an independent multipath channel
reset(multipathChannel)
outMultipathChan = multipathChannel(tx);

% determine clock offset factor
clockOffset = (rand() * 2*maxOffset) - maxOffset;
C = 1 + clockOffset / 1e6;

% add frequency offset
frequencyShifter.FrequencyOffset = -(C-1)*fc;
outFreqShifter = frequencyShifter(outMultipathChan);

% add sampling time drift where time goes from 0 to the size of 'tx' and is
% scaled by the sampling rate
t = ...;
newFs = fs * C;
tp = (0:length(tx)-1)' / newFs;
outTimeDrift = interp1(t, outFreqShifter, tp);

% add noise where 'SIGPOWER' should be defined as 0 dbW
rx = ...;

% generate frames for classification by using 'L04E04_modClassGetNNFrames'
unknownFrames = ...;

% classify unknown frames and store the results
...;

% Check the classifier predictions, which are analogous to hard decisions.
% The network should correctly identify the frames as PAM4 frames. Check
% their associated scores by using 'L04E04_modClassPlotScores' function.
...;

% Note that before we can use a CNN for modulation classification, or any
% other task for that matter, we first need to train the network with known
% (or labeled) data.

%% Predict Modulation Type Using CNN

% Here, we will skip the generation of synthetic training data and
% defining and training the CNN. Rather, we will focus of testing
% pretrained network (whose weights are stored in
% 'trainedModulationClassificationNetwork' mat file) and check test the
% network performance with over-the-air signals using software defined
% radio (SDR) platforms.

% load the measured signal from 'rx_measured.mat' file
...

% generate frames for classification
unknownFrames = ...;

% classify unknown frames
...;

% Check the classifier predictions and check their associated scores by
% using 'L04E04_modClassPlotScores' function.
...;


