import sys
import re
import pyPdf
from openpyxl.reader.excel import load_workbook
import iban
	
def main():
	if len(sys.argv)<2 or len(sys.argv)>2:
		print "======================================================"
		print "Too few or too many arguments. I just need a filename."
		print "======================================================"
	
 
	filename=sys.argv[1]
	extension=filename.split(".")[-1]
	if (extension=="xlsx"):
		spif_spreadsheet(filename)
	elif (extension=="txt") or(extension=="xml"):
		spif_text_file(filename)
	elif (extension=="doc"):
		spif_word_doc(filename)
	elif (extension=="pdf"):
		spif_pdf_doc(filename)
	elif (extension=="csv") or (extension=="sql"):
		spif_csv_file(filename)
	elif (extension=="docx"):
		os.system("python docx2txt.py "+filename+" > docx_to_txt.txt")
		filename=docx_to_txt.txt
		spif_text_file(filename)
	elif (extension=="xls"):
                os.system("python xls2txt.py "+filename+" > xls_to_txt.txt")
                filename=xls_to_txt.txt
                spif_text_file(filename)
	else:
		spif_unknown_format()

# give ur execuse for unknown format
def spif_unknown_format():
	print "==================================================="
	print "Oops! I am not yet able to parse this type of file."
	print "==================================================="

# filter Execel 2007 using openpyxl
def spif_spreadsheet(filename):
	workbook=load_workbook(filename)
	print "WorksheetName\t\tCell\t\tValue\t\t\t\tWhat"
	print "-------------\t\t----\t\t-----\t\t\t\t----"
	for worksheet in workbook.worksheets:
		title=worksheet.title
		for row in worksheet.rows:
			values=[]
			for cell in row:
				row_column=cell.get_coordinate()
				value=cell.value
				if value is None:
					value=''
				if not isinstance(value, unicode):
					value=unicode(value)
				value=value.encode('utf8')
				if looks_like_ssn(value):
					type="Social Security Number"
                                        print  title,"\t\t", row_column,"\t\t",value,"\t\t\t\t",type
				if looks_like_ccn(value):
					type="Credit Card Number"
                                        print  title,"\t\t", row_column,"\t\t",value,"\t\t\t\t",type
				if looks_like_iban(value):
					print "Bank Account Number"
					print  title,"\t\t", row_column,"\t\t",value,"\t\t\t\t",type
				if looks_like_phone_number(value):
					print "Telephone Numbe"
	                                print  title,"\t\t", row_column,"\t\t",value,"\t\t\t\t",type
	
# filter txt files
def spif_text_file(filename):
	data=open(filename)
	line_number=1
	print "Line #\t\tValue\t\t\t\tWhat"
	print "------\t\t-----\t\t\t\t----"
	for line in data.readlines():
		tokens=line.split(' ')
		for value in tokens:
			if value is None:
				value=''
			if not isinstance(value,unicode):
				value=unicode(value)
			value=value.encode('utf8')
			value=value.strip()
			if looks_like_ssn(value):
                                type="Social Security Number"
                                print line_number,"\t\t",value,"\t\t\t\t",type
                        if looks_like_ccn(value):
                                type="Credit Card Number"
                                print line_number,"\t\t",value,"\t\t\t\t",type
                        if looks_like_iban(value):
                                type="Bank Account Number"
                                print line_number,"\t\t",value,"\t\t\t\t",type
                        if looks_like_phone_number(value):
                                type="Telephone Number"
                                print line_number,"\t\t",value,"\t\t\t\t",type	
		line_number=line_number+1		

# filter csv files
def spif_csv_file(filename):
        data=open(filename)
        line_number=1
        print "Line #\t\tColumn\t\tValue\t\t\t\tWhat"
        print "------\t\t------\t\t-----\t\t\t\t----"
        for line in data.readlines():
                tokens=line.split(',')
		column_number=1
                for value in tokens:
                        value=value.encode('utf8')
			value=value.strip()
                        if looks_like_ssn(value):
				type="Social Security Number"
				print line_number,"\t\t",column_number,"\t\t",value,"\t\t\t\t",type
			if looks_like_ccn(value):
				type="Credit Card Number"
				print line_number,"\t\t",column_number,"\t\t",value,"\t\t\t\t",type
			if looks_like_iban(value):
				type="Bank Account Number"
				print line_number,"\t\t",column_number,"\t\t",value,"\t\t\t\t",type
			if looks_like_phone_number(value):
				type="Telephone Number"
             			print line_number,"\t\t",column_number,"\t\t",value,"\t\t\t\t",type
			column_number+=1
                line_number+=1


# filter doc files
def spif_word_doc(filename):
	print "am doing nothing here"

# filter pdf docs using pyPdf
def spif_pdf_doc(filename):
	pdf = pyPdf.PdfFileReader(open(filename, "rb"))
	content=""
	page =[]
	page_number=1
	print "Page #\t\tValue"
	print "------\t\t-----"
	for i in range(0, pdf.getNumPages()):
        	content= pdf.getPage(i).extractText()
        	content = " ".join(content.replace(u"\xa0", " ").strip().split())
        	currentPage=content.split(" ")
        	for value in currentPage:
                	value=value.strip()
			if looks_like_ssn(value):
                                type="Social Security Number"
                                print page_number,"\t\t",value,"\t\t\t\t",type
                        if looks_like_ccn(value):
                                type="Credit Card Number"
                                print page_number,"\t\t",value,"\t\t\t\t",type
                        if looks_like_iban(value):
                                type="Bank Account Number"
                                print page_number,"\t\t",value,"\t\t\t\t",type
                        if looks_like_phone_number(value):
                                type="Telephone Number"
                                print page_number,"\t\t",value,"\t\t\t\t",type
                page_number+=1


# filter xml doc
def spif_xml_doc(filename):
	print "am doing nothing here"


# check for something like SSN
def looks_like_ssn(value):
	ssn=re.compile('\d\d\d-\d\d-\d\d\d\d')
	return ssn.match(value) is not None


# check for something like CCN	
def looks_like_ccn(value):
	ccn1=re.compile('\d\d\d\d\ \d\d\d\d\ \d\d\d\d\ \d\d\d\d')
	ccn2=re.compile('\d\d\d\d-\d\d\d\d-\d\d\d\d-\d\d\d\d')
	ccn3=re.compile('\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d')
	ccn4=re.compile('\d\d\d\d-\d\d\d\d\d\d-\d\d\d\d\d')
	ccn5=re.compile('\d\d\d\d \d\d\d\d\d\d \d\d\d\d\d')
	ccn6=re.compile('\d\d\d\d\d\d\d\d\d\d\d\d\d\d\d')
	return (ccn1.match(value) is not None) or (ccn2.match(value) is not None) or (ccn3.match(value) is not None) or (ccn4.match(value) is not None) or (ccn5.match(value) is not None) or (ccn6.match(value) is not None)


# check for something like IBAN
def looks_like_iban(value):
	iban_object= iban.IBAN(value)
	return iban_object.is_valid()

# check for something like phone number
def looks_like_phone_number(value):
	phone = re.compile(r'^((\d{1,4}[- ]\d{1,3})|(\d{2,3}))[- ](\d{3,4})[- ](\d{4})')	
	return phone.match(value) is not None
	
# main
if __name__=='__main__':
	main()
