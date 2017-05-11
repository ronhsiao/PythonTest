# #encoding=utf-8
# import jieba
#
#
# content = open('D://TestAI.txt', 'rb').read()
#
# print("Input：", content)
#
# words = jieba.cut(content, cut_all=False)
#
# print("Output 精確模式 Full Mode：")
# for word in words:
#     print(word)
#

#encoding=utf-8
import jieba
import jieba.analyse


content = open('D://TestBD.txt', 'rb').read()

jieba.analyse.set_stop_words('D:\\words\\stopwords.txt')

tags = jieba.analyse.extract_tags(content, 500)
f = open('D:\\words\\BD.txt', 'a', encoding='UTF-8')
f.write(",".join(tags))