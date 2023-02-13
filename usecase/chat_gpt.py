import os
import openai
import config.config

openai.organization = config.config.organization
openai.api_key = config.config.CHAT_GPT_SECRET_KEY
openai.Model.list()