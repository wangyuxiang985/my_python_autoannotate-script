"""
数据转excel
"""
import io
import json

import xlwt

def get_scores(infile):
    """读取标注字典数据"""
    date = io.open(infile, mode='r', encoding='UTF-8')
    scores = {}
    for index in date:
        my_json = json.loads(index)
        annotations = my_json['annotations']
        text = my_json['text']
        for annotation in annotations:
            start_offset = annotation['start_offset']
            end_offset = annotation['end_offset']
            keyword = text[start_offset:end_offset]
            scores[keyword] = annotation['label']
    return scores

def main():
    scores = get_scores('D:\dictionry.json')

    workbook = xlwt.Workbook(encoding='UTF-8')
    worksheet = workbook.add_sheet('My Worksheet')
    style = xlwt.XFStyle()  # 初始化样式
    font = xlwt.Font()  # 为样式创建字体
    font.name = 'Times New Roman'
    font.bold = True  # 黑体
    font.underline = True  # 下划线
    font.italic = True  # 斜体字
    style.font = font  # 设定样式
    # 参数对应 行, 列, 值
    # worksheet.write(0, 0, 'Unformatted value')  # 不带样式的写入
    # worksheet.write(1, 0, 'Formatted value', style)  # 带样式的写入
    i = 0
    for index in scores:
        worksheet.write(i, 0, index)
        worksheet.write(i, 1, scores[index])
        i += 1

    workbook.save('formatting.xls')  # 保存文件


if __name__ == '__main__':
    main()