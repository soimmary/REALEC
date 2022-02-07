import pandas as pd


def make_prediction(l1, l2, l3):
    """
    A2_main соответствует A2.2
    B1_minus соответствует B1.1
    B1_main соответствует B1.2
    B2_minus  соответствует B2.1
    B2_main соответствует B2.2
    """
    recalc_lvl = {'a1': 'a1', 'a2_minus': 'a2.1', 'a2_main': 'a2.2',
                  'b1_minus': 'b1.1', 'b1_main': 'b1.2', 'b2_minus': 'b2.1',
                  'b2_main': 'b2.2', 'c1': 'c1', 'c2': 'c2'}

    lvl = sorted([recalc_lvl[l1.lower()], recalc_lvl[l2.lower()], recalc_lvl[l3.lower()]])
    lvl_letter = sorted([l1[0].lower(), l2[0].lower(), l3[0].lower()])

    # ✅ 1. Если два показателя A, то A2;
    if lvl_letter.count('a') >= 2:
        return 'A2'

    # ✅ 2. Если один показатель A1, второй A2_main, а третий B1_minus/B2_minus/C1, то A2;
    elif lvl[0] == 'a1' and lvl[1] == 'a2.2' and lvl[2] in ['b1.1', 'b2.1', 'c1']:
        return 'A2'

    # ✅ 3. Если один показатель A1, второй B1_minus/B1_main, а третий от B1_minus до B2_main включительно, то A2;
    elif lvl[0] == 'a1' and lvl[1] in ['b1.1', 'b1.2'] and lvl[2] in ['a2.2', 'b1.1', 'b1.2', 'b2.1', 'b2.2']:
        return 'A2'

    # ✅ 4. Если первый A1, а остальные A2_main и C2, или B1_minus и C, или B2_minus, то A2_main;
    elif lvl[0] == 'a1' and ((lvl[1] == 'a2.2' and lvl[2] == 'c2') or
                             (lvl[1] == 'b1.1' and lvl_letter[2] == 'c') or
                             (lvl[1] == lvl[2] == 'b2.1')):
        return 'A2_main'

    # ✅ 5. Если первый A2, второй A2_main/B1_minus, а третий B1_minus/B1_main/B2_minus, то A2_main;
    elif lvl[0] == 'a2' and lvl[1] in ['a2.2', 'b1.1'] and lvl[2] in ['b1.1', 'b1.2', 'b2.1']:
        return 'A2_main'

    # ✅ 6. Если все три показателя B1_minus, или два B1_minus и один A2_main, то A2_main;
    elif lvl.count('b1.1') == 3 or (lvl[0] == 'a2.2' and lvl[1] == lvl[2] == 'b1.1'):
        return 'A2_main'

    # ✅ 7. Если один показатель A1, второй B1_main, а третий C, то B1_minus;
    elif lvl[0] == 'a1' and lvl[1] == 'b1.2' and lvl_letter[2] == 'c':
        return 'B1_minus'

    # ✅ 8. Если один показатель A1, второй B2_minus и выше, а третий B2_main и выше, то B1_minus;
    elif lvl[0] == 'a1' and lvl[1] in ['b2.1', 'b2.2', 'c1', 'c2'] and lvl[2] in ['b2.2', 'c1', 'c2']:
        return 'B1_minus'

    # ✅ 9. Если один показатель A2, второй A2_main, а третий C, или второй B1_minus, а третий B2_main и выше, , то B1_minus;
    elif lvl[0] == 'a2' and ((lvl[1] == 'a2.2' and lvl_letter[2] == 'c') or
                             (lvl[1] == 'b1.1' and lvl[2] in ['b2.2', 'c1', 'c2'])):
        return 'B1_minus'

    # ✅ 10. Если один показатель A2, второй B1_main а третий B2_minus/C1, или второй B2_minus, а третий B2_minus и выше, то B1_minus;
    elif lvl[0] == 'a2' and ((lvl[1] == 'b1.2' and lvl[2] in ['b2.1', 'c1']) or
                             (lvl[1] == 'b2.1' and lvl[2] in ['b2.1', 'b2.2', 'c1', 'c2'])):
        return 'B1_minus'

    # ✅ 11. Если один показатель A2_main, второй B1_minus, а третий выше B2_minus, или второй B2_minus, а третий B2_minus/C1, то B1_minus;
    elif lvl[0] == 'a2.2' and ((lvl[1] == 'b1.1' and lvl[2] in ['b2.1', 'c1', 'c2']) or
                               (lvl[1] == 'b2.1' and lvl[2] in ['b2.1', 'c1'])):
        return 'B1_minus'

    # ✅ 12. Если два показателя B1_minus, а третий B1_main/B2_minus, или один B1_minus, второй B1_main, а третий B2_minus, то B1_minus;
    elif (lvl[0] == lvl[1] == 'b1.1' and lvl[2] in ['b1.2', 'b2.1']) or (
            lvl[0] == 'b1.1' and lvl[1] == 'b1.2' and lvl[2] == 'b2.1'):
        return 'B1_minus'

    # ✅ 13. Если первый показатель A2, второй B2_main/C, а третий C, или второй B1_main, а третий C2, то B1_main;
    elif lvl[0] == 'a2' and ((lvl[1] in ['b2.2', 'c1', 'c2'] and lvl_letter[2] == 'c') or \
                             (lvl[1] == 'b1.2' and lvl[2] == 'c2')):
        return 'B1_main'

    # ✅ 14. Если один показатель B1_main/B2_minus, а остальные B2_minus, то B1_main;
    elif lvl[1] == lvl[2] == 'b2.1' and (lvl[0] == 'b1.2' or lvl[0] == 'b2.1'):
        return 'B1_main'

    # ✅ 15. Если один показатель B1_minus, а остальные B2_minus/B2_main/C (но не оба C2), то B1_main;
    elif lvl[0] == 'b1.1' and lvl[1] in ['b2.1', 'b2.2', 'c1', 'c2'] and lvl[2] in ['b2.1', 'b2.2', 'c1', 'c2'] \
            and lvl.count('c2') <= 1:
        return 'B1_main'

    # ✅ 16. Если один показатель B1_minus, второй B1_minus/B1_main, а третий C, то B1_main;
    elif lvl[0] == 'b1.1' and lvl[1] in ['b1.1', 'b1.2'] and lvl_letter[2] == 'c':
        return 'B1_main'

    # ✅ 17. Если два показателя B1_minus, а третий B2_main, то B1_main;
    elif lvl.count('a2.2') == 2 and lvl.count('b2.2') == 1:
        return 'B1_main'

    # ✅ 18. Если один A2_main, второй C1, а третий C, или второй B2_minus, а третий C2, то B1_main;
    elif lvl[0] == 'a2.2' and ((lvl[1] == 'c1' and lvl_letter[2] == 'c') or
                               (lvl[1] == 'b2.1' and lvl[2] == 'c2')):
        return 'B1_main'

    # ✅ 19. Если два показателя B2_minus, а третий B2_main/C1, то B2_minus;
    elif lvl[0] == lvl[1] == 'b2.1' and lvl[2] in ['b2.2', 'c1']:
        return 'B2_minus'

    # ✅ 20. Если один показатель A2_main/B, а остальные C2, то B2_minus;
    elif lvl[0] in ['a2.2', 'b1.1'] and lvl[1] == lvl[2] == 'c2':
        return 'B2_minus'

    # ✅ 21. Если один показатель B1_main, второй B2_minus/C1, а третий C, то B2_minus;
    elif lvl[0] == 'b1.2' and lvl[1] in ['b2.1', 'c1'] and lvl_letter[2] == 'c':
        return 'B2_minus'

    # ✅ 22. Если один показатель B1_main, а остальные C2, то B2_main;
    elif lvl[0] == 'b1.2' and lvl.count('c2') == 2:
        return 'B2_main'

    # ✅ 23. Если один показатель B2_minus, второй B2_minus/B2_main, а третий C2, то B2_main;
    elif lvl[0] == 'b2.1' and lvl[1] in ['b2.1', 'b2.2'] and lvl[2] == 'c2':
        return 'B2_main'

    # ✅ 24. Если один показатель B2_minus/B2_main, второй B2_main/C1, а третий C1, то B2_main;
    elif lvl[0] in ['b2.1', 'b2.2'] and lvl[1] in ['b2.2', 'c1'] and lvl[2] == 'c1':
        return 'B2_main'

    # ✅ 25. Если один показатель B2_minus/B2_main, а остальные C (но не оба С1), или два показателя C1 и третий C, то C1;
    elif (lvl[0] in ['b2.1', 'b2.2'] and lvl_letter[1] == 'c' and lvl[2] == 'c2') or \
            (lvl[0] == lvl[1] == 'c1' and lvl_letter[2] == 'c'):
        return 'C1'

    # ✅ 26. Если один показатель C, а остальные C2, то C1+.
    elif lvl_letter[0] == 'c' and lvl[1] == lvl[2] == 'c2':
        return 'C1+'


df_grammarly = pd.read_csv('grammarly_results.csv')
df_write_improve = pd.read_csv('write_improve_results.csv')

df = pd.merge(df_write_improve, df_grammarly, on='text')
df.columns = ['text', 'Write_Improve', 'Grammarly_1', 'Grammarly_2']
df['Prediction'] = df.apply(lambda row: make_prediction(row.Write_Improve, row.Grammarly_1, row.Grammarly_2),
                            axis=1)
df.to_csv('cefr_prediction_table.csv')
