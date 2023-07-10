import os
import time 

print("In docker...")
print(os.environ["APP_ENV"])
while True:
    print(".")
    time.sleep(10)
  