#SPIF - Sensitive and Private Information Filter

![alt text](http://dl.dropbox.com/u/43653358/logo01.PNG "")

A tool for filtering open data for private/sensitive information before publication

This Tool is developed during the RHoK Global Hackaton in Trento, Italy - Dec 1-2, 2012

The problem statement is at - http://www.rhok.org/problems/ffilter-tool-screening-open-data-privatesensitive-information-publication

We would like to have your feedback! 

##Features

Supports:
- text files, CSV
- XLS, XLSX, DOCX
- XML, HTML
- PDF

Filters:
- Social Security Number
- Credit Cards Number
- Telephone Number
- Bank Account Number

##Requirements/Dependencies

- Python 2.7 - http://www.python.org/
- OpenPyXL library - http://packages.python.org/openpyxl/
- PyPDF - http://pybrary.net/pyPdf/
- pmw  -http://sourceforge.net/projects/pmw/files/Pmw/ (This is mandatory to run the GUI version)

##Operating System
This script is indepent of the host platform (Windows, Linux or MacOS). All it needs is a Python interpretor.
We tested this script on:
- MacOs 10.6.4 
- Ubuntu 12.10 LTS 

##Usage
- Command Line Mode
<code>python spif.py filename.ext</code>
-GUI Mode
 <code>python main.py </code>
##Known issues

Not all pdf files are supported by PyPdf library, do not get surprised if the script is selective on pdf files as the conversion scheme matters. 
Docx conversion does not give the page number where a sensitive or private information is found. So it is a little course-grained.

##Authors
- Birhanu Eshete - birhanu.mekuria(at)gmail.com
- Ali Fawzi Najm Al-Shammari - afnfun(at)yahoo.com 
- Michele Fogarolli - michelefoga(at)gmail.com

##License 
This code is released under the [MIT License](http://opensource.org/licenses/MIT)

