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
TG_CHAT_ID = '@mychat'
TG_TOKEN = '7219856276:AAGKGrSZwgpZf74JGEIBlAjiAosaVjBf4Tw'
```

### How to use
___
To upload images from SpaceX launches use the following command:
```
fetch_spacex_images.py [-l launch_id] [-d directory]
```
* **launch_id** (optional): If not specified, images from the latest launch will be uploaded
* **directory** (optional): Specifies the directory where images will be stored. If not specified, SPACEX_STORAGE_DIR environment variable will be used. If the environment variable is not set, the default subfolder 'images' will be used.


\
To upload NASA images of a day use the following command:
```
fetch_NASA_apod.py [-n pics_number] [-d directory]
```
* **pics_number** (optional): Number of images to be loaded. If not specified, NASA_APOD_PICS_NUMBER environment variable will be used. If the environment variable is not set, the default number of 5 images will be loaded.
* **directory** (optional): Specifies the directory where images will be stored. If not specified, NASA_APOD_STORAGE_DIR environment variable will be used. If the environment variable is not set, the default subfolder 'images' will be used.
  

\
To upload NASA Earth Polychromatic Imaging Camera (EPIC) images use the following command:
```
fetch_NASA_EPIC.py [-n pics_number] [-d directory]
```
* **pics_number** (optional): Maximum number of images to be loaded. If not specified, NASA_EPIC_PICS_NUMBER environment variable will be used. If the environment variable is not set, the default number of maximum 5 images will be loaded.
* **directory** (optional): Specifies the directory where images will be stored. If not specified, NASA_EPIC_STORAGE_DIR environment variable will be used. If the environment variable is not set, the default subfolder 'images' will be used.


\
To post an image to a Telegram channel use the following command:
```
publish_image.py file_name
```  

\
To post all images from a directory to a Telegram channel:
```
publish_all_images.py [-f frequency] [-d directory]
``` 
* **frequency** (optional): Sets the posting frequency in hours. The script will post one image at the specified interval. After all images are posted, it will countinue with the same reshuffled images.
If not specified, TG_POSTING_FREQUENCY environment variable will be used. If the environment variable is not set, the default posting interval is 4 hours.
* **directory** (optional): Specifies the directory containing the images to be posted. If not specified, TG_IMAGE_SOURCE_DIR environment variable will be used. If the environment variable is not set, the default directory is 'images' subfolder.


### Project Goals
___

The code is written for educational purposes on online-course for web-developers dvmn.org.
