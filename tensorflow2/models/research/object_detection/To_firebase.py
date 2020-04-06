import pyrebase
import os

config = {
    "apiKey": "AIzaSyDCXpdwHx2c8N3RpXSPf8SYiNqLMvY5SYc",
    "authDomain": "potholedataset.firebaseapp.com",
    "databaseURL": "https://potholedataset.firebaseio.com",
    "projectId": "potholedataset",
    "storageBucket": "potholedataset.appspot.com",
    "messagingSenderId": "1057519221937",
    "appId": "1:1057519221937:web:a61ef5e279753b2ae4b690",
    "measurementId": "G-B6EE34DTBM"
}

arr = os.listdir("detected/")
dir = "detected/"
countx = 0
county = 0
for x in arr:
    arr2 = os.listdir(dir + arr[countx])
    for x2 in arr2:
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_on_cloud = "images/" + str(arr[countx]) + "/"
        path_on_local = dir + str(arr[countx]) + "/" + str(arr2[county])
        x = path_on_local.split("/")
        storage.child(path_on_cloud + x[len(x) - 1]).put(path_on_local)
        print(path_on_local + "    Uploaded to    " + path_on_cloud)
        print(path_on_cloud+str(arr2[county]))
        print(storage.child(path_on_cloud+str(arr2[county])).get_url(1))
        county += 1
    countx += 1

