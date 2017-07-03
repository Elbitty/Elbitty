#!/usr/bin/env python
# -*- coding:utf-8 -*-

def unescape(text):

    escape_from = ('&nbsp;', '&lt;', '&gt;', '&amp;', '&quot;')
    escape_to = (' ', '<', '>', '&', '"')

    for idx, val in enumerate(escape_from):
        if val in text:
            text = text.replace(val, escape_to[idx])

    return text

if __name__ == "__main__":
    print(unescape('&lt;'))
