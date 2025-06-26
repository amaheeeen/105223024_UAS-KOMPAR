import multiprocessing
import time

def calculate_square(angka):
    return angka * angka

def multiprocessing_approach(x):
    # Using Pool for easier distribution of tasks
    with multiprocessing.Pool(processes=multiprocessing.cpu_count()) as pool:
        results = pool.map(calculate_square, x)
    return results

if __name__ == "__main__":
    x_to_square = list(range(1, 1_000_001))

    print("Menjalankan proses Multiprocessing...")
    start_time_multiprocessing = time.time()
    multiprocessing_approach(x_to_square)
    end_time_multiprocessing = time.time()
    print(f"waktu eksekusi Multiprocessing: {end_time_multiprocessing - start_time_multiprocessing:.4f} detik")