import spider
from time import time
#a = "https://news.ycombinator.com/item?id=11814828"

t0 = time()
root = "https://news.ycombinator.com/"
b = "https://news.ycombinator.com/submitted?id=whoishiring"
posts = spider.log_crawl(b)
with open('output.json', 'w') as thefile:
	for a in posts:
		output = spider.wall_crawl(root+a)
		for item in output:
			thefile.write(str(item.encode('utf-8')))

print time() - t0