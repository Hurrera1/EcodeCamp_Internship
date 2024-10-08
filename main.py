import gradio as gr

# Define the quiz questions and answers
questions =[
    {
        "question": "What is the capital of pakistan?",
        "answers": ["lahore", "Sialkot", "Karachi","Islamabad"],
       "correct_answer": "Islamabad"
    },
    {
       "question": "What is the national language of Pakistan?",
        "answers": ["Urdu", "English", "Punjabi", "Sindhi"],
        "correct_answer": "Urdu"
    },
    {
        "question": "Who is the founder of Pakistan?",
        "answers": ["Muhammad Ali Jinnah", "Liaquat Ali Khan", "Ayub Khan", "Zulfikar Ali Bhutto"],
        "correct_answer": "Muhammad Ali Jinnah"
    },
    {
        "question": "What is the largest city in Pakistan?",
        "answers": ["Karachi", "Lahore", "Islamabad", "Faisalabad"],
        "correct_answer": "Karachi"
    },
    {
       "question": "What is the highest mountain peak in Pakistan?",
        "answers": ["K2", "Nanga Parbat", "Rakaposhi", "Diran"],
        "correct_answer": "K2"
    },
    {
       "question": "What is the national animal of Pakistan?",
        "answers": ["Markhor", "Snow leopard", "Asiatic lion", "Bengal tiger"],
        "correct_answer": "Markhor"
    },
    {
        "question": "What is the national bird of Pakistan?",
        "answers": ["Chukar", "Peacock", "Partridge", "Falcon"],
        "correct_answer": "Chukar"
    },
    {
        "question": "What is the capital of France?",
        "answers": ["Paris", "London", "Berlin", "Rome"],
        "correct_answer": "Paris"
    },
    {
        "question": "What is the largest planet in our solar system?",
        "answers": ["Earth", "Saturn", "Jupiter", "Uranus"],
        "correct_answer": "Jupiter"
    },
    {
        "question": "What is the smallest country in the world?",
        "answers": ["Vatican City", "Monaco", "Nauru", "Tuvalu"],
        "correct_answer": "Vatican City"
    }
]

# Define the quiz function
def quiz(*answers):
    score = 0
    outputs = []
    for i, question in enumerate(questions):
        correct_answer = question["correct_answer"]
        if answers[i] == correct_answer:
            score += 1
        outputs.append(f"Correct answer: {correct_answer}")
        outputs.append(f"Your answer: {answers[i]}")
        outputs.append(f"Score: {score}/{len(questions)}")
    return "\n".join(outputs)

# Create the Gradio interface
demo = gr.Interface(
    fn=quiz,
    inputs=[gr.Radio(questions[0]["answers"], label=questions[0]["question"]),
            gr.Radio(questions[1]["answers"], label=questions[1]["question"]),
            gr.Radio(questions[2]["answers"], label=questions[2]["question"]),
            gr.Radio(questions[3]["answers"], label=questions[3]["question"]),
            gr.Radio(questions[4]["answers"], label=questions[4]["question"]),
            gr.Radio(questions[5]["answers"], label=questions[5]["question"]),
            gr.Radio(questions[6]["answers"], label=questions[6]["question"]),
            gr.Radio(questions[7]["answers"], label=questions[7]["question"]),
            gr.Radio(questions[8]["answers"], label=questions[8]["question"]),
            gr.Radio(questions[9]["answers"], label=questions[9]["question"])],
    outputs="text",
    title="Quiz Game",
    description="Select the correct answer for each question."
)

# Launch the Gradio app
demo.launch()