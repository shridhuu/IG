I=range
D=input
A=print
import requests as F,random as B,re,hashlib as M,string as H
from time import sleep
import time
N=str(int(time.time()))
E='83f2000a-4b95-4811-bc8d-0f3539ef07cf'
C=None
def O(n=10):A=H.ascii_lowercase+'1234567890';return''.join(B.choice(A)for C in I(n))
def J(n=10):A=H.ascii_lowercase;return''.join(B.choice(A)for C in I(n))
def P(stringLength=10):A=H.ascii_lowercase+'1234567890';C=''.join(B.choice(A)for C in I(stringLength-1));return J(1)+C
def Q(ID):B='12345';A=M.md5();A.update(ID.encode('utf-8')+B.encode('utf-8'));return'android-'+A.hexdigest()[:16]
def R():A=['HUAWEI','Xiaomi','samsung','OnePlus'];D=['480','320','640','515','120','160','240','800'];C=B.randrange(2,9)*180;E=C-180;F={'system':'Android','Host':'Instagram','manufacturer':B.choice(A),'model':f"{B.choice(A)}-{P(4).upper()}",'android_version':B.randint(18,25),'android_release':f"{B.randint(1,7)}.{B.randint(0,7)}",'cpu':f"{J(2)}{B.randrange(1000,9999)}",'resolution':f"{C}x{E}",'randomL':O(6),'dpi':B.choice(D)};return'{Host} 155.0.0.37.107 {system} ({android_version}/{android_release}; {dpi}dpi; {resolution}; {manufacturer}; {model}; {cpu}; {randomL}; en_US)'.format(**F)
def G(user_agent):return{'User-Agent':user_agent,'Host':'i.instagram.com','content-type':'application/x-www-form-urlencoded; charset=UTF-8','accept-encoding':'gzip, deflate','x-fb-http-engine':'Liger','Connection':'close'}
def S(req,cookies,user_agent,username):
	I=user_agent;H=cookies;C=req;J=F.get('https://i.instagram.com/api/v1'+C.json()['challenge']['api_path'],headers=G(I),cookies=H);B=J.json().get('step_data',{})
	if'phone_number'in B:A(f"[0] phone_number : {B["phone_number"]}")
	elif'email'in B:A(f"[1] email : {B["email"]}")
	else:A('Unknown verification method.');return
	L=D('Choice: ');M={'choice':str(L),'_uuid':E,'_uid':E,'_csrftoken':'massing'};N=C.json()['challenge']['api_path'];O=F.post(f"https://i.instagram.com/api/v1{N}",headers=G(I),data=M,cookies=H);P=O.json()['step_data']['contact_point'];A(f"Code sent to: {P}");return K(C,H,I,username)
def K(req,cookies,user_agent,username):
	J=username;I=user_agent;H=cookies;global C;L=D('Code: ');M={'security_code':L,'_uuid':E,'_uid':E,'_csrftoken':'massing'};N=req.json()['challenge']['api_path'];B=F.post(f"https://i.instagram.com/api/v1{N}",headers=G(I),data=M,cookies=H)
	if'logged_in_user'in B.text:A(f"Login Successfully as @{J}");C=B.cookies.get('sessionid');A('Session ID:',C)
	else:
		try:O=re.search('"message":"(.*?)",',B.text).group(1);A(O)
		except:A(B.text)
		P=D('Code is not working. Try again? [Y/N]: ')
		if P.lower()=='y':return K(req,H,I,J)
		else:exit()
def L():
	global C;H=D('Username: ');J=D('Password: ');I=R();K=Q(H);M={'guid':E,'enc_password':f"#PWD_INSTAGRAM:0:{N}:{J}",'username':H,'device_id':K,'login_attempt_count':'0'};B=F.post('https://i.instagram.com/api/v1/accounts/login/',headers=G(I),data=M)
	if'logged_in_user'in B.text:A(f"Login Successfully as @{H}");C=B.cookies.get('sessionid');A('Session ID:',C)
	elif'checkpoint_challenge_required'in B.text:A('Challenge checkpoint required.');return S(B,B.cookies,I,H)
	else:
		try:O=re.search('"message":"(.*?)",',B.text).group(1);A(O)
		except:A(B.text)
		P=D('Something went wrong. Try again? [Y/N]: ')
		if P.lower()=='y':return L()
		else:exit()
L()
