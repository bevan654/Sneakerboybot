import json


def openData(file):
    with open("Sneakerboy/"+str(file)) as file:
        data = json.load(file)

    return data