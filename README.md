# YT Downloader
YT Downloader is a simple and user-friendly tool to download audio (MP3) — and soon video (MP4) — from YouTube.

It is designed for everyday users who want an easy way to save their favorite content offline.

## 🚀 Features
- Download YouTube audio in **MP3 format**.
- Download YouTube video in **MP4 format**.
- Automatic conversion using **FFmpeg**.
- Saves files into a dedicated folder for better organization.
- Cross-platform support (Windows, macOS, Linux).

## 🛠️ Getting Started
These instructions will get you a copy of the project up and running on your local machine.

### ✅ Prerequisites
You will need the following software installed on your system:

Python 3.x: 

FFmpeg: A powerful tool for handling multimedia. Download the correct version for your operating system that includes both ffmpeg.exe and ffprobe.exe and include the complete rute to the bin folder in a .env as "FFMPEG_PATH"

### 📥 Installation
1. Clone the repository to your local machine:

        git clone https://github.com/your-username/yt-downloader.git
        cd yt-downloader

2. Install the required Python libraries using pip:

        pip install -r requirements.txt

3. Configure FFmpeg:

    Add the path to the bin folder of your FFmpeg installation to a system environment variable named FFMPEG_PATH.

    Alternatively, you can create a .env file in the project's root folder and add the following line:

        FFMPEG_PATH=/path/to/your/ffmpeg/bin

## ▶️ Usage
Once the setup is complete, you can run the main script from your terminal:

    python main.py

This will start the application. Follow the on-screen prompts to paste a YouTube URL and begin the audio download.

The converted MP3 file will be saved in a new folder created by the program.

## 🤝 Contributing
We welcome contributions from everyone! If you want to help improve this project, here's how you can get started:

1. Fork the repository on GitHub.

2. Clone your forked repository to your local machine.

        git clone https://github.com/your-username/yt-downloader.git

3. Create a new branch for your feature or bug fix:

        git checkout -b feature/your-feature-name.

4. Make your changes and commit them:

        git commit -m "feat: Add new feature"

5. Push your changes to your forked repository: git push origin feature/your-feature-name.

        git push origin feature/your-feature-name

6. Open a pull request from your branch to our main branch.

    We'll review your contribution as soon as we can! 🚀

### 💡 Ideas for new features
- More formats availabe, such as m4p, webm...
- Make a GUI for the programs, using Tkinter or Flask with HTML and CSS
- Other ideas are welcomed 🤗

## 📄 License
This project is licensed under the MIT License. See the LICENSE file for more details.

## 📬 Contact
If you have any questions or feedback, feel free to reach out to us!

- GitHub Issues: Open an issue on this repository to report bugs or suggest new features.

- Or simply star ⭐ the repo to support the project!
