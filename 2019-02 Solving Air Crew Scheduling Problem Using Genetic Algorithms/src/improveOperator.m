function improved_sol = improveOperator(F,matrix,col_cost)
    [row_num,col_num] = size(matrix);
    % Generate current solution matrix
    sol_matrix = [];
    fill_loop_count = 1;
    while(fill_loop_count <= col_num)
        if(F(fill_loop_count) == 0)
            sol_matrix = [sol_matrix zeros(row_num,1)];
        elseif(F(fill_loop_count) == 1)
            sol_matrix = [sol_matrix matrix(:,fill_loop_count)];
        end
        
        fill_loop_count = fill_loop_count + 1;
    end
    
    
    % DROP procedure: identify over-covered rows
    function output_overcovered = findOvercovered(sol_matrix)
        [row_num2,col_num2] = size(sol_matrix);
        drop_loop_count = 1;
        overcovered_rows = [];
        while(drop_loop_count <= row_num2)
            getRow = sol_matrix(drop_loop_count,:);
            covered_position = find(getRow == 1);
            if(length(covered_position) > 1) %if covered cols more than 1
                overcovered_rows = [overcovered_rows drop_loop_count];
            end
            drop_loop_count = drop_loop_count + 1;
        end
        output_overcovered = overcovered_rows;
    end
    sol_matrix;
    
    % DROP procedure: Randomly drop until no over-covered rows
    drop_loop = 1;
    while(~isempty(findOvercovered(sol_matrix)))
        
        overcovered = findOvercovered(sol_matrix);
        if (drop_loop > length(overcovered))
            drop_loop = 1;
        end
        overcovered_row_num = overcovered(drop_loop); % get a row
        locate_row = sol_matrix(overcovered_row_num,:); % locate this row
        repeat_cols = find(locate_row == 1); % find repeat columns in this row
        repeat_length = length(repeat_cols); % how many times of repeat?
        rand_col = ceil(rand*repeat_length); % rand a col to drop?
        row_should_drop = repeat_cols(rand_col); % apply this rand to get col num
        sol_matrix(:,row_should_drop) = zeros(row_num,1); % drop this col
        drop_loop = drop_loop+1;
    end
    
    [~,after_drop] = find(sol_matrix==1);
    after_drop = after_drop';
    after_drop = unique(after_drop);
    
    % ADD procedure: identify under-covered rows
    function output_undercovered = findUndercovered(sol_matrix)
        [row_num3,col_num3] = size(sol_matrix);
        add_loop_count = 1;
        undercovered_rows = [];
        while(add_loop_count <= row_num3)
            getRow = sol_matrix(add_loop_count,:);
            covered_position = find(getRow == 1);
            if(length(covered_position) == 0) %if this row is uncovered
                undercovered_rows = [undercovered_rows add_loop_count];
            end
            add_loop_count = add_loop_count + 1;
        end
        output_undercovered = undercovered_rows;
    end
    sol_matrix;
    
    % ADD procedure: add cols as much as possible without causing over-covered.
    function safe_cols = safeCols(sol_matrix,original_matrix)
        [row_num4,col_num4] = size(sol_matrix);
        [covered_rows,~] = find(sol_matrix==1);
        covered_rows = covered_rows';
        covered_rows = sort(covered_rows);
        safe_col_list = [];
        safe_col_loop = 1;
        while(safe_col_loop <= col_num4)
            getCol = original_matrix(:,safe_col_loop);
            coveredRows = find(getCol == 1);
            coveredRows = coveredRows';
            if (~ismember(coveredRows,covered_rows))
                safe_col_list = [safe_col_list safe_col_loop];
            end
            safe_col_loop = safe_col_loop+1;
        end
        safe_cols = safe_col_list;
    end

    add_loop = 1;
    while(~isempty(findUndercovered(sol_matrix)))
        uncovered_rows = findUndercovered(sol_matrix);
        % Randomly select one uncovered row
        if(length(uncovered_rows)==1)%if this is last row
            selected_row = uncovered_rows;
        else
            selected_row = uncovered_rows(ceil(rand*length(uncovered_rows)));
        end
        safe_cols = safeCols(sol_matrix,matrix);
        best_col_loop = 1;
        best_col = 0;
        test = 0;
        best_col_value = 100000;
        while(best_col_loop <= length(safe_cols))
            thisCol = safe_cols(best_col_loop);
            % Check how many rows this col contains.
            col_howLong = length(find(matrix(:,thisCol)==1));
            % Check cost of this col
            col_howCost = col_cost(thisCol);
            col_howGood = col_howCost/col_howLong;
            if(col_howGood < best_col_value)
                best_col_value = col_howGood;
                best_col = thisCol;
            end
            best_col_loop = best_col_loop + 1;
        end
        
        if(best_col == 0) % if cannot find anymore best col
            %disp('no best');
            break
        end
        sol_matrix(:,best_col) = matrix(:,best_col);

        add_loop = add_loop+1;
    end
    [~,after_add] = find(sol_matrix==1);
    after_add = after_add';
    after_add = unique(after_add);
    %findUndercovered(sol_matrix);
    % after_add is index numbers, trans it to 01010 format
    trans_loop = 1;
    after_add_binaryFormat = [];
    while(trans_loop <= col_num)
        if(ismember(trans_loop,after_add))
            after_add_binaryFormat = [after_add_binaryFormat 1];
        else
            after_add_binaryFormat = [after_add_binaryFormat 0];
        end
        trans_loop = trans_loop + 1;
    end
    
    improved_sol = after_add_binaryFormat;
    
    %disp(num2str(find(F==1)));
end