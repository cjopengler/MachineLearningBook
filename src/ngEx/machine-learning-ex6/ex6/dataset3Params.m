function [C, sigma] = dataset3Params(X, y, Xval, yval)
%EX6PARAMS returns your choice of C and sigma for Part 3 of the exercise
%where you select the optimal (C, sigma) learning parameters to use for SVM
%with RBF kernel
%   [C, sigma] = EX6PARAMS(X, y, Xval, yval) returns your choice of C and 
%   sigma. You should complete this function to return the optimal C and 
%   sigma based on a cross-validation set.
%

% You need to return the following variables correctly.
C = 1;
sigma = 0.3;

% ====================== YOUR CODE HERE ======================
% Instructions: Fill in this function to return the optimal C and sigma
%               learning parameters found using the cross validation set.
%               You can use svmPredict to predict the labels on the cross
%               validation set. For example, 
%                   predictions = svmPredict(model, Xval);
%               will return the predictions on the cross validation set.
%
%  Note: You can compute the prediction error using 
%        mean(double(predictions ~= yval))
%

% 初始化c 和 sigma 向量
cVec = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];
sigmaVec = [0.01, 0.03, 0.1, 0.3, 1, 3, 10, 30];

clen = 2;
slen = 2;
% errs 每一对c sigma 的存储向量
errs = 10000*ones(length(cVec), length(sigmaVec));


for i=1: length(cVec)

  for j=1: length(sigmaVec)
  
    model= svmTrain(X, y, cVec(i), @(x1, x2) gaussianKernel(x1, x2, sigmaVec(j))); 
    
    predictions = svmPredict(model, Xval);
    
    err = mean(double(predictions ~= yval));
    
    
    errs(i, j) = err;
    
    i
    j
    err
    
  end
end

minErr = min(errs(:));

errs

[row, clomn] = find(errs == minErr);

row
clomn

C = cVec(row(1));
sigma = sigmaVec(clomn(1));

C
sigma


% =========================================================================

end
