import tkinter as tk
from tkinter import ttk

class QuizGame:
    def __init__(self, root):
        self.root = root
        self.root.title("AES - Minor Setback")
        self.root.geometry("800x600")
        
        # Couleurs
        self.correct_color = "#4CAF50"      # Vert
        self.wrong_color = "#F44336"        # Rouge
        self.default_color = "#606C5A"      # Couleur des boutons
        self.bg_color = "#424340"           # Couleur de fond
        
        # Configuration de base
        self.root.configure(bg=self.bg_color)
        self.score = 0
        self.current_question = 0
        self.answer_buttons = []
        
        # Questions et réponses
        self.load_questions()
        
        self.current_round = None
        self.create_main_menu()

    def load_questions(self):
        self.questions = {
            "round1": [
                {
                    "question": "What is OOP?",
                    "options": [
                        "Object Oriented Programming",
                        "Online Operating Platform",
                        "Object Oriented Platform",
                        "Online Operating Programming"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is a DB?",
                    "options": [
                        "Data Bytes",
                        "Data Bases",
                        "Digital Backup",
                        "Digital Bytes"
                    ],
                    "correct": 1
                },
                {
                    "question": "What is IP?",
                    "options": [
                        "Internet Protocol",
                        "Internet Platform",
                        "Internal Protocol",
                        "Internal Platform"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is MAC Address?",
                    "options": [
                        "A unique 12-digit device ID",
                        "A unique identifier for Apple computers",
                        "A memory access control system",
                        "A network security protocol"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is ATMEGA328p?",
                    "options": [
                        "Arduino card",
                        "Network protocol",
                        "Programming language",
                        "Operating system"
                    ],
                    "correct": 0
                }
            ],
            "round2": [
                {
                    "question": "What are the four main principles of OOP?",
                    "options": [
                        "Encapsulation, inheritance, polymorphism, and abstraction",
                        "Functions, variables, classes, and objects",
                        "Coding, testing, debugging, and deployment",
                        "Planning, design, implementation, and maintenance"
                    ],
                    "correct": 0
                },
                {
                    "question": "What are best practices for creating strong passwords?",
                    "options": [
                        "Using long, complex, unique passwords and changing them regularly",
                        "Using simple, memorable passwords",
                        "Using the same password for all accounts",
                        "Using only numbers in passwords"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is the Agile methodology?",
                    "options": [
                        "An iterative and adaptive project management approach",
                        "A programming language",
                        "A database management system",
                        "A network protocol"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is a primary key in a database?",
                    "options": [
                        "A unique identifier for each record in a database table",
                        "The main password for accessing the database",
                        "The first column in any database table",
                        "A backup copy of the database"
                    ],
                    "correct": 0
                }
            ],
            "round3": [
                {
                    "question": "What is a network administrator?",
                    "options": [
                        "A position responsible for maintenance of computer networks",
                        "A software developer",
                        "A database manager",
                        "A web designer"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is the difference between Internet and Ethernet?",
                    "options": [
                        "All of the above",
                        "The Internet uses TCP/IP protocol only",
                        "Ethernet is only for gaming",
                        "There is no difference"
                    ],
                    "correct": 0
                },
                {
                    "question": "Which protocol is used for secure communication over the internet?",
                    "options": [
                        "FTP",
                        "HTTP",
                        "HTTPS",
                        "SMTP"
                    ],
                    "correct": 2
                },
                {
                    "question": "Which data structure uses LIFO principle?",
                    "options": [
                        "Queue",
                        "Array",
                        "Stack",
                        "Linked List"
                    ],
                    "correct": 2
                }
            ],
            "final": [
                {
                    "question": "What is Bash?",
                    "options": [
                        "Programming language",
                        "Web browser",
                        "Operating system",
                        "Text editor"
                    ],
                    "correct": 0
                },
                {
                    "question": "What does /n do in code?",
                    "options": [
                        "Returns to the line",
                        "Creates a new file",
                        "Deletes a line",
                        "Adds a number"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is a router?",
                    "options": [
                        "A networking device that connects multiple networks",
                        "A storage device",
                        "A programming tool",
                        "An input device"
                    ],
                    "correct": 0
                },
                {
                    "question": "What is IPv6?",
                    "options": [
                        "The latest version of Internet Protocol",
                        "A programming language",
                        "A web browser",
                        "A security protocol"
                    ],
                    "correct": 0
                }
            ]
        }

    def create_main_menu(self):
        self.clear_window()
        
        main_frame = tk.Frame(self.root, bg=self.bg_color)
        main_frame.pack(expand=True, fill='both')

        title = tk.Label(main_frame, text="AES - Minor Setback", 
                        font=("Arial", 24, "bold"), 
                        bg=self.bg_color, fg="white")
        title.pack(pady=20)

        button_frame = tk.Frame(main_frame, bg=self.bg_color)
        button_frame.pack(pady=20)

        # Création des boutons
        buttons = [
            ("Round 1", lambda: self.start_round("round1")),
            ("Round 2", lambda: self.start_round("round2")),
            ("Round 3", lambda: self.start_round("round3")),
            ("Final", lambda: self.start_round("final")),
            ("Rules", self.show_rules),
            ("Credits", self.show_credits)
        ]

        for text, command in buttons:
            btn = tk.Button(button_frame, text=text,
                          font=("Arial", 12),
                          bg=self.default_color,
                          fg="white",
                          bd=2,
                          relief="solid",
                          width=20,
                          command=command)
            btn.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def show_rules(self):
        self.clear_window()

        rules_frame = tk.Frame(self.root, bg=self.bg_color)
        rules_frame.pack(expand=True, fill='both', padx=20, pady=20)

        title = tk.Label(rules_frame, text="Rules", 
                        font=("Arial", 20, "bold"),
                        bg=self.bg_color, fg="white")
        title.pack(pady=10)

        rules_text = """
        Welcome to AES - Minor Setback!

        1. The game consists of 3 rounds and a final round
        2. Each round contains multiple questions
        3. Select the correct answer from the given options
        4. Correct answers will be highlighted in green
        5. Wrong answers will be highlighted in red
        6. Try to get the highest score possible!
        """
        
        rules_label = tk.Label(rules_frame, text=rules_text,
                             font=("Arial", 12),
                             justify=tk.LEFT,
                             bg=self.bg_color, fg="white")
        rules_label.pack(pady=20)

        self.create_back_button(rules_frame)

    def show_credits(self):
        self.clear_window()

        credits_frame = tk.Frame(self.root, bg=self.bg_color)
        credits_frame.pack(expand=True, fill='both')

        credits_labels = [
            ("Developed", ("Comic Sans MS", 24, "bold"), 45),
            ("by", ("Arial", 16, "italic"), -20),
            ("Beta", ("Impact", 36, "bold"), 30),
            ("2024", ("Courier", 12), 15),
            ("AES - Minor Setback", ("Times", 18, "bold"), 60),
        ]

        for text, font, angle in credits_labels:
            label = tk.Label(credits_frame, text=text,
                           font=font,
                           bg=self.bg_color, fg="white")
            label.place(relx=0.5,
                       rely=0.3 + credits_labels.index((text, font, angle)) * 0.1,
                       anchor="center")

        self.create_back_button(credits_frame)

    def create_back_button(self, parent):
        back_btn = tk.Button(parent,
                           text="Back to Main Menu",
                           font=("Arial", 12),
                           bg=self.default_color,
                           fg="white",
                           bd=2,
                           relief="solid",
                           command=self.create_main_menu)
        back_btn.pack(pady=10) if isinstance(parent, tk.Frame) else back_btn.place(relx=0.5, rely=0.9, anchor="center")

    def start_round(self, round_name):
        self.current_round = round_name
        self.current_question = 0
        self.score = 0
        self.show_question()

    def show_question(self):
        self.clear_window()

        if self.current_question < len(self.questions[self.current_round]):
            question_data = self.questions[self.current_round][self.current_question]

            main_frame = tk.Frame(self.root, bg=self.bg_color)
            main_frame.pack(expand=True, fill='both', padx=20, pady=20)

            question_label = tk.Label(main_frame,
                                    text=question_data["question"],
                                    font=("Arial", 14, "bold"),
                                    bg=self.bg_color, fg="white")
            question_label.pack(pady=20)

            button_frame = tk.Frame(main_frame, bg=self.bg_color)
            button_frame.pack(pady=10)

            self.answer_buttons = []

            for i, option in enumerate(question_data["options"]):
                btn = tk.Button(button_frame,
                              text=option,
                              font=("Arial", 12),
                              width=40, height=2,
                              bg=self.default_color,
                              fg="white",
                              bd=2,
                              relief="solid",
                              command=lambda ans=i: self.check_answer(ans))
                btn.pack(pady=5)
                self.answer_buttons.append(btn)

            progress_label = tk.Label(main_frame,
                                    text=f"Question {self.current_question + 1}/{len(self.questions[self.current_round])}",
                                    font=("Arial", 12),
                                    bg=self.bg_color, fg="white")
            progress_label.pack(pady=10)

            score_label = tk.Label(main_frame,
                                 text=f"Score: {self.score}",
                                 font=("Arial", 12, "bold"),
                                 bg=self.bg_color, fg="white")
            score_label.pack(pady=10)
        else:
            self.show_results()

    def check_answer(self, answer):
        question_data = self.questions[self.current_round][self.current_question]
        correct_answer = question_data["correct"]
        
        for btn in self.answer_buttons:
            btn.config(state="disabled")
        
        if answer == correct_answer:
            self.answer_buttons[answer].config(bg=self.correct_color)
            self.score += 1
        else:
            self.answer_buttons[answer].config(bg=self.wrong_color)
            self.answer_buttons[correct_answer].config(bg=self.correct_color)
        
        self.root.after(1000, self.next_question)

    def next_question(self):
        self.current_question += 1
        self.show_question()

    def show_results(self):
        self.clear_window()

        results_frame = tk.Frame(self.root, bg=self.bg_color)
        results_frame.pack(expand=True, fill='both', padx=20, pady=20)

        result_label = tk.Label(results_frame,
                              text=f"Round Complete!\nYour final score: {self.score}/{len(self.questions[self.current_round])}",
                              font=("Arial", 20, "bold"),
                              bg=self.bg_color, fg="white")
        result_label.pack(pady=30)

        self.create_back_button(results_frame)

if __name__ == "__main__":
    root = tk.Tk()
    app = QuizGame(root)
    root.mainloop()