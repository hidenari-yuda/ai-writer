import os
import openai
import app.config.config

openai.organization = app.config.config.organization
openai.api_key = app.config.config.CHAT_GPT_SECRET_KEY
openai.Model.list()
