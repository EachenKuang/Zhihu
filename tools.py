# tools.py
#
import os
# 获取所有问题ID
questions = []
path = r'D:\Kuangyichen\Repository_py3\Zhihu\Data\topic_transgene_technology'
with open(path,'r',encoding='UTF8') as Reader:
    for line in Reader.readlines():
        if line.strip().isdigit():
            questions.append(int(line))

# 获取已经下载的问题ID
path = r"D:\Kuangyichen\Repository_py3\Zhihu\Data\Gene"
download = [int(i.split('#')[0]) for i in os.listdir(path)]


out = set(questions)-set(download)
print(len(out))
for i in out:
    print(i)