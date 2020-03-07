import jieba
import re


def split_word(text):
	pattern1 = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') #匹配标点符号的正则表达式
	pattern2 = re.compile(r'<br />') #匹配一些无用符号的正则表达式
	pattern3 = re.compile('<BR>')
	text = re.sub(pattern1, '', text)
	text = re.sub(pattern2, ' ', text)
	text = re.sub(pattern3, ' ', text)
	# print(text)

	seg_list_exact = jieba.cut(text, cut_all = False) # 精确模式分词
	# print(seg_list_exact)
	all_words = []
	remove_words = [' ', ',', '!', "'"]#去除词库
	for word in seg_list_exact: # 循环读出每个分词
		if word not in remove_words:
			all_words.append(word) # 分词追加到列表
	return all_words