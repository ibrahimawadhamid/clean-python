def read_file(file_name: str):
    """Use Iterators instead of Lists when possible"""
    with open(file_name) as fread:
        for line in fread:
            yield line

for line in read_file("logfile.txt"):
    print(line)
