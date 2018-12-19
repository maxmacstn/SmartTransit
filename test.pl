
list_len([],0).
list_len([H|T],N):- list_len(T, N1), N is N1 + 1.

reverse_list([H|T], A, R):- reverse_list(T,[H|A], R).
reverse_list([],A,A).

revList(L,R):- reverse_list(L,[],R).

path(mochit, saphankwai).
path(mochit, max).



/**
 *  Distance between two station
 *
 *  dist(start, stop, minute).
 */

% Airport link
dist(arl_phaya_thai, arl_ratchaprarop, 60).
dist(arl_ratchaprarop, arl_makkasan, 180).
dist(arl_makkasan, arl_ramkhamhaeng, 240).
dist(arl_ramkhamhaeng, arl_huai_mak, 240).
dist(arl_huai_mak, arl_ban_thap_chang, 240).
dist(arl_ban_thap_chang, arl_lat_krabang, 300).
dist(arl_lat_krabang, arl_suvannabhumi, 300).

% BTS Sukhumvit
dist(bts_sukhumvit_mo_chit, bts_sukhumvit_saphan_khwai, 120).
dist(bts_sukhumvit_saphan_khwai, bts_sukhumvit_ari, 120).
dist(bts_sukhumvit_ari, bts_sukhumvit_sanam_pao, 120).
dist(bts_sukhumvit_sanam_pao, bts_sukhumvit_victory_monument, 120).
dist(bts_sukhumvit_victory_monument, bts_sukhumvit_phaya_thai, 120).
dist(bts_sukhumvit_phaya_thai, bts_sukhumvit_ratchathewi, 60).
dist(bts_sukhumvit_ratchathewi, bts_sukhumvit_siam, 180).
dist(bts_sukhumvit_siam, bts_sukhumvit_chit_lom, 120).
dist(bts_sukhumvit_chit_lom, bts_sukhumvit_phloen_chit, 60).
dist(bts_sukhumvit_phloen_chit, bts_sukhumvit_nana, 120).
dist(bts_sukhumvit_nana, bts_sukhumvit_asok, 120).
dist(bts_sukhumvit_asok, bts_sukhumvit_phrom_phong, 120).
dist(bts_sukhumvit_phrom_phong, bts_sukhumvit_thong_lo, 60).
dist(bts_sukhumvit_thong_lo, bts_sukhumvit_ekkamai, 120).
dist(bts_sukhumvit_ekkamai, bts_sukhumvit_phra_khanong, 120).
dist(bts_sukhumvit_phra_khanong, bts_sukhumvit_on_nut, 120).
dist(bts_sukhumvit_on_nut, bts_sukhumvit_bang_chak, 120).
dist(bts_sukhumvit_bang_chak, bts_sukhumvit_punnawithi, 120).
dist(bts_sukhumvit_punnawithi, bts_sukhumvit_udom_suk, 60).
dist(bts_sukhumvit_udom_suk, bts_sukhumvit_bang_na, 180).
dist(bts_sukhumvit_bang_na, bts_sukhumvit_bearing, 60).
dist(bts_sukhumvit_bearing, bts_sukhumvit_samrong, 120).

% BTS Silom
dist(bts_silom_national_stadium, bts_silom_siam, 60).
dist(bts_silom_siam, bts_silom_ratchadamri, 60).
dist(bts_silom_ratchadamri, bts_silom_sala_daeng, 120).
dist(bts_silom_sala_daeng, bts_silom_chong_nonsi, 120).
dist(bts_silom_chong_nonsi, bts_silom_surasak, 120).
dist(bts_silom_surasak, bts_silom_saphan_taksin, 120).
dist(bts_silom_saphan_taksin, bts_silom_krung_thon_buri, 180).
dist(bts_silom_krung_thon_buri, bts_silom_wongwian_yai, 120).
dist(bts_silom_wongwian_yai, bts_silom_pho_nimit, 120).
dist(bts_silom_pho_nimit, bts_silom_talat_phlu, 120).
dist(bts_silom_talat_phlu, bts_silom_wutthakat, 120).
dist(bts_silom_wutthakat, bts_silom_bang_wa, 120).

% MRT Blue
dist(mrt_blue_hua_lamphong, mrt_blue_sam_yan, 135).
dist(mrt_blue_sam_yan, mrt_blue_silom, 81).
dist(mrt_blue_silom, mrt_blue_lumphini, 82).
dist(mrt_blue_lumphini, mrt_blue_khlong_toei, 81).
dist(mrt_blue_khlong_toei, mrt_blue_queen_sirikit_national_convention_centre, 80).
dist(mrt_blue_queen_sirikit_national_convention_centre, mrt_blue_sukhumvit, 138).
dist(mrt_blue_sukhumvit, mrt_blue_phetchaburi, 124).
dist(mrt_blue_phetchaburi, mrt_blue_phra_ram_9, 86).
dist(mrt_blue_phra_ram_9, mrt_blue_thailand_cultural_centre, 93).
dist(mrt_blue_thailand_cultural_centre, mrt_blue_huai_khwang, 123).
dist(mrt_blue_huai_khwang, mrt_blue_sutthisan, 89).
dist(mrt_blue_sutthisan, mrt_blue_ratchadapisak, 82).
dist(mrt_blue_ratchadapisak, mrt_blue_lat_phrao, 84).
dist(mrt_blue_lat_phrao, mrt_blue_phahon_yothin, 94).
dist(mrt_blue_phahon_yothin, mrt_blue_chatuchak_park, 127).
dist(mrt_blue_chatuchak_park, mrt_blue_kamphaeng_phet, 78).
dist(mrt_blue_kamphaeng_phet, mrt_blue_bang_sue, 88).
dist(mrt_blue_bang_sue, mrt_blue_tao_poon, 86).

% MRT Purple
dist(mrt_purple_tao_poon, mrt_purple_bang_son, 135).
dist(mrt_purple_bang_son, mrt_purple_wong_sawang, 81).
dist(mrt_purple_wong_sawang, mrt_purple_yaek_tiwanon, 82).
dist(mrt_purple_yaek_tiwanon, mrt_purple_ministry_of_public_health, 81).
dist(mrt_purple_ministry_of_public_health, mrt_purple_nonthaburi_civic_centre, 80).
dist(mrt_purple_nonthaburi_civic_centre, mrt_purple_bang_krasor, 138).
dist(mrt_purple_bang_krasor, mrt_purple_yaek_nonthaburi_1, 124).
dist(mrt_purple_yaek_nonthaburi_1, mrt_purple_phra_nang_klao_bridge, 86).
dist(mrt_purple_phra_nang_klao_bridge, mrt_purple_sai_ma, 93).
dist(mrt_purple_sai_ma, mrt_purple_bang_rak_noi_tha_it, 123).
dist(mrt_purple_bang_rak_noi_tha_it, mrt_purple_bang_rak_yai, 89).
dist(mrt_purple_bang_rak_yai, mrt_purple_bang_phu, 82).
dist(mrt_purple_bang_phu, mrt_purple_sam_yaek_bang_yai, 84).
dist(mrt_purple_sam_yaek_bang_yai, mrt_purple_talad_bang_yai, 94).
dist(mrt_purple_talad_bang_yai, mrt_purple_khlong_bang_phai, 127).

% Junction
dist(bts_sukhumvit_mo_chit, mrt_blue_chatuchak_park, 300).
dist(bts_sukhumvit_phaya_thai, arl_phaya_thai, 300).
dist(bts_sukhumvit_siam, bts_silom_siam, 180).
dist(bts_sukhumvit_asok, mrt_blue_sukhumvit, 300).
dist(bts_silom_sala_daeng, mrt_blue_silom, 300).
dist(mrt_blue_phetchaburi, arl_makkasan, 300).
dist(mrt_blue_tao_poon, mrt_purple_tao_poon, 180).



/**
 *  Location - station information
 *
 *  location(start, lat, lng).
 */

% Airport Link
location(arl_phaya_thai, 13.7567379, 100.5326535).
location(arl_ratchaprarop, 13.7551169, 100.5399626).
location(arl_makkasan, 13.7504988, 100.5602287).
location(arl_ramkhamshaeng, 13.7425102, 100.5995472).
location(arl_huai_mak, 13.738068, 100.6371115).
location(arl_ban_thap_chang, 13.7327841, 100.6891566).
location(arl_lat_krabang, 13.7275472, 100.7487334).
location(arl_suvannabhumi, 13.6976619, 100.7513383).

% BTS Sukhumvit
location(bts_sukhumvit_mo_chit, 13.8026249, 100.5516764).
location(bts_sukhumvit_saphan_khwai, 13.793972, 100.5475849).
location(bts_sukhumvit_ari, 13.7804291, 100.543054).
location(bts_sukhumvit_sanam_pao, 13.7726406, 100.5393306).
location(bts_sukhumvit_victory_monument, 13.7627945, 100.5348922).
location(bts_sukhumvit_phaya_thai, 13.757061, 100.5316856).
location(bts_sukhumvit_ratchathewi, 13.7519015, 100.5293805).
location(bts_sukhumvit_siam, 13.7461695, 100.5310261).
location(bts_sukhumvit_chit_lom, 13.7430232, 100.5399102).
location(bts_sukhumvit_phloen_chit, 13.7430414, 100.5467728).
location(bts_sukhumvit_nana, 13.7405166, 100.5532405).
location(bts_sukhumvit_asok, 13.7397513, 100.556066).
location(bts_sukhumvit_phrom_phong, 13.7309015, 100.5649927).
location(bts_sukhumvit_thong_lo, 13.7241679, 100.5722138).
location(bts_sukhumvit_ekkamai, 13.7174176, 100.581649).
location(bts_sukhumvit_phra_khanong, 13.7143071, 100.5861792).
location(bts_sukhumvit_on_nut, 13.7051076, 100.5953248).
location(bts_sukhumvit_bang_chak, 13.6938019, 100.6032513).
location(bts_sukhumvit_punnawithi, 13.6846678, 100.6068278).
location(bts_sukhumvit_udom_suk, 13.6787272, 100.6064021).
location(bts_sukhumvit_bang_na, 13.6684507, 100.6027064).
location(bts_sukhumvit_bearing, 13.66059, 100.5991299).
location(bts_sukhumvit_samrong, 13.6467506, 100.5939193).

% BTS Silom
location(bts_silom_national_stadium, 13.745473, 100.5251455).
location(bts_silom_siam, 13.7432615, 100.5322244).
location(bts_silom_ratchadamri, 13.739277, 100.5369153).
location(bts_silom_sala_daeng, 13.7275148, 100.5324394).
location(bts_silom_chong_nonsi, 13.7230202, 100.5276385).
location(bts_silom_surasak, 13.7184548, 100.5191694).
location(bts_silom_saphan_taksin, 13.7176477, 100.5132589).
location(bts_silom_krung_thon_buri, 13.7199508, 100.501764).
location(bts_silom_wongwian_yai, 13.7203952, 100.4944963).
location(bts_silom_pho_nimit, 13.71891, 100.4853876).
location(bts_silom_talat_phlu, 13.7145978, 100.4763118).
location(bts_silom_wutthakat, 13.7134344, 100.4682806).
location(bts_silom_bang_wa, 13.7193594, 100.4618039).

% MRT Blue
location(mrt_blue_hua_lamphong, 13.7379408, 100.5140327).
location(mrt_blue_sam_yan, 13.7314107, 100.5275353).
location(mrt_blue_silom, 13.72843, 100.5340584).
location(mrt_blue_lumphini, 13.7246675, 100.5412145).
location(mrt_blue_khlong_toei, 13.7210637, 100.5500087).
location(mrt_blue_queen_sirikit_national_convention_centre, 13.7210949, 100.5573901).
location(mrt_blue_sukhumvit, 13.7358529, 100.5591818).
location(mrt_blue_phetchaburi, 13.7477858, 100.5611452).
location(mrt_blue_phra_ram_9, 13.757229, 100.564753).
location(mrt_blue_thailand_cultural_centre, 13.7628779, 100.5669514).
location(mrt_blue_huai_khwang, 13.7774406, 100.5709649).
location(mrt_blue_sutthisan, 13.7875853, 100.5715713).
location(mrt_blue_ratchadapisak, 13.7994485, 100.5730681).
location(mrt_blue_lat_phrao, 13.8042929, 100.571635).
location(mrt_blue_phahon_yothin, 13.8103818, 100.5560495).
location(mrt_blue_chatuchak_park, 13.8038914, 100.552439).
location(mrt_blue_kamphaeng_phet, 13.7987302, 100.5471484).
location(mrt_blue_bang_sue, 13.801529, 100.5368549).
location(mrt_blue_tao_poon_blue, 13.8070074, 100.5281396).

% MRT Purple
location(mrt_purple_tao_poon, 13.8062767, 100.5302246).
location(mrt_purple_bang_son, 13.8197916, 100.5312241).
location(mrt_purple_wong_sawang, 13.8292557, 100.5256099).
location(mrt_purple_yaek_tiwanon, 13.8386857, 100.5138599).
location(mrt_purple_ministry_of_public_health, 13.8468927, 100.5124268).
location(mrt_purple_nonthaburi_civic_centre, 13.8603983, 100.5111339).
location(mrt_purple_bang_krasor, 13.8611267, 100.5022749).
location(mrt_purple_yaek_nonthaburi_1, 13.8656184, 100.4941257).
location(mrt_purple_phra_nang_klao_bridge, 13.8702017, 100.4782818).
location(mrt_purple_sai_ma, 13.8712928, 100.4641305).
location(mrt_purple_bang_rak_noi_tha_it, 13.8747051, 100.4550654).
location(mrt_purple_bang_rak_yai, 13.8762148, 100.4422704).
location(mrt_purple_bang_phu, 13.8747956, 100.4304391).
location(mrt_purple_sam_yaek_bang_yai, 13.873481, 100.4176872).
location(mrt_purple_talad_bang_yai, 13.8811424, 100.4077083).
location(mrt_purple_khlong_bang_phai, 13.8913357, 100.4074302).

