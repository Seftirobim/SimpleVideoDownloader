import yt_dlp
import os
from rich.console import Console
from rich.markdown import Markdown
import webbrowser
from rich.table import Table,box
from rich.align import Align
from win10toast import ToastNotifier
from plyer import notification
import subprocess
import platform

console = Console()
current_os = platform.system()
menu_options = {
   1: 'Open links.txt',
   2: 'Open Folder',
   3: 'Download Video(s)',
   4: 'Download Video(s) and Convert to Mp3',
   5: 'Exit'
}

title_markdown = """
# Simple Video Downloader & Mp3 Converter
"""
md = Markdown(title_markdown)

SRM_logo = """
  █████████  ███████████   ██████   ██████
 ███░░░░░███░░███░░░░░███ ░░██████ ██████ 
░███    ░░░  ░███    ░███  ░███░█████░███ 
░░█████████  ░██████████   ░███░░███ ░███ 
 ░░░░░░░░███ ░███░░░░░███  ░███ ░░░  ░███ 
 ███    ░███ ░███    ░███  ░███      ░███ 
░░█████████  █████   █████ █████     █████
 ░░░░░░░░░  ░░░░░   ░░░░░ ░░░░░     ░░░░░                                                                                            
"""
class MyLogger:
    def debug(self, msg):
        # For compatibility with youtube-dl, both debug and info are passed into debug
        # You can distinguish them by the prefix '[debug] '
        if msg.startswith('[debug] '):
            pass
        else:
            self.info(msg)

    def info(self, msg):
        pass

    def warning(self, msg):
        pass

    def error(self, msg):
        print(msg)

class MyCustomPP(yt_dlp.postprocessor.PostProcessor):
    def run(self, info):
        self.to_screen('Doing stuff')
        return [], info

def print_title():
    console.print(SRM_logo, justify="center",style="bright_cyan")
    console.print('https://github.com/Seftirobim/SimpleYTDownloader', justify="center", style="bold grey100")
    console.print(md)

def print_menu():
    table = Table(box=box.SIMPLE_HEAD)
    table.add_column("No",justify="center",style="bold bright_yellow")
    table.add_column("Options",justify="center",style="gold1")

    for k in menu_options.keys():
        table.add_row('['+str(k)+']',Align(menu_options[k],'left'))
    console.print(table)

def my_hook(d):
    if d['status'] == 'finished':
        print(' Success')

def download_videos(links, save_folder,convert=False):
    failed_links = []
    
    for link in links :
        try:
            if convert == False:
                ydl_opts = {
                    'format': 'bestvideo[height<=360][ext=mp4]+bestaudio[ext=m4a]/best[height<=360][ext=mp4]',
                    'outtmpl': os.path.join(save_folder, '%(title)s.%(ext)s'),
                    'progress_hooks': [my_hook],
                    'quiet': True,
                    'ignoreerrors': True,
                }
            else:
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'postprocessors': [{
                        'key': 'FFmpegExtractAudio',
                        'preferredcodec': 'mp3',
                        'preferredquality': '192',
                    }],
                    'outtmpl': os.path.join(save_folder, '%(title)s.%(ext)s'),
                    'progress_hooks': [my_hook],
                    'quiet': True,
                    'ignoreerrors': True
                }  
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.add_post_processor(MyCustomPP(), when='pre_process')
                ydl.download([link])
                # Notification script tested on windows 10
                if current_os == 'Windows' or current_os == 'Linux': # Show Windows or linux notification
                    notification.notify(title="Process Finished !", message=f"{menu_options[prompt]} process has completed.", timeout=10)
                elif current_os == 'Darwin': # Show mac notification
                    subprocess.run(['osascript', '-e', f'display notification "{menu_options[prompt]} process has completed." with title "Process Finished !"'])

        except Exception as e:
            error_message = e
            failed_links.append(link)
            console.print(f"Error downloading video from {link}: {str(e)}",style="red1")
        
            

    return failed_links


def run(C=False):
    current_path = os.getcwd()
    #get links.txt file from path
    file_path = ''.join([current_path,'/links.txt'])

    with open(file_path, "r") as file:
        video_links = file.read().splitlines()

    console.print(f"\nTotal link(s): {len(video_links)} link",style="plum2")

    #get save path
    if C == False:
        save_path = ''.join([current_path,"/downloads/video"])
        failed_videos = download_videos(video_links, save_path,False)
    else:
        save_path = ''.join([current_path,"/downloads/mp3"])
        failed_videos = download_videos(video_links, save_path,True)

    # Display the failed videos, if any
    if failed_videos:
        print("\nList of videos that failed to download :")
        for link in failed_videos:
            print(link)
    else:
        if C == False :
            console.print("\nAll video(s) have been successfully downloaded.!",style="bold spring_green1")
        else:    
            console.print("\nAll video(s) have been successfully downloaded and converted!",style="bold spring_green1")
        
        while True:
            try:
                open_folder = input("Would you like to open the folder? (y/n): ")
            except:
                console.print(f"Invalid Input ! Enter (y/n)",style="red1")
            if open_folder.lower() == "y":
                webbrowser.open(os.path.abspath(save_path))
                break
            elif open_folder.lower() == "n":
                console.print(f"Exit !",style="yellow")
                break
            else:
                console.print(f"Invalid Input ! Enter (y/n)",style="red1")

if __name__ == "__main__":
    while True:
        prompt = int;
        try:
            print_title()
            print_menu()
            prompt = int(input("Select an option between [1-5] : "))
        except:
            print("Invalid Input !")
        if prompt == 1 :
            file= 'links.txt'

            open_file =  os.startfile(file) 
        elif prompt == 2:
            folder = os.getcwd()
            webbrowser.open(os.path.abspath(folder))            
            
        elif prompt == 3:
            run(False)            
            break
        elif prompt == 4:
            run(True)            
            break
        elif prompt == 5:
            console.print("Exit !",style="red1")
            break
        else:
            print('Invalid Input, Enter (y/n)')        