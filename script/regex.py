# -*- coding: utf-8 -*-
'''
This script is used for text matching using regular expression.
'''

import re
import json
# import pandas as pd

# filename = input(u"请输入语料库txt名称:")
# filename = "/label.xlsx"
# data = pd.read_excel(filename)
# label_location_map = dict(zip(data[u"对应词"], data[u"类别"]))
# labels = data[u"对应词"]

text ="当前，{AE}市、{J}市受资金、土地、能耗等发展要素的制约，{CC}建设重大项目出现招引难、落地难问题。"
label_list = ["{AI}", "{CC}", "{AE}"]


class ExtractLocations():
    def __init__(self, label_list):
        self.label_list =  label_list

    def run(self, text):
        res = []
        for label in label_list:
            pattern = re.compile(label)
            result = re.findall(pattern, text, flags=0)
            if result != []:
                res.append(label)
        return res

if __name__== '__main__':
    el = ExtractLocations(label_list)
    exist_label = el.run(text)

    print("Text:" + text)
    print("Target label: " + json.dumps(label_list))
    print('Existing Label: ' + json.dumps(exist_label))