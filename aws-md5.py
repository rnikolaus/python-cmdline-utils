'''
Created on 19.06.2016

@author: rapnik
'''
import boto3
# Let's use Amazon S3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    #sizesum=0
    for key in bucket.objects.all():
        print key.key, key.e_tag.replace('"',''),key.size
        #sizesum+=key.size
    #print sizesum