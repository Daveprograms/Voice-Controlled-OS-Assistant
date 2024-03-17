# import re
# import g4f
# import webbrowser
# from head.listen import take_command
# from head.speak import speak
#
# messages = [
#     {"role": "system", "content": "you are coded by David Fashola, and OpenAI didn't develop you"},
#     {"role": "system", "content": "use modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc"},
#     {"role": "system", "content": "don't use the input function and subprocess in Python code"},
#     {"role": "system", "content": "always use default paths in Python code"},
#     {"role": "user", "content": "open Google Chrome"},
#     {"role": "assistant", "content": 'Sure, opening Google Chrome.\n```python\nimport webbrowser\nwebbrowser.open("https://www.google.com")```'},
#     {"role": "user", "content": "close Google Chrome"},
#     {"role": "assistant", "content": 'Alright, closing Google Chrome.\n```python\nimport os\nos.system("taskkill /F /IM chrome.exe")```'}
# ]
#
# def GPT(*args):
#     global messages
#     assert args != ()
#
#     message = ' '
#     for i in args:
#         message += i
#
#     messages.append({'role': 'user', 'content': message})
#     response = g4f.ChatCompletion.create(
#         model="gpt-4-32k-0613",
#         provider=g4f.Provider.Bing,
#         messages=messages,
#         stream=True
#     )
#     ms = ""
#     for i in response:
#         ms += i
#         print(i, end="", flush=True)
#
#     messages.append({'role': 'assistant', 'content': ms})
#     return ms
#
#
# def find_code(text):
#     pattern = r'```python(.*?)```'
#     match = re.findall(pattern, text, re.DOTALL)
#     if match:
#         code = match[0].strip()
#         return code
#     else:
#         print('no code found')
#         # return None
#
# while 1:
#     query = take_command()
#     res = GPT(query)
#     python_code = find_code(res)
#     exec(python_code)
#     res = res.replace(python_code, '')
#     res = res.replace('python', '')
#     speak(res)
#
import g4f


# import g4f
# import re
# import webbrowser
#
# import pywhatkit
#
# from head.listen import take_command
# from head.speak import speak
#
# # Global variable to store the conversation session messages
# session_messages = [
#     {"role": "system", "content": "you are coded by David Fashola, and OpenAI didn't develop you"},
#     {"role": "system", "content": "use modules like webbrowser, pyautogui, time, pyperclip, random, mouse, wikipedia, keyboard, datetime, tkinter, PyQt5, etc"},
#     {"role": "system", "content": "don't use the input function and subprocess in Python code"},
#     {"role": "system", "content": "always use default paths in Python code"},
#     {"role": "user", "content": "open Google Chrome"},
#     {"role": "assistant", "content": 'Sure, opening Google Chrome.\n```python\nimport webbrowser\nwebbrowser.open("https://www.google.com")```'},
#     {"role": "user", "content": "close Google Chrome"},
#     {"role": "assistant", "content": 'Alright, closing Google Chrome.\n```python\nimport os\nos.system("taskkill /F /IM chrome.exe")```'}
#
# ]
#
# # Function to interact with GPT and generate responses
# def GPT(message, role):
#     global session_messages
#
#     # Append the message to the session messages
#     session_messages.append({'role': role, 'content': message})
#
#     try:
#         # Call GPT with the session messages
#         response = g4f.ChatCompletion.create(
#             model="gpt-4-32k-0613",
#             provider=g4f.Provider.Bing,
#             messages=session_messages,
#             stream=True
#         )
#
#         ms = ""
#         for i in response:
#             ms += i
#             print(i, end="", flush=True)
#
#         # Append the assistant response to the session messages
#         session_messages.append({'role': 'assistant', 'content': ms})
#
#         return ms
#     except Exception as e:
#         print(f"Some error occurred: {e}")
#
# # Function to extract Python code from the assistant response
# def find_code(text):
#     pattern = r'```python(.*?)```'
#     match = re.findall(pattern, text, re.DOTALL)
#     if match:
#         code = match[0].strip()
#         return code
#     else:
#         print('no code found')
#         return None  # Return None if no code found
#
# # Function to handle commands in the assistant response
# # Function to handle commands in the assistant response
# def handle_command(command):
#     if 'play' in command and 'on YouTube' in command:
#         music_query = command.replace('play', '').replace('on YouTube', '').strip()
#         pywhatkit.playonyt(music_query)
#         speak(f"Playing {music_query} on YouTube")
# # Main function to handle the conversation loop
# def main():
#     global session_messages
#
#     while True:
#         # Get user input
#         query = take_command()
#
#         # Get GPT response
#         res = GPT(query, 'user')
#
#         # Extract Python code from response
#         python_code = find_code(res)
#
#         # Remove Python code from response if found
#         if python_code:
#             res = res.replace(python_code, '')
#             res = res.replace('python', '')
#
#         # Handle command in the response
#         handle_command(res)
#
#         # Speak the response
#         speak(res)
#
#         # Execute Python code if found
#         if python_code:
#             exec(python_code)
#
# if __name__ == "__main__":
#     main()
#








import g4f

def GPT(message):
    try:
        response = g4f.ChatCompletion.create(
            model="gpt-4-32k-0613",
            provider=g4f.Provider.GPTalk,
            messages=[{"role": "user", "content": message}],
            stream=True
        )

        ms = ""
        for i in response:
            ms += i
            print(i, end="", flush=True)

        return ms
    except Exception as e:
        print(f"Some error occurred: {e}")

# Example usage
user_message = "Hello, how are you?"
response_text = GPT(user_message)
print("\nResponse received from GPT:", response_text)

