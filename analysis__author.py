import os
from collections import OrderedDict
from zhihu_oauth import ZhihuClient


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
        yield client.people(id)
        # print(id,sep='\t')


def get_authors_from_files(file_path):
    with open(file_path, 'r', encoding='utf8') as Reader:
        # return [line.split('#')[0] for line in Reader.readlines()[1:]]
        for line in Reader.readlines()[1:]:
            yield line.split('#')[0]


if __name__ == '__main__':

    client = ZhihuClient()
    client.load_token('token.pkl')

    authors_file_path = r"Data\author_left"
    authors_list = get_authors_from_files(authors_file_path)
    # print(authors_list)

    # person feature
    # (name\gender\follower_count\following_count\thanked_count\collected_count\
    # answer_count\article_count
    # voteup_count\question_count\*locations\*employments\*educations)

    for person in analyze(authors_list, client):
        if person.over:
            print(person.id,person.over_reason,sep='\t')
            continue
        print(person.id, person.name, person.gender, person.follower_count,
              person.following_count, person.voteup_count, person.thanked_count,
              person.collected_count, person.answer_count, person.question_count, person.article_count,
              [location.name for location in person.locations][0] if any(location.name for location in person.locations) else None,
              sep='\t',end='\n')
