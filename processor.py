import google.generativeai as genai
from dotenv import load_dotenv
from utility import prompt
import os
load_dotenv()


class Processor:
    """
    The Processor class facilitates redrafting text using generative AI.

    Attributes:
    - model (GenerativeModel): The generative AI model for redrafting text.

    Methods:
    - __init__(API_KEY: str | None = None): Initialize the Processor with the specified API key or retrieve it from the environment variables.
    - redraft(text: str, tone: str) -> str: Generate a redrafted version of the input text with a specified tone.

    Example Usage:
    ```python
    processor = Processor()
    redrafted_text = processor.redraft("Original text", "general")
    ```

    Note: The redraft method uses a pre-defined prompt based on the specified tone for redrafting text.

    """
    def __init__(self, API_KEY: str | None = None) -> None:
        """
        Initialize the Processor with the specified API key or retrieve it from the environment variables.

        Parameters:
        - API_KEY (str | None): The API key for the generative AI. If None, it attempts to retrieve it from the environment variables.
        """
        if API_KEY is None:
            API_KEY = os.getenv("API_KEY")
            assert API_KEY is not None, "Cannot Load API key"

        genai.configure(api_key=API_KEY)
        self.model = genai.GenerativeModel('gemini-pro')

    def redraft(self, text: str, tone: str) -> str:
        """
        Generate a redrafted version of the input text with a specified tone.

        Parameters:
        - text (str): The input text to be redrafted.
        - tone (str): The desired tone for the redrafted text.

        Returns:
        - str: The redrafted text with the specified tone.
        """
        tone = tone.lower()
        sel_prompt = prompt[tone]

        print("Input: ", text)

        response = self.model.generate_content([sel_prompt, text])

        print(response.text)

        return response.text
