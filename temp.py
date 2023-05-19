import psutil

def get_memory_usage():
    try:
        memory = psutil.virtual_memory()
        return memory
    except Exception as e:
        print("Unable to retrieve memory usage information.")
        print(e)
        return None

def print_memory_information():
    memory_usage = get_memory_usage()
    if memory_usage is not None:
        total_memory = memory_usage.total
        used_memory = memory_usage.used
        free_memory = memory_usage.available
        print(f"Total memory: {total_memory // (2**30)} GB")
        print(f"Used memory: {used_memory // (2**30)} GB")
        print(f"Free memory: {free_memory // (2**30)} GB")
    else:
        print("Unable to retrieve memory information.")

# Call the function
print_memory_information()

