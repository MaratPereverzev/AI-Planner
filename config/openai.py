from openai import OpenAI

from config.globals import config

client = OpenAI(api_key=config.OPENAI_TOKEN)