function print(cost,solution,constraint,mode)
    switch mode
        case 'initial'
            disp('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
            disp(['The cost after pseudo-random initialisation is: ', num2str(cost)]);
            disp(['The sum of violations of the constraints is: ', num2str(constraint)]);
            disp(['The index of solution is: ', num2str(find(solution==1))]);
            disp(['The solution after the pseudo-random initialisation is: ', num2str(solution)]);
        case 'mutation'
            disp('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
            disp(['The cost after mutation is: ', num2str(cost)]);
            disp(['The sum of violations of the constraints is: ', num2str(constraint)]);
            disp(['The index of solution is: ', num2str(find(solution==1))]);
            disp(['The solution after mutation algorithm is:               ', num2str(solution)]);
        case 'cross'
            disp('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
            disp(['The cost after crossover is: ', num2str(cost)]);
            disp(['The sum of violations of the constraints is: ', num2str(constraint)]);
            disp(['The index of solution is: ', num2str(find(solution==1))]);
            disp(['The solution after crossover algorithm is:              ', num2str(solution)]); 
        case 'improve'
            disp('----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------');
            disp(['The cost after huristic improvement is: ', num2str(cost)]);
            disp(['The sum of violations of the constraints is: ', num2str(constraint)]);
            disp(['The index of solution is: ', num2str(find(solution==1))]);
            disp(['The solution after huristic improvement algorithm is:   ', num2str(solution)]); 
   
    end
end