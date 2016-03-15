function [bestEpsilon bestF1] = selectThreshold(yval, pval)
%SELECTTHRESHOLD Find the best threshold (epsilon) to use for selecting
%outliers
%   [bestEpsilon bestF1] = SELECTTHRESHOLD(yval, pval) finds the best
%   threshold to use for selecting outliers based on the results from a
%   validation set (pval) and the ground truth (yval).
%

bestEpsilon = 0;
bestF1 = 0;
F1 = 0;

stepsize = (max(pval) - min(pval)) / 1000;
for epsilon = min(pval):stepsize:max(pval)
    
    % ====================== YOUR CODE HERE ======================
    % Instructions: Compute the F1 score of choosing epsilon as the
    %               threshold and place the value in F1. The code at the
    %               end of the loop will compare the F1 score for this
    %               choice of epsilon and set it to be the best epsilon if
    %               it is better than the current choice of epsilon.
    %               
    % Note: You can use predictions = (pval < epsilon) to get a binary vector
    %       of 0's and 1's of the outlier predictions


% 概率p 小于ε,说明是异常的 1表示；概率p 大于等于ε,说明是正常的 0表示；这种表述要和yval是一样的
% 先计算基于概率的预测向量
predictions = pval < epsilon;

% 接下来计算查准率(precision)和召回率(recall)

% 1 计算predictions与实际的y 相同以及不相同的地方，也就是真阳，假阳，真阴，假阴
P = (predictions == yval);

% 2 计算真阳性的数量, predictions 等于1 并且yval也等于1. predictions & yval 会只保留1 1 这种 其他的 1 0, 0 1, 0 0 都会变成0.
turePositive = sum(predictions & yval);

% 3 计算查准率
positiveInPredictions = sum(predictions);
prec = turePositive / positiveInPredictions;

% 4 计算召回率
positiveInY = sum(yval);
rec = turePositive / positiveInY;

% 5 计算F1
F1 = 2 * prec * rec / (prec + rec);





    % =============================================================

    if F1 > bestF1
       bestF1 = F1;
       bestEpsilon = epsilon;
    end
end

end
