import time,random
sentences = ["The quick brown fox jumps over the lazy dog.",
             "A journey of a thousand miles begins with a single step.",
             "To be or not to be, that is the question.",
                "All that glitters is not gold.",
                "I think, therefore I am."]

def typing_test():
    test_sentence = random.choice(sentences)
    print("Type the following sentence as fast you can:")
    print(sentences)
    input("Press Enter to start...")
    start_time = time.time() #Mesure the time when the user starts typing
    user_input = input("Start typing: ")
    end_time = time.time() #Mesure the time when the user finishes typing
    time_taken = end_time - start_time
    time_taken_in_minutes = time_taken / 60
    word_count = len(test_sentence.split())
    print("Results:")
    print(f"Time taken: {time_taken:.2f} seconds")
    print(f"Words per minute: {word_count / time_taken_in_minutes:.2f} WPM")
    print("Typing Sped: {:.2f} characters per second".format(len(test_sentence) / time_taken))

typing_test()