function [total_cost, F] = StochasticSetCover(matrix_a, column_cost)

% number of rows ??m
m = size(matrix_a,1);
% number of columns ??n
n = size(matrix_a, 2);

% ???I??????????(I[i] = 0???i?????)
% Initiate I to indicate all rows are not cover (I_i = 0 means the i_th row is not covered)
I = zeros(1,m);

% F???F[j] = 1???j?????????
% F is the solution, i.e., F_j=1 means the j_th column is selcted, F_j=0,
% otherwise
F = zeros(1,n);
U = I;
loop_counter = 1;
% It terminates when all rows are covered, i.e., sum(I)=m
while (ismember(0,U))
    % Find out which rows have not been covered 
    uncovered_rows_idx = find(U==0);
    % randomly select an uncovered row i
    i = uncovered_rows_idx(randi(length(uncovered_rows_idx)));
    % alpha_i is the indices of columns that cover row i
    alpha_i = find(matrix_a(i,:)==1);

    %  select column j \in \alpha_i which covers row i with minimum cost
    [mincost, idx] = min(column_cost(alpha_i));
    
    % However, there are multiple column with the same minimum cost 
    % If we use min function in matlab, we will always selet the first column with the minimum cost
    idx_array = find(column_cost(alpha_i) == mincost);
    num_same_mincost = length(idx_array);
    % To prevent this problem, we randomly select one column if there are multiple column with the same minimum cost
    if num_same_mincost > 1
      idx = idx_array(randi(num_same_mincost));
    end
    %j = alpha_i(idx);
    
    % randomly select an uncovered column
    j = alpha_i(randi(numel(alpha_i),1));
    % beta_j is the indices of rows that cover column j
    beta_j = find(matrix_a(:,j)==1);
    
    index_I = find(I==0);
    index_U = find(U==0);
    I_exclude_U = setdiff(index_I,index_U);
    
    % Randomly select a column j ? ?i such that ?j ? (I?U) = ?;
    %if(isempty(intersect(beta_j,I-U)))
    if(isempty(intersect(beta_j, I_exclude_U)))
    % Set Sk ? Sk+j
        F(1,j) = 1;
        % Set U ? U?i, ?i ? ?j
        U(1, beta_j) = 1;
    else
        U(1, i) = 1;
    end
    
    % Set column j as part of the solution
    %F(1,j) = 1;
    % Set I to include the rows covered by column j
    % I(1, matrix_a(:,j)==1) = 1;
    loop_counter = loop_counter +1;
end

%total_cost = F*column_cost';
%best_constraint = constraint(F,matrix_a);%sum(((temp2-1).^2)');
 [best_constraint,total_cost] = constraintNcost(F,matrix_a,column_cost);
% disp(['The minimum cost found by the Stochastic Greedy algorithm is: ', num2str(total_cost)]);
% disp(['The solution found by the Stochastic Greedy algorithm is: ', num2str(F)]);
% disp(['The sum of violations of the constraints is: ', num2str(best_constraint)]);
% disp(['The index of solution is: ', num2str(find(F==1))]);