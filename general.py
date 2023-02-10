import os


# Create a directory for each project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print(f"Creating directory for a project: {directory}")
        os.makedirs(directory)


# Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = f"{project_name}/queue.txt"
    crawled = f"{project_name}/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


# Create a new file
def write_file(filename, data):
    with open(filename, "w") as file:
        file.write(data)


# Add data to an existing file
def append_to_file(filename, data):
    with open(filename, "a") as file:
        file.write(f"{data}\n")


# Delete the contents of a file
def delete_file_contents(filename):
    with open(filename, 'w'):
        pass
