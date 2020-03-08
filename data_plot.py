import numpy as np
import matplotlib.pyplot as plt

if __name__ == "__main__":
	# positive = [0.95, 0.9065, 0.9029, 0.9, 0.8936]
	# negetive = [0.05, 0.0935, 0.0971, 0.1, 0.1064]

	p1 = [0.549668, 0.498587, 0.518210]
	p2 = [0.185899, 0.037811, 0.096527]
	p3 = [0.439312, 0.469300, 0.414042]

	n_groups = 3

	fig, ax = plt.subplots()

	index = np.arange(n_groups)
	bar_width = 0.2

	opacity = 0.4

	error_config = {'ecolor': '0.3'}

	rects1 = ax.bar(index, p1, bar_width,
                alpha=opacity, color='b',
                error_kw=error_config,
                label='star_rating')

	rects2 = ax.bar(index + bar_width, p2, bar_width,
                alpha=opacity, color='m',
                error_kw=error_config,
                label='helpful_factors')

	rects3 = ax.bar(index + bar_width + bar_width, p3, bar_width,
                alpha=opacity, color='r',
                error_kw=error_config,
                label='review_scores')


	ax.set_xticks(index + 2 * bar_width / 2)
	ax.set_xticklabels(('microwave', 'pacifier', 'hair_dryer'))

	ax.legend()
	plt.xlabel(u"product")
	plt.ylabel(u'entropy')
	 
	fig.tight_layout()
	plt.savefig('./img/entropy.png', dpi=200)
	plt.show()


def little(a, b):
	return a/(a + b), b/(a + b)
