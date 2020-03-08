import numpy as np 
import pandas as pd 
import pickle
import matplotlib.pyplot as plt #图像展示库
import re	#正则表达式库
import collections	#词频统计库
import jieba	#结巴分词
import wordcloud	#词云库
from PIL import Image	#图像处理库


def word2cloud(text):
	pattern1 = re.compile(u'\t|\n|\.|-|:|;|\)|\(|\?|"') #匹配标点符号的正则表达式
	pattern2 = re.compile(r'<br />') #匹配一些无用符号的正则表达式
	pattern3 = re.compile('<BR>')
	text = re.sub(pattern1, '', text)
	text = re.sub(pattern2, ' ', text)
	text = re.sub(pattern3, ' ', text)
	# print(text)

	seg_list_exact = jieba.cut(text, cut_all = False) # 精确模式分词
	# print(seg_list_exact)
	object_list = []
	remove_words = [' ', 'the', 'I', ',', 'it', 'and', 'a', 'to', 'hair', "'"
	, 'is', 'my', 'this', 'for', '!', 'of', 'that', 'in', 'have', 'was', 'with'
	, 'It', 'but', 't', 'on', 'one', 'not', 's', 'so', 'as', 'The'
	, 'very', 'you', 'use', 'had', 'than', 'has', 'be', 'dry', 'just', 'out'
	, 'blow', 'at', 'time', 'product', 'This', 'used', 'me', 'when', 'can', 'cord'
	, 'about', 'are', 'really', 'or', 'only', 'becaues', 'works', 'get'
	, 'more', 'all', 'does']#去除词库
	for word in seg_list_exact: # 循环读出每个分词
	    if word not in remove_words: # 如果不在去除词库中
	        object_list.append(word) # 分词追加到列表

	# 词频统计
	word_counts = collections.Counter(object_list) # 对分词做词频统计
	word_counts_top10 = word_counts.most_common(20) # 获取前10最高频的词
	# print (word_counts_top10) # 输出检查

	# 词频展示
	mask = np.array(Image.open('./img/background.jpg')) # 定义词频背景
	wc = wordcloud.WordCloud(
	    background_color='white', # 设置背景颜色
	    # font_path='/System/Library/Fonts/Hiragino Sans GB.ttc', # 设置字体格式
	    mask=mask, # 设置背景图
	    max_words=200, # 最多显示词数
	    max_font_size=100 , # 字体最大值
	    scale=10  # 调整图片清晰度，值越大越清楚
	)

	wc.generate_from_frequencies(word_counts) # 从字典生成词云
	image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
	wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
	wc.to_file("./img/temp.jpeg") # 将图片输出为文件
	plt.imshow(wc) # 显示词云
	plt.axis('off') # 关闭坐标轴
	plt.show() # 显示图像


if __name__ == "__main__":
	# classifier_f = open("./bayes_model/naivebayes.pickle", "rb")
	# classifier = pickle.load(classifier_f)
	# classifier_f.close()
	# classifier.show_most_informative_features(100)
	# class_ = classifier.prob_classify({"good":True})
	# print(class_.prob(1), class_.prob(0))
	good_dic = {"works":21,
			"nice":9.7,
			"great":9.3,
			"Excellent":9.0,
			"price":8.4,
			"fine":8.3,
			"best":7.0,
			"lot":6.3,
			"fits":6.3,
			"cell":6.1,
			"free":5.7,
			"years":5.7,
			"highly":5.0,
			"Jabra":5.0,
			"without":5.0,
			"handas":5.0,
			"high":4.6,
			"quick":4,
			"well":4,
			"semm":4,
			"ears":4,
			"working":4
			}
	mask = np.array(Image.open('./img/good_cloud.jpg')) # 定义词频背景
	wc = wordcloud.WordCloud(
	    background_color='white', # 设置背景颜色
	    # font_path='/System/Library/Fonts/Hiragino Sans GB.ttc', # 设置字体格式
	    mask=mask, # 设置背景图
	    max_words=200, # 最多显示词数
	    max_font_size=100 , # 字体最大值
	    scale=10  # 调整图片清晰度，值越大越清楚
	)
	wc.generate_from_frequencies(good_dic) # 从字典生成词云
	image_colors = wordcloud.ImageColorGenerator(mask) # 从背景图建立颜色方案
	wc.recolor(color_func=image_colors) # 将词云颜色设置为背景图方案
	wc.to_file("./img/good.jpeg") # 将图片输出为文件
	plt.imshow(wc) # 显示词云
	plt.axis('off') # 关闭坐标轴
	plt.show() # 显示图像	
























