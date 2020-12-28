import requests
import json
import numpy as np
import os 
url = os.environ["TENSOR_SERVER_IP"] + '/v1/models/img_classifier:predict'



def make_prediction(instances):
    data = json.dumps({ "instances": instances.tolist()})
    headers = {"content-type": "application/json"}
    json_response = requests.post(url, data=data, headers=headers)
    try:
        predictions = json.loads(json_response.text)['predictions']
    except KeyError:
        return "The model did not return any values. Please make sure that the upload is a picture."
    if predictions[0][0] == 1:
        return "No mask found."
    else:
        return "Mask in picture."

