function [deviation,average] = SA(loop_num)
% SET ITERATION OF OUTTER LOOP
loop_num = 30;
% read ulysses22
function city_position = Read(fileName)
    fid = fopen(fileName,'rt');
    location=[];
    A = [1 2];
    textline = fgetl(fid);
    while ischar(textline)
        if(strcmp(textline,'NODE_COORD_SECTION'))
            while ~isempty(A)
                A=fscanf(fid,'%f',[3,1]);
                if isempty(A)
                    break;
                end
                location=[location;A(2:3)'];
            end
        end
        textline = fgetl(fid);%this is catago in that file 
        if strcmp(textline,'EOF')
            break;
        end
    end
    city_position=location;
    fclose(fid);
end


% calculate the total distance of a list of cities
function d = distance(list)
    cityNum = 1;
    totalDistance = 0;
    while(cityNum < size(list,1)+1)
        degX = fix(list(cityNum,1));
        minX = list(cityNum,1) - degX; % get minute of nearest int
        latitude = pi * (degX + 5.0 * minX / 3.0) / 180.0;
        degY = fix(list(cityNum,2));
        minY = list(cityNum,2) - degY;
        longtitude = pi * (degY + 5.0 * minY /3.0) / 180.0;

        RRR = 6378.388;

        if cityNum ~= 1 % compare current coord to last coord
            q1 = cos(longtitude - prev_longtitude);
            q2 = cos(latitude - prev_latitude);
            q3 = cos(latitude + prev_latitude);
            distance = fix(RRR * acos(0.5*((1.0+q1)*q2 - (1.0-q1)*q3)) + 1.0);
            totalDistance = totalDistance + distance;
            d = totalDistance;
        end
        prev_latitude = latitude;
        prev_longtitude = longtitude;
        cityNum = cityNum + 1;
    end
end

% 2-opt route for once
function [ans_route,list_order] = opt2(list)
    % two rand ints
    randi1 = randi([2,21]);
    randi2 = randi([randi1,22]);
    
    % split the list as 3 parts, reverse the 2nd part
    list_order = [1:randi1-1 fliplr(randi1:randi2) randi2+1:22];
    
    ans_route_22 = list(list_order,:);
    % add first start point
    ans_route = [ans_route_22;list(1,:)];
end

std_list = [];
avg_list = [];
i = 2000;
loop = 1;
while(loop <= loop_num)
    city_position = Read('ulysses22.tsp');
    a = city_position(1,:); % start city
    solution = 20000;
    distance_sa = 20000;
    loop_count = 0;
    best_route_to_plot = city_position;
    avg_distance = 0;
    realTime_distance_list=[];
    sa_dynamic_distance_list=[];
    sa_best_distance_list=[];
    std_1000 = 0;
    sa_counter = 1;
    temp = 1500;
    cities = [city_position;a];
    size(cities)
    %while(loop_count < 2000)
    while(loop_count < i)
        temp = temp * 0.995;
        
        % 2-opt the city list
        [opted_cityList,~] = opt2(city_position);
        
        % calculate the distance of city list
        distance_cityList = distance(opted_cityList);
        
        % Simulated Annealing
        if distance_cityList < solution % if new solution better than current solution.
            city_position = opted_cityList(1:22,:); % put 2-opted list into city_position to recurse
            solution = distance_cityList; % save this solution as new best
            best_route_to_plot = city_position; % record the best solution's order
        else
            % if new solution is worse
            % probability of jump to another point
            prob2jumpOut = exp((solution - distance_cityList)/temp);
            % should we move to it? Yes!
            if rand < prob2jumpOut
                % jump out from local maximum
                city_position = opted_cityList;
                % distance of jumped-out-point
                distance_sa = distance(city_position);
            end
            % if new route is shorter than jumped-out-point
            if distance_cityList <= distance_sa
               % save this route to recurse
               city_position = opted_cityList(1:22,:);
               distance_sa = distance_cityList;
            end
        end
        
        % average result in small iterations.
        avg_distance = (avg_distance + distance_cityList);

        % distance list of small iterations.
        realTime_distance_list = [realTime_distance_list distance_cityList];
        sa_dynamic_distance_list = [sa_dynamic_distance_list distance([city_position;a])];
        sa_best_distance_list = [sa_best_distance_list solution];
         % loop graph ploting
         figure(3)
         plot_city_position = [city_position;a];
         %plot_city_position = [opted_cityList;a];
         plot(plot_city_position(:,1),plot_city_position(:,2),'o-','LineWidth',2,'MarkerFaceColor','y');
         title('The Best Solution');
         text(33.1,-7,['The Shortest Distance: ', num2str(solution),'; Iteration: ',num2str(loop_count)]);
         text(33.1,-8.5,['The average distance: ', num2str(fix(avg_distance/(loop_count+1))), '; Current Distance: ', num2str(distance([city_position;a]))]);
         pause(0.01);
         loop_count = loop_count + 1;

    end
    
    % plot average best results of 30 iterations
    figure(10);
    if loop == 1
        avg_dynamic_distance_list = sa_best_distance_list;
        plot(avg_dynamic_distance_list, '-','LineWidth',2);
        title('SA Average Result of 30 Independent Runs');
    elseif loop > 1
    avg_dynamic_distance_list = mean([avg_dynamic_distance_list; [sa_best_distance_list]]);
    plot(avg_dynamic_distance_list, '-','LineWidth',2);
    title('SA Average Result of 30 Independent Runs');
    end
    
    % standard deviation calculation & save
    std_list = [std_list solution];
    avg_list = [avg_list fix(avg_distance/(loop_count+1))];
    
    if loop == loop_num-1
        std_list;
        deviation = std(std_list)
        average = mean(std_list)
%         figure(9);
%         avg_dynamic_distance_list = avg_dynamic_distance_list/(loop);
%         plot(avg_dynamic_distance_list, '-');
    end
    % plot costs in 30th iteration
    figure(4);
    plot(realTime_distance_list,'-');
    title('2-OPT Real Time Distance Figure');
    
    figure(5);
    plot(sa_dynamic_distance_list, '-');
    title('Simulated Annealing Dynamic Distance Figure');
    
    
    disp(['Loop Number: ', num2str(loop), '; Shortest Distance: ', num2str(solution)]);
    loop = loop + 1;
    
end

% The best result
figure(6);
best_route_to_plot = [best_route_to_plot;a];
plot(best_route_to_plot(:,1),best_route_to_plot(:,2),'o-','LineWidth',2,'MarkerFaceColor','y');
title('The Best Solution');
text(33.1,-7,['The Shortest Distance: ', num2str(solution),' Iteration: ',num2str(loop_count)]);
text(33.1,-8.5,['The Average Distance: ', num2str(fix(avg_distance/(loop_count+1)))]);
%function
end