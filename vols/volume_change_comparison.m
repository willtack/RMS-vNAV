%
% Comparing % volume change between active scans vs passive scans
%
% Using Wilcoxon signed rank test to test significance. 
%
% April 8th, 2020
%

load('volume_change_comparison.mat')

% combined hemispheres
diff_caudate = active_caudate - passive_caudate;
diff_pallidum = active_pallidum - passive_pallidum;
diff_putamen = active_putamen - passive_putamen;
diff_accumbens = active_accumbens - passive_accumbens;
diff_cortex = active_cortex - passive_cortex;

matrix = [diff_caudate; diff_pallidum; diff_putamen; diff_accumbens; diff_cortex]';
labels = ['caudate  '; 'pallidum '; 'putamen  '; 'accumbens'; 'cortex   '];

figure(1)
boxplot(matrix, labels)
title("Volume Change Comparison (active vs passive)")
ylabel("Active scans' % volume change - passive scans' % volume change")


% separate hemispheres
diff_caudate_left = active_caudate_left - passive_caudate_left;
diff_caudate_right = active_caudate_right - passive_caudate_right;
diff_pallidum_left = active_pallidum_left - passive_pallidum_left;
diff_pallidum_right = active_pallidum_right - passive_pallidum_right;
diff_putamen_left = active_putamen_left - passive_putamen_left;
diff_putamen_right = active_putamen_right - passive_putamen_right;
diff_accumbens_left = active_accumbens_left - passive_accumbens_left;
diff_accumbens_right = active_accumbens_right - passive_accumbens_right;

separate_matrix = [diff_caudate_left; diff_pallidum_left; diff_putamen_left; diff_accumbens_left;
                   diff_caudate_right; diff_pallidum_right; diff_putamen_right; diff_accumbens_right; diff_cortex]';
               
separate_labels = ['left caudate   '; 'left pallidum  '; 'left putamen   '; 'left accumbens ';
                   'right caudate  '; 'right pallidum '; ' right putamen '; 'right accumbens'; 'cortex         '];
               
figure(2)            
boxplot(separate_matrix, separate_labels) 
title("Volume Change Comparison (active vs passive)")
ylabel("Active scans' % volume change - passive scans' % volume change")


%%% Wilcoxon Signed Rank test
active_matrix = [active_caudate; active_pallidum; active_putamen; active_accumbens;
                 active_caudate_left; active_pallidum_left; active_putamen_left;
                 active_accumbens_left; active_caudate_right; active_pallidum_right;
                 active_putamen_right; active_accumbens_right; active_cortex];
passive_matrix = [passive_caudate; passive_pallidum; passive_putamen; passive_accumbens;
                 passive_caudate_left; passive_pallidum_left; passive_putamen_left;
                 passive_accumbens_left; passive_caudate_right; passive_pallidum_right;
                 passive_putamen_right; passive_accumbens_right; passive_cortex];
             
height = size(active_matrix,1);
p = zeros(height,1);

for i = 1:height
    active_vector = active_matrix(i, :);
    passive_vector = passive_matrix(i, :);
    p(i)=signrank(active_vector, passive_vector);
end

ROIName = {'Caudate'; 'Pallidum'; 'Putamen'; 'Accumbens'; 'Left Caudate'; 'Left Pallidum';
           'Left Putamen'; 'Left Accumbens'; 'Right Caudate'; 'Right Pallidum'; 'Right Putamen';
           'Right Accumbens'; 'Cortex'};

T = table(ROIName, p);


