

import os
import io
import json
def main(len):
    print(len)
    filenames = os.listdir('C://Users//wb-wyx657769//Desktop//脚本//未标注//')
    for filename in filenames:
        """读取待标注文件"""
        datas = io.open('C://Users//wb-wyx657769//Desktop//脚本//未标注//' + filename, mode='r', encoding='UTF-8')
        getsize = os.path.getsize('C://Users//wb-wyx657769//Desktop//脚本//未标注//' + filename)
        print('*****', getsize / 1024)
        filepath = 'C://Users//wb-wyx657769//Desktop//脚本//未标注//' + filename
        print(filepath)
        new_filepath = filepath.replace('.json', '1.json')
        print(new_filepath)
        lists = [json.loads(index)['text'] for index in datas]
        print(lists)



if __name__ == '__main__':
    main(111)
