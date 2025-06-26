import threading
import time

def calculate_square(angka):
    return angka * angka

def multithreading_approach(x):
    threads = []
    results = [0] * len(x)

    def thread_task(start_index, end_index):
        for i in range(start_index, end_index):
            results[i] = calculate_square(x[i])

    num_threads = 4 # adjustable
    chunk_size = len(x) // num_threads
    
    for i in range(num_threads):
        start_index = i * chunk_size
        end_index = (i + 1) * chunk_size if i != num_threads - 1 else len(x)
        thread = threading.Thread(target=thread_task, args=(start_index, end_index))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()
    
    return results

if __name__ == "__main__":
    x_to_square = list(range(1, 1_000_001))

    print("Menjalankan Multithreading...")
    start_time_threading = time.time()
    multithreading_approach(x_to_square)
    end_time_threading = time.time()
    print(f"Waktu eksekusi Multithreading: {end_time_threading - start_time_threading:.4f} detik")