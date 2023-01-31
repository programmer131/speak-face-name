import requests
import playsound
import time
import os
from preferredsoundplayer import *
import vlc
import requests # request img from web
from PIL import Image
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
#player=vlc.MediaPlayer('rtsp://192.168.18.64/live/ch00_0')
#player=vlc.MediaPlayer('http://192.168.18.112:8080/video')
#player.play()


def my_func():
	image_path="photo.jpg"	
	#player.video_take_snapshot(0, image_path, 0, 0)
	img_data = requests.get('http://192.168.18.112:8080/shot.jpg').content
	with open(image_path, 'wb') as handler:
  		handler.write(img_data)
	check_file = os.path.isfile(image_path)
	if check_file:
		#image = Image.open(image_path)
		#image.show()
		image_data = open(image_path,"rb").read()
		response = requests.post("http://localhost:32168/v1/vision/face/recognize",
		files={"image":image_data}).json()
		if "predictions" in response:
			for user in response["predictions"]:
				if user["confidence"] > 0.75:
					print(user["userid"])
					if user["userid"] == "farrukh":
						soundplay('hello.wav')
						time.sleep(2)
					if user["userid"] == "amna":
						soundplay('amna.wav')
						time.sleep(2)
					if user["userid"] == "maryam":
						soundplay('maryam.wav')
						time.sleep(2)
					if user["userid"] == "abdullah":
						soundplay('abd.wav')
						time.sleep(2)
		print("Full Response: ",response)
		
while 1:
	my_func()