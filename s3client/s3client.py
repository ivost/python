
ENDPOINT = 'localhost:9090'
ACCESS_KEY = '1V07RX7WMBH5C7G3OKVZ'
SECRET_KEY = 'YBEaJPx3yQC1sQiTOB0I58eFPJ2RCYAqFw6jLVZD'

# # https://github.com/smore-inc/tinys3
# import tinys3
# # Creating a simple connection
# conn = tinys3.Connection(ACCESS_KEY, SECRET_KEY, endpoint=ENDPOINT)
#
# # This will return an iterator over the metadata of the files starting with 'prefix' in 'my_bucket'
# # The iterator will yield dicts with the following keys: key, etag, size, last_modified, storage_class
# for obj in conn.list(bucket='mydir'):
#     print(obj)

# Import Minio library.
# https://docs.minio.io/docs/python-client-api-reference

from minio import Minio

# Initialize minioClient with an endpoint and access/secret keys.
s3 = Minio(ENDPOINT,
           access_key=ACCESS_KEY,
           secret_key=SECRET_KEY,
           secure=False)

buckets = s3.list_buckets()
for bucket in buckets:
    print(bucket.name, bucket.creation_date)

for obj in s3.list_objects('mydir'):
    print(obj)

# <Object: bucket_name: mydir
# object_name: b'41344.pdf'
# last_modified: 2017-05-10 13:28:32.024000+00:00
# etag: 8f4f0d6a5f3740a64d0a6a1df1bfade1
# size: 415514
# content_type: None,
# is_dir: False,
# metadata: None>
####################

# # Make a bucket with the make_bucket API call.
#from minio.error import (ResponseError, BucketAlreadyOwnedByYou,
#                         BucketAlreadyExists)

# try:
#        s3.make_bucket("maylogs", location="us-east-1")
# except BucketAlreadyOwnedByYou as err:
#        pass
# except BucketAlreadyExists as err:
#        pass
# except ResponseError as err:
#        raise
# else:
#         try:
#                s3.fput_object('maylogs', 'pumaserver_debug.log', '/tmp/e.csv')
#         except ResponseError as err:
#                print(err)

