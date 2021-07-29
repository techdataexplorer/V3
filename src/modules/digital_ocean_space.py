from boto3 import session
from botocore.client import Config

ACCESS_ID   = 'ORVL2QNOJHPJSRCFQ7E6'
SECRET_KEY  = 'KdqAOLnANz/mBe2UYTjiESD8jKht+J9msFAMTchi4AM'

# Initiate session
session = session.Session()
client  = session.client(
    's3',
    region_name = 'sfo3',
    endpoint_url = 'https://tdx-dev-documentation.sfo3.digitaloceanspaces.com/',
    aws_access_key_id = ACCESS_ID,
    aws_secret_access_key = SECRET_KEY
)

# Upload a file to your Space
client.upload_file('./../img/user.png', 'test', 'new-folder/user.png')
