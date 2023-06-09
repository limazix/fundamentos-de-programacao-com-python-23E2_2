# -*- coding: utf-8 -*-

# Expressão Regular
# https://docs.python.org/3/howto/regex.html

# 'hello world!'.split(' ') -> ['hello', 'world!']

import re
from urllib.parse import urlparse

# dado uma url extraia a primeira bparte do domínio desta string
# http://google.com -> google
# https://google.com -> google
# www.google.com -> google
# https://google.com/search -> google
# https://google.com/search?q=casa -> google


def get_domain(url):
    url = url.replace('http://', '').replace('https://', '')
    parsed = urlparse(url)
    path_parts = parsed.path.split('.')
    return path_parts[0] if path_parts[0] != 'www' else path_parts[1]
    # pattern = "(//|www.)(\w+)[.]"
    # result = re.search(pattern, url)
    # return result.group(2)
