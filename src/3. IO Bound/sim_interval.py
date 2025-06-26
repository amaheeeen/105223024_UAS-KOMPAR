import threading
import time
import datetime

SIMULATION_DURATION = 5

def sensor_task(name, interval_ms):
    interval_s = interval_ms / 1000.0 
    start_time = time.monotonic() 
    
    print(f"[{datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {name} sensor started (interval: {interval_ms} ms).")
    
    next_send_time = start_time + interval_s
    
    while time.monotonic() - start_time < SIMULATION_DURATION:
        sleep_until = next_send_time
        time_to_sleep = sleep_until - time.monotonic()

        if time_to_sleep > 0:
            time.sleep(time_to_sleep)
        
        if time.monotonic() - start_time >= SIMULATION_DURATION:
            break

        current_real_time = datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]
        print(f"[{current_real_time}] {name} sensor sent data.")
        
        next_send_time += interval_s
        while next_send_time < time.monotonic():
            next_send_time += interval_s

    print(f"[{datetime.datetime.now().strftime('%H:%M:%S.%f')[:-3]}] {name} sensor finished.")

if __name__ == "__main__":
    print("--- Starting Sensor Simulation ---")
    
    threads = []
    
    camera_thread = threading.Thread(target=sensor_task, args=("Kamera", 100))
    threads.append(camera_thread)
    
    lidar_thread = threading.Thread(target=sensor_task, args=("LIDAR", 50))
    threads.append(lidar_thread)
    
    gps_thread = threading.Thread(target=sensor_task, args=("GPS", 1000)) # 1 detik = 1000 ms
    threads.append(gps_thread)
    
    for t in threads:
        t.start()
        
    for t in threads:
        t.join()
        
    print("--- Sensor Simulation Finished ---")