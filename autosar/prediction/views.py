from django.shortcuts import render
from django.http import JsonResponse
import json
from .utils import predict_func
import binascii, base64
import cv2 as cv
import numpy as np
from django.views.decorators.clickjacking import xframe_options_exempt
# Create your views here.

playlists = {
    "happy": "1tTXdi6Bp04Pgmam9bSN7W",
    "angry":"37i9dQZF1EIfX5bt1426JC",
    "sad":"37i9dQZF1DXdFesNN9TzXT",
    "neutral":"7H6gu7y5AkuZPxd3bPM3N6"
}
@xframe_options_exempt
def predict(request):
    return render(request, "index.html",context={"":""})


def model(request):
    if request.method == "POST":
        image = json.loads(request.body.decode())["img"].split("data:image/jpeg;base64,")[1]
        # print(image)
        # print(is_base64(image))
        try:
            image = base64.b64decode(image, validate=True)
            file_to_save = "my_image.png"
            with open(file_to_save, "wb") as f:
                f.write(image)

            ims = cv.imread(file_to_save, cv.IMREAD_COLOR)
            gray_image = cv.cvtColor(ims, cv.COLOR_BGR2GRAY) 
            bigger = cv.resize(gray_image, (48, 48))
            numpydata = np.asarray(bigger)
            val= predict_func(numpydata)
            print(val)
        except binascii.Error as e:
            print(e)
        playlist = ""
        if val in playlists.keys():
            playlist = playlists[val]
        else:
            playlist = "7H6gu7y5AkuZPxd3bPM3N6"
        return JsonResponse({"data":val, "playlist":playlist})