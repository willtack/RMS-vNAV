% for a given subject
% for a given region
% where V is a 4x1 vector of volume measurements

function diff_matrix = permute_vols(V)

% permute, get 6x2 matrix,
% each row a combination of 2 items chosen from V
C = nchoosek(V, 2);

% To calculate the coefficient of variance, we need two values for each
% label... So every permutation should have four values.

% nchoosek gives us a 6x2 matrix where each row is a combination of 
% 2 items chosen from V. That is the correct number of permutations.
% We just need to append the other 2 numbers to complete the quadruplet.

% extend the matrix
E = zeros(length(C),2);
C_extens = [C E];

% initialize diff matrix
diff_matrix = zeros(length(C_extens),1);

% loop thru rows and grab items in V that aren't already in that row
for i = 1:length(C_extens)
    set = C(i,:);
    AllVals = V';
    p = ismember(AllVals, set);
    Remainder = AllVals(~p);
    C_extens(i,3:4) = Remainder;
    % now we calc diff for every row in C_extens
    diff = calc_diff(C_extens(i,1:2),C_extens(i,3:4));
    diff_matrix(i) = diff;
end

