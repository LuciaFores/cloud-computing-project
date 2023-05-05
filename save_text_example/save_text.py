# Python script to create and save a file in a folder

# This example will be used as starting point to understand
# how to redirect the save of a file in a AWS S3 Bucket

with open("text_file.txt", "w+") as F:
    F.writelines([
        "Hello, I am an example text file.\n",
        "If everything works as it should, I will be found in an AWS S3 Bucket.\n",
        "Of course this will happen only if the container in which my script is is already on AWS,\n"
        "don't worry if working locally you will find my somewhere else"
    ])