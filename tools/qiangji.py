import os

import pandas as pd
from pprint import pprint
def parse_xls_to_json():
    path = os.path.expanduser('~/Desktop/q.xls')
    xls = pd.ExcelFile(path)
    print(1)
    res = dict()
    for sheet in xls.sheet_names:
        if sheet == '判断':
            df = pd.read_excel(xls.book, sheet, engine='xlrd')
            df.columns = df.iloc[0]
            df = df.drop([0])
            columns = ['序号', '题干', '答案']
            d = dict()
            for index, each in df.iterrows():
                single = each[columns].to_dict()
                d[each['序号']] = single
            res[sheet] = d
            continue
        try:
            df = pd.read_excel(xls.book, sheet, engine='xlrd')
            if '答案' not in df.columns:
                continue
            df = df[pd.notnull(df['序号'])]
            df=df.fillna('_')
            columns = ['序号','题干', 'A', 'B', 'C', 'D', '答案'] if 'A' in df.columns else ['题干', '答案']
            columns = columns.append('E') if 'E' in df.columns else columns
            d = dict()
            for index, each in df.iterrows():
                single = each[columns].to_dict()
                single['xuanxiang']= list('ABCDE') if 'E' in columns else list('ABCD') if 'A' in columns else []
                d[each['序号']] = single
            res[sheet] = d
        except:
            continue
    # for k in res.keys():
    #     print(k)
    #     pprint(res[k])
    import json
    return json.dumps(res)


if __name__ == '__main__':
    parse_xls_to_json()