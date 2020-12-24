import requests

def inicial_base():
    question_data = [
        {"text": "A slug's blood is green.", "answer": "True"},
        {"text": "The loudest animal is the African Elephant.", "answer": "False"},
        {"text": "Approximately one quarter of human bones are in the feet.", "answer": "True"},
        {"text": "The total surface area of a human lungs is the size of a football pitch.", "answer": "True"},
        {"text": "In West Virginia, USA, if you accidentally hit an animal with your car, you are free to take it home to eat.", "answer": "True"},
        {"text": "In London, UK, if you happen to die in the House of Parliament, you are entitled to a state funeral.", "answer": "False"},
        {"text": "It is illegal to pee in the Ocean in Portugal.", "answer": "True"},
        {"text": "You can lead a cow down stairs but not up stairs.", "answer": "False"},
        {"text": "Google was originally called 'Backrub'.", "answer": "True"},
        {"text": "Buzz Aldrin's mother's maiden name was 'Moon'.", "answer": "True"},
        {"text": "No piece of square dry paper can be folded in half more than 7 times.", "answer": "False"},
        {"text": "A few ounces of chocolate can to kill a small dog.", "answer": "True"}
    ]
question_data = []


def PrepareQuestionList(count):
    url = "https://opentdb.com/api.php?type=boolean"
    url += "&amount="+ str(count)
    request = requests.request("get", url)
    #prepering question_data
    if request.status_code == 200:
        for question in request.json()['results']:
            aux = {}
            aux['text'] = f"Cat: {question['category']} - {question['question']}"
            aux['answer']  = question['correct_answer']
            question_data.append(aux)
    else:
        inicial_base()
    return question_data
