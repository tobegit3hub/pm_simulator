import os
from collections import deque
import openai
import re
import logging
logger = logging.getLogger(__name__)

class GptManager:

    def __init__(self, api_key: str, model_engine: str, temperature: float, max_tokens: int, keep_history_num: int):
        # Set the OpenAI API key
        openai.api_key = api_key
        self.model_engine = model_engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.keep_history_num = keep_history_num

        self.history_message_queue = deque(maxlen=keep_history_num)
        self.history_message_queue.append({"role": "system", "content": self.generate_system_message()})

    @classmethod
    def create(cls):
        api_key = os.environ["OPENAI_API_KEY"]
        model_engine = "gpt-3.5-turbo"
        temperature = 0.0
        max_tokens = 512
        keep_history_num = 5
        return cls(api_key, model_engine, temperature, max_tokens, keep_history_num)

    def generate_system_message(self) -> str:
        """
        You are a helpful website developer and help to update the CSS file.

Here is the HTML file.

<!DOCTYPE html>
<html>
<head>
  <title>My Website Title</title>
  <!-- <link rel="stylesheet" type="text/css" href="style.css"> -->
  <link rel="stylesheet" type="text/css" href="{{ url_for('static', filename='style.css') }}">
</head>
<body>
  <div class="background">
    <h1>Welcome to My Website</h1>
    <p>This is the homepage of my website.</p>
  </div>
</body>
</html>

Here is the original CSS file.

.background {
  background-color: #11e;
  padding: 50px;
  text-align: center;
}

Get user's input and only output the new CSS file. No instruction, introduction and other message.
        """


        with open('./templates/index.html', 'r') as file:
          html = file.read()

        with open('./assets/style.css', 'r') as file:
          css = file.read()


        system_message_template = """You are a helpful website designer and developer to help to update the CSS file.

Here is the HTML file.

{}

Here is the original CSS file.

{}

Update the CSS file for user's command and make sure to keep the original CSS style. Only output the CSS file and no instruction, introduction nor other message.
"""
        system_message = system_message_template.format(html, css)
        print("system_message: ", system_message)
        return system_message


    def extrace_css_code(self, input_text: str) -> str:
      # Regular expression to match the code block delimiter and extract the content
      pattern = r"```(?P<lang>[a-zA-Z]*)\n(?P<code>.*?)```"

      # Search for the code block in the text output
      match = re.search(pattern, input_text, re.DOTALL)

      # If a match is found, extract the code block content as a string
      if match:
          code_block = match.group("code")
          return code_block
      else:
         return input_text
      
    
    def generate_css(self, command: str):
        request_messages = list(self.history_message_queue)
        request_messages.append({"role": "user", "content": command})

        response = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=request_messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )

        # TODO: Update user command as needed, append system output as needed
        # self.history_message_queue.append()

        output_content = response.choices[0].message["content"]
        print("ChatGPT output_content", output_content)

        if "```" in output_content:
           css_code = self.extrace_css_code(output_content)
        else:
           css_code =output_content

        return css_code
