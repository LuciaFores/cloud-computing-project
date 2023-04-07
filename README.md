 Execute the following steps to work with the container:
 
 **Build the image** 

 docker build -t toy-image-recognition .

 **Run the container**

 sudo docker run -d toy-image-recognition

<br>
 Notice that if the container is not presented as running in Docker Desktop is probably due to the fact that the context used is the *default* instead that the *desktop* one.
 To fix this please do the following:

**Check the context present**

(Notice that the current context used is marked by a *)

docker context ls

**Choose the *desktop* one** 

docker context use < desktop-context-name >

**Open Docker Desktop BEFORE running the container**

(Or else you will incur in an error)
