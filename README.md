To build and run: copy the contents of the zip file into a directory, then run:

 >> docker build -t web .
 >> docker-compose up

Description of the stack: Docker & Docker Compose deploying Django with a Postgres database;
also includes 'uploads' and 'histograms' directories for persistent storage of images and their histograms

Description of the Algorithm: currently unimplemented; however, the intent was to leverage the python-binding
for the opencv library as follows: fix an image type T for the database and let I be a newly uploaded image of type T,
then we calculate:

>> H = cv2.calcHist([I],*options)

where options determine the number of bins and specific type of histogram dependent on T. We then compute,
for each histogram H' of some database image I' (which is not equal to the id of I), the score

>> S = cv2.compareHist(H, H', method)

where method could be any of 5 different metrics (again, we choose a single one for the whole image database
for consistency). We then display the 3 highest scoring pairs (I', S) in basic.html. 
