
X = [1 2 3; 4 5 6]

R = logical([1   1   0  ; 1   0   0])

RL = [true true false; true false false]

Result = X(1, R(1, :))

ResultL = X(1, RL(1, :))

