import spider
from time import time
import pdfkit
#a = "https://news.ycombinator.com/item?id=11814828"

def getMonthlyPostings(filename, city):
	print "Getting postings, please wait up to 2-3 minutes..."

	#setting time
	t0 = time()

	#setting root
	root = "https://news.ycombinator.com/"
	
	posts = spider.findMonthPostings()

	#write to file
	with open(filename, 'w') as thefile:
		for a in posts:
			output = spider.findCityPostings(root+a, city)
			for item in output:
				thefile.write(str(item.encode('utf-8')))

    #calculate duration
	seconds = time() - t0
	m, s = divmod(seconds, 60)

	#print stats
	print "Total run time: %02d mins %02d seconds" % (m, s)
	print "Total postings: %d" % (spider.totalItems)
	print "See %s for selected postings" % filename

if __name__ == "__main__":
	textfile = "stdout.txt"
	city = "Toronto"
	getMonthlyPostings(textfile, city)
#	getIndividualPostings(textfile, city)