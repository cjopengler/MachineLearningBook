function sim = gaussianKernel(x1, x2, sigma)
%RBFKERNEL returns a radial basis function kernel between x1 and x2
%   sim = gaussianKernel(x1, x2) returns a gaussian kernel between x1 and x2
%   and returns the value in sim

% Ensure that x1 and x2 are column vectors
% 注意这一点，必须要保证是列向量
x1 = x1(:); x2 = x2(:);

% You need to return the following variables correctly.
sim = 0;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the similarity between x1
%               and x2 computed using a Gaussian kernel with bandwidth
%               sigma
%
%

% 计算x1-x的差向量
deltaX = x1 - x2;

% 计算平方和
qs = deltaX' * deltaX;

% 计算核函数内部全部参数
interal = -qs /(2*(sigma^2));

% 最后计算核函数值
sim = exp(interal);


% =============================================================
    
end
