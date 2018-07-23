# js404

This script is a penetration tester's recon tool to verify valid external javascript calls.

Inspired by this story of how an NHS developer mistakingly requested javascript from googlea**s**pis.com (extra 's'). A malicious actor was able to purchase the mispelling of the domain name and served malicious javascript to over 800 NHS pages.

https://www.bbc.co.uk/news/technology-26016802


requires phantomjs (apt-get install phantomjs or brew install phantomjs)

```

usage: js404.py [-h] -o output -u URL

Check for misspelled or expired external JS calls

optional arguments:
  -h, --help  show this help message and exit
  -o output   Output file to write to

required arguments:
  -u URL      Single URL to scan
 ``` 
  
  
 __e.g.:__
```
python js404.py -u http://localhost -o outfile
alickisjustsogreat.com <<< doesnt exist!
full error: https://alickisjustsogreat.com/countToTen.js
```
 
 will output a file only if positive results are found.
