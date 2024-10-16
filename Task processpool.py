import concurrent.futures
from collections import defaultdict
from pathlib import Path
import time


def search_in_file(file_path, keywords):
    result = []
    try:
    # TODO Додати обробку можливих помилок 
        with open(file_path, 'r') as file:
            content = file.read()
            for keyword in keywords:
                if keyword in content:
                    result.append((keyword, file_path))
        return result
    except IOError as e:
        print(f"Error reading file {file_path}: {e}")


def main_concurrent_process(file_paths, keywords):
    # TODO Додати вимір часу виконання
    start_time = time.time()
    results = defaultdict(list)





    # Submit tasks to the executor
    futures = {executor.submit(search_in_file, file_path, keywords): file_path for file_path in file_paths}
        
        # Process completed futures
    for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
                for keyword, file_path in result:
                    results[keyword].append(file_path)
            except Exception as e:
                print(f"Error processing file {futures[future]}: {e}")
    end_time = time.time()
    print(f"Time taken: {end_time - start_time} seconds")
    return results



if __name__ == '__main__':
    file_paths = list(Path("input").glob("*.py"))
    for file in file_paths:
     print(f"File paths: {file_paths}\n")
    keywords = []
    results = main_concurrent_process(file_paths, keywords)
    print(results)