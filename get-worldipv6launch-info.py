# -*- coding: utf-8 -*-

#import itertools
from pyquery import PyQuery as pq

# First fill ASN dictionary:
import re
# autnums.html is from http://bgp.potaroo.net/cidr/autnums.html
asn2country = {}
asn2name = {}
for line in open("autnums.html",'r'):
	# search lines like: 
	# <a href="/cgi-bin/as-report?as=AS1128&view=2.0">AS1128 </a> TUDELFT-NL DTO TUDELFT, The Netherlands - AS,NL
	# <a href="/cgi-bin/as-report?as=AS18&view=2.0">AS18   </a> UTEXAS - University of Texas at Austin,US
	try:
		asn, name, country = re.match(r".*AS(\d+).*\> (.*)\,(.*)", line).group(1,2,3)	# last occurences are matched
		#print asn, "---", name, "---", country
		asn2country[asn] = country
		asn2name[asn] = name
	except:
		pass
print asn2country["3320"]
print asn2country["3265"]

print asn2country["3320"]
print asn2country["3265"]

'''
html = pq(url="http://www.worldipv6launch.org/apps/ipv6week/measurement/timeline-nets.html")
for isp in [[td.text for td in tr] for tr in html("tr")]:
	try:
		# ['XS4ALL', '3265', '55.23%', '24']
		if isp[0].lower().find("xs4all") >= 0 :
			print "GEVONDEN", isp
			asn = isp[1]
			country = asn2country[asn]
			print "country is", country
		if isp[0].lower().find("telenet") >= 0 :
			print "GEVONDEN", isp
			asn = isp[1]
			country = asn2country[asn]
			print country
	except:
		pass
'''

html = pq(url="http://www.worldipv6launch.org/apps/ipv6week/measurement/timeline-nets.html")
for isp in [[td.text for td in tr] for tr in html("tr")]:
	try:
		# [None, '6389, 7018, 7132', '39.63%', '2']
		# ['XS4ALL', '3265', '55.23%', '24']
		# [None, '2516', '19.33%', '3']
		'''
		>>> isp = [None, '638', '39.63%', '2']
		>>> isp[1].split(',')[0]
		'638'

		>>> isp = [None, '6389, 7018, 7132', '39.63%', '2']
		>>> isp[1].split(',')[0]
		'6389'
		'''
		firstasn = isp[1].split(',')[0]
		#print "firstasn", firstasn
		#print "ISP is", isp[0]
		#asn = isp[1]
		
		country = asn2country[firstasn]
		ispname = asn2name[firstasn]
		print country, " ---", ispname, " ---", isp[2]
	except:
		pass

'''
html = pq(url="http://www.worldipv6launch.org/apps/ipv6week/measurement/timeline-nets.html")
for isp in [[td.text for td in tr] for tr in html("tr")]:
	try:
		# ['XS4ALL', '3265', '55.23%', '24']
		asn = isp[1]
		country = asn2country[asn]
		#print isp, country
		if country == "BE":
			print "BE ISP", isp

	except:
		pass

'''


