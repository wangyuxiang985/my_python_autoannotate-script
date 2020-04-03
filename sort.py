"""
[
[4, 6, "术后"], [6, 8, "康复"], [0, 3, "膝关节"],
[3, 6, "手术后"], [3, 5, "手术"], [6, 10, "康复锻炼"],
[8, 10, "锻炼"], [0, 5, "膝关节手术"], [0, 6, "膝关节手术后"],
[1, 3, "关节"], [9, 10, "炼"], [0, 1, "膝"]
]
"""
def remove_duplicate():
    labels = [[4, 6, "术后"], [6, 8, "康复"], [0, 3, "膝关节"], [3, 6, "手术后"], [3, 5, "手术"], [6, 10, "康复锻炼"], [8, 10, "锻炼"], [0, 5, "膝关节手术"], [0, 6, "膝关节手术后"], [1, 3, "关节"], [9, 10, "炼"], [0, 1, "膝"]]
    list2 = sorted(labels, key=lambda x: (x[0], -x[1]))

    new_labels = []
    x, y = 0, 0
    print(list2)

    for index in list2:
        if new_labels == []:
            new_labels.append(index)
        else:
            if new_labels[len(new_labels) -1][1] <= index[0]:

                new_labels.append(index)
    print(new_labels)
    # for index in range(0, len(list2)):
    #     if index == 0:
    #         new_labels.append(list2[index])
    #     else:
    #         if new_labels[len(new_labels) -1][1] < list2[index][0]:
    #             new_labels.append(list2[index])




if __name__ == '__main__':
    remove_duplicate()