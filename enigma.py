import csv

# Load the dataset into a dictionary where the key is the question and the value is the answer
def load_data(file_path):
    qa_dict = {}
    with open(file_path, mode='r', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            qa_dict[row['Questions'].lower()] = row['Answers']
    return qa_dict

# Function to get the answer for the user query
def get_answer(user_question, qa_dict):
    # Preprocess the user's question (convert to lowercase for matching)
    user_question = user_question.lower()
    
    # Check if the user's question matches any question in the dataset
    for question, answer in qa_dict.items():
        if user_question in question:
            return answer
    
    return "Sorry, I couldn't find an answer to your question."

# Main chatbot function
def chatbot():
    # Load the data from the provided file path
    qa_dict = load_data(r'C:\Users\udiks\OneDrive\Desktop\chatbot\archive\Mental_Health_FAQ.csv')
    
    print("Chatbot: Hello! Ask me about mental health, and I'll do my best to answer.")
    
    while True:
        user_input = input("You: ")
        
        if user_input.lower() == 'exit':
            print("Chatbot: Goodbye!")
            break
        
        response = get_answer(user_input, qa_dict)
        print(f"Chatbot: {response}")

# Run the chatbot
if __name__ == "__main__":
    chatbot()
