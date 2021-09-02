import pandas as pd


def make_prediction(l1, l2, l3):
    """
    B1- соответствует B1.1
    B1  соответствует B1.2
    B1+ соответствует B1.3
    B2  соответствует B2.1
    B2+ соответствует B2.2
    """
    recalc_lvl = {'a1': 'a1', 'a2': 'a2', 'b1-': 'b1.1',
                  'b1': 'b1.2', 'b1+': 'b1.3', 'b2': 'b2.1',
                  'b2+': 'b2.2', 'c1': 'c1', 'c2': 'c2'}

    lvl = sorted([recalc_lvl[l1.lower()], recalc_lvl[l2.lower()], recalc_lvl[l3.lower()]])
    lvl_letter = sorted([l1[0].lower(), l2[0].lower(), l3[0].lower()])

    # ✅ 1. Если два показателя A, то A2;
    if lvl_letter.count('a') >= 2:
        return 'A2'

    # ✅ 2. Если один показатель A1, второй B1-, а третий B1/B2/C1, то A2;
    elif lvl[0] == 'a1' and lvl[1] == 'b1.1' and lvl[2] in ['b1.2', 'b2.1', 'c1']:
        return 'A2'

    # ✅ 3. Если один показатель A1, второй B1/B1+, а третий от B1 до B2+ включительно, то A2;
    elif lvl[0] == 'a1' and lvl[1] in ['b1.2', 'b1.3'] and lvl[2] in ['b1.1', 'b1.2', 'b1.3', 'b2.1', 'b2.2']:
        return 'A2'

    # ✅ 4. Если первый A1, а остальные B1- и C2, или B1 и C, или B2, то B1-;
    elif lvl[0] == 'a1' and ((lvl[1] == 'b1.1' and lvl[2] == 'c2') or
                             (lvl[1] == 'b1.2' and lvl_letter[2] == 'c') or
                             (lvl[1] == lvl[2] == 'b2.1')):
        return 'B1-'

    # ✅ 5. Если первый A2, второй B1-/B1, а третий B1/B1+/B2, то B1-;
    elif lvl[0] == 'a2' and lvl[1] in ['b1.1', 'b1.2'] and lvl[2] in ['b1.2', 'b1.3', 'b2.1']:
        return 'B1-'

    # ✅ 6. Если все три показателя B1, или два B1 и один B1-, то B1-;
    elif lvl.count('b1.2') == 3 or (lvl[0] == 'b1.1' and lvl[1] == lvl[2] == 'b1.2'):
        return 'B1-'

    # ✅ 7. Если один показатель A1, второй B1+, а третий C, то B1;
    elif lvl[0] == 'a1' and lvl[1] == 'b1.3' and lvl_letter[2] == 'c':
        return 'B1'

    # ✅ 8. Если один показатель A1, второй B2 и выше, а третий B2+ и выше, то B1;
    elif lvl[0] == 'a1' and lvl[1] in ['b2.1', 'b2.2', 'c1', 'c2'] and lvl[2] in ['b2.2', 'c1', 'c2']:
        return 'B1'

    # ✅ 9. Если один показатель A2, второй B1-, а третий C, или второй B1, а третий B2+ и выше, , то B1;
    elif lvl[0] == 'a2' and ((lvl[1] == 'b1.1' and lvl_letter[2] == 'c') or
                             (lvl[1] == 'b1.2' and lvl[2] in ['b2.2', 'c1', 'c2'])):
        return 'B1'

    # ✅ 10. Если один показатель A2, второй B1+ а третий B2/C1, или второй B2, а третий B2 и выше, то B1;
    elif lvl[0] == 'a2' and ((lvl[1] == 'b1.3' and lvl[2] in ['b2.1', 'c1']) or
                             (lvl[1] == 'b2.1' and lvl[2] in ['b2.1', 'b2.2', 'c1', 'c2'])):
        return 'B1'

    # ✅ 11. Если один показатель B1-, второй B1, а третий выше B2, или второй B2, а третий B2/C1, то B1;
    elif lvl[0] == 'b1.1' and ((lvl[1] == 'b1.2' and lvl[2] in ['b2.1', 'c1', 'c2']) or
                               (lvl[1] == 'b2.1' and lvl[2] in ['b2.1', 'c1'])):
        return 'B1'

    # ✅ 12. Если два показателя B1, а третий B1+/B2, или один B1, второй B1+, а третий B2, то B1;
    elif (lvl[0] == lvl[1] == 'b1.2' and lvl[2] in ['b1.3', 'b2.1']) or (
            lvl[0] == 'b1.2' and lvl[1] == 'b1.3' and lvl[2] == 'b2.1'):
        return 'B1'

    # ✅ 13. Если первый показатель A2, второй B2+/C, а третий C, или второй B1+, а третий C2, то B1+;
    elif lvl[0] == 'a2' and ((lvl[1] in ['b2.2', 'c1', 'c2'] and lvl_letter[2] == 'c') or \
                             (lvl[1] == 'b1.3' and lvl[2] == 'c2')):
        return 'B1+'

    # ✅ 14. Если один показатель B1+/B2, а остальные B2, то B1+;
    elif lvl[1] == lvl[2] == 'b2.1' and (lvl[0] == 'b1.3' or lvl[0] == 'b2.1'):
        return 'B1+'

    # ✅ 15. Если один показатель B1, а остальные B2/B2+/C (но не оба C2), то B1+;
    elif lvl[0] == 'b1.2' and lvl[1] in ['b2.1', 'b2.2', 'c1', 'c2'] and lvl[2] in ['b2.1', 'b2.2', 'c1', 'c2'] \
            and lvl.count('c2') <= 1:
        return 'B1+'

    # ✅ 16. Если один показатель B1, второй B1/B1+, а третий C, то B1+;
    elif lvl[0] == 'b1.2' and lvl[1] in ['b1.2', 'b1.3'] and lvl_letter[2] == 'c':
        return 'B1+'

    # ✅ 17. Если два показателя B1, а третий B2+, то B1+;
    elif lvl.count('b1.1') == 2 and lvl.count('b2.2') == 1:
        return 'B1+'

    # ✅ 18. Если один B1-, второй C1, а третий C, или второй B2, а третий C2, то B1+;
    elif lvl[0] == 'b1.1' and ((lvl[1] == 'c1' and lvl_letter[2] == 'c') or
                               (lvl[1] == 'b2.1' and lvl[2] == 'c2')):
        return 'B1+'

    # ✅ 19. Если два показателя B2, а третий B2+/C1, то B2;
    elif lvl[0] == lvl[1] == 'b2.1' and lvl[2] in ['b2.2', 'c1']:
        return 'B2'

    # ✅ 20. Если один показатель B1-/B, а остальные C2, то B2;
    elif lvl[0] in ['b1.1', 'b1.2'] and lvl[1] == lvl[2] == 'c2':
        return 'B2'

    # ✅ 21. Если один показатель B1+, второй B2/C1, а третий C, то B2;
    elif lvl[0] == 'b1.3' and lvl[1] in ['b2.1', 'c1'] and lvl_letter[2] == 'c':
        return 'B2'

    # ✅ 22. Если один показатель B1+, а остальные C2, то B2+;
    elif lvl[0] == 'b1.3' and lvl.count('c2') == 2:
        return 'B2+'

    # ✅ 23. Если один показатель B2, второй B2/B2+, а третий C2, то B2+;
    elif lvl[0] == 'b2.1' and lvl[1] in ['b2.1', 'b2.2'] and lvl[2] == 'c2':
        return 'B2+'

    # ✅ 24. Если один показатель B2/B2+, второй B2+/C1, а третий C1, то B2+;
    elif lvl[0] in ['b2.1', 'b2.2'] and lvl[1] in ['b2.2', 'c1'] and lvl[2] == 'c1':
        return 'B2+'

    # ✅ 25. Если один показатель B2/B2+, а остальные C (но не оба С1), или два показателя C1 и третий C, то C1;
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
