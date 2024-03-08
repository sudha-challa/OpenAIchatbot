
<h1>OpenAI API ChatBot</h1>

This is the code for basic implementation of a chatbot using Tkinter and the OpenAI  **Generative Pre-Trained Transformer** model.Here I have explained the code in detail by dividing into parts. 

Let's know about how each part acts as....

**1.imports** :<br>
- **tkinter** : it is used for creating the Graphical user interface **(GUI)**.<br>
- **openai** : it used for interacting with the OpenAI API.

**2.'ChatApplication' class** :<br>
- This class inherits from **tk.Tk**, which is the main application window in Tkinter.<br>
- The **__ init __** method initializes the application window and calls two methods: **initialize_openai()** and **create_widgets()**.
- **initialize_openai()** sets up the **OpenAI API** key.
- **base_messages** contains initial messages for the conversation between the user and system.<br>

**3.create_widgets() method** :
- It creates and configures the **GUI components** such as Text, Scrollbar, Entry, and Button.
- Binds the <Return> key to the send button for sending messages.<br>

**4.get_response() method** :
- Sends the user input along with the base messages to the **OpenAI GPT-3.5** model.
- Retrieves and returns the response from the model.<br>

**5.send_message() method** :

- Retrieves the user input, sends it to **get_response()**, and displays both user input and bot response in the conversation window.<br>

**6.on_entry_click() and on_focusout() methods** :

- Handle the behavior of the entry field when it is clicked and when it loses focus.<br>

**7.if __ name __ == "__ main __": block** :
- Instantiates the ChatApplication class and starts the main event loop.<br>

**Output**:
<figure>
    <img src=chatbot.png>
    <figcaption>This is the output window of the ChatBot</figcaption>
</figure>