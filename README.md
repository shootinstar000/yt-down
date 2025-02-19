# Termux Downloader Android (aka Youtube-Downloader-Android)

## History of developement of this script
Hi all! This script was once intended to download video and audio, only from youtube. Later it is extended to download videos from almost all sites and social media, torrents and Google drive.


## Installation (Stable version):

1. 📥 **Install Termux** from [GitHub](https://github.com/termux/termux-app/releases) (arm64 recommended, use arm only for devices lower than Android 7).
2. 🔧 **Run the following commands in Termux**:
    ```sh
    pkg up -y
    pkg install git -y
    git clone https://github.com/shootinstar000/yt-down/ -b master --single-branch
    cd Youtube-Downloader-Android
    sh install.sh
    ```
3. 🛡️ **Press ALLOW** to give storage permission.
4. ⚠️ **For Android 10 or above users**: Go to app settings -> Termux app settings -> Allow "Display over other apps" permission for the script to work.

## Troubleshooting or Repairing:

If the program is not working properly or showing errors, follow these steps:

1. 📱 **Open Termux app**.
2. 🔄 **Type**:
    ```sh
    sh refresh.sh
    ```
3. The program will be clean installed or returned to factory default.

## Usage:

### How to Download Videos or Audio:

1. 🌐 **Open the desired video or audio or playlist**.
2. 📤 **Select the share option**.
3. 📲 **Choose TERMUX from the share list**.
4. 📥 Your video/audio/playlist will be downloaded (Location: Internal storage of your device -> Termux-Downloader).
5. 🎥 **For YouTube Download**: Select Video/audio/best -> Pick required resolution once, it will be set as default (can change by typing "y") -> Skip next unless custom format needed.
6. 🎵 **For YouTube Music**: Type your preferred audio codec (like mp3, m4a, aac, webm, flac...) once as default (can change later) -> Audio will be downloaded in your preferred format.
7. ☕ **Note**: This script is completely automated, closes itself after downloading. Just share your link to Termux and relax!

## Features:

### History:

1. 📝 The name, site of download, and URL of the files downloaded by this script are saved as history.
2. 🔒 Don't worry, only a code makes it visible. Otherwise, none will know about it.
3. 📜 History feature helps to:
   - Redownload files previously downloaded.
   - Revisit sites from where files were downloaded.
4. 🧹 You can clear the history too!
5. Code to see history:
    ```sh
    python history.py
    ```

### Updates:

1. 🔄 Updates are completely automatic, no need to worry about it.
2. 🛠️ If facing issues with new updates or having suggestions, note them in the issue section.




**We extend our special thanks to @DrDelin for the script.**
