import os
from collections import OrderedDict


def print_author():
    authors = {}
    authors["匿名用户"]=0
    path = r"D:\Kuangyichen\Repository_py3\Zhihu\Data\Gene"
    folders = os.listdir(path)
    for folder in folders:
        files = os.listdir(path+os.sep+folder)
        for file in files:
            name = file.split('.')[0]
            if "匿名用户" in name:
                authors["匿名用户"] += 1
                break
            if name in authors:
                authors[name] += 1
            else:
                authors[name] = 1

    author_inorder = OrderedDict(reversed(sorted(authors.items(), key=lambda t: t[1])))
    for key,value in author_inorder.items():
        print(key+':'+str(value))

def analyze(authors, client):
    """
    分析每个作者的结构信息
    :param authors: [str,str,...]
    :return:
    """
    for id in authors:
        people = client.people(id)
        print(id,sep='\t')

if __name__ == '__main__':
    pass
