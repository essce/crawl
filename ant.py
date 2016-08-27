import spider
from time import time
import pdfkit
#a = "https://news.ycombinator.com/item?id=11814828"

def fire(filename):
	t0 = time()
	root = "https://news.ycombinator.com/"
	b = "https://news.ycombinator.com/submitted?id=whoishiring"
	posts = spider.log_crawl(b)
	with open(filename, 'w') as thefile:
		for a in posts:
			output = spider.wall_crawl(root+a)
			for item in output:
				thefile.write(str(item.encode('utf-8')))

	print time() - t0


def water():
	link = "https://news.ycombinator.com/item?id=12016568"
	with open("stdout.txt", 'w') as thefile:
		output = spider.wall_crawl(link)
		for item in output:
			thefile.write(str(item.encode('utf-8')))		

def chop(filename):
	f = open(filename,"r")
	lines = f.readlines()
	f.close()

	f = open(filename,"w")
	for line in lines:
		if (line!="reply\n"):
			f.write(line)
	f.close()

def wrapit(filename):
	options = {
	    'page-size': 'Letter',
	    'margin-top': '0.75in',
	    'margin-right': '0.75in',
	    'margin-bottom': '0.75in',
	    'margin-left': '0.75in',
	    'encoding': "UTF-8",
	    'no-outline': None
	}

	#f = open(filename, "r")
	#lines = f.readlines()
	config = pdfkit.configuration(wkhtmltopdf='/Users/stanleychin/.ws/python_ws/scraping/venv/lib/python2.7/site-packages/wkhtmltopdf')
	#pdfkit.from_file(filename, "output.pdf", configuration=config, options=options)
	with open(filename) as f:
		pdfkit.from_file(f, "output.pdf", configuration=config, options=options)


if __name__ == "__main__":
	textfile = "stdout.txt"
	fire(textfile)
	chop(textfile)
	#wrapit(textfile)