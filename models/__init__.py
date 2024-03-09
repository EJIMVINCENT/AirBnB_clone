#!/usr/bin/python3
"""This module contains classes for modeling data in the application."""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
