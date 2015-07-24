# worldipv6launch-info
Info from worldipv6launch (http://www.worldipv6launch.org/apps/ipv6week/measurement/timeline-nets.html)

You need python module pyquery
```
sudo apt-get install python-pyquery
```
Usage:

Get NL (Netherlands) IPv6 usage:
```
$ python get-worldipv6launch-info.py | grep -e "^NL  ---"
NL  --- XS4ALL-NL XS4ALL Internet BV  --- 31.71%
NL  --- KPN KPN Internet Solutions  --- 2.50%
NL  --- ZEELANDNET ZeelandNet BV  --- 3.09%
NL  --- ZIGGO Ziggo B.V.  --- 0.17%
NL  --- NL-SOLCON SOLCON  --- 2.93%
NL  --- EDUTEL-AS Edutel B.V.  --- 1.24%
NL  --- UTWENTE-AS University Twente  --- 21.33%
NL  --- AMS-IX1 Amsterdam Internet Exchange B.V.  --- 47.41%
NL  --- NL-BIT BIT BV  --- 2.41%
NL  --- COMPUKOS-AS DirectVPS B.V.  --- 41.37%
NL  --- DUOCAST-AS Duocast B.V.  --- 1.78%
NL  --- LUNA Luna.nl B.V.  --- 4.19%
NL  --- COLOCLUE-AS Netwerkvereniging Coloclue, Amsterdam, Netherlands  --- 0.77%
NL  --- OXILION-AS Oxilion B.V.  --- 1.45%
NL  --- PCEXTREME PCextreme B.V.  --- 16.03%
NL  --- SIDN Stichting Internet Domeinregistratie Nederland  --- 9.91%
NL  --- SURFNET-NL SURFnet, The Netherlands  --- 0.85%
NL  --- SIGNET-AS Signet B.V.  --- 0.53%

```

Get top IPv6 usage ISPs:
```
$ python get-worldipv6launch-info.py | grep '%' | awk '{print $NF,$0}' |  sort -nr | cut -f2- -d' ' | head
AU  --- NINEWIRE-AS-AP NineWire Pty Ltd  --- 99.94%
DE  --- SPEEDPARTNER SpeedPartner GmbH  --- 99.31%
IT  --- FUSOLAB Fusolab Onlus  --- 86.17%
BR  --- UNIVERSIDADE ESTADUAL DE PONTA GROSSA  --- 84.39%
US  --- LSU-1 - Louisiana State University  --- 78.78%
IT  --- TOPIX-AS Consorzio Topix - Torino e Piemonte Exchange Point  --- 73.73%
FR  --- HIVANE Hivane  --- 73.43%
US  --- GOOGLE-FIBER - Google Fiber Inc.  --- 71.77%
US  --- CELLCO-PART - Cellco Partnership DBA Verizon Wireless  --- 70.27%
BR  --- FUNDACAO PARQUE TECNOLOGICO ITAIPU - BRASIL  --- 68.38%
```

Get Belgium ISPs usage, sorted on usage:
```
$ python get-worldipv6launch-info.py  | grep -e "^BE" | grep "%" | awk '{print $NF,$0}' |  sort -nr | cut -f2- -d' '
BE  --- ASBRUTELE Brutele SC  --- 61.90%
BE  --- TELENET-AS Telenet N.V.  --- 43.10%
BE  --- BELGACOM-SKYNET-AS BELGACOM S.A.  --- 24.79%
BE  --- BELNET BELNET  --- 5.84%
BE  --- EDPNET EDPNET  --- 0.91%
```
