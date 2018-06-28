#!/usr/bin/env python										
#-*- coding: utf-8 -*-	

from setuptools import setup, find_packages
import glob
setup(
   name='pynetworkblocker',
   version='1.0',
   description='İstenmeyen kullanıcılara arp paket gönderir.',
   author='Onur Ağtaş',
   author_email='agtasonur@gmail.com',
   packages=['pynetworkblocker'],  #same as name
   install_requires=['scapy', 'python-nmap'], #external packages as dependencies
   scripts=['scripts/pynetworkblocker','pynetworkblocker/pynetworkblocker.py','pynetworkblocker/Ui_gui.py','pynetworkblocker/interfaces.py'],
#    data_files = [ ("pynetworkblocker",glob.glob('pynetworkblocker/main.py') ),
#                         ("pynetworkblocker",glob.glob('pynetworkblocker/Ui_gui.py') ),    
#                         ("pynetworkblocker",glob.glob('pynetworkblocker/interfaces.py') ),    
#                              ("pynetworkblocker",glob.glob('pynetworkblocker/gui.ui') ),			
# 	                     ("/usr/share/applications",glob.glob('scripts/pynetworkblocker.desktop') )]
)