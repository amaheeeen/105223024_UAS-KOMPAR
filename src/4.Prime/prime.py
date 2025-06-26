import math
import time
from multiprocessing import Pool, cpu_count
import os

# memeriksa bilangan prima
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

# mencari bilangan prima
def find_primes_in_range(start, end):
    primes = []
    for num in range(start, end + 1):
        if is_prime(num):
            primes.append(num)
    return primes

# bilangan prima paralel
def run_prime_finder_parallel(num_workers):
    MAX_NUMBER = 5_000_000
    
    ranges = []
    
    step = MAX_NUMBER // num_workers
    for i in range(num_workers):
        start = i * step + 1
        end = (i + 1) * step
        if i == num_workers - 1: 
            end = MAX_NUMBER
        ranges.append((start, end))

    print(f"\n--- Running with {num_workers} worker(s) ---")
    start_time = time.perf_counter()
    
    all_primes = []
    with Pool(num_workers) as pool:
        results = pool.starmap(find_primes_in_range, ranges)
    
   # Menggabungkan hasil dari semua worker
    for prime_list in results:
        all_primes.extend(prime_list)

    end_time = time.perf_counter()
    execution_time = end_time - start_time
    total_primes = len(all_primes)
    
    print(f"Total primes found: {total_primes}")
    print(f"Execution time with {num_workers} worker(s): {execution_time:.4f} seconds")
    return execution_time, total_primes

if __name__ == "__main__":
    available_cores = cpu_count()
    print(f"Number of CPU cores available: {available_cores}")

    worker_configs = [1, 2, 4, 8] 
    
    if any(w > available_cores for w in worker_configs):
         print(f"Warning: Some worker configurations ({worker_configs}) exceed the number of available CPU cores ({available_cores}). Performance might not scale linearly due to context switching overhead or system resource contention.")

    results_table = {
        "Jumlah Worker": [],
        "Waktu Eksekusi (s)": [],
        "Speedup": [],
        "Efisiensi (%)": []
    }
    
    time_1_worker = 0.0 

    for num_workers in worker_configs:
        exec_time, total_primes = run_prime_finder_parallel(num_workers)
        
        results_table["Jumlah Worker"].append(num_workers)
        results_table["Waktu Eksekusi (s)"].append(f"{exec_time:.4f}")
        
        if num_workers == 1:
            time_1_worker = exec_time
            results_table["Speedup"].append("1.00")
            results_table["Efisiensi (%)"].append("100.00")
        else:
            speedup = time_1_worker / exec_time
            efficiency = (speedup / num_workers) * 100
            results_table["Speedup"].append(f"{speedup:.2f}")
            results_table["Efisiensi (%)"].append(f"{efficiency:.2f}")

    print("\n--- Hasil Tabel Eksekusi ---")
    print("| Jumlah Worker | Waktu Eksekusi (s) | Speedup | Efisiensi (%) |")
    print("|---------------|--------------------|---------|---------------|")
    for i in range(len(results_table["Jumlah Worker"])):
        print(f"| {results_table['Jumlah Worker'][i]:<13} | {results_table['Waktu Eksekusi (s)'][i]:<18} | {results_table['Speedup'][i]:<7} | {results_table['Efisiensi (%)'][i]:<13} |")