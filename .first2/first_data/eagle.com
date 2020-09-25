/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 50 -o eagle-L_Accu_first -m /usr/local/fsl/data/first/models_336_bin/L_Accu_bin.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-L_Accu_first -o eagle-L_Accu_corr -i act12_15_t1 -b fast
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 40 -o eagle-L_Pall_first -m /usr/local/fsl/data/first/models_336_bin/05mm/L_Pall_05mm.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-L_Pall_first -o eagle-L_Pall_corr -i act12_15_t1 -b none
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 40 -o eagle-L_Puta_first -m /usr/local/fsl/data/first/models_336_bin/05mm/L_Puta_05mm.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-L_Puta_first -o eagle-L_Puta_corr -i act12_15_t1 -b none
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 40 -o eagle-L_Thal_first -m /usr/local/fsl/data/first/models_336_bin/05mm/L_Thal_05mm.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-L_Thal_first -o eagle-L_Thal_corr -i act12_15_t1 -b none
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 50 -o eagle-R_Accu_first -m /usr/local/fsl/data/first/models_336_bin/R_Accu_bin.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-R_Accu_first -o eagle-R_Accu_corr -i act12_15_t1 -b fast
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 30 -o eagle-R_Caud_first -m /usr/local/fsl/data/first/models_336_bin/intref_thal/R_Caud.bmv -intref /usr/local/fsl/data/first/models_336_bin/05mm/R_Thal_05mm.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-R_Caud_first -o eagle-R_Caud_corr -i act12_15_t1 -b fast
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 40 -o eagle-R_Pall_first -m /usr/local/fsl/data/first/models_336_bin/05mm/R_Pall_05mm.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-R_Pall_first -o eagle-R_Pall_corr -i act12_15_t1 -b none
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 40 -o eagle-R_Puta_first -m /usr/local/fsl/data/first/models_336_bin/05mm/R_Puta_05mm.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-R_Puta_first -o eagle-R_Puta_corr -i act12_15_t1 -b none
/usr/local/fsl/bin/run_first -i act12_15_t1 -t act12_15_t1_to_std_sub.mat -n 40 -o eagle-R_Thal_first -m /usr/local/fsl/data/first/models_336_bin/05mm/R_Thal_05mm.bmv; /usr/local/fsl/bin/first_boundary_corr -s eagle-R_Thal_first -o eagle-R_Thal_corr -i act12_15_t1 -b none