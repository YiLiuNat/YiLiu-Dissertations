function [rankedIndiv,rankedCost,rankedVio]=stochasticRanking(populationF,populationCost,populationVio)
    [indiv_num,~] = size(populationF);
    % Double loops to iterate all pairs of individuals
    for j = 1:indiv_num
        for i = 2:indiv_num
            U = rand; % a uniformly distributed random num
            Pf = 0.45; % Introduce Pf to allow infeasible solutions
            if ((populationVio(i) == 0 && populationVio(i-1) == 0) || U <= Pf)
                if(populationCost(i-1) > populationCost(i))
                    % Swap individual list
                    temp1 = populationF(i-1,:);
                    populationF(i-1,:) = populationF(i,:);
                    populationF(i,:) = temp1;
                    % Swap cost list
                    temp2 = populationCost(i-1);
                    populationCost(i-1) = populationCost(i);
                    populationCost(i) = temp2;
                    % Swap constraint violation list
                    temp3 = populationVio(i-1);
                    populationVio(i-1) = populationVio(i);
                    populationVio(i) = temp3;
                end    
            else % which means there are constraint violations
                if(populationVio(i-1) > populationVio(i))
                    % Swap individual list
                    temp1 = populationF(i-1,:);
                    populationF(i-1,:) = populationF(i,:);
                    populationF(i,:) = temp1;
                    % Swap cost list
                    temp2 = populationCost(i-1);
                    populationCost(i-1) = populationCost(i);
                    populationCost(i) = temp2;
                    % Swap constraint violation list
                    temp3 = populationVio(i-1);
                    populationVio(i-1) = populationVio(i);
                    populationVio(i) = temp3;
                end
            end
        end % Inner loop
    end % Outter loop
    rankedIndiv = populationF;
    rankedCost = populationCost;
    rankedVio = populationVio;
end