function [J, grad] = costFunctionReg(theta, X, y, lambda)
%COSTFUNCTIONREG Compute cost and gradient for logistic regression with regularization
%   J = COSTFUNCTIONREG(theta, X, y, lambda) computes the cost of using
%   theta as the parameter for regularized logistic regression and the
%   gradient of the cost w.r.t. to the parameters. 

% Initialize some useful values
m = length(y); % number of training examples

% You need to return the following variables correctly 
J = 0;
grad = zeros(size(theta));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the cost of a particular choice of theta.
%               You should set J to the cost.
%               Compute the partial derivatives and set grad to the partial
%               derivatives of the cost w.r.t. each parameter in theta


hx = 1 ./ (1 + exp(-X*theta));
h1 = log(hx);
h2 = log(1 - hx);

J = -(h1'*y + h2'*(1-y))/m;

% 去掉θ0的θ矩阵
thetaLamda = theta(2:end);

% 计算lambda项
JLamda = (lambda*thetaLamda'*thetaLamda)/(2*m);

J += JLamda;

hx = 1 ./ (1 + exp(-X*theta));


for j = 1 : size(theta, 1)

  if j == 1 
    grad(j) = (hx - y)'*X(:, j) / m;
  elseif
    grad(j) = (hx - y)'*X(:, j) / m + lambda*theta(j, 1)/m;
  end
  
end

% =============================================================

end
