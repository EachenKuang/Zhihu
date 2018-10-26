# main.py
import os
from zhihu_oauth import ZhihuClient
from zhihu_oauth import Topic


def login():
    TOKEN_FILE = 'token.pkl'
    client = ZhihuClient()

    if os.path.isfile(TOKEN_FILE):
        client.load_token(TOKEN_FILE)
    else:
        client.login_in_terminal()
        client.save_token(TOKEN_FILE)

    """
    me = client.me()
    print('name', me.name)
    print('headline', me.headline)
    print('description', me.description)

    print('following topic count', me.following_topic_count)
    print('following people count', me.following_topic_count)
    print('followers count', me.follower_count)

    print('voteup count', me.voteup_count)
    print('get thanks count', me.thanked_count)

    print('answered question', me.answer_count)
    print('question asked', me.question_count)
    print('collection count', me.collection_count)
    print('article count', me.articles_count)
    print('following column count', me.following_column_count)

    # 获取最近 5 个回答
    for _, answer in zip(range(5), me.answers):
        print(answer.question.title, answer.voteup_count)

    print('----------')

    # 获取点赞量最高的 5 个回答
    for _, answer in zip(range(5), me.answers.order_by('votenum')):
        print(answer.question.title, answer.voteup_count)

    print('----------')

    # 获取最近提的 5 个问题
    for _, question in zip(range(5), me.questions):
        print(question.title, question.answer_count)

    print('----------')

    # 获取最近发表的 5 个文章
    for _, article in zip(range(5), me.articles):
        print(article.title, article.voteup_count)
    """
    topic = client.topic(19560072)  # 转基因
    # topic = client.topic(19578906)  # 气候变化
    # topic = client.topic(19551296)  # 网络游戏

    answers_count = 0
    # questions = topic.unanswered_questions
    for question in topic.unanswered_questions:
        print(question.id)
        print(question.title)
        print(question.answer_count)
        answers_count += question.answer_count
    print("总共有{0}个回答".format(answers_count))



login()

