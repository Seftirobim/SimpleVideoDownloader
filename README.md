<div align="center">
 
```
  █████████  ███████████   ██████   ██████
 ███░░░░░███░░███░░░░░███ ░░██████ ██████ 
░███    ░░░  ░███    ░███  ░███░█████░███ 
░░█████████  ░██████████   ░███░░███ ░███ 
 ░░░░░░░░███ ░███░░░░░███  ░███ ░░░  ░███ 
 ███    ░███ ░███    ░███  ░███      ░███ 
░░█████████  █████   █████ █████     █████
 ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░     ░░░░░ 
```
</div> 

# SimpleVideoDownloader

SimpleVideoDownloader is a simple script for downloading videos in 360p resolution (default) based on the list of YouTube links in the "links.txt" file.And it can also directly convert to MP3 files.

- Python 3.
- Easy to use.
- Downloading videos from the links provided in the `links.txt` file in 360p resolution (You can modify it within the script).
- It can directly convert to MP3 files.
- This script is assisted by Chat GPT.

## NOTE
```
- Not all websites use the same format or provide the same options for downloading videos. For example, this code may not work properly for downloading videos from websites that employ different download methods or are incompatible with youtube_dl
- Tested on YouTube 
```

## HOW TO USE

- First, install Python (if you haven't already).
- Simply edit the `links.txt` file, enter each YouTube link on a separate line.
- Run the script and enter the prompted command.

```sh
$ python main.py
```
- choose an option
  
## SCREENSHOOTS
![image](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/9e4aa1b6-c6a4-471d-a865-9742cfc90b17)
![image](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/ac190447-3cc0-4f11-9d9d-53dc2173132d)


## IMPORTANT
is highly recommended that you install FFmpeg and FFprobe. FFprobe comes when you install the  FFmpeg package.

**To install FFmpeg on a MacOS machine, use the following command:**
```
brew install ffmpeg
```
**To install FFmpeg on a Linux machine (Ubuntu 22.04), use the following command:** 
```sh
$ sudo apt install ffmpeg
```
**To install FFmpeg on a Windows machine, use the following command:**
<details>
<summary>First step</summary>

 go to [this repository](https://github.com/BtbN/FFmpeg-Builds/releases)
</details>

<details>
<summary>Second step</summary>

 Choose your release, download the 7z or zip file.

![1](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/307963ef-0a9b-43c2-abf8-89c36efc9198)
</details>

<details>
<summary>Third step</summary>
 
 * Download the package and save it anywhere you want and uncrompress it. For example, we open the compression in `C:/ffmpeg`
 * Record the path `C:\ffmepg\bin)` and head over to “Edit the system environment variables".
 
![copy path](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/f547f0b5-e232-44b9-a0fb-e34808a95621)

</details>

<details>
<summary>Fourth step</summary>
 
 To open this, go to the search bar on Windows and type “path” or "envi"
 
![3](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/3f88e5ee-3405-4141-8417-bc335a237400)

</details>
<details>
<summary>Fifth step</summary>
 
 In System Properties > Advanced, head over to “Environment Variables”
 
![4](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/3c0d86ac-9584-4c1f-be08-49e2c93bbada)

</details>
<details>
<summary>Sixth step</summary>
 
 In Environment Variables, under “User variables for Administrators” choose Path (1) > then click on “Edit”.
 
![5](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/269685ca-39aa-4051-b48f-4691c507e9c9)

</details>
<details>
<summary>Seventh step</summary>
 
 The new “Edit Enviromnet variable” window will open. Click on New (1) > Enter the Path where FFmpeg is stored (2) > Click on Ok (3).
 
![6](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/a71ce1eb-6689-4ccb-9db7-b691333c4b31)

</details> 
<details>
<summary>Eighth step</summary>
 
- Now, test the FFmpeg configuration from the Windows command prompt. Open the “cmd” and type ‘ffmpeg’. You should get an output such as the one below.
 

![7](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/3137e2cf-1510-4ccf-a051-494e62ecc087)

- **If an error occurs, try restarting the machine.** 
</details>   


## INSTALLATION REQUIREMENTS 

Windows:
```sh
$ pip install -r requirements.txt
```

Linux:
```sh
$ pip3 install -r requirements.txt
```
