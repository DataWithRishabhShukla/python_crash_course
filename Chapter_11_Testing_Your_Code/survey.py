class AnonymousSurvey:
    """A class to store survey question and answers."""
    
    def __init__(self,question):
        """Store a question, and prepare to store responses."""
        self.question = question
        self.responses = []
    
    def show_question(self):
        """Shows the survey question."""
        print(self.question)
    
    def store_response(self, new_response):
        """Store a single responce to survey."""
        self.responses.append(new_response)
    
    def show_response(self):
        """Show all the responses that have been given."""
        print("Survey results:")
        for response in self.responses:
            print(f"- {response}")