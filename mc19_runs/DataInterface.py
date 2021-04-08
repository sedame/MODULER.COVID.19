
from tkinter import *
import math
import requests
import wget
import os
import folium
from folium import Choropleth, Circle, Marker
from folium.plugins import HeatMap, MarkerCluster 


def case():
		
	window = Tk()# First window

	# MAIN WINDOWS OR ROOT WINDOWS
	window.title("MODULER.COVID.19")#  The tile of the file personalise
	#window.iconbitmap("mc19ico.ico") # The logo of the file
	window.geometry("1080x720") #480x360
	window.minsize(480, 360)
	window.config(background='#101720')

	frame = Frame(window)
	frame.pack()






	window.mainloop()#afficher

	return case