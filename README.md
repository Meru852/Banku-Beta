# OnlineClassBot

The Online Class Bot is built on Python and its main purpose is to attend online classes for you.This bot gets the meeting ID of the class from user and opens Google Meet and logs in on your behalf . It can use both Speech Recognition and Image Processing techniques to interact with other people in the meeting.Once the class is over, it closes the Google Chrome page and this process continues every time you have an online class to attend.

Speech Recognition will be used to identify when your name is being called by the teacher for attendance and the bot automatically types Present in the chat box.
Image Processing will be used to convert all the messages in the chatbox into an array of strings and use some string manipulation techniques to find the most common phrase most of the students said and type it in the chat box.For eg: When a teacher asks everyone to type the answer to a certain question in the chat box.

## Libraries to be used:
* PyAutoGUI/Selenium ---> To automate the browser 
* Pillow ---> To do image processing 
* PyTesseract ---> To convert images to text 
* WinSound ---> To play 'present' sound while attendance 
* speech_recognition ---> Used for speech to text conversion 
* Regular Expressions 
* PyAudio ---> To get acces to the microphone when the user gets alerted

This bot will be made entirely for learning and implementing the functionality of these libraries/packages of python and educational purposes.
