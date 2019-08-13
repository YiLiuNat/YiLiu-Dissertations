function [best_constraint,total_cost] = constraintNcost(F,matrix,column_cost)
    total_cost = F*column_cost';
    temp2 = (matrix*F')';
    best_constraint = sum(((temp2-1).^2)');
end