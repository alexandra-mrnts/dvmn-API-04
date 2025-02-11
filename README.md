# Space Telegram

A set of scripts that fetch and upload space-related images (SpaceX launches, NASA pictures of the day and NASA Earth pictures) and automatically post them to a Telegram channel.

### How to install
___

Python3 should already be installed. 
Use `pip` (or `pip3`, if there is a conflict with Python2) to install dependencies:
```
pip install -r requirements.txt
```

Your NASA API key should be added to the .env file.
```
NASA_API_KEY = 'sdVN2WyjQycGe7WIdxDHr68hQFCKHrhl1bcbfMat' 
```
You can generate your API key here: https://api.nasa.gov/

Telegram chat ID and access token should be added to the .env file.
```
CHAT_ID = '@mychat'
TG_TOKEN = '7219856276:AAGKGrSZwgpZf74JGEIBlAjiAosaVjBf4Tw'
```

### How to use
___
Upoading SpaceX launches images:
```
fetch_spacex_images.py [launch_id]
```
If launch id is not specified images from the latest launch will be uploaded.  
\
Uploading NASA images of a day:
```
fetch_NASA_apod.py
```
Number of images can be set in .env file:
```
NASA_APOD_PICS_NUMBER = 5
```  
\
Uploading NASA Earth Polychromatic Imaging Camera (EPIC) images:
```
fetch_NASA_EPIC.py
```
Number of images can be set in .env file:
```
NASA_EPIC_PICS_NUMBER = 5
```  
\
All images will be stored in 'images' subfolder.    
\
Posting an image to a Telegram channel:
```
publish_image.py file_name
```  

Posting all images from 'images' subfolder to a Telegram channel:
```
publish_all_images.py [posting_frequency]
``` 
Set default posting frequency in hours in a .env file.
```
POSTING_FREQUENCY = 24
```  

### Project Goals
___

The code is written for educational purposes on online-course for web-developers dvmn.org.
