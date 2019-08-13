function mutated = mutation(F)
    length_solution = length(F);
    % Set mutation rate here. (1/length : 1/2 is recommended)
    prob_mutation = 1/length_solution;
    loop_count = 1;
    while(loop_count <= length_solution)
        current_value = F(1,loop_count);
        % should we mutate it?
        if rand <= prob_mutation
            if(current_value == 1)
                F(1,loop_count) = 0;
            elseif(current_value == 0)
                F(1,loop_count) = 1;
            end
        end
        loop_count = loop_count+1;
    end
    mutated = F;
end