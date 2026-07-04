# Quize Program 

def quiz():
    questions = [
        {
            "question" :  "1: What is the capital of France?",
            "options" : ["a) Berlin", "b) Madrid", "c) Paris", "d) Rome"],
            "answer" : "c) Paris"
        },
        {
            "question" :  "2: What is the largest planet in our solar system?",
            "options" : ["a) Earth", "b) Jupiter", "c) Mars", "d) Saturn"],
            "answer" : "b) Jupiter"
        },
        {
            "question" :  "3: What is the chemical symbol for water?",
            "options" : ["a) H2O", "b) CO2", "c) NaCl", "d) O2"],
            "answer" : "a) H2O"
        },
        {
            "question" :  "4: Who wrote 'To Kill a Mockingbird'?",
            "options" : ["a) Harper Lee", "b) J.K. Rowling", "c) Ernest Hemingway", "d) Mark Twain"],
            "answer" : "a) Harper Lee"
        },
        {
            "question" :  "5: What is the smallest prime number?",
            "options" : ["a) 0", "b) 1", "c) 2", "d) 3"],
            "answer" : "c) 2"
            
        },
        {
            "question" :  "6: What is the speed of light in a vacuum?",
            "options" : ["a) 299,792 km/s", "b) 150,000 km/s", "c) 1,080,000 km/s", "d) 300,000 km/s"],
            "answer" : "a) 299,792 km/s"
        }
    ]
    
    score = 0
    
    for index,q in enumerate(questions):
        print(q["question"])
        for option in q["options"]:
            print(option)
        user_answer = input("Your answer: ")
        
        if user_answer.lower() == q["answer"][0]:
            print("Correct!")
            score += 1
        else:
            print(f"Wrong! The correct answer is: {q['answer']}")
        print()
    
    print(f"Quiz completed! Your score is: {score}/{len(questions)}")
    
quiz()