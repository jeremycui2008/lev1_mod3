class JeopardyGame:
    def __init__(self):
        self.categories = ["History", "Science", "Literature"]
        self.questions = {
            "History": {
                "100": "What year did World War I end?",
                "200": "Who was the first President of the United States?",
                "300": "What is the capital of France?"
            },
            "Science": {
                "100": "What is the chemical symbol for gold?",
                "200": "Who discovered penicillin?",
                "300": "What is the largest planet in our solar system?"
            },
            "Literature": {
                "100": "Who wrote 'Romeo and Juliet'?",
                "200": "What is the sequel to 'To Kill a Mockingbird'?",
                "300": "What is the name of the main character in 'Moby Dick'?"
            }
        }
        self.scores = {
            "player1": 0,
            "player2": 0,
            "player3": 0
        }

    def display_board(self):
        # Display the game board with categories and questions
        for category in self.categories:
            print(category)
            for value, question in self.questions[category].items():
                print(f"${value} - {question}")

    def choose_question(self, category, value):
        # Retrieve and display the chosen question
        question = self.questions[category][value]
        print(f"The question is: {question}")

    def answer_question(self, player, answer, category, value):
        # Check if the answer is correct and update the player's score
        if answer == "answer":
            self.scores[player] += int(value)
            print(f"Correct! Player {player} earns ${value}.")
        else:
            self.scores[player] -= int(value)
            print(f"Incorrect! Player {player} loses ${value}.")

    def display_scores(self):
        # Display the current scores of all players
        for player, score in self.scores.items():
            print(f"Player {player}: ${score}")
jeopardy = JeopardyGame()

# Display the game board
jeopardy.display_board()

# Choose a question
jeopardy.choose_question("Science", "200")

# Answer the question
jeopardy.answer_question("player1", "gold", "Science", "200")

# Display the current scores
jeopardy.display_scores()
