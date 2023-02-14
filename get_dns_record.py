import json
import requests

cloudflare_api = "https://api.cloudflare.com/client/v4/"
zone_id = "76f2fb27077bfc7a3fbf8bee90739657"
auth_key = "45caf666401690e41da888da405b0b99ac01a"
auth_email = "dlin12457.work@gmail.com"
headers = {'X-Auth-Key': auth_key, 'Content-Type':'application/json',"X-Auth-Email": auth_email}

cloudflare_dns = cloudflare_api + "zones/" + zone_id + "/dns_records"  
cloudflare_dns_respon = requests.get(cloudflare_dns, headers=headers)

if cloudflare_dns_respon.status_code == 200:
    print("Ok")
else:
    print(cloudflare_dns_respon.status_code)    

dns_data = json.loads(cloudflare_dns_respon.text)
print(dns_data)