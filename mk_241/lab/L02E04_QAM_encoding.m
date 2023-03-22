k = 4;
M = 2^k;
y = int2bit((0:M-1)',k,false);
symorder = 'gray';
xmap = qammod(y,M,symorder,'InputType','bit','PlotConstellation',true);