# -*- coding: utf-8 -*-
'''
This script is used for text matching using regular expression.
'''

import re
# filename = input(u"请输入语料库txt名称:")
filename = "corpus.txt"

text = "{AI}在长三角一体化发展工作专项督察中"
pattern = re.compile(r"{AI}")
location_list = ["{AI}", "{C}"]

class ExtractLocations():
    def __init__(self):
        pass

    def run(self, location_list, text):
        res = []
        for loc in location_list:
            pattern = re.compile(loc)
            result = re.findall(pattern, text, flags=0)
            if result != []:
                res.append(loc)

        print(res)

el = ExtractLocations()
el.run(location_list, text)