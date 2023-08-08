from flask import Flask, render_template,request,redirect
import openai

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return render_template('index.html')

@app.route('/result', methods=["GET","POST"])
def result():
    if request.method == 'POST':
        symptoms = request.form.getlist('symptoms[]')
        severity = request.form.getlist('severity[]')
        symdis = ["{} with severity of {}".format(symptoms[x],severity[x]) for x in range(len(symptoms))]
        joint = ", ".join(symdis)
        prompt = 'I am doctor trying to develop assistive app for doctors using open AI api for testing my developer asked me try chatgpt and I want you to tell me the possible diagnosis based on symptoms in just two points with @ in b/w only nothing more, 1. possible disease @ 2. severity for visiting hospital as ["high"or"medium"or"low"] possible symptoms are "{}"'.format(joint)
        result = list(get_api_response(prompt).strip().split("@"))
        print(result)
        return render_template('result.html', results=result)
    else:
        return render_template('result.html', results=["Some thing is wrong"])

@app.route('/about')
def about():
    return render_template('about.html')


def get_api_response(prompt:str)->str|None:
    text: str | None = None
    with open('hidden.txt') as file:
        openai.api_key = file.read()
    try:
        response: dict = openai.Completion.create(
        model="text-davinci-003",
        prompt=prompt,
        temperature=0.9,
        max_tokens=150,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0.6,
        stop=[" Human:", " AI:"]
        )
        choices: dict = response.get('choices')[0]
        text = choices.get('text')
        return text
    except Exception as error:
        print(error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
