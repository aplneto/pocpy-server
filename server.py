#!/usr/bin/env python3

import requests

response = requests.get('https://www.google.com.br')
print(response.raw)