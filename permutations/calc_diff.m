
function diff = calc_diff(vols_active,vols_passive)
% vols "active" and "passive" are how the volumes are labelled in
% the permutation. 
% vols_active and vols_passive are nx2 vectors

% pre-allocate
cvs_active = zeros(length(vols_active), 1);
cvs_passive = zeros(length(vols_passive), 1);

% calculate coefficients of variation
for i = 1:length(vols_active)-1
    a_vo1ume_one = vols_active(i,1);
    a_volume_two = vols_active(i, 2);
    a_cv_sub = calc_cv(a_vo1ume_one, a_volume_two);
    cvs_active(i) = a_cv_sub;

    p_vo1ume_one = vols_passive(i, 1);
    p_volume_two = vols_passive(i, 2);
    p_cv_sub = calc_cv(p_vo1ume_one, p_volume_two);
    cvs_passive(i) = p_cv_sub;
end

% calculate RMS average of CVs
CV_active = rms(cvs_active);
CV_passive = rms(cvs_passive);

% Just double-checking
% n_subs = length(vols_active);
% CV_active2 = sqrt(sum(cvs_active.^2)/n_subs);

diff = CV_passive - CV_active;

