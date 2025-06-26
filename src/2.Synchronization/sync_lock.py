import threading
import time

global_counter = 0
counter_lock = threading.Lock() # Membuat objek Lock

def increment_counter_synchronized():
    global global_counter
    for _ in range(100_000):
        with counter_lock: # Mengunci saat mengakses shared resource
            global_counter += 1 # Operasi increment yang aman

if __name__ == "__main__":
    print("Running Synchronized Multithreaded Program...")
    
    threads = []
    for _ in range(2): # Dua thread
        thread = threading.Thread(target=increment_counter_synchronized)
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    print(f"Final global counter (synchronized): {global_counter}")