# ubiquitous_health_recorder
It's used to capture,maintain and retrieve patient data at instance by doctors.
(post method) http://"your_ip"/get used to get data of a patient[{"id":"patient_Id","proof":"1256","data":"he has fever"}]
(post method) http://"your_ip"/put used to get data of a patient[{"id":"patient_Id"}]
A docker file is updated so it can be used to create docker image
To pull docker image use - docker pull vishwak1998/ubiquitous_health_recorder_v1:uhr1
To run container use - sudo docker run -d -p 80:80 --name containername imagename 
docker link - https://hub.docker.com/r/vishwak1998/ubiquitous_health_recorder_v1
