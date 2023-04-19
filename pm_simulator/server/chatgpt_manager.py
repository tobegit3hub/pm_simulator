import os
from collections import deque
import openai
import re
import logging
import queue

logger = logging.getLogger(__name__)


class GptManager:

    def __init__(self, api_key: str, model_engine: str, temperature: float, max_tokens: int):
        # Set the OpenAI API key
        openai.api_key = api_key
        self.model_engine = model_engine
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.history_css_queue = queue.Queue(2)

        # Put two CSS content in the queue
        with open('./assets/style.css', 'r') as file:
            css_content = file.read()
            self.history_css_queue.put(css_content)
            self.history_css_queue.put(css_content)


    @classmethod
    def create(cls):
        api_key = os.environ["OPENAI_API_KEY"]
        model_engine = "gpt-3.5-turbo"
        temperature = 0.0
        # TODO: May support more for larger CSS file
        max_tokens = 1024
        return cls(api_key, model_engine, temperature, max_tokens)

    def generate_system_message(self) -> str:
        system_message_template = """You are a helpful website designer and developer to help to update the CSS file.

Here is the original CSS file.

{}

Generate the new CSS for user's input.

Keep the original CSS styles. Only output the content of CSS file. No more introduction nor other messages.
"""
        last_css = self.history_css_queue.get()
        system_message = system_message_template.format(last_css)
        print("Genereate system message: ", system_message)
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
        request_messages = [{"role": "system", "content": self.generate_system_message()}]
        request_messages.append({"role": "user", "content": command})

        response = openai.ChatCompletion.create(
            model=self.model_engine,
            messages=request_messages,
            temperature=self.temperature,
            max_tokens=self.max_tokens
        )
        print("ChatGPT output response", response)

        new_css = self.extrace_css_code(response.choices[0].message["content"])
        self.history_css_queue.put(new_css)

        return new_css


def extrace_css_code(input_text: str) -> str:
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
