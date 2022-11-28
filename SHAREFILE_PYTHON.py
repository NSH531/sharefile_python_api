import requests,os,random
import pandas as PD
env="we-can"
class out():
    def CSV(Json:dict):
        return PD.DataFrame(Json).to_csv(os.getcwd()+str(random.randint(10001,99999))+".csv")
class sharefile():
    def ti(self,t="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJTaGFyZUZpbGUiLCJzdWIiOiI2NDZiYzFkZi0zMjI5LTRhZmMtYTkxYy0zYmQ2ZWE0MDE4MTciLCJpYXQiOjE2Njk2MjY5ODQsImV4cCI6MTY2OTY1NTc4NCwiYXVkIjoicEc5QmZteUpGbXcyeWQ1RE5mU0MzRXIxY25LUW50c0wiLCJzaGFyZWZpbGU6dG9rZW5pZCI6IkduSTRVcUdleWROdVpqb0QwNkI2Q25KZTdpcFRMdHlYJCRsMGo3RXpqR005NVdLOHJ4RG0zWmRnN25wcTNyWHFjSCIsInNjb3BlIjoidjMgdjMtaW50ZXJuYWwiLCJzaGFyZWZpbGU6c3ViZG9tYWluIjoid2UtY2FuIiwic2hhcmVmaWxlOmFjY291bnRpZCI6ImFhZWZiOThkLTFlODktNDllNi05ZTc4LTg0YmZiZTY0YzE4YiJ9.ZdvyoJ2QQYlAUywP3-PElMXmcaU96-Qf05M9d4-vNfg",env="we-can",sub=""):
        headers = {
            'Authorization': f'Bearer {t}',
        }

        Re = requests.get(f'https://we-can.sf-api.com/sf/v3/{sub}', headers=headers)
        return Re

    def TOKEN(self,t="eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJTaGFyZUZpbGUiLCJzdWIiOiI2NDZiYzFkZi0zMjI5LTRhZmMtYTkxYy0zYmQ2ZWE0MDE4MTciLCJpYXQiOjE2Njk2MjY5ODQsImV4cCI6MTY2OTY1NTc4NCwiYXVkIjoicEc5QmZteUpGbXcyeWQ1RE5mU0MzRXIxY25LUW50c0wiLCJzaGFyZWZpbGU6dG9rZW5pZCI6IkduSTRVcUdleWROdVpqb0QwNkI2Q25KZTdpcFRMdHlYJCRsMGo3RXpqR005NVdLOHJ4RG0zWmRnN25wcTNyWHFjSCIsInNjb3BlIjoidjMgdjMtaW50ZXJuYWwiLCJzaGFyZWZpbGU6c3ViZG9tYWluIjoid2UtY2FuIiwic2hhcmVmaWxlOmFjY291bnRpZCI6ImFhZWZiOThkLTFlODktNDllNi05ZTc4LTg0YmZiZTY0YzE4YiJ9.ZdvyoJ2QQYlAUywP3-PElMXmcaU96-Qf05M9d4-vNfg",env="we-can",sub=""):
        Re=sharefile.ti(sharefile,t,env="we-can")
        rx=[]
        rx.append(Re.json()["value"])
        for I in Re.json()["value"]:
            rx.append(sharefile.ti(sharefile,t=t,sub=I["url"]).json())
        return Re.json()   
    """
    this class implements sharefile's API
    methods:
     
    > auth -  get autenticating token 
    > items - Get Root Items
     
    """
    def dl(self,env:str,item_id,token,filepath:str):
        headers = {
            'Authorization': f'Bearer {token}',
        }

        response = requests.get(f'https://{env}.sf-api.com/sf/v3/Items({item_id})/Download', headers=headers, verify=False)

        with open(filepath, 'wb') as f:
            f.write(response.content)
        return response.json()

    def uploader(self,env:str,item_id,token,filepath:str,arg="rb"):
        headers = {
                    'Authorization': f'Bearer {token}',
                    }   
        a=arg            
        res = requests.get(f'https://{env}.sf-api.com/sf/v3/Items({item_id})/Upload', headers=headers, verify=False)
        f=dict(File1=open(file=filepath,mode=a))
        

        resp = requests.post(res, files=f, verify=False)
        return resp.json()
    def items(self,env:str,token):
        
        headers = {
                    'Authorization': f'Bearer {token}',
                    }   
        res = requests.get(f'https://{env}.sf-api.com/sf/v3/Items', headers=headers, verify=False)
        return res.json()
    def index(self,env:str,creds=None,comm=None):
      

        res = requests.get(f'https://{env}.sf-api.com/sf/v3')

        print(res)
        return res.json()
    def auth(self,env:str,creds={"USERNAME":"my@user.name","PASSWORD":'mypassword',"CLIENT_ID":"myclient-id","myclient-SECRET":"myclient-secret"},comm="Shares"):
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'grant_type=password&client_id={creds["CLIENT_ID"]}&client_secret=creds["myclient-SECRET"]&username=creds["USERNAME"]&password=creds["PASSWORD"]'

        T = requests.post(f'https://{env}.sharefile.com/oauth/token', headers=headers, data=data)

        return T.json()
print(sharefile.TOKEN(sharefile,env=env)["value"])
#print(out.CSV(sharefile.index(sharefile,env=env)))
print(sharefile.index(sharefile,env=env))
#print(sharefile.auth(sharefile,env=env,creds={"USERNAME":"NETANELST@WE-ANKOR.CO.IL","PASSWORD":'318962420Ns$',"CLIENT_ID":"myclient-id","myclient-SECRET":"myclient-secret"}))

