#!/usr/bin/env python
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
'''
# Example usage: print country for an ASN:
print asn2country["3320"]
print asn2country["3265"]

print asn2country["3320"]
print asn2country["3265"]
'''


html = pq(url="http://www.worldipv6launch.org/apps/ipv6week/measurement/timeline-nets.html")

for isp in [[td.text for td in tr] for tr in html("tr")]:
	try:
		# Format as of September 2015
		# ['12', 'Liberty Global', '5089, 6830, 20825, 29562', '5.57%']
		firstasn=isp[2].split(',')[0]
		country = asn2country[firstasn]
		ispname = asn2name[firstasn]
		print country, " ---", ispname, " ---", isp[3]
	except:
		print "Problem with", isp
		pass


