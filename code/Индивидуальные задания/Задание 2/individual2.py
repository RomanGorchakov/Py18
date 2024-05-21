#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
from datetime import date
from show_plane import show_plane
from dotenv import load_dotenv


if __name__ == '__main__':
    dotenv_path = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(dotenv_path):
        load_dotenv(dotenv_path)

    show_plane()