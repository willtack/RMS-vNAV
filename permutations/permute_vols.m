% for a given subject
% for a given region

% random volumes
V = [41; 42; 31; 400];

% permute, get 6x2 matrix,
% each row a combination of 2 items chosen from V
C = nchoosek(V, 2);

% calc_diff for c
% gdiff = calc_diff(c(:,1), c(:,2));

%%%% But wait, that won't work. To calculate the coefficient of variance,
%%%% we need two values for each label... So every permutation should have
%%%% four values.

%%%%%%%%%%%%%

% % Not sure if this is right...
% P = perms(V);
% 
% % Two columns are labelled "passive", two are labelled "active"
% 
% Active = P(:, 1:2);
% Passive = P(:, 3:4);
% 
% % Now calculate diff for each permutation:
% diff_mat = zeros(size(Active, 1), 1);
% for i = 1:size(Active, 1)
%     diff = calc_diff(Active(i,:), Passive(i,:));
%     diff_mat(i) = diff;
% end
% 
% diff_mat




% Okay, think I got it:

% So we have a 6x2 matrix where each row is a combination of 2 items chosen from V
% That is the correct number of permutations. We just need to append the
% other 2 numbers to complete the quadruplet.

% extend the matrix
E = zeros(6,2);

C_extens = [C E];

% now loop through the rows and grab the items in V that aren't already in that
% row

for i = 1:length(C_extens)
    set = C(i,:);
    AllVals = V';
    p = ismember(AllVals, set);
    Remainder = AllVals(~p);
    C_extens(i,3:4) = Remainder;
end

C_extens