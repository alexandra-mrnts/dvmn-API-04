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

Telegram chat ID should be added to the .env file.
```
CHAT_ID = '@mychat'
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


### Project Goals
___

The code is written for educational purposes on online-course for web-developers dvmn.org.
