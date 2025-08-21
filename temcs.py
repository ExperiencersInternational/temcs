import requests
import time
import os
from datetime import datetime

print("TEMCS Version 0.1.1 by ExperiencersInternational, https://github.com/ExperiencersInternational/temcs")
print("Insert camera ID below from Traffic England website:")
cameraID = input().strip()

folder = "Cameras"
os.makedirs(folder, exist_ok=True)

while True:
	try:
		# Insert code for downloading images
		filename = "CAM_" + cameraID + "_" + datetime.now().strftime("%Y%m%d_%H%M%S") + ".jpg"
		image = requests.get("https://public.highwaystrafficcameras.co.uk/cctvpublicaccess/images/" + cameraID + ".jpg")
		if image.status_code == 200:
			# Download Image
			with open(os.path.join(folder, filename), "wb") as f:
				f.write(image.content)
			print(filename + " saved to device.")
		else:
			print("Image failed to download")
	
	except Exception as e:
		print(f"Error: {e}")
	time.sleep(60)