# import turtle as tur
# import colorsys as cs
# tur.setup(800,800)
# tur.speed(0)
# tur.tracer(10)
# tur.width(2)
# tur.bgcolor("black")
# for j in range(25):
#     for i in range(15):
#         tur.color(cs.hsv_to_rgb(i/15,j/25,1))
#         tur.right(90)
#         tur.circle(200-j*4,90)
#         tur.left(90)
#         tur.circle(200-j*4,90)
#         tur.right(180)
#         tur.circle(50,24)
# tur.hideturtle()
#
#
# tur.done()

# import tkinter as tk
# from tkinter import scrolledtext
# import threading
# import subprocess
#
# class AIGUI:
#     def __init__(self, root):
#         self.root = root
#         self.root.title("AI Terminal GUI")
#
#         # Create and configure the text area
#         self.output_text = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=50, height=20)
#         self.output_text.grid(row=0, column=0, padx=10, pady=10, columnspan=2)
#
#         # Create input field
#         self.input_entry = tk.Entry(root, width=40)
#         self.input_entry.grid(row=1, column=0, padx=10, pady=10)
#
#         # Create send button
#         self.send_button = tk.Button(root, text="Send", command=self.send_command)
#         self.send_button.grid(row=1, column=1, padx=10, pady=10)
#
#     def send_command(self):
#         # Get the command from the input field
#         command = self.input_entry.get()
#         # Clear the input field
#         self.input_entry.delete(0, tk.END)
#         # Display the command in the output area
#         self.output_text.insert(tk.END, f">> {command}\n")
#
#         # Execute the command in the terminal
#         output = subprocess.getoutput(command)
#         # Display the output in the output area
#         self.output_text.insert(tk.END, f"{output}\n\n")
#
# # Create a Tkinter root window
# root = tk.Tk()
# # Create an instance of the AIGUI class
# app = AIGUI(root)
# # Start the Tkinter main loop
# root.mainloop()



# import random
#
# # Dictionary containing predefined commands and responses
# responses = {
#     "hello": "Hello! How can I assist you?",
#     "how are you": "I'm just a computer program, but I'm doing fine. Thank you for asking!",
#     "what is your name": "I am your personal AI assistant.",
#     "bye": "Goodbye! Have a great day!",
#     "thank you": "You're welcome!",
#     "calculate": "Sure, I can help you with that. The answer is {result}.",
# }
#
# def generate_response(user_input):
#     # Check if the user input matches any predefined command
#     for command in responses.keys():
#         if command in user_input.lower():
#             # If the command contains "{result}", replace it with a random number for demonstration purposes
#             if "{result}" in responses[command]:
#                 response = responses[command].format(result=random.randint(1, 100))
#             else:
#                 response = responses[command]
#             return response
#     # If no predefined command matches, return a default response
#     return "I'm sorry, I don't understand that command."
#
# def personal_ai():
#     print("Personal AI: Hello! How can I assist you? (Type 'bye' to exit)")
#
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "bye":
#             print("Personal AI: Goodbye! Have a great day!")
#             break
#
#         response = generate_response(user_input)
#         print("Personal AI:", response)
#
# if __name__ == "__main__":
#     personal_ai()



# import nltk
# from nltk.chat.util import Chat, reflections
#
# # Define some reflections (used for pronouns in responses)
# reflectioons = {
#     "i am": "you are",
#     "i was": "you were",
#     "i": "you",
#     "i'm": "you are",
#     "i'd": "you would",
#     "i've": "you have",
#     "i'll": "you will",
#     "my": "your",
#     "you are": "I am",
#     "you were": "I was",
#     "you've": "I have",
#     "you'll": "I will",
#     "your": "my",
#     "yours": "mine",
#     "you": "me",
#     "me": "you"
# }
#
# # Define some patterns and responses for the chatbot
# patterns = [
#     (r"(.*)(hi|hello|hey|howdy)(.*)", ["Hello!", "Hi there!", "Hey!"]),
#     (r"(.*)(bye|goodbye)(.*)", ["Goodbye!", "See you later!", "Bye!"]),
#     (r"(.*)(your name)(.*)", ["I am a chatbot.", "My name is ChatGPT.", "You can call me ChatGPT."]),
#     (r"(.*)(how are you)(.*)", ["I'm just a computer program, but I'm doing fine. How can I help you?"]),
# ]
#
# # Create a chatbot using the patterns and reflections
# chatbot = Chat(patterns, reflections)
#
# # Function to start the chat
# def start_chat():
#     print("Hello! I'm your chatbot. Type 'bye' to exit.")
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() == "bye":
#             print("Chatbot: Goodbye! Have a great day!")
#             break
#         response = chatbot.respond(user_input)
#         print("Chatbot:", response)
#
# # Call the function to start the chat
# if __name__ == "__main__":
#     start_chat()


