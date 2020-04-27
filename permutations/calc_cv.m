function cv = calc_cv(vol1, vol2)
    cv = 2 * ( sqrt(( (vol1-vol2)^2 )/2)/(vol1 + vol2));
end
