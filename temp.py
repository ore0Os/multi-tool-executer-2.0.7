import shutil

def get_disk_usage():
    try:
        total, used, free = shutil.disk_usage('/')
        return total, used, free
    except Exception as e:
        print("Unable to retrieve disk usage information.")
        print(e)
        return None

def print_disk_information():
    disk_usage = get_disk_usage()
    if disk_usage is not None:
        total_size, used_size, free_size = disk_usage
        print(f"Total disk size: {total_size // (2**30)} GB")
        print(f"Used disk space: {used_size // (2**30)} GB")
        print(f"Free disk space: {free_size // (2**30)} GB")
    else:
        print("Unable to retrieve disk information.")

# Call the function
print_disk_information()
