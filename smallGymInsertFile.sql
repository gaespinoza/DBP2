delete from users;
delete from league;
delete from team;
delete from gymnast;
delete from lineup_slot;
delete from score;
delete from user_league;
delete from roster;
delete from matchup;
insert into users values ('00000001', 'Terese', 'toldcroft0@reddit.com', 'rzLKFk');
insert into users values ('00000002', 'Guillaume', 'ggouldsmith1@aboutads.info', 'znxmFN');
insert into users values ('00000003', 'Craig', 'ckersey2@whitehouse.gov', 'PbUUGTwv4ya');
insert into users values ('00000004', 'Thorndike', 'tthoma3@illinois.edu', 'qXoX80V');
insert into users values ('00000005', 'Dianna', 'dshevlane4@bbb.org', 'NXyPeW9vAW');
insert into users values ('00000006', 'Inglis', 'itroak5@state.tx.us', '6nHqzop6dEh7');
insert into league values ('00000001', '00000003', 'Hand-Giene E-2', 7, 5);
insert into league values ('00000002', '00000004', 'ATOMY SUNSCREEN', 7, 5);
insert into league values ('00000003', '00000002', 'Clonazepam', 7, 5);
insert into league values ('00000004', '00000005', 'Anticavity Fluoride', 7, 5);
insert into team values ('00000001', '00000001','00000001', 'VA Vegans', 10, 8);
insert into team values ('00000002', '00000002', '00000001', 'MD Mothers', 7, 1);
insert into team values ('00000003', '00000003', '00000001', 'VT Vets', 1, 3);
insert into team values ('00000004', '00000004', '00000001', 'TX Toasts', 10, 6);
insert into team values ('00000005', '00000005', '00000001', 'FL Flies', 10, 1);
insert into team values ('00000006', '00000006', '00000001', 'PA Pencils', 3, 1);
insert into team values ('00000007', '00000001','00000002', 'NH Hams', 10, 8);
insert into team values ('00000008', '00000002', '00000002', 'ND Faces', 7, 1);
insert into team values ('00000009', '00000003', '00000002', 'CA Commies', 1, 3);
insert into team values ('00000010', '00000004', '00000002', 'AL Aligators', 10, 6);
insert into team values ('00000011', '00000005', '00000002', 'UT Urns', 10, 1);
insert into team values ('00000012', '00000006', '00000002', 'NV Nattys', 3, 1);
insert into team values ('00000013', '00000001','00000003', 'WA Walruses', 10, 8);
insert into team values ('00000014', '00000002', '00000003', 'SD Sux', 7, 1);
insert into team values ('00000015', '00000003', '00000003', 'OR Pickers', 1, 3);
insert into team values ('00000016', '00000004', '00000003', 'GA Peaches', 10, 6);
insert into team values ('00000017', '00000005', '00000003', 'WI Cheese', 10, 1);
insert into team values ('00000018', '00000006', '00000003', 'MA Maams', 3, 1);
insert into team values ('00000019', '00000001','00000004', 'MI Mines', 10, 8);
insert into team values ('00000020', '00000002', '00000004', 'CT Cows', 7, 1);
insert into team values ('00000021', '00000003', '00000004', 'RI Roads', 1, 3);
insert into team values ('00000022', '00000004', '00000004', 'SC Seals', 10, 6);
insert into team values ('00000023', '00000005', '00000004', 'NC Nubs', 10, 1);
insert into team values ('00000024', '00000006', '00000004', 'TN Tins', 3, 1);
insert into gymnast values ('00000001', 'Lilian', 2022);
insert into gymnast values ('00000002', 'Alyosha', 2027);
insert into gymnast values ('00000003', 'Dulsea', 2025);
insert into gymnast values ('00000004', 'Ann-marie', 2021);
insert into gymnast values ('00000005', 'Cherri', 2025);
insert into gymnast values ('00000006', 'King', 2028);
insert into gymnast values ('00000007', 'Lester', 2027);
insert into gymnast values ('00000008', 'Philippa', 2022);
insert into gymnast values ('00000009', 'Karie', 2028);
insert into gymnast values ('00000010', 'Kara', 2021);
insert into gymnast values ('00000011', 'Maddy', 2028);
insert into gymnast values ('00000012', 'Emmalee', 2024);
insert into gymnast values ('00000013', 'Duffy', 2022);
insert into gymnast values ('00000014', 'Jacquie', 2028);
insert into gymnast values ('00000015', 'Felix', 2028);
insert into gymnast values ('00000016', 'Luce', 2021);
insert into gymnast values ('00000017', 'Marv', 2023);
insert into gymnast values ('00000018', 'Ivonne', 2029);
insert into gymnast values ('00000019', 'Bayard', 2025);
insert into gymnast values ('00000020', 'Zuzana', 2021);
insert into gymnast values ('00000021', 'Cornie', 2022);
insert into gymnast values ('00000022', 'Anabel', 2022);
insert into gymnast values ('00000023', 'Leyla', 2022);
insert into gymnast values ('00000024', 'Valentina', 2025);
insert into gymnast values ('00000025', 'Judas', 2029);
insert into gymnast values ('00000026', 'Calla', 2020);
insert into gymnast values ('00000027', 'Gram', 2026);
insert into gymnast values ('00000028', 'Janos', 2025);
insert into gymnast values ('00000029', 'Vivianne', 2029);
insert into gymnast values ('00000030', 'Rubia', 2028);
insert into gymnast values ('00000031', 'Gunner', 2025);
insert into gymnast values ('00000032', 'Rockey', 2021);
insert into gymnast values ('00000033', 'Dee dee', 2023);
insert into gymnast values ('00000034', 'Duncan', 2022);
insert into gymnast values ('00000035', 'Philippe', 2029);
insert into gymnast values ('00000036', 'Pearl', 2021);
insert into gymnast values ('00000037', 'Ciel', 2025);
insert into gymnast values ('00000038', 'Wright', 2020);
insert into gymnast values ('00000039', 'Sauncho', 2029);
insert into gymnast values ('00000040', 'Xerxes', 2020);
insert into lineup_slot values ('00000001', 'Vault', 1, '00000001');
insert into lineup_slot values ('00000001', 'Vault', 2, '00000002');
insert into lineup_slot values ('00000001', 'Vault', 3, '00000003');
insert into lineup_slot values ('00000001', 'Floor', 1, '00000002');
insert into lineup_slot values ('00000001', 'Floor', 2, '00000005');
insert into lineup_slot values ('00000002', 'Vault', 1, '00000004');
insert into lineup_slot values ('00000002', 'Vault', 2, '00000007');
insert into lineup_slot values ('00000002', 'Pommel Horse', 1, '00000006');
insert into lineup_slot values ('00000002', 'Rings', 1, '00000008');
insert into lineup_slot values ('00000002', 'Rings', 2, '00000006');
insert into lineup_slot values ('00000003', 'Rings', 1, '00000009');
insert into lineup_slot values ('00000003', 'Parallel Bars', 1, '00000009');
insert into lineup_slot values ('00000003', 'Horizontal Bar', 1, '00000010');
insert into lineup_slot values ('00000004', 'Floor', 1, '00000011');
insert into lineup_slot values ('00000004', 'Floor', 2, '00000014');
insert into lineup_slot values ('00000004', 'Pommel Horse', 1, '00000011');
insert into lineup_slot values ('00000004', 'Pommel Horse', 2, '00000012');
insert into lineup_slot values ('00000004', 'Rings', 1, '00000011');
insert into lineup_slot values ('00000004', 'Vault', 1, '00000014');
insert into lineup_slot values ('00000004', 'Parallel Bars', 1, '00000013');
insert into lineup_slot values ('00000004', 'Horizontal Bar', 1, '00000013');
insert into lineup_slot values ('00000005', 'Rings', 1, '00000015');
insert into lineup_slot values ('00000005', 'Parallel Bars', 1, '00000015');
insert into lineup_slot values ('00000005', 'Horizontal Bar', 1, '00000019');
insert into lineup_slot values ('00000005', 'Floor', 1, '00000020');
insert into lineup_slot values ('00000005', 'Floor', 2, '00000017');
insert into lineup_slot values ('00000005', 'Pommel Horse', 1, '00000019');
insert into score values ('00000001', '00000027', '2021-02-06', 'Rings', 12);
insert into score values ('00000002', '00000024', '2018-08-11', 'Parallel Bars', 11);
insert into score values ('00000003', '00000021', '2019-09-10', 'Rings', 10);
insert into score values ('00000004', '00000028', '2018-08-19', 'Floor', 13);
insert into score values ('00000005', '00000020', '2019-09-01', 'Rings', 13);
insert into score values ('00000006', '00000011', '2020-05-23', 'Pommel Horse', 12);
insert into score values ('00000007', '00000013', '2021-01-15', 'Vault', 14);
insert into score values ('00000008', '00000006', '2019-04-26', 'Horizontal Bar', 10);
insert into score values ('00000009', '00000019', '2019-09-28', 'Pommel Horse', 13);
insert into score values ('00000010', '00000001', '2018-07-31', 'Rings', 13);
insert into score values ('00000011', '00000025', '2019-07-30', 'Vault', 13);
insert into score values ('00000012', '00000012', '2020-04-03', 'Vault', 11);
insert into score values ('00000013', '00000025', '2020-10-11', 'Parallel Bars', 14);
insert into score values ('00000014', '00000018', '2019-12-23', 'Horizontal Bar', 9);
insert into score values ('00000015', '00000013', '2019-01-11', 'Vault', 13);
insert into score values ('00000016', '00000027', '2018-08-29', 'Rings', 12);
insert into score values ('00000017', '00000026', '2019-10-06', 'Rings', 9);
insert into score values ('00000018', '00000009', '2018-10-30', 'Floor', 12);
insert into score values ('00000019', '00000024', '2018-09-03', 'Floor', 13);
insert into score values ('00000020', '00000012', '2018-10-27', 'Rings', 14);
insert into score values ('00000021', '00000006', '2019-08-18', 'Pommel Horse', 8);
insert into score values ('00000022', '00000028', '2020-06-29', 'Pommel Horse', 11);
insert into score values ('00000023', '00000029', '2019-06-11', 'Vault', 14);
insert into score values ('00000024', '00000024', '2020-10-16', 'Rings', 11);
insert into score values ('00000025', '00000025', '2020-10-19', 'Parallel Bars', 9);
insert into score values ('00000026', '00000021', '2020-04-14', 'Vault', 9);
insert into score values ('00000027', '00000020', '2019-07-25', 'Parallel Bars', 10);
insert into score values ('00000028', '00000031', '2019-02-16', 'Floor', 12);
insert into score values ('00000029', '00000025', '2021-02-13', 'Rings', 14);
insert into score values ('00000030', '00000023', '2018-12-05', 'Rings', 12);
insert into score values ('00000031', '00000021', '2021-01-05', 'Pommel Horse', 7);
insert into score values ('00000032', '00000015', '2021-05-05', 'Horizontal Bar', 12);
insert into score values ('00000033', '00000024', '2020-12-03', 'Vault', 15);
insert into score values ('00000034', '00000027', '2018-12-20', 'Vault', 14);
insert into score values ('00000035', '00000008', '2020-04-13', 'Parallel Bars', 11);
insert into score values ('00000036', '00000004', '2020-03-24', 'Rings', 11);
insert into score values ('00000037', '00000004', '2018-12-10', 'Floor', 15);
insert into score values ('00000038', '00000032', '2020-09-19', 'Vault', 12);
insert into score values ('00000039', '00000019', '2019-02-27', 'Horizontal Bar', 14);
insert into score values ('00000040', '00000026', '2020-07-25', 'Parallel Bars', 14);
insert into user_league values ('00000001', '00000001');
insert into user_league values ('00000002', '00000001');
insert into user_league values ('00000003', '00000001');
insert into user_league values ('00000004', '00000001');
insert into user_league values ('00000005', '00000001');
insert into user_league values ('00000006', '00000001');
insert into user_league values ('00000001', '00000002');
insert into user_league values ('00000002', '00000002');
insert into user_league values ('00000003', '00000002');
insert into user_league values ('00000004', '00000002');
insert into user_league values ('00000005', '00000002');
insert into user_league values ('00000006', '00000002');
insert into user_league values ('00000001', '00000003');
insert into user_league values ('00000002', '00000003');
insert into user_league values ('00000003', '00000003');
insert into user_league values ('00000004', '00000003');
insert into user_league values ('00000005', '00000003');
insert into user_league values ('00000006', '00000003');
insert into user_league values ('00000001', '00000004');
insert into user_league values ('00000002', '00000004');
insert into user_league values ('00000003', '00000004');
insert into user_league values ('00000004', '00000004');
insert into user_league values ('00000005', '00000004');
insert into user_league values ('00000006', '00000004');
insert into roster values ('00000001', '00000001');
insert into roster values ('00000002', '00000002');
insert into roster values ('00000003', '00000003');
insert into roster values ('00000004', '00000004');
insert into roster values ('00000005', '00000005');
insert into roster values ('00000006', '00000006');
insert into roster values ('00000007', '00000007');
insert into roster values ('00000008', '00000008');
insert into roster values ('00000001', '00000009');
insert into roster values ('00000002', '00000010');
insert into roster values ('00000003', '00000011');
insert into roster values ('00000004', '00000012');
insert into roster values ('00000005', '00000013');
insert into roster values ('00000006', '00000014');
insert into roster values ('00000007', '00000015');
insert into roster values ('00000008', '00000016');
insert into roster values ('00000001', '00000017');
insert into roster values ('00000002', '00000018');
insert into roster values ('00000003', '00000019');
insert into roster values ('00000004', '00000020');
insert into roster values ('00000005', '00000021');
insert into roster values ('00000006', '00000022');
insert into roster values ('00000007', '00000023');
insert into roster values ('00000008', '00000024');
insert into roster values ('00000001', '00000025');
insert into roster values ('00000002', '00000026');
insert into roster values ('00000003', '00000027');
insert into roster values ('00000004', '00000028');
insert into roster values ('00000005', '00000029');
insert into roster values ('00000006', '00000030');
insert into roster values ('00000007', '00000031');
insert into roster values ('00000008', '00000032');
insert into matchup values ('00000001','00000002', 1);
insert into matchup values ('00000003','00000004', 1);
insert into matchup values ('00000005','00000006', 1);
insert into matchup values ('00000003','00000006', 1);
insert into matchup values ('00000007','00000009', 1);
insert into matchup values ('00000008','00000011', 1);
insert into matchup values ('00000012','00000007', 1);
insert into matchup values ('00000010','00000011', 1);
insert into matchup values ('00000015', '00000014', 2);
insert into matchup values ('00000014', '00000015', 2);
insert into matchup values ('00000018', '00000015', 2);
insert into matchup values ('00000015', '00000017', 2);
insert into matchup values ('00000023', '00000024', 2);
insert into matchup values ('00000020', '00000024', 2);
insert into matchup values ('00000019', '00000020', 2);
insert into matchup values ('00000021', '00000020', 2);