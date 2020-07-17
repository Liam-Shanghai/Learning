import csv
import numpy as np

def read_libsvm(input_file):
    """
    读取libsvm格式的数据集
    :param input_file: 数据集文件名
    :param max_feature: 数据集最大维
    :return: SVM的训练参数x,y
    """
    count = 0  # 样本个数
    y = []
    X=[]
    with open(input_file, 'r', newline='') as f:
        for num in f:
            x=[0]*300000
            num=num.split(" ")
            if num[0]=="1":
                y.append(1)
            else:
                y.append(-1)
            for num1 in num[1:]:
                a=num1.split(":")
                x[int(a[0])]=int(a[1])
            X.append(x)
    return X,y


def transform_libsvm(inputfile):
    """
    将libsvm格式转换成csv格式，保留原数据集
    :param inputfile: libsvm格式的数据集
    :param max_feature: 要转换的数据集的最大维
    :return: 输出csv格式的数据集
    """
    import numpy as np
    x, y = read_libsvm(inputfile)
    x=np.array(x)
    rows = x.shape[0]
    columns = x.shape[1]
    file = open(inputfile, "w+")
    for r in range(rows):
        print(r)
        r_line = ""
        for c in range(columns):
            temp = str(x[r, c]) + ","
            r_line += temp
        r_line += str(y[r])
        file.write(r_line + "\n")
    file.close()

if __name__ == '__main__':
    read_libsvm("C:\\Users\\wangs70\\6out.txt")
    transform_libsvm("C:\\Users\\wangs70\\a1a.csv")
