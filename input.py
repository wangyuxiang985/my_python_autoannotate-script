import io
import json
import time
import os

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

def targer_file(infile):
    """
    读取待标注文件
    文件格式：{"text": "\u819d\u5173\u8282\u672f\u540e\u600e\u6837\u5eb7\u590d\u8bad\u7ec3\uff1f"}
    """
    datas = io.open(infile, mode='r', encoding='UTF-8')
    lists = [json.loads(index)['text'] for index in datas]
    return lists

def targer_file2(infile):
    """
    读取待标注文件
    文件格式：{"id": 35756, "text": "膝盖退行性病变 膝关节置换手术后10天，还无法站立;膝盖退行性病变;4月16日入院，18日做了右腿膝关节置换手术，23日出院。出院后一直在家里按照关注的JST矫形护理视频进行肌肉锻炼，肌肉操的前三节自己都能做，但第四节的直腿抬高运动始终抬不起来。腿软弱无力，完全无法站立，更没法行走，目前只在床上躺着。;是否手术后的正常现象？什么时候能站立行走？还需要注意什么？;大于半年;积水潭医院 矫形骨科;【手术】：4月18日做完右腿膝关节置换手术，23号出院，之后按照肌肉操每天锻炼，但做手术的腿一直软弱无力，无法站立。（2019-04-28填写）", "meta": {}, "annotation_approver": null, "labels": []}
    """
    datas = io.open(infile, mode='r', encoding='UTF-8')
    lists = [json.loads(index)['text'] for index in datas]
    return lists

def write_json(admin, filename):
    """将admin文件追加到filename中"""
    with open(filename, 'a+') as file_obj:
        json.dump(admin, file_obj)
        file_obj.write('\n')



def get_text_labels(id):
    lables_new = io.open('D://project_3_labels.json', mode='r', encoding='UTF-8')
    for index in lables_new:
        loads = json.loads(index)
        if loads['id'] == id:
            return loads['text']

def remove_duplicate(labels):
    """
    将labels去重
    """
    # labels = [[4, 6, "术后"], [6, 8, "康复"], [0, 3, "膝关节"], [3, 6, "手术后"], [3, 5, "手术"], [6, 10, "康复锻炼"], [8, 10, "锻炼"], [0, 5, "膝关节手术"], [0, 6, "膝关节手术后"], [1, 3, "关节"], [9, 10, "炼"], [0, 1, "膝"]]
    # sorted(labels, key=lambda x: (x[0], -x[1])) [[0, 6, '膝关节手术后'], [0, 5, '膝关节手术'], [0, 3, '膝关节'], [0, 1, '膝'], [1, 3, '关节'], [3, 6, '手术后'], [3, 5, '手术'], [4, 6, '术后'], [6, 10, '康复锻炼'], [6, 8, '康复'], [8, 10, '锻炼'], [9, 10, '炼']]
    # sorted(labels) [[0, 1, '膝'], [0, 3, '膝关节'], [0, 5, '膝关节手术'], [0, 6, '膝关节手术后'], [1, 3, '关节'], [3, 5, '手术'], [3, 6, '手术后'], [4, 6, '术后'], [6, 8, '康复'], [6, 10, '康复锻炼'], [8, 10, '锻炼'], [9, 10, '炼']]

    list2 = sorted(labels, key=lambda x: (x[0], -x[1]))
    new_labels = []

    for index in list2:
        if new_labels == []:
            new_labels.append(index)
        else:
            if new_labels[len(new_labels) -1][1] <= index[0]:
                new_labels.append(index)
    return new_labels


def handle(dictionary, lists, out_filename):
    """根据字典数据标注文件"""
    i = 2
    for index in lists:
        # {"text": "膝关节腘窝囊肿术后康复", "labels": [[0, 7, "疾病"], [7, 9, "病程"]]}
        admin = {}
        admin['text'] = index
        admin['labels'] = []
        for dic in dictionary:
            aaa = index.find(dic)
            if aaa != -1:
                # 添加到labels中
                lable_text = get_text_labels(dictionary[dic])
                admin['labels'].append([aaa, aaa+len(dic), lable_text])
        # 去重
        admin['labels'] = remove_duplicate(admin['labels'])
        # 追加到文件中
        write_json(admin, out_filename)
        # 保证文件一直小于1MB
        if os.path.getsize(out_filename)/1024 > 900:
            new_json = str(i) + '.json'
            i += 1
            out_filename = out_filename.replace('.json', new_json)

    #time_end = time.time()
    #print('处理文件结束,时间：', time_end)
    #print('程序运行：', time_end - time_start)

def main(input_basefile, output_basefile, dictinory_basefile):
    """
    input_basefile: 待标注文件所在文件夹路径
    output_basefile: 标注完文件输出文件夹路径
    dictinory_basefile: 字典文件路径
    """
    filenames = os.listdir(input_basefile)
    # 读取字典数据
    scores = get_scores(dictinory_basefile)

    for filename in filenames:
        """循环读取待标注文件"""
        print('%s,文件开始' % filename)
        time_start = time.time()

        lists = targer_file(input_basefile + filename)
        handle(scores, lists, output_basefile + filename)

        time_end = time.time()
        print('程序运行：', time_end - time_start)


if __name__ == '__main__':
    # scores = get_scores('D:\dictionry.json')
    # print(scores)
    # lists = targer_file('C://Users//wb-wyx657769//Desktop//脚本//未标注//3-chunyuyisheng_qa_bak.json')
    # # # print(lists)
    # # labels = get_id_labels('D://project_3_labels.json', 2)
    # # print(labels)
    # handle(scores, lists, 'D://3-chunyuyisheng_qa_bak.json')
    # admin = {"text": "膝关节腘窝囊肿术后康复", "labels": [[0, 7, "疾病"], [7, 9, "病程"]]}
    # write_json(admin, 'D://test123.json')
    # write_json(admin, 'D://test123.json') 自动标注脚本
    input_basefile = 'file/未标注/'
    # input_basefile = 'C://Users//wb-wyx657769//Desktop//脚本//未标注0121//'
    output_basefile = 'file/脚本标注/'
    # output_basefile = 'C://Users//wb-wyx657769//Desktop//脚本//脚本标注0121//'
    dictinory_basefile = 'file/dictionry.json'
    main(input_basefile, output_basefile, dictinory_basefile)


