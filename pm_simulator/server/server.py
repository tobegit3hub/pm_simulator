#!/usr/bin/env python3

from flask import Flask, render_template, request, jsonify, redirect, url_for

from chatgpt_manager import GptManager

app = Flask(__name__, template_folder='templates', static_folder='assets')

gpt_manager = GptManager.create()


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/update_css', methods=['POST'])
def update_css():
    command = request.form.get('command')

    new_css = gpt_manager.generate_css(command)

    # Update CSS file with new_css
    with open('./assets/style.css', 'w') as f:
        f.write(new_css)

    return_data = {
        'command': command,
        'success': True,
        'css': new_css
    }
    return jsonify(return_data)


@app.route('/update_html', methods=['POST'])
def update_html():
    command = request.form.get('command')

    new_css = gpt_manager.generate_css(command)

    # Update CSS file with new_css
    with open('./assets/style.css', 'w') as f:
        f.write(new_css)

    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)

