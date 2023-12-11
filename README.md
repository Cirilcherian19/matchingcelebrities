Face matching app

This is  project having the faces 100 bollywood celebrities.When we give an image.It reads the image and provides best suitable celebrites face..


Work flow of this project:


1:create requirements.txt and setup.py and install requiremnets using

pip install -r requirements.txt
run python.setup.py for building packages


Update params.yaml file with all the parameters requiresd for the project.


First we need to read all the 100 celebrities photos.create a function to read all the photos with labels and store this as pickle file.So that we will be able to read this file under any time.we are taking all the CNN part of the resnet50 architecture.We dont want to take feed forward network part of the model through transfer learning.



When we are giving an image image is transformed to a particular dimension and this is mapped with all the celebrities images.To check similiarity cosine similiarity is used.and it rturns the best similiar image with label..


in order to view all these things from a web page .I used flask webframework with html and css.
