function [J, grad] = linearRegCostFunction(X, y, theta, lambda)
%LINEARREGCOSTFUNCTION Compute cost and gradient for regularized linear 
%regression with multiple variables
%   [J, grad] = LINEARREGCOSTFUNCTION(X, y, theta, lambda) computes the 
%   cost of using theta as the parameter for linear regression to fit the 
%   data points in X and y. Returns the cost in J and the gradient in grad

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost and gradient of regularized linear 
%               regression for a particular choice of theta.
%
%               You should set J to the cost and grad to the gradient.
%

% X 已经加了偏置项，所以这里不用增加直接使用
% 计算h(x)的向量
hx = X * theta;

% 计算 hx - y 的向量
cost = hx - y;

% 计算总的代价函数

J = cost'*cost / (2*m);

% 计算正规化
% 去掉θ0 这个偏置项
R_theta = theta(2:end);

% 计算θ平方和
R = R_theta' * R_theta * lambda / (2*m);

% 最终的代价函数
J = J + R;

% =========================================================================

% 计算J的梯度
cost = hx - y;

% 所有θ的grad
grad_J = cost' * X / m;

% 将grad_J转换成列向量和θ保持一致
grad_J = grad_J';


% 计算正规化grad 
% 将θ0 偏置项变成0
R_Grad_Theta = [0; theta(2:end)];

% size_R_Grad_Theta = size(R_Grad_Theta)

% 正规化梯度
R_Grad = R_Grad_Theta*lambda / m;

% 最后的grad
grad = grad_J + R_Grad;

grad = grad(:);

end
