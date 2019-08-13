function [deviation,average] = TABU(loop_num)
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
    [m,n]=size(location);
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

    list_order = [1:randi1-1 fliplr(randi1:randi2) randi2+1:22];
    
    
    % split the list as 3 parts
    % city1ToCityi = list(1:randi1-1,:);
    % cityiToCityj = list(randi1:randi2,:);
    % cityjToCityEnd = list(randi2+1:end,:);

    %reverse route between city i to city j
    %ans_route = [city1ToCityi;flipud(cityiToCityj);cityjToCityEnd;list(1,:)];
    ans_route_22 = list(list_order,:);
    % add first start point
    ans_route = [ans_route_22;list(1,:)];
end

% tabu search tabu(city_list, required tabu list length, last tabu list)
function [opted_List,tabu_list_out] = tabu(city_list,required_length,tabu_list_in)
    [opted_List,opted_order] = opt2(city_list);
    tabu_list_out = [tabu_list_in; opted_order];
    
    if ~isempty(tabu_list_in)
        tabu_counter = 0;
        while ismember(opted_order,tabu_list_in,'rows')
            tabu_counter;
            [opted_List,opted_order] = opt2(city_list);
            tabu_list_out = [tabu_list_in; opted_order];
            tabu_counter = tabu_counter+1;
        end
    end

    % if row of tabu_list is more than required length
    if size(tabu_list_out,1) >= required_length+1
        % delete oldest row
        tabu_list_out = tabu_list_out(2:required_length+1,:);
    end  
end
std_list = [];
avg_list = [];
i = 2000; % SET ITERATION of INNER LOOP
loop = 1;
while(loop < loop_num+1)
    city_position = Read('ulysses22.tsp');
    a = city_position(1,:); % start city
    solution = 20000;
    loop_count = 0;
    best_route_to_plot = city_position;
    avg_distance = 0;
    realTime_distance_list=[];
    tb_dynamic_distance_list=[];
    sa_best_distance_list=[];
    temp = 100;
    %tabu_list = [];
    cities = [city_position;a];
    size(cities)
    %while(loop_count < 2000)
    while(loop_count < i)
        temp = temp * 0.999;
        
        % Tabu Search with 2-opt
        %[opted_cityList,list_order] = opt2(city_position);
        if loop_count == 0
            [opted_cityList,tabu_list] = tabu(city_position,20,[]);
        else
            [opted_cityList,tabu_list] = tabu(city_position,20,tabu_list);
            tabu_list;
        end
        
        % calculate the distance of city list
        distance_cityList = distance(opted_cityList);
       
        if distance_cityList <= solution % if new solution better than current solution.
             city_position = opted_cityList(1:22,:); % put this list into city_position to recurse
             solution = distance_cityList; % save this solution as new best
             best_route_to_plot = city_position; % record the best solution's order
         
        end

        % average result of 2000 iterations.
        avg_distance = (avg_distance + distance_cityList);

        % distance list of 2000 iterations.
        realTime_distance_list = [realTime_distance_list distance_cityList];
        tb_dynamic_distance_list = [tb_dynamic_distance_list distance([city_position;a])];
         % loop graph ploting
         figure(3)
         plot_city_position = [city_position;a];
         %plot_city_position = [opted_cityList;a];
         plot(plot_city_position(:,1),plot_city_position(:,2),'o-','LineWidth',2,'MarkerFaceColor','y');
         title('The Best Solution');
         text(33.1,-7,['The Shortest Distance: ', num2str(solution),'; Iteration: ',num2str(loop_count)]);
         text(33.1,-8.5,['The average distance: ', num2str(fix(avg_distance/(loop_count+1))), '; Current Distance: ', num2str(distance([city_position;a]))]);
         
         sa_best_distance_list = [sa_best_distance_list solution];
         pause(0.01);
         loop_count = loop_count + 1;

    end
    
    % plot average best results of 30 iterations
    figure(9);
    if loop == 1
        avg_dynamic_distance_list = sa_best_distance_list;
        plot(avg_dynamic_distance_list, '-','LineWidth',2);
        title('Average Result of 30 Independent Runs');
    elseif loop > 1
    avg_dynamic_distance_list = mean([avg_dynamic_distance_list; [sa_best_distance_list]]);
    plot(avg_dynamic_distance_list, '-','LineWidth',2);
    title('Average Result of 30 Independent Runs');
    end
    
    % standard deviation calculation & save
    
    std_list = [std_list solution];
    avg_list = [avg_list fix(avg_distance/(loop_count+1))];

    if loop == loop_num-1
        std_list
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
    plot(tb_dynamic_distance_list, '-');
    title('Tabu Search Result Dynamic Distance Figure');
    
    
    if loop == loop_num-1
        std_list
        deviation = std(std_list)
        average = mean(std_list)        
    end
    
    
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