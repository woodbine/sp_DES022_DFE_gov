# -*- coding: utf-8 -*-

import scraperwiki
import urllib2
from datetime import datetime
from bs4 import BeautifulSoup

# Set up variables
entity_id = "DES022_DFE_gov"
url = "https://www.gov.uk/government/collections/dfe-department-and-executive-agency-spend-over-25-000"

# Set up functions
def convert_mth_strings ( mth_string ):
	month_numbers = {'Jan': '01', 'Feb': '02', 'Mar':'03', 'Apr':'04', 'May':'05', 'Jun':'06', 'Jul':'07', 'Aug':'08', 'Sep':'09','Oct':'10','Nov':'11','Dec':'12' }
	#loop through the months in our dictionary
	for k, v in month_numbers.items():
		#then replace the word with the number
		mth_string = mth_string.replace(k, v)
	return mth_string

# pull down the content from the webpage
html = urllib2.urlopen(url)
soup = BeautifulSoup(html)

# find all entries with the required class
blocks = soup.findAll('li', {'class':'publication document-row'})

for block in blocks:

	link = block.a['href']

	# add the right prefix onto the url
	pageUrl = link.replace("/preview","")
	pageUrl = pageUrl.replace("/government","http://www.gov.uk/government")
	
	html2 = urllib2.urlopen(pageUrl)
	soup2 = BeautifulSoup(html2)
	
	fileBlocks = soup2.findAll('div',{'class':'attachment-details'})
	
	for fileBlock in fileBlocks:
		fileUrl = fileBlock.a['href']
		title = fileBlock.h2.contents[0]
		fileUrl = fileUrl.replace("/government","http://www.gov.uk/government")
		print title
		
		if title.has_attr('href')
			print "not a csv"
		else:
			# create the right strings for the new filename
			csvYr = title.split(' ')[-1]
			csvMth = title.split(' ')[-2][:3]
			csvMth = convert_mth_strings(csvMth);
		
			filename = entity_id + "_" + csvYr + "_" + csvMth
		
			todays_date = str(datetime.now())
		
			scraperwiki.sqlite.save(unique_keys=['l'], data={"l": fileUrl, "f": filename, "d": todays_date })
