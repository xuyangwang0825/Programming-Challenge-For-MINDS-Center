#!/usr/bin/env python
import collections
import json
import re
from tqdm import tqdm
from bs4 import BeautifulSoup

def pre_process():
    all_texts_dict = collections.defaultdict(list)
    # we got 48 data files
    for i in tqdm(range(1, 49)):
        # generate data path
        data_path = f'./data/messages{i}.html'

        fp = open(data_path, encoding='utf-8')

        # read html file
        soup = BeautifulSoup(fp, 'lxml')

        all_texts = soup.find_all('div', class_='text')
        all_times = soup.find_all('div', class_='pull_right date details')
        diff = len(all_texts) - len(all_times)
        if diff > 0:
            last_time = all_times[-1]
            for _ in range(diff):
                all_times.append(last_time)

        # print(len(all_texts))

        # extract text and store in dict
        for pos, text_class in enumerate(all_texts):
            text_content = text_class.text.strip()
            # print(str(all_times[pos]).split()[4][7:])
            time = str(all_times[pos]).split()[4][7:]
            # remove non-English messages and keep only messages mention "SHIB" or "DOGE"
            if text_content.isascii() and (re.search('SHIB', text_content, re.IGNORECASE) or re.search('DOGE', text_content, re.IGNORECASE)):
                all_texts_dict[time].append(text_content)

        fp.close()

    # export json file
    all_texts_json = json.dumps(all_texts_dict)
    f_json = open('data.json', 'w')
    f_json.write(all_texts_json)
    f_json.close()

    return all_texts_dict

# pre_process()