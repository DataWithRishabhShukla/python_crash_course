from survey import AnonymousSurvey

# Define a question and make a survey
print("\n\n")
question = "What language did you first learn to speak?"
language_sruvey = AnonymousSurvey(question)

#Show the question and store response to question 

language_sruvey.show_question()
print("Enter 'q' to exit any time .\n")
while True:
    response = input("Language: ")
    if response == 'q':
        break

    language_sruvey.store_response(response)

#Show the survey results 
print("\nThank you everyone who participated in the survey!")
language_sruvey.show_response()
