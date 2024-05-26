for sec, (s, e) in [('0_intro', (1, 20)), ('1_sort_and_search', (20, 55)), ('2_dp', (55, 74)), ('3_graphs', (74, 110)),
               ('4_range_queries', (110, 129)), ('5_trees', (129, 145)), ('6_maths', (145, 176)), ('7_strings', (176, 193)),
               ('8_geometry', (193, 200)), ('9_advanced', (200, 224)), ('A_additional', (224, 301))]:
    for i in range(s, e):
        with open(f'{sec}/cses_{str(i).zfill(3)}.py', 'a+') as f: f.write(f'#{i}: NOT SOLVED\n')
