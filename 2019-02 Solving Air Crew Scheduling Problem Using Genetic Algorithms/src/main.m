% Read Data
[matrix,col_cost] = ReadInData('sppnw41.txt');
% Pseudo-random Initialisation
individuals = 100; % Change polulation size here
totalF_list = [];
totalCost_list = [];
totalFitness_list = [];
totalVio_list = [];
initial_loop_count = 1;
while(initial_loop_count <= individuals)
    [~,F] = StochasticSetCover(matrix,col_cost);
    [initial_constraint,initial_cost] = constraintNcost(F,matrix,col_cost);
    while(ismember(initial_cost,totalCost_list))
        [~,F] = StochasticSetCover(matrix,col_cost);
        [initial_constraint,initial_cost] = constraintNcost(F,matrix,col_cost);
    end
    totalF_list = [totalF_list; F];
    totalCost_list = [totalCost_list initial_cost];
    totalFitness_list = [totalFitness_list 1/initial_cost];
    totalVio_list = [totalVio_list initial_constraint];
    lastLoop_cost = initial_cost;
    initial_loop_count = initial_loop_count + 1;
end
reminder_counter = 1;
% Generation loop
gen_loop_count = 1;
while(gen_loop_count <= 30)
    offspringF_list = [];
    offspringCost_list = [];
    offspringFitness_list = [];
    offspringVio_list = [];
    parent_pairs_num = 300;
    parents_loop_count = 1;
    while(parents_loop_count <= parent_pairs_num)
        % Select Parents
        zeroVio = find(totalVio_list == 0);
        if (length(zeroVio) > 1)
            parent1 = totalF_list(zeroVio(1),:);
            parent2 = totalF_list(zeroVio(2),:);
        else
            parent1 = totalF_list(ceil(rand*length(totalCost_list)),:);
            parent2 = totalF_list(ceil(rand*length(totalCost_list)),:);
            while(parent1 == parent2)
                parent2 = totalF_list(ceil(rand*length(totalCost_list)),:);
            end
        end
        while(parent1 == parent2)% make sure two selected parents are different
            loop_parent12Compare = 2;
            while(loop_parent12Compare <= length(zeroVio))
                parent2 = totalF_list(zeroVio(loop_parent12Compare),:);
                if(parent1 ~= parent2)
                    break
                end
                loop_parent12Compare = loop_parent12Compare+1;
            end
            parent2 = totalF_list(ceil(rand*length(totalCost_list)),:);
        end
       
        
        % Crossover
        after_cross = crossover(parent1,parent2,'nPoint');
        [cross_constraint,cross_cost] = constraintNcost(after_cross,matrix,col_cost);
        %print(cross_cost,after_cross,cross_constraint,'cross');
        
        % Mutation
        after_mutation = mutation(after_cross);
        [mutation_constraint,mutation_cost] = constraintNcost(after_mutation,matrix,col_cost);
        %print(mutation_cost,after_mutation,mutation_constraint,'mutation');
        
        % Heuristic improvement
        after_improve = improveOperator(after_mutation,matrix,col_cost);
        [improve_constraint,improve_cost] = constraintNcost(after_improve,matrix,col_cost);
        %print(improve_cost,after_improve,improve_constraint,'improve');
    
        % Save offsprings as a list
        if (parents_loop_count ~= 1)     
            i = 1;
            while(ismember(after_improve,offspringF_list,'rows'))
                %offspringVio_list
                zeroVio = find(totalVio_list == 0);
                while(i <= length(zeroVio))
                    parent1 = totalF_list(zeroVio(i),:);
                    j = 2;
                    while(j <= length(zeroVio))
                        parent2 = totalF_list(zeroVio(j),:);
                        j = j+1;
                    end
                    %parent2 = totalF_list(ceil(rand*length(totalCost_list)),:);
                    i = i+1;
                end
                if(i >= length(zeroVio))
                   parent1 = totalF_list(ceil(rand*length(totalCost_list)),:);
                   parent2 = totalF_list(ceil(rand*length(totalCost_list)),:);
                   while(parent1 == parent2)% make sure two selected parents are different
                       parent2 = totalF_list(ceil(rand*length(totalCost_list)),:);              
                   end
                end
                after_cross = crossover(parent1,parent2,'nPoint');
                [cross_constraint,cross_cost] = constraintNcost(after_cross,matrix,col_cost);                % Mutation
                after_mutation = mutation(after_cross);
                [mutation_constraint,mutation_cost] = constraintNcost(after_mutation,matrix,col_cost);                % Heuristic improvement
                after_improve = improveOperator(after_mutation,matrix,col_cost);
                [improve_constraint,improve_cost] = constraintNcost(after_improve,matrix,col_cost);
            end
        end
        offspringF_list = [offspringF_list;after_improve];
        offspringCost_list = [offspringCost_list improve_cost];
        offspringVio_list = [offspringVio_list improve_constraint];
        parents_loop_count = parents_loop_count+1;
    end
    
    
    % Stochastic Ranking
    totalF_list = [totalF_list;offspringF_list];
    totalCost_list = [totalCost_list offspringCost_list];
    totalVio_list = [totalVio_list offspringVio_list];
    [rankedIndiv,rankedCost,rankedVio] = stochasticRanking(totalF_list,totalCost_list,totalVio_list);
    
    totalF_list = rankedIndiv(1:individuals,:);% take first 100 indivs
    totalCost_list = rankedCost(1:individuals);
    totalVio_list = rankedVio(1:individuals);

    
%     nonzero_vio = find(rankedVio ~= 0);
%     if(isempty(nonzero_vio))
%         if (improve_cost < rankedCost(end))
%             rankedIndiv(end,:) = after_improve;
%             totalF_list = rankedIndiv;
%             rankedCost(end) = improve_cost;
%             totalCost_list = rankedCost;
%             rankedVio(end) = improve_constraint;
%             totalVio_list = rankedVio;
%         end
%     else
%         if(gen_loop_count == 1)
%             kill_index = nonzero_vio(end);
%             rankedIndiv(kill_index,:) = after_improve;
%             totalF_list = rankedIndiv;
%             rankedCost(kill_index) = improve_cost;
%             totalCost_list = rankedCost;
%             rankedVio(kill_index) = improve_constraint;
%             totalVio_list = rankedVio;
%         else
%             if ~ismember(improve_cost,rankedCost)
%                 kill_index = nonzero_vio(end);
%                 rankedIndiv(kill_index,:) = after_improve;
%                 totalF_list = rankedIndiv;
%                 rankedCost(kill_index) = improve_cost;
%                 totalCost_list = rankedCost;
%                 rankedVio(kill_index) = improve_constraint;
%                 totalVio_list = rankedVio;
%             end
%         end
%     end
%     last_improveCost = improve_cost;
    disp(['Generation: ',num2str(gen_loop_count)]);
    feasible_positions = find(totalVio_list == 0);
    
    if(~isempty(feasible_positions))
        loop_findBest_count = 1;
        while(loop_findBest_count <= length(feasible_positions))
           temp = totalCost_list(feasible_positions(loop_findBest_count));
           if(loop_findBest_count == 1)
              bestResult =  temp;
           else
              if(temp < bestResult) 
                  bestResult = temp;
              end
           end
           loop_findBest_count = loop_findBest_count+1;
        end
        %bestCost = totalCost_list(feasible_positions(1));
        disp(['Best Result: ',num2str(bestResult)]);
    else
        disp(['Best Result: wait for the next generation.']);
        reminder_counter = reminder_counter + 1;
        if(reminder_counter > 4)
            disp(['Tips: The probability of this happening is extremely low, you can try to restart if you want.']);
            reminder_counter = 1;
        end
    end
    
    gen_loop_count = gen_loop_count + 1;
end

%unique(rankedCost)
%rankedVio
