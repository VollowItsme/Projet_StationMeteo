from datetime import date, datetime
from signal import signal, SIGPIPE, SIG_DFL
from urllib.request import urlopen
from flask import Flask, render_template
import threading
import re
import json
import socket
import sys
import time
import os
import csv
import webbrowser

accueil_message = "Bonjour"
historique_temp = ['0','0','0','0','0','0','0','0','0','0']
historique_hum = ['0','0','0','0','0','0','0','0','0','0']
historique_pres = ['0','0','0','0','0','0','0','0','0','0']
a = 0

def page_accueil(temp, hum, pres):
	html = open('/var/www/html/accueil.html').read()
	liste = html.split()
	#print(liste[25])
	liste[64] = str(temp)
	liste[68] = str(hum)
	liste[72] = str(pres)
	#print(liste)
	new_liste = " ".join(liste)
	print(new_liste)
	with open('/var/www/html/accueil.html', 'w') as file:
		file.write(new_liste)

def page_temp(historique_temp):
	html = open('/var/www/html/historique_temp.html').read()
	liste = html.split()
	print(liste)
	liste[29] = str(historique_temp[0])
	liste[32] = str(historique_temp[1])
	liste[35] = str(historique_temp[2])
	liste[38] = str(historique_temp[3])
	liste[41] = str(historique_temp[4])
	liste[44] = str(historique_temp[5])
	liste[47] = str(historique_temp[6])
	liste[50] = str(historique_temp[7])
	liste[53] = str(historique_temp[8])
	liste[56] = str(historique_temp[9])
	#print(liste[29], '', liste[32], '', liste[35], '', liste[38])
	new_liste = " ".join(liste)
	print(new_liste)
	with open('/var/www/html/historique_temp.html', 'w') as file:
		file.write(new_liste)


def page_hum(historique_hum):
        html = open('/var/www/html/historique_hum.html').read()
        liste = html.split()
        print(liste)
        liste[29] = str(historique_hum[0])
        liste[32] = str(historique_hum[1])
        liste[35] = str(historique_hum[2])
        liste[38] = str(historique_hum[3])
        liste[41] = str(historique_hum[4])
        liste[44] = str(historique_hum[5])
        liste[47] = str(historique_hum[6])
        liste[50] = str(historique_hum[7])
        liste[53] = str(historique_hum[8])
        liste[56] = str(historique_hum[9])
        #print(liste[29], '', liste[32], '', liste[35], '', liste[38])
        new_liste = " ".join(liste)
        print(new_liste)
        with open('/var/www/html/historique_hum.html', 'w') as file:
                file.write(new_liste)


def page_pres(historique_pres):
        html = open('/var/www/html/historique_press.html').read()
        liste = html.split()
        print(liste)
        liste[29] = str(historique_pres[0])
        liste[32] = str(historique_pres[1])
        liste[35] = str(historique_pres[2])
        liste[38] = str(historique_pres[3])
        liste[41] = str(historique_pres[4])
        liste[44] = str(historique_pres[5])
        liste[47] = str(historique_pres[6])
        liste[50] = str(historique_pres[7])
        liste[53] = str(historique_pres[8])
        liste[56] = str(historique_pres[9])
        #print(liste[29], '', liste[32], '', liste[35], '', liste[38])
        new_liste = " ".join(liste)
        print(new_liste)
        with open('/var/www/html/historique_press.html', 'w') as file:
                file.write(new_liste)




if __name__ == "__main__":
	#cmd = 'sudo python3 test.py'
	#os.system(cmd)
	signal(SIGPIPE, SIG_DFL)
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
	well_known_port = 8080
	sock.bind(('0.0.0.0', well_known_port))
	sock.listen(1)
	print("listening...")

	while (True):
		newSocket, address = sock.accept()
		print("connected:", address)
		try:
			while (True):
				receivedCommand = newSocket.recv(2000)
				accueil = receivedCommand.decode()
				accueil_split = accueil.split("-")
				temp = accueil_split[0]
				hum = accueil_split[1]
				pres = accueil_split[2]
				#creation_html_accueil(accueil)

				historique_temp[a] = temp
				historique_hum[a] = hum
				historique_pres[a] = pres
				a += 1
				print(temp, ' ', hum, ' ', pres)
				page_accueil(temp, hum, pres)
				page_temp(historique_temp)
				page_pres(historique_pres)
				page_hum(historique_hum)
				if a == 10:
					print("historique temp:", historique_temp)
					print()
					print("historique hum:", historique_hum)
					print()
					print("historique pres:", historique_pres)
					print()
					a = 0

		finally:

			sock.close()
