#!/usr/bin/env python										
#-*- coding: utf-8 -*-										
 													
from distutils.core import setup								
import glob
with open('requirements.txt') as f:
    requirements = f.read().splitlines()											
setup(name = "PyNetworkBlocker",									
	version = "1.0.0"[1:],									
	author = "Onur Ağtaş",							
	url = "http://resoft.org",					
	author_email ="agtasonur@gmail.com",					
	description = "İstenmeyen kullanıcılara arp paket gönderir.",								
	long_description = "PyNetworkBlocker",						
	license = "GPL",									
	platforms = 'linux',									
	data_files = [ ("/usr/share/pynetworkblocker",glob.glob('pynetworkblocker/main.py') ),
                        ("/usr/share/pynetworkblocker",glob.glob('pynetworkblocker/Ui_gui.py') ),    
                        ("/usr/share/pynetworkblocker",glob.glob('pynetworkblocker/interfaces.py') ),    
                             ("/usr/share/pynetworkblocker",glob.glob('pynetworkblocker/gui.ui') ),			
	                     ("/usr/share/applications",glob.glob('scripts/pynetworkblocker.desktop') )],		
scripts = ['scripts/pynetworkblocker'],
install_requires = ['scapy', 'nmap'])