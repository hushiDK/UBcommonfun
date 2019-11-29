# 删除数组中指定位置的元素
def del_shuzu(data,x):
    data.pop(x)
    return data
    
#  把data2中的数据按顺序插入到data1的空值项中
def merge_shuzu_0(data1, data2):
    number=0
    for i in range(len(data1)-1):
        if data1[i]=='':
            data1[i] = data2[number]
            number = number + 1
    return data1
