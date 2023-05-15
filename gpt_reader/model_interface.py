from typing import List
import openai


class ModelInterface(object):

    def __init__(self) -> None:
        pass

    def send_msg(self, *args):
        pass


class OpenAIModel(object):

    def __init__(self, api_key, model='gpt-3.5-turbo-0301', temperature=0.2) -> None:
        # openai.api_key = api_key
        openai.api_type = "azure"

        openai.api_key = "b5e8fdce88e74faeac165e878d742632"

        # The base URL for your Azure OpenAI resource. e.g. "https://<your resource name>.openai.azure.com"
        openai.api_base = "https://azureopenai-lei.openai.azure.com/"

        # Currently OPENAI API have the following versions available: 2022-12-01
        openai.api_version = "2023-03-15-preview"
        self.model = model
        self.temperature = temperature

    def send_msg(self, msg: List[dict], return_raw_text=True):
        
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=msg,
            temperature=self.temperature
        )

        if return_raw_text:
            return response["choices"][0]["message"]["content"]
        else:
            return response
