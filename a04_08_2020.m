% combined hemispheres
active_caudate = [0.04	0.06	0.02	0.02	0.01	0.01	0.00	0.04	0.02	0.01];
passive_caudate = [0.04	0.02	0.01	0.02	0.01	0.00	0.08	0.09	0.01	0.00];
diff_caudate = active_caudate - passive_caudate;

active_pallidum = [0.01	0.03	0.02	0.07	0.01	0.02	0.00	0.00	0.00	0.01];
passive_pallidum = [0.00	0.01	0.00	0.00	0.02	0.06	0.05	0.05	0.05	0.02];
diff_pallidum = active_pallidum - passive_pallidum;

active_putamen = [0.01	0.01	0.00	0.05	0.01	0.00	0.03	0.01	0.01	0.00];
passive_putamen = [0.01	0.06	0.00	0.08	0.00	0.00	0.02	0.02	0.03	0.02];
diff_putamen = active_putamen - passive_putamen;

active_accumbens = [0.07	0.07	0.06	0.07	0.10	0.07	0.02	0.02	0.08	0.10];
passive_accumbens = [0.02	0.04	0.01	0.14	0.02	0.05	0.14	0.08	0.03	0.05];
diff_accumbens = active_accumbens - passive_accumbens;

matrix = [diff_caudate;diff_pallidum;diff_putamen; diff_accumbens]';
labels = ['caudate  '; 'pallidum '; 'putamen  '; 'accumbens'];

%boxplot(matrix, labels)


% separate hemispheres
active_caudate_left =  [1.40     6.39	2.53	3.47	1.14	1.70	0.13	0.01	1.89	0.47];
passive_caudate_left = [0.64	2.70	1.73	2.20	0.16	0.05	5.36	2.85	1.43	0.25];
diff_caudate_left = active_caudate_left - passive_caudate_left;
active_caudate_right =  [8.40	6.48	0.81	1.52	0.79	0.57	0.42	7.04	1.38	0.87];
passive_caudate_right = [5.74	1.80	0.26	1.37	1.96	0.62	10.41	12.71	0.12	0.60];
diff_caudate_right = active_caudate_right - passive_caudate_right;

active_pallidum_left = [2.14	2.32	2.28	4.42	0.45	1.82	1.20	1.11	0.53	0.41];
passive_pallidum_left = [3.54	0.91	1.16	1.49	3.79	6.46	3.14	3.86	1.80	3.11];
diff_pallidum_left = active_pallidum_left - passive_pallidum_left;
active_pallidum_right = [0.42	4.35	1.81	8.89	2.10	2.86	1.46	0.20	0.40	2.69];
passive_pallidum_right = [3.62	1.70	1.48	1.82	1.12	4.69	12.11	6.23	8.03	0.62];
diff_pallidum_right = active_pallidum_right - passive_pallidum_right;

active_putamen_left = [2.25	0.73	0.04	0.13	0.09	0.00	3.72	1.00	1.17	1.37];
passive_putamen_left = [ 0.81	8.97	0.30	6.79	0.10	0.80	1.48	3.35	2.95	3.65];
diff_putamen_left = active_putamen_left - passive_putamen_left;
active_putamen_right = [0.03	0.38	0.67	11.19	2.62	0.10	1.38	3.57	0.20	0.64];
passive_putamen_right = [3.35	2.71	1.20	8.75	0.22	1.42	6.39	7.21	3.92	1.15];
diff_putamen_right = active_putamen_right - passive_putamen_right;

active_accumbens_left = [0.28	19.84	5.76	8.48	16.61	9.44	0.24	1.06	19.89	21.00];
passive_accumbens_left = [4.44	9.38	2.54	16.49	2.85	7.25	15.18	4.24	2.52	4.86];
diff_accumbens_left = active_accumbens_left - passive_accumbens_left;
active_accumbens_right = [12.29	2.87	5.77	6.80	5.96	4.96	3.82	3.41	0.06	3.19];
passive_accumbens_right = [1.12	12.89	4.46	11.81	1.75	2.98	13.37	16.05	3.07	4.81];
diff_accumbens_right = active_accumbens_right - passive_accumbens_right;

combined_matrix = [diff_caudate_left; diff_pallidum_left; diff_putamen_left; diff_accumbens_left;
                   diff_caudate_right; diff_pallidum_right; diff_putamen_right; diff_accumbens_right]';
               
combined_labels = ['caudate  left  '; 'pallidum left  '; 'putamen  left  '; 'accumbens left ';
                   'caudate  right '; 'pallidum right '; 'putamen  right '; 'accumbens right'];
               
               
boxplot(combined_matrix, combined_labels)               
