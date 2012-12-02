#SPIF-Sensitive and Private Information Filterer

![picture alt](/spif/blob/master/logos/logo01.PNG "")  

A tool for filtering open data for private/sensitive information before publication

This Tool is developed during the RHoK Global Hackaton in Trento, Italy - Dec 1-2, 2012

The problem statement is at - http://www.rhok.org/problems/ffilter-tool-screening-open-data-privatesensitive-information-publication

##Features

- supports text files, CSV, PDFs, XLS, XLSX, XML, HTML 
- filters SSNs - Social Security Number
- filters CCNs - Credit Cards Number
- firters Telephone Numbers
- filters Bank Account Numbers

##Requirements/Dependencies

- Python 2.7 - http://www.python.org/
- OpenPyXL library - http://packages.python.org/openpyxl/
- PyPDF - http://pybrary.net/pyPdf/

##Operating System

We tested this script on:
- MacOs 10.6.4 
- Ubuntu 12.10 LTS

##Usage

<code>python spif.py filename.ext</code>

##Known issues

##Authors
Birhanu Eshete - birhanu.mekuria(at)gmail.com
Ali Fawzi Najm Al-Shammari - afnfun(at)yahoo.com 
Michele Fogarolli - michelefoga(at)gmail.com


