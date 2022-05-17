% Digital modulation and demodulation blocks incur delays between their
% inputs and outputs, depending on their configuration and on properties
% of their signals.

% As a result of delays, data that enters a modulation or demodulation
% block at time T appears in the output at time T+delay. In particular, if
% your simulation computes error statistics or compares transmitted with
% received data, it must take the delay into account when performing such
% computations or comparisons.

% In addition to the delays mentioned above, the M-DPSK, DQPSK, and DBPSK
% demodulators produce output whose first sample is unrelated to the input.
% This is related to the differential modulation technique, not the
% particular implementation of it.

% Example: delays from demodulation
% Demodulation in the model below causes the demodulated signal to lag,
% compared to the unmodulated signal. When computing error statistics, the
% model accounts for the delay by setting the Error Rate Calculation
% block's Receive delay parameter to 0. If the Receive delay parameter had
% a different value, then the error rate showing at the top of the Display
% block would be close to 1/2.

doc_oqpsk_modulation_delay