import time
import MoveSensors

with open("Thisdata.csv","w+") as File:
    File.write("Time (s),Gyroscope X (deg/s),Gyroscope Y (deg/s),Gyroscope Z (deg/s),Accelerometer X (g),Accelerometer Y (g),Accelerometer Z (g)")
    
    StartTime = time.perf_counter()
    
    while True:
        Data = MoveSensors.Get_Values()
        Gyro = Data["gyro"]
        Accel = Data["acceleration"]
        
        print(Gyro,Accel)
        
        File.write(f"\n{time.perf_counter()-StartTime},{Gyro[0]},{Gyro[1]},{Gyro[2]},{Accel[0]},{Accel[1]},{Accel[2]}")
        print("Wrote")