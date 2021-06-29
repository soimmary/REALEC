import time
import re
import pandas as pd
import gspread
from tqdm import tqdm
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
credentials = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
client = gspread.authorize(credentials)
sheet = client.open('marks-vs-errors--DBsearch-results').sheet1


def get_new_value(l1, l2, l3):
    l1 = re.findall(r'[abcABC][12]', l1, re.IGNORECASE)[0].lower()
    l2 = re.findall(r'[abcABC][12]', l2)[0].lower()
    l3 = re.findall(r'[abcABC][12]', l3)[0].lower()

    l_list = [l1, l2, l3]
    l_letter_list = [l1[0], l2[0], l3[0]]

    l_to_num = {'a': 1, 'b': 10, 'c': 100}
    l_nums_list = [l_to_num[l1[0]], l_to_num[l2[0]], l_to_num[l3[0]]]

    # 1. If at least two predictions were at level A (А1 or А2), we choose A2.

    if l_letter_list.count('a') >= 2:
        return 'A2'

    # 2. If two predictions were at level B (B1 or B2), and one at level A (A1 or A2),
    # we choose A2-B1.
    elif sum(l_nums_list) == 21:
        return 'A2-B1'

    # 3. If one prediction was at level A (А1 or А2), and at least one was
    # at level C (C1 or C2), we choose B1.

    elif l_letter_list.count('a') == 1 and l_letter_list.count('c') >= 1:
        return 'B1'

    # 4. If all three predictions were B1, we choose A2-B1.
    elif l_list.count('b1') == 3:
        return 'A2-B1'

    # 5. If two predictions were B1, and the rest, C2, we choose B2.
    elif l_list.count('b1') == 2 and l_list.count('c2') == 1:
        return 'B2'

    # 6. If all three predictions were B2, we choose B1-B2.
    elif l_list.count('b2') == 3:
        return 'B1-B2'

    # 7. If one or two predictions were B1, and the rest, B2, we choose B1.
    elif sum(l_nums_list) == 30 and l_list.count('b2') != 3 and l_list.count('b1') != 3:
        return 'B1'

    # 8. If one prediction was B1 and the second, B2, or two predictions were B1, and the
    # third was C1, we choose B1-B2.
    elif (l_list.count('b1') == 2 and l_list.count('c1') == 1) or \
            (l_list.count('b1') == 1 and l_list.count('b2') == 1 and l_list.count('c1') == 1):
        return 'B1-B2'

    # 9. If two predictions were B2, and the third was C1, we choose B2.
    elif l_list.count('b2') == 2 and l_list.count('c1') == 1:
        return 'B2'

    # 10. If one prediction was B1 or B2, and the other two were C1, we choose B2.
    elif sum(l_nums_list) == 210 and l_list.count('c1') == 2:
        return 'B2'

    # 11. If one prediction was B1, the second, C1, and the third, C2, we choose B2-C1.
    elif l_list.count('b1') == 1 and l_list.count('c1') == 1 and l_list.count('c2') == 1:
        return 'B2-C1'

    # 12. If two predictions were B1, and the third was C2, we choose B2.
    elif l_list.count('b1') == 2 and l_list.count('c2') == 1:
        return 'B2'

    # 13. If two predictions were B2, and the third was C2, we choose B2-C1.
    elif l_list.count('b2') == 2 and l_list.count('c2') == 1:
        return 'B2-C1'

    # 14. If one prediction was B1, and the other two were C2, we choose B2-C1.
    elif l_list.count('c2') == 2 and l_list.count('b1') == 1:
        return 'B2-C1'

    # 15. If one prediction was B1, the second, B2, and the third, C2, we choose B2-C1.
    elif l_list.count('b1') == 1 and l_list.count('b2') == 1 and l_list.count('c2') == 1:
        return 'B2-C1'

    # 16. If one prediction was B2, the second, C1, and the third, C2, we choose C1.
    elif l_list.count('b2') == 1 and l_list.count('c1') == 1 and l_list.count('c2') == 1:
        return 'C1'

    # 17. If one prediction was B2, and the other two were C2, we choose C1.
    elif l_list.count('b2') == 1 and l_list.count('c2') == 2:
        return 'C1'

    # 18. If all three predictions were at level C (C1 or C2), we choose C1.
    elif sum(l_nums_list) == 300:
        return 'C1'

    else:
        return '??'


# Use this if you want to add the predicted level right into the google sheet.
'''for i in tqdm(range(2, sheet.row_count + 1)):
    if not sheet.cell(i, 5).value:
        time.sleep(2)
        if sheet.cell(i, 7).value and sheet.cell(i, 8).value and sheet.cell(i, 10).value:
            new_value = get_new_value(sheet.cell(i, 7).value,
                                      sheet.cell(i, 8).value,
                                      sheet.cell(i, 10).value)
            time.sleep(2)
            sheet.update_cell(i, 5, new_value)

    # since Google Sheets have quota limit:
    time.sleep(3)'''


# Use this if you want to update the csv file with the levels.
df = pd.read_csv('new_table.csv')
df['Prediction'] = df.apply(lambda row: get_new_value(row.Duolingo, row.Grammarly, row.Write_Improve), axis=1)
df.to_csv('new_table.csv')
