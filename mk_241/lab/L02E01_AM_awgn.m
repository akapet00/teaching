% Prepare to sample a signal for two seconds,
% at a rate of 100 samples per second.
Fs = 100; % Sampling rate
t = [0:2*Fs+1]'/Fs; % Time points for sampling

% Create the signal, a sum of sinusoids.
x = sin(2*pi*t)+sin(4*pi*t);

Fc = 10; % Carrier frequency in modulation
phasedev = pi/2; % Phase deviation for phase modulation

tx = pmmod(x, Fc, Fs, phasedev); % Modulate.
rx = awgn(tx, 10, 'measured'); % Add noise.
y = pmdemod(rx, Fc, Fs, phasedev); % Demodulate.

% Plot the original and recovered signals.
figure; plot(t, x, '-', t, y, '-', linewidth=2);
legend('Original signal', 'Recovered signal')
xlabel('Time (s)');
ylabel('Amplitude (V)');