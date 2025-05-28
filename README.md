Instructions (no virtual environment):
1. Install Python 3.11.9.
2. Install Microsoft C++ Build Tools.
3. Select "Desktop development with C++".
4. Individually select MSVC v14.x compiler toolset (latest version) and Windows 10/11 SDK (or appropriate SDK) if needed.
5. Install eSpeak. Set eSpeak to PATH (system environment).
6. Install the best_model.pth from [https://drive.google.com/file/d/1-35ZCl1vb_8UFxwTHNlYWNgbVXGZVx_0/view]. You may have to rename the .pth file to best_model. Move the best_model.pth file to the installation folder.
7. Run the setup.bat, which will install gradio and TTS directly to your system.
8. Install the requirements (gradio and TTS) on your system.
9. Copy the link and paste it on your browser.

Instructions (virtual environment):
1. Setup the virtual environment. Make sure the python version is 3.11.9.
2. Move into the virtual environment, if you have not already done so.
3. Make sure you already have Microsoft C++ Build Tools installed, and eSpeak. Set eSpeak to PATH (system environment).
4. On terminal, run "pip install gradio". (Alternatively, just download the requirements directly.)
5. On terminal, run "pip install TTS". (Alternatively, just download the requirements directly.)
6. If in case "pip install TTS" errors due to Microsoft C++ Build Tools, navigate to the Microsoft Visual C++ Compiler (the x64 version or the x86 version depending on your computer) and move into the virtual environment and run "pip install TTS" there.
7. Run the app.py, which will output a link.
8. Copy the link and paste it on your browser.

Run via virtual environment or directly.
We also provide a much more accessible version on huggingface, which enables an always online demo of our model. The link can be accessed here: 
[https://huggingface.co/spaces/Yabes456/Text_To_Speech_LJSpeech_Project/tree/main]
