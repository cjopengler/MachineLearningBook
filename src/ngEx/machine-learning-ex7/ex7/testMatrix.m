X = [1 2; 3 4; 5 6]
fprintf("times for every row\n");
a = [1; 2; 3]
A = bsxfun(@times, X, a)

fprintf("times for every column\n");
b = [1 2]
B = bsxfun(@times, X, b)
