import requests

class sharefile():
  
    def index(env:str,creds=None,comm=None):
      

        res = requests.get(f'https://{env}.sf-api.com/sf/v3')

        print(res)
        return res.json()
    def upload(env:str,creds={"USERNAME":"my@user.name","PASSWORD":'mypassword',"CLIENT_ID":"myclient-id","myclient-SECRET":"myclient-secret"},comm="Shares"):
        
        headers = {
            'Content-Type': 'application/x-www-form-urlencoded',
        }

        data = f'grant_type=password&client_id={creds["CLIENT_ID"]}&client_secret=creds["myclient-SECRET"]&username=creds["USERNAME"]&password=creds["PASSWORD"]'

        T = requests.post(f'https://{env}.sharefile.com/oauth/token', headers=headers, data=data)

        return T

print(sharefile.index("weankor"))