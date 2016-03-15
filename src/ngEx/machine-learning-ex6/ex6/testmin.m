X = [1 10 3; 6 5 4; 7 8 9]
[minX, index] = min(X, [], 1);
minX
index

minErr = min(X(:));
[row, clomn] = find(X == minErr);

row
clomn

cVec = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
sigmaVec = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];

C = cVec(row);
sigma = sigmaVec(clomn);

C
sigma
