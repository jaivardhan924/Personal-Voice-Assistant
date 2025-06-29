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

1.![Screenshot 2025-06-29 154351](https://github.com/user-attachments/assets/ea586b88-749a-4318-92b9-2b02fe241434)

There will be 3 attempts to open

2.![Screenshot 2025-06-29 154626](https://github.com/user-attachments/assets/416d6659-2c2d-4ab8-b2e3-76886bd3a01f)

3.![Screenshot 2025-06-29 154713](https://github.com/user-attachments/assets/ff6e877e-8ea6-409c-aaa5-465e2ecfa74b)

2 and 3 -> When we use the commands show info and clear info

4.![Screenshot 2025-06-29 155318](https://github.com/user-attachments/assets/234cbf0a-7326-483d-9fbc-bcc9bfba6a20)
Accessing the camera(Resize , Camera flip)

5.![Screenshot 2025-06-29 155447](https://github.com/user-attachments/assets/db13f651-b14e-4b00-91fe-5be75f425aa9)

It asks a name to save the pic and It will store the pic in gallery with the respective given name

6.![Screenshot 2025-06-29 155931](https://github.com/user-attachments/assets/c9ee46f2-5080-4200-bbcb-72755507ceb1)
Locks the assistant,close the assistant

7.![Screenshot 2025-06-29 160121](https://github.com/user-attachments/assets/45cb94cc-77df-46b3-b740-291fb24d06ba)

tells the joke,shows Screen time,Check the Live time


Modular, voice-controlled, and customizable — this assistant brings together key Python libraries and system automation. Ideal for learning, demos, or personal use.


