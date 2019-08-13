function crossovered = crossover(sol1,sol2,mode)
    length_sol = length(sol1);
    
    switch mode
        case 'onePoint'
            cut_point = 1+round(rand*(length_sol-1));%produce rand num 1-(length-1)
            part1 = sol1(1:cut_point-1);
            part2 = sol2(cut_point:length_sol);
            crossovered = [part1 part2];
            length(crossovered);
        
        case 'nPoint'
            %n = 1+round((rand*length_sol)/10);
            n = 10;
            unsorted_points = randperm(length_sol-1,n);
            cut_points = sort(unsorted_points);
            loop_count = 1;
            first_point = 1;
            sol = [];
            while(loop_count <= n)
                if loop_count == n % if this is the last loop
                    sol = [sol sol1(first_point:length_sol)];
                elseif mod(loop_count,2) == 0 % even number of loop
                    second_point = cut_points(loop_count);
                    sol = [sol sol2(first_point:second_point-1)];
                    first_point = second_point;
                else % odd number of loop
                    second_point = cut_points(loop_count);
                    sol = [sol sol1(first_point:second_point-1)];
                    first_point = second_point;
                end
                loop_count = loop_count+1;
            end
            crossovered = sol;
            length(crossovered);
        
        case 'uniform'
            n = 10;
            unsorted_points = randperm(length_sol-1,n);
            cross_points = sort(unsorted_points);
            loop_count = 1;
            first_point = 1;
            sol = [];
            while(loop_count <= n)
                if loop_count == n
                    sol = [sol sol1(first_point:length_sol)];
                else
                    second_point = cross_points(loop_count);
                    sol = [sol sol1(first_point:second_point-1)];
                    sol = [sol sol2(second_point)];
                    first_point = second_point+1;
                end
                loop_count = loop_count+1;
            end
            crossovered = sol;
            length(crossovered);
    end
            
end