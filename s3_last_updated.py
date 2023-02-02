import s3fs
import boto3

fs = s3fs.S3FileSystem(anon=False)
s3r = boto3.resource('s3')
# Connect to a specific bucket
bucket = s3r.Bucket('')

#Todays date - 1
d = (datetime.today() - timedelta(days=1)).strftime("%Y-%m-%d")

keys = []
dates = []
for i in to_loop:
    try:
        for obj in bucket.objects.filter(Prefix='/' + i + '/', Delimiter='/'):
            if obj.last_modified.strftime("%Y-%m-%d") == d:
                dates.append(obj.last_modified.strftime("%Y-%m-%d"))
                keys.append(obj.key) 
            else:
                pass
