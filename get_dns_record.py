import json,os
import requests
import setting


cloudflare_api = os.getenv('cloudflare_api')
zone_id = os.getenv('zone_id')
auth_key = os.getenv('auth_key')
auth_email = os.getenv('auth_email') 
headers = {'X-Auth-Key': auth_key, 'Content-Type':'application/json',"X-Auth-Email": auth_email}

cloudflare_dns = cloudflare_api + "zones/" + zone_id + "/dns_records"  
cloudflare_dns_respon = requests.get(cloudflare_dns, headers=headers)

if cloudflare_dns_respon.status_code == 200:
    print("Ok")
else:
    print(cloudflare_dns_respon.status_code)    

dns_data = json.loads(cloudflare_dns_respon.text)
print(dns_data)