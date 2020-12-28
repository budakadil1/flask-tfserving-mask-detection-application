# flask-tfserving-mask-detection-application
This is an application that determines if someone is wearing a mask or not using with a tensorflow model, flask and tfserving.

### How does this work?
The flask app sends a request to the tensorflow/serving server (set up on a private vps) after processing the uploaded images to appropriate size. 

### Usage
Install requirements.txt. 


Change the system environment ```"TENSOR_SERVER_IP"``` to an IP:PORT which has tensorflow/serving installed. 


Also change the ```'/v1/models/img_classifier:predict'``` to ```'/v1/models/(YOUR MODEL NAME):predict'``` - or to any other url the post request is supposed to go to.

##### The actual model itself is not really good, this project was created so that I could learn about tfserving and machine learning model deployments into production in general.
