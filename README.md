# Personal-Voice-Assistant
An AI-based personal voice assistant built using Python

This project is a voice-controlled personal assistant built using Python. It can perform tasks like telling time, searching YouTube, telling jokes, capturing photos, clearing logs, and more — all through simple voice commands. The assistant uses speech recognition to understand the user's voice, and text-to-speech to respond back, creating a basic but functional AI interaction system.

The project is organized in a clean and modular way:

🔑 mainf.py: The entry point that launches the assistant by verifying a password.

🧠 main1/main.py: Contains core logic including run_siri() and password() functions.

🗣️ AI/ai.py: Handles the text-to-speech functionality via the talk(text) function.

🎙️ command1/command.py: Converts spoken words into text using take_command().

📸 camera/: Contains photo capture (capture.py) and file-saving (picture.py) logic.

⚙️ general/: Handles specific features like:

time.py – tells the current time

yout.py – searches YouTube

joke.py – tells random jokes

log.py, clear.py – shows/clears the query log

chrome.py – opens browser

inform.py and coding.py – extra commands like giving info or help with coding

📁 data/qandA.txt: Maintains logs of all questions and commands for history tracking.

🔐 Only the commands listed in path.txt are allowed to run, which ensures control and safety over what the assistant can execute.

This structure makes the assistant easy to expand and maintain. You can plug in new features just by adding Python files to relevant folders.

Below diagrams shows how the Voice Assistant works: 

1.![Screenshot 2025-06-29 154351](https://github.com/user-attachments/assets/07f01504-a32f-431d-8a25-9b8fc7ae62a2)
There will be 3 attempts to open

2.![Screenshot 2025-06-29 154626](https://github.com/user-attachments/assets/6ec0f5cd-c859-4ec2-aa0f-2d0f1f7a5a6d)
3.![Screenshot 2025-06-29 154713](https://github.com/user-attachments/assets/c673eea9-12d4-4166-af4c-f42e89e3237e)
2 and 3 -> When we use the commands show info and clear info

4.![Screenshot 2025-06-29 155318](https://github.com/user-attachments/assets/eb17d1ed-f1b4-4db6-ab64-c84f94826e7b)
Accessing the camera(Resize , Camera flip)

5.![Screenshot 2025-06-29 155447](https://github.com/user-attachments/assets/405efd87-ef84-4091-8c1c-26a72f6b8b1f)
It asks a name to save the pic and It will store the pic in gallery with the respective given name

6.![Screenshot 2025-06-29 155931](https://github.com/user-attachments/assets/87f8d4d3-e817-4cea-a6a3-456a67c4db38)
Locks the assistant,close the assistant

7.![Screenshot 2025-06-29 160121](https://github.com/user-attachments/assets/f22d59da-f36d-4249-9b2b-301eacda2b61)
tells the joke,shows Screen time,Check the Live time


Modular, voice-controlled, and customizable — this assistant brings together key Python libraries and system automation. Ideal for learning, demos, or personal use.


