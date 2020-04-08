gunzip *.nii.gz
series=$(cat series)
# square
for x in ./*.nii; do
  name=$(basename -s .nii $x)
  fslmaths $x -sqr ${name}_sqr.nii
done

# sum
e1=$(find -type f | grep e1_sqr)
e2=$(find -type f | grep e2_sqr)
e3=$(find -type f | grep e3_sqr)
e4=$(find -type f | grep e4_sqr)

fslmaths $e1 -add $e2 -add $e3 -add $e3 sum_squares.nii

# mean
fslmaths sum_squares.nii -div 4 mean_square.nii

# root
fslmaths mean_square.nii -sqrt rms.nii

mv rms.nii.gz rms_series"${series}".nii.gz
