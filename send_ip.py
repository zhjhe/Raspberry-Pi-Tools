#/bin/evn python
# -*-coding:utf-8-*-

import socket
import fcntl
import time
import struct
import smtplib
import urllib.request
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_email(smtp_server, username, password, sender, receiver, subject, msghtml):
    msgRoot = MIMEMultipart('related')
    msgRoot["TO"] = ','.join(receiver)
    msgRoot["From"] = sender
    msgRoot["Subject"] = subject
    msgText = MIMEText(msghtml, 'html', 'utf-8')
    msgRoot.attach(msgText)

    # send mail
    smtp = smtplib.SMTP()
    smtp.connect(smtp_server)
    smtp.login(username, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

# check net
def check_network():
    while True:
        try:
            result = urllib.request.urlopen('https://www.baidu.com').read()
            #print(result)
            print("Network is Ready!")
            break
        except Exception:
            print("Network is not ready, Sleep 5s...")
            time.sleep(5)
    
    return True

def get_ip_address():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    ifname='wlan0'
    ip_address = socket.inet_ntoa(fcntl.ioctl(
        s.fileno(),
        0x8915,
        struct.pack('256s', ifname[:15].encode(encoding="utf-8"))
        )[20:24])
    return ip_address

if __name__ == "__main__":
    check_network()
    ip = get_ip_address()
    print(ip)
    smtp_server = "smtp.example.com"
    username = "username"
    password = "password"
    sender = "username@example.com"
    receiver = ["username@example.com"]
    subject = "IP Address Of My Raspberry Pi"
    send_email(smtp_server, username, passwword, sender, receiver, subject, ip)
