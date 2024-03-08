import tkinter as tk
# from PIL import Image, ImageTk  # Uncomment if you're using an image
from tkinter import PhotoImage
import openai

class ChatApplication(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("My ChatBot")
        self.initialize_openai()
        self.create_widgets()
    
    def initialize_openai(self):
        # It's better to store API keys in environment variables or config files
        openai.api_key = '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'
    
    base_messages = [
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "system", "content": "The user's name is Sudha."}
    ]
    
    def create_widgets(self):
        self.conversation = tk.Text(self, bg="navyblue", fg="white", font="Arial,14", wrap="word")
        scrollbar = tk.Scrollbar(self, command=self.conversation.yview)
        self.entry_field = tk.Entry(self, font="Arial,14", bg="lightblue", fg="black")
        self.entry_field.insert(0, 'Ask a question...')
        send_button = tk.Button(self, text="Send", command=self.send_message, compound='left', bg="lightblue")

        self.conversation.grid(row=1, column=1, columnspan=2, sticky='nsew', padx=10, pady=10)
        scrollbar.grid(row=1, column=3, sticky='nsew')
        self.entry_field.grid(row=2, column=1, sticky='nsew', padx=10)
        send_button.grid(row=2, column=2, sticky='nsew', ipadx=10)
        self.bind('<Return>', lambda event: send_button.invoke())

        self.conversation.configure(yscrollcommand=scrollbar.set)

        self.entry_field.bind('<FocusIn>', self.on_entry_click)
        self.entry_field.bind('<FocusOut>', self.on_focusout)
        
    def get_response(self, user_input):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=self.base_messages + [{"role": "user", "content": user_input}]
            )
            return response.choices[0].message['content']
        except Exception as e:
            return f"An error occurred: {e}"

    def send_message(self):
        user_input = self.entry_field.get().strip()
        if user_input and user_input != 'Ask a question...':
            response = self.get_response(user_input)
            self.conversation.insert(tk.END, f'\n Me: { user_input }\n')
            self.conversation.insert(tk.END, f'\n Bot: { response}\n')
            self.entry_field.delete(0, tk.END)
            self.conversation.see(tk.END)

    def on_entry_click(self, event=None):
        if self.entry_field.get() == 'Ask a question...':
            self.entry_field.delete(0, tk.END)
            self.entry_field.config(fg='black')

    def on_focusout(self, event=None):
        if not self.entry_field.get().strip():
            self.entry_field.insert(0, 'Ask a question...')
            self.entry_field.config(fg='grey')

if __name__ == "__main__":
    app = ChatApplication()
    app.mainloop()
