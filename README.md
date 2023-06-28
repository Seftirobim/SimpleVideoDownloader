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
![image](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/3fcb7f90-40e5-46dc-98ce-c19b527da2d7)
![image](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/f3d85bfc-ca42-4972-9891-a21443c389a9)

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

![1](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/b5f272fa-7ebe-4208-ab59-87e606e54b27)
</details>

<details>
<summary>Third step</summary>
 
 * Download the package and save it anywhere you want and uncrompress it. For example, we open the compression in `C:/ffmpeg`
 * Record the path `C:\ffmepg\bin)` and head over to “Edit the system environment variables".
 
![copy path](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/5e569130-9776-4ecd-88dc-3fa37c2bb0d2)
</details>

<details>
<summary>Fourth step</summary>
 
 To open this, go to the search bar on Windows and type “path” or "envi"
 
![3](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/e87b5c57-e4d1-4d7f-b3e6-b54868c99549)
</details>
<details>
<summary>Fifth step</summary>
 
 In System Properties > Advanced, head over to “Environment Variables”
 
![4](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/9f19ddd8-4300-425c-a35c-135096e1f7b9)
</details>
<details>
<summary>Sixth step</summary>
 
 In Environment Variables, under “User variables for Administrators” choose Path (1) > then click on “Edit”.
 
![5](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/c44bceb0-11d3-43b9-8fc4-24a8c35a404e)
</details>
<details>
<summary>Seventh step</summary>
 
 The new “Edit Enviromnet variable” window will open. Click on New (1) > Enter the Path where FFmpeg is stored (2) > Click on Ok (3).
 
![6](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/b0e94f1c-a5f6-4201-8df7-4898909571b5)
</details> 
<details>
<summary>Eighth step</summary>
 
- Now, test the FFmpeg configuration from the Windows command prompt. Open the “cmd” and type ‘ffmpeg’. You should get an output such as the one below.
 
![7](https://github.com/Seftirobim/SimpleVideoDownloader/assets/16395774/4dd3289c-a4ae-430d-b73e-97ffa0d43d4f)

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
