
#========================================================================= LIBRARIES
import os
import sys
import wget
import urllib.request
import urllib.parse
from urllib.request import urlopen
from bs4 import *
from bs4 import BeautifulSoup
import requests
import parse



#----------------------------------------------------- GET ALL URL IN A CLASS
def getlinks(linktosite):
	pass



#------------------------------------------------------ BUILD FILE NAME
def build_name(url):

	doxname =  url.split('%20DU%')[-2]
	name = doxname.split('%')[-1]
	return name



#------------------------------------------------------ DOWLOAD A FILE IN PDF
def download_file(download_url, filename):

	req= urllib.request.Request(download_url, headers={'User-Agent': 'Mozilla/5.0'})
	response = urllib.request.urlopen(req)
	os.chdir('DataStors/')
	file = open(filename +".pdf", 'wb')
	file.write(response.read())
	file.close()
	return download_file

	  

def data extraction ():
	pass





#_________________________________________________________TEST TEST________________________________________________________

URL404 ="https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20404%20DU%2008%20AVRIL%202021.pdf"
URL403 ="https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20403%20DU%2008%20AVRIL%202021.pdf"
URL402 ="https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20402%20DU%2007%20AVRIL%202021.pdf"
URL401 ="https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20401%20DU%2007%20AVRIL%202021.pdf"
URL400 ="https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20400%20DU%2007%20AVRIL%202021.pdf"
URL399 ="https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20399%20DU%2004%20AVRIL%202021.pdf"
URL3991 = "https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20399.pdf"
URL398 ="https://sante.sec.gouv.sn/sites/default/files/COMMUNIQUE%20398%20DU%2004%20AVRIL%202021.pdf"

#file_name = build_name(URL40)

download_file(URL3991, "20339")




