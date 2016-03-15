function [mu sigma2] = estimateGaussian(X)
%ESTIMATEGAUSSIAN This function estimates the parameters of a 
%Gaussian distribution using the data in X
%   [mu sigma2] = estimateGaussian(X), 
%   The input X is the dataset with each n-dimensional data point in one row
%   The output is an n-dimensional vector mu, the mean of the data set
%   and the variances sigma^2, an n x 1 vector
% 

% Useful variables
[m, n] = size(X);

% You should return these values correctly
mu = zeros(n, 1);
sigma2 = zeros(n, 1);

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the mean of the data and the variances
%               In particular, mu(i) should contain the mean of
%               the data for the i-th feature and sigma2(i)
%               should contain variance of the i-th feature.
%

% 计算每个特征分量的均值，是将每一列相加求平均, sum(X) 会将列相加
mu = sum(X) / m;

% 计算方差
% X每一个元素减去相应的均值
subMu = bsxfun(@minus, X, mu);
% 减去均值的做平方
sqSubMu = subMu .* subMu;

% 方差就是 平方相加/m
sigma2 = sum(sqSubMu) / m;








% =============================================================


end
