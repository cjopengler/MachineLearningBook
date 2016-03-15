function p = predict(Theta1, Theta2, X)
%PREDICT Predict the label of an input given a trained neural network
%   p = PREDICT(Theta1, Theta2, X) outputs the predicted label of X given the
%   trained weights of a neural network (Theta1, Theta2)

% Useful values
m = size(X, 1);
num_labels = size(Theta2, 1);




% You need to return the following variables correctly 
p = zeros(size(X, 1), 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Complete the following code to make predictions using
%               your learned neural network. You should set p to a 
%               vector containing labels between 1 to num_labels.
%
% Hint: The max function might come in useful. In particular, the max
%       function can also return the index of the max element, for more
%       information see 'help max'. If your examples are in rows, then, you
%       can use max(A, [], 2) to obtain the max for each row.
%

% X 增加偏置项1 变成a1 表示第一层

a1 = [ones(m, 1) X];

size_theta1 = size(Theta1)
size_theta2 = size(Theta2)
size_X = size(X)
size_a1 = size(a1)

% 计算第2层a2
a2 = sigmoid(a1 * Theta1');

size_a2 = size(a2)

% a2 需要增加偏置项1
a2 = [ones(size(a2, 1), 1) a2];

size_a2_1 = size(a2)

% 计算第3层a3, a3就是输出层，注意
a3 = sigmoid(a2 * Theta2');


fprintf("get result -----------\n");
Theta1(1, 1:10)
Theta2(1, 1:10)
a3(1, 1:10)
% a3 应该是[0, 1, 0, 0,...,0]这种形式，其中1的位置就是哪个分类,所以取出最大的所在的索引
[h_max, p] = max(a3, [], 2);


% =========================================================================


end
