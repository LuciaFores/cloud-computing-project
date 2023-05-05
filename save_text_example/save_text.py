import boto3

# Python script to create and save a file in a folder

# This example will be used as starting point to understand
# how to redirect the save of a file in a AWS S3 Bucket

s3_client = boto3.client('s3')

fileName = "text_file.txt"
bucketName = "cloud-computing-model-bucket" 

with open(fileName, "w+") as F:
    F.writelines([
        "Hello, I am an example text file.\n",
        "If everything works as it should, I will be found in an AWS S3 Bucket.\n",
        "Of course this will happen only if the container in which my script is is already on AWS,\n"
        "don't worry if working locally you will find my somewhere else"
    ])

s3_client.upload_file(fileName, bucketName, fileName)