import setting
import os

cloudflare_api = os.getenv('cloudflare_api')
zone_id = os.getenv('zone_id')
auth_key = os.getenv('auth_key')
auth_email = os.getenv('auth_email') 

print(cloudflare_api,zone_id,sep='\n')