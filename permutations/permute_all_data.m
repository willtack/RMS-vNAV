imax=6^10-1;
n_permutations=5000;
load('subjects.mat')

% generate 5000 pseudorandom integers
X = randi(imax,[n_permutations,1]); 

for i = 1:length(X)
   % convert each integer to base 6
   integer=X(i,1);
   hexi_int = dec2base(integer,6);
   hexi_int = sprintf('%010s', hexi_int); % pad to 10 places
   % each digit of hexi_int encodes one of 6 permutations for a subject
   results = zeros(length(subjects),1);
   for j=1:length(subjects)
       diff_matrix = permute_vols(subjects(j), vols_vector);
       permut_idx = hexi_int(j); % the specified permutation for the current subject
       results(j) = diff_matrix(permut_idx);
   end
end
