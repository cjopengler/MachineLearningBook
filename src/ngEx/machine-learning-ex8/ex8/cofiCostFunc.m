function [J, grad] = cofiCostFunc(params, Y, R, num_users, num_movies, ...
                                  num_features, lambda)
%COFICOSTFUNC Collaborative filtering cost function
%   [J, grad] = COFICOSTFUNC(params, Y, R, num_users, num_movies, ...
%   num_features, lambda) returns the cost and gradient for the
%   collaborative filtering problem.
%

% 先将R变成logical类型，因为外面可能传进来的是double
R = logical(R);

% Unfold the U and W matrices from params
X = reshape(params(1:num_movies*num_features), num_movies, num_features);
Theta = reshape(params(num_movies*num_features+1:end), ...
                num_users, num_features);

            
% You need to return the following values correctly
J = 0;
X_grad = zeros(size(X));
Theta_grad = zeros(size(Theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost function and gradient for collaborative
%               filtering. Concretely, you should first implement the cost
%               function (without regularization) and make sure it is
%               matches our costs. After that, you should implement the 
%               gradient and use the checkCostFunction routine to check
%               that the gradient is correct. Finally, you should implement
%               regularization.
%
% Notes: X - num_movies  x num_features matrix of movie features
%        Theta - num_users  x num_features matrix of user features
%        Y - num_movies x num_users matrix of user ratings of movies
%        R - num_movies x num_users matrix, where R(i, j) = 1 if the 
%            i-th movie was rated by the j-th user
%
% You should set the following variables correctly:
%
%        X_grad - num_movies x num_features matrix, containing the 
%                 partial derivatives w.r.t. to each element of X
%        Theta_grad - num_users x num_features matrix, containing the 
%                     partial derivatives w.r.t. to each element of Theta
%


% 计算X*theta'，矩阵的预测Y的值
Predicats = X * Theta';

% 将Predicats与Y 做差
Diff = Predicats - Y;

% 将Diff 用 R 来获取那些R(i,j)=1的部分的数据
DiffR = Diff(R);

% 对上面的数据求平方和就是代价函数
J = DiffR' * DiffR / 2;

% 加入正规化, 代价函数的正规化就是 所有Θ平方和 和 所有X平方和
JRegular = (X(:)' * X(:) + Theta(:)'*Theta(:)) * lambda / 2;

% 代价函数的计算
J = J + JRegular;

% 计算梯度

% Diff = m * u; Θ = u * f; X= m*f
% grad_X = Diff * Θ = m * f
% grad_Theta = Diff' * X = u * f;

% 构造DiffR_grad 使得 对于DiffR来说R(i,j)=0的位置Y(i,j)=0; R(i,j)=1的位置，DiffR(i,j)=DiffR(i,j)
DiffR_grad = Diff .* R;

% 计算X的梯度
X_grad = DiffR_grad * Theta;

% X梯度的正规化项, x正规化项就是自己本身乘以lambda
X_grad_regular = lambda*X;

% 带有正规化的x梯度计算
X_grad = X_grad + X_grad_regular;

% 计算Θ的梯度
Theta_grad = DiffR_grad' * X;

% Θ的梯度的正规化项, Θ自己乘以lambda
Theta_grad_regular = lambda * Theta;

% 带有正规化项的Θ计算
Theta_grad = Theta_grad + Theta_grad_regular;



% =============================================================

grad = [X_grad(:); Theta_grad(:)];

end
