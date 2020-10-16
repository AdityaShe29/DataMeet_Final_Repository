#Copyright 2018 Amazon.com, Inc. or its affiliates. All Rights Reserved.
#PDX-License-Identifier: MIT-0 (For details, see https://github.com/awsdocs/amazon-rekognition-developer-guide/blob/master/LICENSE-SAMPLECODE.)

import boto3
import json
client=boto3.client('rekognition')

def detect_faces(photo):
    photo1=open(photo,'rb')
    response = client.detect_faces(Image={'Bytes': photo1.read()},Attributes=['ALL'])

    print('Detected faces for ' + photo)    
    for faceDetail in response['FaceDetails']:
        print('The detected face is between ' + str(faceDetail['AgeRange']['Low']) 
              + ' and ' + str(faceDetail['AgeRange']['High']) + ' years old')
        print('Here are the other attributes:')
        print(json.dumps(faceDetail, indent=4, sort_keys=True))
    return len(response['FaceDetails'])
def main():
    photo='C:/Users/adity/Desktop/Coding Stuff/Hackathons/HackMIT Stuff/AWS/Confused_Test_Image.png'
    face_count=detect_faces(photo)
    print("Faces detected: " + str(face_count))


if __name__ == "__main__":
    main()

