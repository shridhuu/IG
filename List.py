import requests as G,json,random as A,string as D
from concurrent.futures import ThreadPoolExecutor as F
B=0
H=21254029834
E='\x1b[0m'
def I():
	global B
	while True:
		F={'lsd':''.join(A.choices(D.ascii_letters+D.digits,k=32)),'variables':json.dumps({'id':int(A.randrange(2500000000,H)),'render_surface':'PROFILE'}),'doc_id':'25618261841150840'};I=G.post('https://www.instagram.com/api/graphql',headers={'X-FB-LSD':F['lsd']},data=F)
		try:
			C=I.json().get('data',{}).get('user',{}).get('username')
			if C:
				B+=1;J=A.randint(5,208);K=f"[1m[38;5;{J}m";print(E+str(B)+f"{K}  </>  {E}"+C)
				with open('username.txt','a',encoding='utf-8')as L:L.write(C+'\n')
		except Exception as M:''
C=F(max_workers=300)
for J in range(200):C.submit(I)
C.shutdown(wait=True)
