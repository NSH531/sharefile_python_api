import requests

class sharefile():
    """
    this class implements sharefile's API
    methods:
     
    > auth -  get autenticating token 
    > items
    """
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

print(sharefile.index("weankor"))
print(sharefile.auth("weankor",creds={"USERNAME":"my@user.name","PASSWORD":'mypassword',"CLIENT_ID":"myclient-id","myclient-SECRET":"myclient-secret"}))