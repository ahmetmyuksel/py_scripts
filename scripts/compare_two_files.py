import urllib2                                                                 
import filecmp                                                                 
import os                                                                      
import string                                                                  
from email.mime.text import MIMEText                                           
from subprocess import Popen, PIPE                                             
import smtplib                                                                 
                                                                               
temp_wsdl = urllib2.urlopen("http://10.10.10.10:8181/webservices/WebService?wsdl")
with open('temp.xml','wb') as output:                                          
  output.write(temp_wsdl.read())                                               
                                                                               
def compare_files():                                                           
        compare_boolean = filecmp.cmp('/root/wsdl_compare/WebService?wsdl', 'temp.xml')
        return compare_boolean                                                 
                                                                               
def send_message():                                                            
    SUBJECT = "WSDL farkli"                                                    
    TO = ["my_mail@gmail.com", "group_mail@gmail.com"]                         
    FROM = "smtp@domain.com"                                                   
    TEXT = "WSDL farkli. Ben DB1 makinasiyim."                                 
    SMTP_USER = "smtpuser"                                                     
    SMTP_PASS = "smtppass"                                                     
    SMTP_HOST = "smtphost"                                                     
    SMTP_PORT = "25"                                                           
    BODY = string.join((                                                       
            "From: %s" % FROM,                                                 
            "To: %s" % TO,                                                     
            "Subject: %s" % SUBJECT ,                                          
            "",                                                                
            TEXT                                                               
            ), "\r\n")                                                         
    server = smtplib.SMTP(SMTP_HOST, SMTP_PORT)                                
    server.sendmail(FROM, TO, BODY)                                            
    server.quit()                                                              
                                                                               
if compare_files():                                                            
    pass                                                                       
else:                                                                          
        send_message()                                                         
                                                                               
os.system("rm -rf temp.xml")   
