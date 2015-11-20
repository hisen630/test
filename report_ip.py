#!/usr/bin/env python2.7
#coding=utf-8

import win32serviceutil
import win32service
import win32event


class ReportIPService(win32serviceutil.ServiceFramework):

    _svc_name_ = "ReportIPService_Python"
    _svc_display_name_ = "Python Report IP Service"
    _svc_description_ = "Python report ip service"

    def __init__(self, args):
        #win32serviceutil.ServiceFramework.__init__(self, args)
	self.hWaitStop = win32event.CreateEvent(None, 0, 0, None)
	self.isAlive = True

    def SvcDoRun(self):
        import time
	import socket
	import os,sys
	while self.isAlive:
	    localIP = socket.gethostbyname(socket.gethostname())
	    f = open("C:/Users/hisen/dev/test/ip.txt",'w')
	    print >> f, localIP
	    f.close()
	    os.system("cd C:/Users/hisen/dev/test && git commit -am'auto report ip %s'"%time.asctime())
	    os.system("cd C:/Users/hisen/dev/test && git push origin master")
	    time.sleep(60*10)

    def SvcStop(self):
        self.ReportServiceStatus(win32service.SERVICE_STOP_PENDING)
	win32event.SetEvent(self.hWaitStop)
	self.isAlive = False

if __name__ == '__main__':
    #win32serviceutil.HandleCommandLine(ReportIPService)
    a = ReportIPService("")
    a.SvcDoRun()
