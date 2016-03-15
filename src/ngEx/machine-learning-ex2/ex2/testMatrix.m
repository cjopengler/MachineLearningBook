% 测试矩阵的性质
% 1 矩阵中每一个元素都加1
fprintf("1 X+1 \n");
X = eye(3)
X = X+1

% 2 矩阵中每一个元素都求对数
fprintf("2 log10(X) \n");
X = [1 10; 100 1000]
X = log10(X)

% 3 矩阵中每一个元素都求指数
fprintf("3 exp\n");
X = [1 log(2); log(3) log(4)]
X = exp(X)

% 4 矩阵中每一个元素求倒数
fprintf("4 1/X \n");
X = [1 5; 10 20]
X = 1./X

% 5 矩阵中所有元素都取负数

fprintf("4 -X \n");
X = [1 5; 10 20]
X = 1./X

% 6 测试zero

fprintf("test zero \n");
zeros(4)
zeros(4, 3)
zeros(4, 4)

% 7 测试逻辑运算
fprintf("test <= 0.5 \n")
X = eye(3)
X = X <= 0.5