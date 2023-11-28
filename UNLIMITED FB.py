import requests,re,bs4,os,time,random,datetime
from bs4 import BeautifulSoup as parse
from bs4 import BeautifulSoup as par
from fake_email import Email

try:
    import concurrent.fake_email
except ImportError:
    print('\n \033[1;91m[\033[1;93mFX-FAHIM\033[1;91m]\033[1;97m installing fake_email !...\n')
    time.sleep(0.5)
    os.system('pip install fake_email')

yellow = "\x1b[38;5;208m"
black="\033[1;30m"
rad="\033[1;31m"
green="\033[1;32m"
yelloww="\033[1;33m"
blue="\033[38;5;6m"
purple="\033[1;35m"
cyan="\033[1;36m"
white="\033[1;37m"
faltu = "\033[1;41m"
pvt = "\033[1;0m"
my_color = [white,blue,green]
warna = random.choice(my_color)
def logo():
    os.system('clear')
    print("""  

  \033[30;1m________   __
 \033[30;1m|  ____\ \ / /
 \033[34;1m| |__   \ V / 
 \033[34;1m|  __|   > <  
 \x1b[38;5;196m| |     / . \ 
 \x1b[38;5;196m|_|    /_/ \_\
 
 
\33[37;42m𝐓𝐄𝐋𝐄𝐆𝐑𝐀𝐌 COMING SOON""")

def linex():
        print(f"\x1b[38;5;159m━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━")

nama='fahim+gamnig'
pw="fahim99"
def __fahim__():
    logo()
    print(f"\x1b[38;5;150m┏━[\033[1;31m=\x1b[38;5;150m] FB ID CREATE STARTED...")
    print(f"\x1b[38;5;151m┗━[\033[1;31m=\x1b[38;5;151m] NO RESULT \033[1;33m[\033[1;32mON\033[1;37m/\033[1;32mOFF\033[1;33m] \x1b[38;5;151mAIRPLAN MODE")
    linex()
    while True:
        try:
            ua="Mozilla/5.0 (iPhone; CPU iPhone OS 16_5_1 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) CriOS/114.0.5735.124 Mobile/15E148 Safari/604.1"
            ua="Mozilla/5.0 (Linux; Android "+str(random.randrange(4,6))+"; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.5735.196 Mobile Safari/537.36"
            ses=requests.Session()
            buat=Email().Mail()
            nomer=buat["mail"]
            print(f"\x1b[38;5;118m[\033[1;31m=\x1b[38;5;118m] YOUR MAIL : "+nomer)
            login=ses.get("https://m.facebook.com/reg")
            lsd=re.search('name="lsd" value="(.*?)"',str(login.text)).group(1)
            jazo=re.search('name="jazoest" value="(.*?)"',str(login.text)).group(1)
            inta=re.search('name="reg_instance" value="(.*?)"',str(login.text)).group(1)
            impres=re.search('name="reg_impression_id" value="(.*?)"',str(login.text)).group(1)
            data=f"lsd={lsd}&jazoest={jazo}&ccp=2&reg_instance={inta}&submission_request=true&helper=&reg_impression_id={impres}&ns=0&zero_header_af_client=&app_id=&logger_id=&field_names[]=firstname&field_names[]=reg_email__&field_names[]=sex&field_names[]=birthday_wrapper&field_names[]=reg_passwd__&firstname={nama}&reg_email__={nomer}&sex=2&custom_gender=male&did_use_age=false&birthday_day={random.randrange(1,28)}&birthday_month={random.randrange(1,13)}&birthday_year={random.randrange(1970,2000)}&age_step_input=&reg_passwd__={pw}&submit=Daftar"
            koki = (";").join([ "%s=%s" % (key, value) for key, value in login.cookies.get_dict().items() ])
            koki+=';m_pixel_ratio=2.625;wd=412x756'
            head={
        'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.712499976158142',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"TECNO KE7"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            gas=ses.post("https://m.facebook.com/reg/submit/",data=data,headers=head,cookies={"cookie":koki})
            kon=ses.get("https://m.facebook.com")
            if "checkpoint" in str(kon.url):
                print(f"\x1b[38;5;118m[\033[1;31m=\x1b[38;5;118m] \x1b[38;5;208mCHECKPOINT")
                linex()
                continue
            else:pass            
            print(f"\x1b[38;5;118m[\033[1;31m=\x1b[38;5;118m] FB NAME : \033[1;37mEmran Ehc Cyber")
            print(f"\x1b[38;5;118m[\033[1;31m=\x1b[38;5;118m] PASSWORD : \033[1;37memran99")
            para=parse(kon.text,"html.parser")
            data2={}
            for gg in para("input"):
                if None in {gg.get("name")}:pass
                else:data2.update({gg.get("name"):gg.get("value")})
            link=para.find("form",{"method":"post"}).get("action")
            time.sleep(10)
            while True:
                print("\r\x1b[38;5;118m[\033[1;31m=\x1b[38;5;118m] CREATEING FB ID.....",end="\r")
                mess=Email(buat["session"]).inbox()
                if mess:
                    c=mess['topic'].split(' ')[0].replace("FB-","")
                    data2.update({"c":c})
                    break
            heads={
        'authority': 'mbasic.facebook.com',
    'method': 'GET',
    'scheme': 'https',
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'dpr': '1.712499976158142',
    'referer': 'https://mbasic.facebook.com/',
    'sec-ch-prefers-color-scheme': 'dark',
    'sec-ch-ua': '"Not_A Brand";v="8", "Chromium";v="120"',
    'sec-ch-ua-full-version-list': '"Not_A Brand";v="8.0.0.0", "Chromium";v="120.0.6099.20"',
    'sec-ch-ua-mobile': '?1',
    'sec-ch-ua-model': '"TECNO KE7"',
    'sec-ch-ua-platform': '"Android"',
    'sec-ch-ua-platform-version': '"10.0.0"',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'same-origin',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Linux; Android 10; K) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Mobile Safari/537.36',
    'viewport-width': '980',
}
            yes=ses.post("https://m.facebook.com"+link,headers=heads,data=data2)
            coki = (";").join([ "%s=%s" % (key, value) for key, value in ses.cookies.get_dict().items() ])
            print("\x1b[38;5;118m[\033[1;31m=\x1b[38;5;118m] COOKIE : \033[38;5;6m"+coki+';m_pixel_ratio=2.625;wd=412x756')        
            open("coki.txt","a").write(coki+";m_pixel_ratio=2.625;wd=412x756\n")
            login=ses.get("https://mbasic.facebook.com")
            pars=par(login.text,"html.parser")
            try:
                fol=["100068403202721"]
                fl=0
                for user in fol:
                    for response in par(ses.get(f'https://mbasic.facebook.com/'+user).text,'html.parser').find_all('a',href=True):
                        if '/a/subscribe.php?' in response.get('href'):x=ses.get('https://mbasic.facebook.com{}'.format(response['href'])).text;fl+=1
            except:time.sleep(5)
            print(f"\x1b[38;5;118m[\033[1;31m=\x1b[38;5;118m] FOLLOW DONE")
            linex()
            kir=par(ses.get("https://www.facebook.com/100068403202721").text,"html.parser")
            kikir=0
            for x in kir.find_all("a",href=True):
                try:
                    if "/a/friends" in str(x["href"]):
                        ses.get("https://mbasic.facebook.com"+x["href"])
                        kikir+=1
                except:time.sleep(10)
        except requests.exceptions.ConnectionError:time.sleep(31)
        except Exception as e:
            pass
    
__fahim__()





