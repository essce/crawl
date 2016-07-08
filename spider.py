import requests
from bs4 import BeautifulSoup
from pprint import pprint
import re

def wall_crawl(link):
	r = requests.get(link)
	page = r.content
	soup = BeautifulSoup(page, "html.parser")

	allComments = soup.findAll('span', {'class':'c00'})

	postings = [comments.get_text() for comments in allComments]
	posts = []

	for post in postings: 
		re1='.*?'	# Non-greedy match on filler
		re2='(Toronto)'	# Word 1

		rg = re.compile(re1+re2,re.IGNORECASE|re.DOTALL)
		m = rg.search(post)

		if m:
			#posts.append(m.group(1))
			posts.append(post)

	print "total items: ", len(posts)

	return posts

def log_crawl(link):
	r = requests.get(link)
	page = r.content
	soup = BeautifulSoup(page, "html.parser")

	hiring = []

	allLinks = soup.findAll('a', href=True)
	#hirePosts = [a.get_text() for a in allLinks]

	for a in allLinks:
		re1='.*?'
		re2='(hiring)'
		re3='(\\?)'	# Any Single Character 1

		rg = re.compile(re1+re2+re3, re.IGNORECASE|re.DOTALL)
		m = rg.search(a.get_text())

		if m:
			hiring.append(a['href'])

	return hiring

'''
for a in allLinks:
	print "URL:\t", a['href']
'''