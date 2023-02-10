import os


# Create a directory for each project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print(f"Creating directory for a project: {directory}")
        os.makedirs(directory)


# Create queue and crawled files
def create_data_fiels(project_name, base_url):
    queue = f"{project_name}/queue.txt"
    crawled = f"{project_name}/crawled.txt"
    if not os.path.isfile(queue):
        write_file(queue, base_url)
    if not os.path.isfile(crawled):
        write_file(crawled, "")


# Create a new file
def write_file(filename, data):
    f = open(filename, 'w')
    f.write(data)
    f.close()
