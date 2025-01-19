from flask import Flask, render_template, request
import openai

app = Flask(__name__)

# Replace with your OpenAI API key
openai.api_key = "your_openai_api_key"

def generate_cover_letter(resume_text, job_description):
    prompt = (
        "Using the following resume and job description, create a professional and personalized cover letter.\\n\\n"
        f"Resume:\\n{resume_text}\\n\\n"
        f"Job Description:\\n{job_description}\\n\\n"
        "Cover Letter:"
    )

    try:
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=prompt,
            max_tokens=500,
            temperature=0.7
        )
        return response.choices[0].text.strip()
    except Exception as e:
        return f"An error occurred: {e}"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate', methods=['POST'])
def generate():
    resume = request.form['resume']
    job_description = request.form['job_description']
    cover_letter = generate_cover_letter(resume, job_description)
    return render_template('result.html', cover_letter=cover_letter)

if __name__ == '__main__':
    app.run(debug=True)
