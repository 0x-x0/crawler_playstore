#!/usr/bin/python
import argparse
import urlparse
import urllib
from bs4 import BeautifulSoup

parser = argparse.ArgumentParser()
parser.add_argument("-u", "--url", help="Url to crawl",action="store_true")
parser.add_argument('args', nargs=argparse.REMAINDER)
args = parser.parse_args()

def main():
	try:
		url = args.args[0];
	except:
		print("Usage: python crawler.py -u URL ")
		
	if args.url:
		try:
			response = urllib.urlopen(url).read()
			soup = BeautifulSoup(response,"lxml")
			name = soup.findAll(attrs={"itemprop" : "name"})
			appName = name[0].div.string
			lastUpdate = soup.findAll(attrs={"itemprop" : "datePublished"})
			updateDate = lastUpdate[0].string
			print ('\n' + appName + ' was last updated on ' + updateDate + '\n' )
		except:
			print 'Error:Cannot fetch details from the specified URL' 
			
if __name__ == '__main__':
	main()
