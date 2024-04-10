# -*- coding: utf-8 -*-
"""
Created on Tue Mar  5 08:51:46 2024

@author: jotaerre
"""

# import llama helper function
from utils import llama

# define the prompt
prompt = "Help me write a birthday card for my dear friend Andrew."

# pass prompt to the llama function, store output as 'response' then print
response = llama(prompt)
print(response)

# Set verbose to True to see the full prompt that is passed to the model.
prompt = "Help me write a birthday card for my dear friend Andrew."
response = llama(prompt, verbose=True)

