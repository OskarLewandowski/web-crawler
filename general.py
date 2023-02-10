import os

WEB_NAME = "mediaexpert"


def create_project_dir(directory):
    if not os.path.exists(directory):
        print(f"Creating directory: {directory}")
        os.makedirs(directory)
