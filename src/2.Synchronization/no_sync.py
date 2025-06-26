import threading
import time

global_counter = 0

def increment_counter_unsynchronized():
    global global_counter
    for _ in range(100_000):
        temp = global_counter
        temp += 1
        global_counter = temp

if __name__ == "__main__":
    print("Running Unsynchronized Multithreaded Program...")
    
    threads = []
    for _ in range(2): # Dua thread
        thread = threading.Thread(target=increment_counter_unsynchronized)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final global counter (unsynchronized): {global_counter}")
    