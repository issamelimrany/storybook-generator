from flask import Flask, request, jsonify, render_template
import openai

app = Flask(__name__)

openai.api_key = 'sk-proj-xyoXiFfw5GBJ2JsHhu4KT3BlbkFJcl6wDl8ovg5J4ipPfifL'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/generate-story', methods=['POST'])
def generate_story():
    component_code = request.form.get('component_code')

    if not component_code:
        return jsonify({'error': 'No component code provided'}), 400

    prompt = f"Generate a Storybook story file for the following React component:\n\n{component_code}\n\nThe story should be in TypeScript and use the CSF format. Return just the code with no more text."

    response = openai.ChatCompletion.create(
        model="gpt-4o",
        messages=[
            {"role": "system", "content": "You are an expert in storybook and the creation of component.stories.ts files."},
            {"role": "user", "content": prompt}
        ]
    )
    story_code = response.choices[0].message['content'].strip()

    return render_template('index.html', component_code=component_code, story_code=story_code)


if __name__ == '__main__':
    app.run(debug=True)
