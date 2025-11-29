# Print 3 messages in order
import time

def download():
    start = time.time()
    time.sleep(5)
    print("Downloading data...")
    end = time.time()
    print(f"To perform task it takse {end - start} second...")
    
print("Starting Task...")
download()
print("End Task...")








