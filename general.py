import os


# Create a directory for each project
def create_project_dir(directory):
    if not os.path.exists(directory):
        print(f"Creating directory for a project: {directory}")
        os.makedirs(directory)


# Create queue and crawled files
def create_data_files(project_name, base_url):
    queue = os.path.join(project_name, "queue.txt")
    crawled = os.path.join(project_name, "crawled.txt")
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
    open(filename, 'w').close()


# Convert file items to a set
def file_to_set(filename):
    results = set()
    with open(filename, "rt") as file:
        for line in file:
            results.add(line.replace("\n", ""))
    return results


# Convert set to a file items with new line
def set_to_file(links_data_set, filename):
    with open(filename, "w") as file:
        for link in sorted(links_data_set):
            file.write(f"{link}\n")
