import threading
import timeit
import time
import random
from collections import defaultdict
from pathlib import Path


def search_in_file(file_path, keywords, results):
    try:
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    results[keyword].append(file_path)
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")


def thread_task(files, keywords, results):
    for file in files:
        search_in_file(file, keywords, results)


def main_threading(file_paths, keywords):
    start_time = time.time()
    num_threads = 4
    files_per_thread = len(file_paths) // num_threads
    threads = []
    results = defaultdict(list)

    for i in range(num_threads):
        start = i * files_per_thread
        end = None if i == num_threads - 1 else start + files_per_thread
        thread_files = file_paths[start:end]
        thread = threading.Thread(target=thread_task, args=(thread_files, keywords, results))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    return results

if __name__ == '__main__':
    # Приклад виклику
    file_paths = list(Path("input").glob("*.py"))
    for file in file_paths:
     search_in_file(file, keywords, results)
    print(f"File paths: {file_paths}\n")
    keywords = []
    results = main_threading(file_paths, keywords)
    print(results)




