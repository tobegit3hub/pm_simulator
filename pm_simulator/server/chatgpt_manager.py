import os
from collections import deque
import openai
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
        system_message = """
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

        return system_message

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

        return response.choices[0].message["content"]

