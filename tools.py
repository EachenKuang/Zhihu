# tools.py
#
import os
from zhihu_oauth import ZhihuClient

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

    TOKEN_FILE = 'token.pkl'
    client = ZhihuClient()

    if os.path.isfile(TOKEN_FILE):
        client.load_token(TOKEN_FILE)
    else:
        client.login_in_terminal()
        client.save_token(TOKEN_FILE)
    path = r'D:\Kuangyichen\Repository_py3\Zhihu\Data\lefted'
    questions = []
    with open(path, 'r', encoding='UTF8') as Reader:
        for line in Reader.readlines():
            questions.append(int(line))
    for q in questions:
        question_t = client.question(q)
        print(str(q)+"start")
        for answer in question_t.answers:
            print(answer.author.id, answer.author.name)
            answer.save('Data\\Gene\\' + str(question_t.id) + '#' + question_t.title,
                        str(answer.author.id) + '#' + answer.author.name)
        print(str(q) + "end")