#!/bin/usr/env python3 
import os
import sys
import time
import logging

log = logging.Logger("errors")

#EAFP - Easy to Ask Forgiveness thant Permission

def try_open_file(filepath,retry=1):
    """Tries to open a file, if error, retries n times."""
    if retry > 999:
        raise ValueError("Retry cannot be above 999")
    try:
        return open(filepath).readline() # FileNotFoundError
    except FileNotFoundError as e:
        log.error("ERRO: %s",e)
        if retry > 1:
            # recursão
            return try_open_file(filepath,retry = retry - 1)
    else:
        print("Sucesso!")
    finally:
        print("Execute isso sempre")
    return []

for line in try_open_file("name.txt", retry=5):
    print(line)
