function [J grad] = nnCostFunction(nn_params, ...
                                   input_layer_size, ...
                                   hidden_layer_size, ...
                                   num_labels, ...
                                   X, y, lambda)
                                   
%NNCOSTFUNCTION Implements the neural network cost function for a two layer
%neural network which performs classification
%   [J grad] = NNCOSTFUNCTON(nn_params, hidden_layer_size, num_labels, ...
%   X, y, lambda) computes the cost and gradient of the neural network. The
%   parameters for the neural network are "unrolled" into the vector
%   nn_params and need to be converted back into the weight matrices. 
% 
%   The returned parameter grad should be a "unrolled" vector of the
%   partial derivatives of the neural network.
%

% Reshape nn_params back into the parameters Theta1 and Theta2, the weight matrices
% for our 2 layer neural network
% input_layer_size 就是 sl, 之所以+1是因为Theta1中包含了偏置项的缘故,所以input_layer_size+1 才是正确的数目
% 对于Θ矩阵来说，每一行对应着的是下一层的激活想的全部Θ参数个数也就是 sl

Theta1 = reshape(nn_params(1:hidden_layer_size * (input_layer_size + 1)), ...
                 hidden_layer_size, (input_layer_size + 1));

% size_Theta1 = size(Theta1)              


Theta2 = reshape(nn_params((1 + (hidden_layer_size * (input_layer_size + 1))):end), ...
                 num_labels, (hidden_layer_size + 1));


% Setup some useful variables
m = size(X, 1);
         
% You need to return the following variables correctly 
J = 0;
Theta1_grad = zeros(size(Theta1));
Theta2_grad = zeros(size(Theta2));

% ====================== YOUR CODE HERE ======================
% Instructions: You should complete the code by working through the
%               following parts.
%
% Part 1: Feedforward the neural network and return the cost in the
%         variable J. After implementing Part 1, you can verify that your
%         cost function computation is correct by verifying the cost
%         computed in ex4.m
%
% Part 2: Implement the backpropagation algorithm to compute the gradients
%         Theta1_grad and Theta2_grad. You should return the partial derivatives of
%         the cost function with respect to Theta1 and Theta2 in Theta1_grad and
%         Theta2_grad, respectively. After implementing Part 2, you can check
%         that your implementation is correct by running checkNNGradients
%
%         Note: The vector y passed into the function is a vector of labels
%               containing values from 1..K. You need to map this vector into a 
%               binary vector of 1's and 0's to be used with the neural network
%               cost function.
%
%         Hint: We recommend implementing backpropagation using a for-loop
%               over the training examples if you are implementing it for the 
%               first time.
%
% Part 3: Implement regularization with the cost function and gradients.
%
%         Hint: You can implement this around the code for
%               backpropagation. That is, you can compute the gradients for
%               the regularization separately and then add them to Theta1_grad
%               and Theta2_grad from Part 2.
%

% 总的层数定义 L，当前情况是3层

L = 3;

% 激活项的矩阵，每一层是一个列向量，不包含偏置项
% 第1层的激活项 不包含偏置项，同时m个样本一起表述
a1 = X;

% 增加偏置项1
a1 = [ones(size(X,1), 1) X];

% size_X = size(X)
% size_a1 = size(a1)


% 第2层的激活项 不包含偏置项
z2 = a1 * Theta1';
a2 = sigmoid(z2);

% a2 增加偏置项1
a2 = [ones(size(a2, 1), 1) a2];

% 第三层激活项 也就是输出项

z3 = a2 * Theta2';
a3 = sigmoid(z3);

% a1 a2 a3 计算完毕接下来计算J(θ),计算J(θ)使用的是a3,因为aL = a3
% 关于a3, size(a3) = 5000*10 = m * K.
% 所以a3, 每一行就是一个最终向量
% A 将a3向量换成行的形式 注意 X(:) 变成列向量


A = [log(a3)(:)' log(1-a3)(:)'];

% size_A = size(A)


% y 的转化 因为y=1,2,...,10 是这些分类，那么我们需要将其转换成向量,
% 如果是y=2, 那么 则转换成 y2 = [0 1 0 0 ... 0] 这种形式才能参与运算


Y1 = [];
Y2 = [];

for i = 1: length(y)
  yy = y(i) * ones(num_labels, 1);
  Y1 = [Y1; yy];

  Y2 = [Y2; [1:num_labels]'];
end

yK = (Y1 == Y2);

% size_y = size(y)
% size_yK = size(yK)



% Y y本身是列向量，1-y 也是列向量
Y = [yK; 1-yK];

% J = -A * Y/m;
a3T = a3';


J = log((a3T(:))')*yK + log((1-a3T(:))')*(1-yK);
J = J / (-m);


% 计算正规化项,要去掉偏置项对应的θ后计算

t1 = Theta1(:, 2:size(Theta1, 2));
t2 = Theta2(:, 2: size(Theta2, 2));
R = (t1'(:))' * t1'(:) + (t2'(:))' * t2'(:);

R = (R * lambda)/(2*m);

J = J + R;


% -------------------------------------------------------------

% 先把y的对应的矩阵方式写好，对应的矩阵方式
% 第1个样本 [a3,1 a3,2 ..., a3,10] [y1, y2, ..., y10]
% 第2个样本 [a3,1 a3,2 ..., a3,10] [y1, y2, ..., y10]
% 这种格式需要得到y的行向量进行计算。

Y1 = [];
Y2 = [];
for i = 1: length(y)
  yy = y(i) * ones(1, num_labels);
  Y1 = [Y1; yy];

  Y2 = [Y2; [1:num_labels]];
end

Y = (Y1 == Y2);

% Y(1:3, :)

delta3 = a3 - Y;

% delta3_size = size(delta3)

delta2 = delta3*Theta2.*a2.*(1-a2);

% delta2_size = size(delta2)

% delta2 包含了偏置项，所以需要在这里剔除掉第一个
delta2ColumnSize = size(delta2, 2);

delta2 = delta2(:, 2:delta2ColumnSize);

% 去掉偏置项中的delta2 用来计算delta1 
delta1 = delta2*Theta1.*a1.*(1-a1);

% delta1_size = size(delta1)

% 所有的delta 计算完毕， 接下来计算偏导

for i = 1 : m 
% 第一层
Theta1_grad += delta2(i, :)' * a1(i, :);

% 第二层偏导
Theta2_grad += delta3(i, :)' * a2(i, :);
end

Theta1_grad = (1/m) * Theta1_grad;
Theta2_grad = (1/m) * Theta2_grad;

% size_Theta1_grad = size(Theta1_grad)
% size_Theta2_grad = size(Theta2_grad)


% 增加正规化一项

% Theta1 和 Theta2需要先去掉偏置项，也就是将第一列全部变成0就可以直接进行操作了
R_Theta1 = [zeros(size(Theta1, 1), 1) Theta1(:, 2:end)];
R_Theta2 = [zeros(size(Theta2, 1), 1) Theta2(:, 2:end)];

% size_R_Theta1 = size(R_Theta1)
% size_R_Theta2 = size(R_Theta2)


% 计算带有正规化的梯度

Theta1_grad = Theta1_grad + lambda * R_Theta1/m;
Theta2_grad = Theta2_grad + lambda * R_Theta2/m;

% =========================================================================

% Unroll gradients
grad = [Theta1_grad(:) ; Theta2_grad(:)];


end
