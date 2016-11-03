#!/usr/bin/python

from PyQt4 import QtGui 
import sys # We need sys so that we can pass argv to QApplication
import datetime

#for emails
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEBase import MIMEBase
from email.MIMEText import MIMEText
from email import Encoders

import os
import subprocess

import time

import TensionUI # This file holds our MainWindow and all design related things
              # it also keeps events etc that we defined in Qt Designer

class TensionApp(QtGui.QMainWindow, TensionUI.Ui_MainWindow):
    def __init__(self):
        super(self.__class__, self).__init__()
        self.setupUi(self)  # This is defined in TensionUI.py file automatically
                            # It sets up layout and widgets that are defined

        self.ElogButton.setEnabled(True)

        self.saveButton.clicked.connect(self.SaveData)
        self.ElogButton.clicked.connect(self.ELOG)
        self.CloseBtn.clicked.connect(self.close)
        self.EmailBtn.clicked.connect(self.email)

        self.ElogButton.setEnabled(False)
        self.EmailBtn.setEnabled(False)

###############################################################################################################
    def ELOG(self):
        if ((self.beforeJacking.isChecked() == False and self.afterJacking.isChecked() == False) or (self.beforeJacking.isChecked() == True and self.afterJacking.isChecked() == True)):
            print("Please Select Correct Jacking State")
        else:
            ModuleNumber = int(self.ModuleNumber.text())
            Localtime = time.asctime( time.localtime(time.time()) )
            date = time.strftime("%d_%m_%y")
            os.environ["MODULE_NUMBER"] = str(ModuleNumber)
            if self.beforeJacking.isChecked() == True:
                os.environ["TENSION_ELOG_COMMENT"]= "Tensions for Module " + str(ModuleNumber) + " before being jacked apart, were recorded on " + Localtime
                os.environ["TENSION_FILENAME"] = str("Module_" + str(ModuleNumber) + "_TensionData_BeforeJacking_"+str(date)+".txt")
            if self.afterJacking.isChecked() == True:
                os.environ["TENSION_ELOG_COMMENT"]= "Tensions for Module " + str(ModuleNumber) + " after being jacked apart, were recorded on " + Localtime
                os.environ["TENSION_FILENAME"] = str("Module_" + str(ModuleNumber) + "_TensionData_BeforeJacking_"+str(date)+".txt")
            subprocess.call("./Tension_elog_script.sh", shell=True)
            print "sent to elog"

            self.ElogButton.setText("Sent")
            self.ElogButton.setEnabled(False)

################################################################################################################

    def SaveData(self):
        if ((self.beforeJacking.isChecked() == False and self.afterJacking.isChecked() == False) or (self.beforeJacking.isChecked() == True and self.afterJacking.isChecked() == True)):
            print("Please Select Correct Jacking State")
        else:
            ModuleNumber = int(self.ModuleNumber.text())
            Localtime = time.asctime( time.localtime(time.time()) )
            date = time.strftime("%d_%m_%y")
            
            if self.beforeJacking.isChecked() == True:
                filename = "Module_" + str(ModuleNumber) + "_TensionData_BeforeJacking_"+str(date)+".txt"
            if self.afterJacking.isChecked() == True:
                filename = "Module_" + str(ModuleNumber) + "_TensionData_AfterJacking_"+str(date)+".txt"
                
            self.ElogButton.setText("Send to Elog")
            UA1 = int(self.UA1.text())
            UA2 = int(self.UA2.text())
            UA3 = int(self.UA3.text())
            UA4 = int(self.UA4.text())
            UA5 = int(self.UA5.text())
            UA6 = int(self.UA6.text())
            UA7 = int(self.UA7.text())
            UA8 = int(self.UA8.text())
            UA9 = int(self.UA9.text())
            UA10  = int(self.UA10.text())
            UA11  = int(self.UA11.text())
            UA12  = int(self.UA12.text())
            UA13  = int(self.UA13.text())
            UA14  = int(self.UA14.text())
            UA15  = int(self.UA15.text())
            UA16  = int(self.UA16.text())
            UA17  = int(self.UA17.text())
            UA18  = int(self.UA18.text())
            UA19  = int(self.UA19.text())
            UA20  = int(self.UA20.text())
            UA21  = int(self.UA21.text())
            UA22  = int(self.UA22.text())
            UA23  = int(self.UA23.text())
            UA24  = int(self.UA24.text())
            UA25  = int(self.UA25.text())
            UA26  = int(self.UA26.text())
            UA27  = int(self.UA27.text())
            UA28  = int(self.UA28.text())
            UA29  = int(self.UA29.text())
            UA30  = int(self.UA30.text())
            UA31  = int(self.UA31.text())
            UA32  = int(self.UA32.text())
            
            UB1 = int(self.UB1.text())
            UB2 = int(self.UB2.text())
            UB3 = int(self.UB3.text())
            UB4 = int(self.UB4.text())
            UB5 = int(self.UB5.text())
            UB6 = int(self.UB6.text())
            UB7 = int(self.UB7.text())
            UB8 = int(self.UB8.text())
            UB9 = int(self.UB9.text())
            UB10  = int(self.UB10.text())
            UB11  = int(self.UB11.text())
            UB12  = int(self.UB12.text())
            UB13  = int(self.UB13.text())
            UB14  = int(self.UB14.text())
            UB15  = int(self.UB15.text())
            UB16  = int(self.UB16.text())
            UB17  = int(self.UB17.text())
            UB18  = int(self.UB18.text())
            UB19  = int(self.UB19.text())
            UB20  = int(self.UB20.text())
            UB21  = int(self.UB21.text())
            UB22  = int(self.UB22.text())
            UB23  = int(self.UB23.text())
            UB24  = int(self.UB24.text())
            UB25  = int(self.UB25.text())
            UB26  = int(self.UB26.text())
            UB27  = int(self.UB27.text())
            UB28  = int(self.UB28.text())
            UB29  = int(self.UB29.text())
            UB30  = int(self.UB30.text()) 
            UB31  = int(self.UB31.text())
            UB32  = int(self.UB32.text())
            
            VA1 = int(self.VA1.text())   
            VA2 = int(self.VA2.text())   
            VA3 = int(self.VA3.text())   
            VA4 = int(self.VA4.text())   
            VA5 = int(self.VA5.text())   
            VA6 = int(self.VA6.text())   
            VA7 = int(self.VA7.text())   
            VA8 = int(self.VA8.text())   
            VA9 = int(self.VA9.text())   
            VA10  = int(self.VA10.text())
            VA11  = int(self.VA11.text())
            VA12  = int(self.VA12.text())
            VA13  = int(self.VA13.text())
            VA14  = int(self.VA14.text())
            VA15  = int(self.VA15.text())
            VA16  = int(self.VA16.text())
            VA17  = int(self.VA17.text())
            VA18  = int(self.VA18.text())
            VA19  = int(self.VA19.text())
            VA20  = int(self.VA20.text())
            VA21  = int(self.VA21.text())
            VA22  = int(self.VA22.text())
            VA23  = int(self.VA23.text())
            VA24  = int(self.VA24.text())
            VA25  = int(self.VA25.text())
            VA26  = int(self.VA26.text())
            VA27  = int(self.VA27.text())
            VA28  = int(self.VA28.text())
            VA29  = int(self.VA29.text())
            VA30  = int(self.VA30.text())
            VA31  = int(self.VA31.text())
            VA32  = int(self.VA32.text())
            
            VB1 = int(self.VB1.text())   
            VB2 = int(self.VB2.text())   
            VB3 = int(self.VB3.text())   
            VB4 = int(self.VB4.text())   
            VB5 = int(self.VB5.text())   
            VB6 = int(self.VB6.text())   
            VB7 = int(self.VB7.text())   
            VB8 = int(self.VB8.text())   
            VB9 = int(self.VB9.text())   
            VB10  = int(self.VB10.text())
            VB11  = int(self.VB11.text())
            VB12  = int(self.VB12.text())
            VB13  = int(self.VB13.text())
            VB14  = int(self.VB14.text())
            VB15  = int(self.VB15.text())
            VB16  = int(self.VB16.text())
            VB17  = int(self.VB17.text())
            VB18  = int(self.VB18.text())
            VB19  = int(self.VB19.text())
            VB20  = int(self.VB20.text())
            VB21  = int(self.VB21.text())
            VB22  = int(self.VB22.text())
            VB23  = int(self.VB23.text())
            VB24  = int(self.VB24.text())
            VB25  = int(self.VB25.text())
            VB26  = int(self.VB26.text())
            VB27  = int(self.VB27.text())
            VB28  = int(self.VB28.text())
            VB29  = int(self.VB29.text())
            VB30  = int(self.VB30.text())
            VB31  = int(self.VB31.text())
            VB32  = int(self.VB32.text())
            
            f = open(filename, 'w')
            f.write(
                "Tension Data for Module Number " + str(ModuleNumber) + " Recorded on " + Localtime + " measured in gramms \n"
                "UA1  " + str(UA1 ) + " , UB1  " + str(UB1 ) + " , VB1  " + str(VB1 )   + " , VA1  " + str(VA1 )   + "\n" 
                "UA2  " + str(UA2 ) + " , UB2  " + str(UB2 ) + " , VB2  " + str(VB2 )   + " , VA2  " + str(VA2 )   + "\n" 
                "UA3  " + str(UA3 ) + " , UB3  " + str(UB3 ) + " , VB3  " + str(VB3 )   + " , VA3  " + str(VA3 )   + "\n" 
                "UA4  " + str(UA4 ) + " , UB4  " + str(UB4 ) + " , VB4  " + str(VB4 )   + " , VA4  " + str(VA4 )   + "\n" 
                "UA5  " + str(UA5 ) + " , UB5  " + str(UB5 ) + " , VB5  " + str(VB5 )   + " , VA5  " + str(VA5 )   + "\n" 
                "UA6  " + str(UA6 ) + " , UB6  " + str(UB6 ) + " , VB6  " + str(VB6 )   + " , VA6  " + str(VA6 )   + "\n" 
                "UA7  " + str(UA7 ) + " , UB7  " + str(UB7 ) + " , VB7  " + str(VB7 )   + " , VA7  " + str(VA7 )   + "\n" 
                "UA8  " + str(UA8 ) + " , UB8  " + str(UB8 ) + " , VB8  " + str(VB8 )   + " , VA8  " + str(VA8 )   + "\n" 
                "UA9  " + str(UA9 ) + " , UB9  " + str(UB9 ) + " , VB9  " + str(VB9 )   + " , VA9  " + str(VA9 )   + "\n" 
                "UA10 " + str(UA10) + " , UB10 " + str(UB10) + " , VB10 " + str(VB10)   + " , VA10 " + str(VA10)   + "\n" 
                "UA11 " + str(UA11) + " , UB11 " + str(UB11) + " , VB11 " + str(VB11)   + " , VA11 " + str(VA11)   + "\n" 
                "UA12 " + str(UA12) + " , UB12 " + str(UB12) + " , VB12 " + str(VB12)   + " , VA12 " + str(VA12)   + "\n" 
                "UA13 " + str(UA13) + " , UB13 " + str(UB13) + " , VB13 " + str(VB13)   + " , VA13 " + str(VA13)   + "\n" 
                "UA14 " + str(UA14) + " , UB14 " + str(UB14) + " , VB14 " + str(VB14)   + " , VA14 " + str(VA14)   + "\n" 
                "UA15 " + str(UA15) + " , UB15 " + str(UB15) + " , VB15 " + str(VB15)   + " , VA15 " + str(VA15)   + "\n" 
                "UA16 " + str(UA16) + " , UB16 " + str(UB16) + " , VB16 " + str(VB16)   + " , VA16 " + str(VA16)   + "\n" 
                "UA17 " + str(UA17) + " , UB17 " + str(UB17) + " , VB17 " + str(VB17)   + " , VA17 " + str(VA17)   + "\n" 
                "UA18 " + str(UA18) + " , UB18 " + str(UB18) + " , VB18 " + str(VB18)   + " , VA18 " + str(VA18)   + "\n" 
                "UA19 " + str(UA19) + " , UB19 " + str(UB19) + " , VB19 " + str(VB19)   + " , VA19 " + str(VA19)   + "\n" 
                "UA20 " + str(UA20) + " , UB20 " + str(UB20) + " , VB20 " + str(VB20)   + " , VA20 " + str(VA20)   + "\n" 
                "UA21 " + str(UA21) + " , UB21 " + str(UB21) + " , VB21 " + str(VB21)   + " , VA21 " + str(VA21)   + "\n" 
                "UA22 " + str(UA22) + " , UB22 " + str(UB22) + " , VB22 " + str(VB22)   + " , VA22 " + str(VA22)   + "\n" 
                "UA23 " + str(UA23) + " , UB23 " + str(UB23) + " , VB23 " + str(VB23)   + " , VA23 " + str(VA23)   + "\n" 
                "UA24 " + str(UA24) + " , UB24 " + str(UB24) + " , VB24 " + str(VB24)   + " , VA24 " + str(VA24)   + "\n" 
                "UA25 " + str(UA25) + " , UB25 " + str(UB25) + " , VB25 " + str(VB25)   + " , VA25 " + str(VA25)   + "\n" 
                "UA26 " + str(UA26) + " , UB26 " + str(UB26) + " , VB26 " + str(VB26)   + " , VA26 " + str(VA26)   + "\n" 
                "UA27 " + str(UA27) + " , UB27 " + str(UB27) + " , VB27 " + str(VB27)   + " , VA27 " + str(VA27)   + "\n" 
                "UA28 " + str(UA28) + " , UB28 " + str(UB28) + " , VB28 " + str(VB28)   + " , VA28 " + str(VA28)   + "\n" 
                "UA29 " + str(UA29) + " , UB29 " + str(UB29) + " , VB29 " + str(VB29)   + " , VA29 " + str(VA29)   + "\n" 
                "UA30 " + str(UA30) + " , UB30 " + str(UB30) + " , VB30 " + str(VB30)   + " , VA30 " + str(VA30)   + "\n" 
                "UA31 " + str(UA31) + " , UB31 " + str(UB31) + " , VB31 " + str(VB31)   + " , VA31 " + str(VA31)   + "\n" 
                "UA32 " + str(UA32) + " , UB32 " + str(UB32) + " , VB32 " + str(VB32)   + " , VA32 " + str(VA32)   + "\n" 
            )

            print "Data Saved"
            f.close()
            self.EmailBtn.setEnabled(True)
            self.ElogButton.setEnabled(True)
######################################################################
    def email(self):
        if (((self.beforeJacking.isChecked() == False) and (self.afterJacking.isChecked() == False)) or ((self.beforeJacking.isChecked() == True) and (self.afterJacking.isChecked() == True))):
            print("Please Select Jacking State")
        else:
            EMAIL_SERVER = "hep.ph.liv.ac.uk"
            ModuleNumber = int(self.ModuleNumber.text())
            date = time.strftime("%d_%m_%y")
            if self.beforeJacking.isChecked() == True:
                filename = "Module_" + str(ModuleNumber) + "_TensionData_BeforeJacking_"+str(date)+".txt"
                SUBJECT = "Tension Data from Module " + str(ModuleNumber) + " before being jacked apart"
            if self.afterJacking.isChecked() == True:
                SUBJECT = "Tension Data from Module " + str(ModuleNumber) + " after being jacked apart"
                filename = "Module_" + str(ModuleNumber) + "_TensionData_AfterJacking_"+str(date)+".txt"


            print("filename is " + filename)
            msg = MIMEMultipart()
            msg['Subject'] = SUBJECT
            msg['From'] = "Will Turner"
            msg['To'] = "You"
            msg.attach(MIMEText("Email automatically sent from Tension Test Recorder. \n \n \n \n \n \n \n \n email wturner@hep.ph.liv.ac.uk or visit http://hep.ph.liv.ac.uk/~wturner/Recorders.html for more infomation about this script"))
            
            part = MIMEBase('application', "octet-stream")
            part.set_payload(open(filename, "rb").read())
            Encoders.encode_base64(part)
            
            part.add_header('Content-Disposition', 'attachment; filename=' + str(filename))
        
            msg.attach(part)
        
            server = smtplib.SMTP(EMAIL_SERVER)
            server.sendmail("Will Turner", str(self.email_box.text()), msg.as_string())
            print("Email Sent")

######################################################################
def main():
    app = QtGui.QApplication(sys.argv)  # A new instance of QApplication
    form = TensionApp()                 # We set the form to be our ExampleApp (design)
    form.show()                         # Show the form
#    app.exec_()                         # and execute the app
    sys.exit(app.exec_())


if __name__ == '__main__':              # if we're running file directly and not importing it
    main()                              # run the main function
