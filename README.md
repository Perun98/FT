# PythonTutorial
Chatbot creation and embeddings tutorial for GPT-3

1. obican_chatbot.py

This code defines a simple chatbot that uses OpenAI's GPT-3 natural language processing model to generate responses to user input.
Here is what the code does, step by step:
The code imports the necessary libraries, including the OpenAI API and the regular expressions library.
The code defines a function called open_file that takes a filepath as an argument and returns the contents of the file as a string. This function is used to 
retrieve the API key for OpenAI from a text file.
The code sets the OpenAI API key by calling the open_file function with the filepath of the API key file.
The code defines a function called get_openai_response that takes a user input as an argument and returns a response generated by the OpenAI API. The response
 is generated using the GPT-3 model, which is set to engine='text-davinci-003', with a prompt equal to the user input, a maximum of 60 tokens, a single 
response, a stop character of ".", and a temperature of 0.7.
The code defines a function called generate_response that takes a user input as an argument and returns a response generated by calling the 
get_openai_response function with the user input.
The code defines a main function called run_chatbot that prints a welcome message and then enters a loop to receive user input. The loop continues until the 
user enters "exit". Each time through the loop, the user input is passed to the generate_response function to generate a response, which is then printed to 
the console.
Finally, the code calls the run_chatbot function to start the chatbot.

2. tkinterchatbot.py

This code creates a simple GUI chatbot application that uses OpenAI's GPT-3 model to generate responses to user input. The chatbot is initialized with a 
prompt message that is read from a text file.
The code first imports the necessary modules: openai and tkinter. It then defines some constants for colors and fonts that are used in the GUI.
The open_file() function is defined to read the OpenAI API key and the prompt message from their respective text files.
The messages list is initialized with the prompt message and will be updated with the user's input and the chatbot's responses.
The ChatApp class is defined, which inherits from the tk.Frame class. The class contains a constructor that initializes the chatbot's GUI. The GUI includes an
 input field, an output label, and an output text box. The send_message() method is defined to handle user input and generate responses from the GPT-3 model. 
The method appends the user's input to the messages list and calls the openai.ChatCompletion.create() method to generate a response from the GPT-3 model. The 
chatbot's response is appended to the messages list and displayed in the output text box.
The main block checks if the script is being run as the main program, and creates a Tk object that represents the chatbot window. The window is then 
configured and the ChatApp object is created and passed the Tk object as an argument. Finally, the mainloop() method is called to start the event loop and 
display the chatbot window.

3. whisper_glas.py

This Python script uses the OpenAI API to transcribe an audio file and save the resulting transcript as a JSON file. Here is a brief explanation of what each 
part of the code does:
import openai: imports the OpenAI API package, which allows the script to interact with the OpenAI API.
import json: imports the built-in JSON library, which the script will use to convert the transcript to a JSON string.
def open_file(filepath): defines a function that takes a file path as an argument and returns the contents of the file.
openai.api_key = open_file('openaiapikey.txt'): sets the API key for the OpenAI package by calling the open_file function with the file path of a file 
containing the API key.
audio_file= open(input("Unesi naziv audio fajla: "), "rb"): prompts the user to enter the name of an audio file and opens the file in binary mode.
transcript = openai.Audio.transcribe("whisper-1", audio_file, language = "en"): uses the openai.Audio.transcribe method to transcribe the audio file using the
 "whisper-1" model and English language.
transcript_dict = transcript.to_dict(): converts the resulting OpenAIObject to a dictionary.
transcript_json = json.dumps(transcript_dict): converts the dictionary to a JSON string.
with open(input("Unesi naziv tekst fajla: "), 'w', encoding='utf-8') as outfile:: prompts the user to enter the name of a text file and opens the file for 
writing.
outfile.write(transcript_json): writes the JSON string to the text file.
print(f'Transcription complete. Transcript saved to {outfile.name}'): prints a message indicating that the transcription is complete and the transcript has 
been saved to the specified file.

4. init_embedings.py

This code is performing several tasks related to natural language processing and machine learning.
First, it imports modules from the langchain package for loading and processing PDF documents, text splitting, and vector embedding. It also imports Pinecone 
for indexing and searching documents.
The function open_file() is defined to read in a text file containing an API key for OpenAI or Pinecone.
Then, the code loads a PDF document using the UnstructuredPDFLoader module and displays the number of documents and characters in the PDF.
Next, the RecursiveCharacterTextSplitter module is used to split the document into smaller chunks of text, and the resulting texts are displayed along with 
the number of documents.
After this, the code initializes the OpenAI API key and Pinecone API key, and then initializes the OpenAIEmbeddings and Pinecone modules. The 
Pinecone.from_texts() method is used to create an index of the documents in Pinecone, which can be used to search for similar documents.
Finally, the code prints a message indicating that Pinecone has been populated with the documents.

5. odg_embedings.py

This code imports Pinecone, a vector similarity search engine, and OpenAIEmbeddings from the LangChain library. It also imports the Pinecone library itself, 
which is used to initialize the Pinecone API and load saved indexes.
The open_file() function is defined to read the contents of a file.
Then, the API keys for OpenAI and Pinecone are read from files and stored in variables OPENAI_API_KEY and PINECONE_API_KEY, respectively. The environment for 
the Pinecone API is also set to 'us-west1-gcp'.
Next, the OpenAI API and Pinecone API are initialized using their respective keys. An index name of 'embedings1' is specified for the Pinecone index.
Then, an OpenAI model is loaded using the OpenAI class from LangChain, and a question-answering chain is initialized using the load_qa_chain() function from 
the question_answering module.
A while loop is used to repeatedly prompt the user for a question. The user's question is used to search the Pinecone index for similar documents, and the 
question-answering chain is used to generate an answer based on the top results from the search. The answer is then printed to the console.
