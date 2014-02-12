import urllib, sys
from HTMLParser import HTMLParser

class URLLister(HTMLParser):
    def reset(self):
        HTMLParser.reset(self)
        self.urls = []
        self.src = []
        self.srcs = []
        self.alts = []
	last_src = ''

    def handle_starttag(self, tag, attrs):
        try:
            # get handler for tag and call it e.g. self.start_a
            getattr(self, "start_%s" % tag)(attrs)
        except AttributeError:
            pass

    def start_a(self, attrs):
        href = [v for k, v in attrs if k == "href"]
        if href:
	    #print href
            self.urls.extend(href)
    def start_img(self, attrs):
        src = [v for k, v in attrs if k == "src"]
	alt = [v for k, v in attrs if k == "alt"]
	if(src and alt):	
		self.srcs.extend([(src[0],alt[0])])

def get_all_urls(depth,url_obj,rootUrl,result):
	""" gets child urls of any given url. This function is called recursively depth times """
	for urls in url_obj:
	    	if(urls[0] == '/' or urls[0] == '.'):
			url = rootUrl+urls
		if(urls[:4] == "http"):
			usock = urllib.urlopen(urls)
			parser = URLLister()
			parser.feed(usock.read())
			usock.close()
			parser.close()
			for url in parser.urls:
			    if(url[0] == '/' or url[0] == '.'):
				url = rootUrl+url
			for src in parser.srcs:
				result.extend(src)
			if depth == 0:
				return result 
			else:
				result = get_all_urls((depth-1),parser.urls,url,result)
				return result
			
def imageCrawler(rootUrl,depth):
	""" Function called by the user for getting images in the given url and urls at a given depth """
	srcPairs = []
	result = get_all_urls((depth-1),[rootUrl],rootUrl,srcPairs)
	return result
