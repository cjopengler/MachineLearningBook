function X_rec = recoverData(Z, U, K)
%RECOVERDATA Recovers an approximation of the original data when using the 
%projected data
%   X_rec = RECOVERDATA(Z, U, K) recovers an approximation the 
%   original data that has been reduced to K dimensions. It returns the
%   approximate reconstruction in X_rec.
%

% You need to return the following variables correctly.
X_rec = zeros(size(Z, 1), size(U, 1));

% ====================== YOUR CODE HERE ======================
% Instructions: Compute the approximation of the data by projecting back
%               onto the original space using the top K eigenvectors in U.
%
%               For the i-th example Z(i,:), the (approximate)
%               recovered data for dimension j is given as follows:
%                    v = Z(i, :)';
%                    recovered_j = v' * U(j, 1:K)';
%
%               Notice that U(j, 1:K) is a row vector.
%               

% 先计算Ureduce, 维度是 n*K (n是x的原始维度)
Ureduce = U(:, 1:K);

Ureduce_size = size(Ureduce)
Z_size = size(Z)
X_rec_size = size(X_rec)

% 计算X_rec, Z的维度是 m*K, X_rec 的维度是 m*n

X_rec = Z * Ureduce';

% =============================================================

end
