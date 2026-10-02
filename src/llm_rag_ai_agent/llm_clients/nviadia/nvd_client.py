from openai import OpenAI
from llm_rag_ai_agent.config import settings



class Client:
    """
    This class is used to get the NVIDIA client
    """
    def __init__(self):
        """
        Initializes the NVIDIA client
        """
        self._validate()


        self._client = OpenAI(
            api_key=settings.nvidia_api_key,
            base_url=settings.nvidia_base_url,
        )


    @staticmethod
    def _validate():
        """
        Validates the NVIDIA client
        """
        try:
            if settings.nvidia_api_key is None or settings.nvidia_api_key == "":
                raise ValueError("NVIDIA API key is not set")
            if settings.nvidia_base_url is None or settings.nvidia_base_url == "":
                raise ValueError("NVIDIA base URL is not set")
        except Exception as e:
            raise e

    @property
    def client(self):
        """
        Returns the NVIDIA client
        """
        return self._client

    @client.setter
    def client(self, api_key:str=None, base_url:str=None):
        """
        Sets the NVIDIA client
        """
        if api_key is None:
            api_key = settings.nvidia_api_key
        if base_url is None:
            base_url = settings.nvidia_base_url
        self._client = OpenAI(
            api_key=api_key,
            base_url=base_url,
        )

        


class Model:
    def __init__(self, model_name:str|None=None, messages:list[dict[str, str|list[dict[str, str]]|list[dict]]]|None=None, temperature:float=0.7, max_tokens:int=1000, top_p:float=0.9, frequency_penalty:float=0.0, presence_penalty:float=0.0):
        """
        Initializes the Model
        """
        try:
            self.client = Client().get_client()
            self.model_name = settings.nvidia_model
            self.messages = messages
            self.temperature = temperature
            self.max_tokens = max_tokens
            self.top_p = top_p
            self.frequency_penalty = frequency_penalty
            self.presence_penalty = presence_penalty
        except Exception as e:
            raise e


    
        
    