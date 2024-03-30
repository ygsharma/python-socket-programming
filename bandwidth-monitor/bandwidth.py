import time 
import psutil
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

timestamps = []
mb_recv =[]
mb_sent = []

last_recv = psutil.net_io_counters().bytes_recv
last_sent = psutil.net_io_counters().bytes_sent

def update_data(i):
    global last_recv, last_sent
    bytes_recv = psutil.net_io_counters().bytes_recv
    bytes_sent = psutil.net_io_counters().bytes_sent
    
    new_recv = (bytes_recv - last_recv)/1024/1024
    new_sent = (bytes_sent - last_sent)/1024/1024
    
    timestamps.append(time.time())
    mb_recv.append(new_recv)
    mb_sent.append(new_sent)
    
    if len(timestamps) > 60:
        timestamps.pop(0)
        mb_recv.pop(0)
        mb_sent.pop(0)
        
    ax.clear()
    ax.plot(timestamps, mb_recv, label = 'MB Received')
    ax.plot(timestamps, mb_sent, label = 'MB Sent')
    
    ax.legend()
    
    last_recv = bytes_recv
    last_sent = bytes_sent        
        
# Initialize the plot÷
fig, ax = plt.subplots()
plt.xlabel('Time')
plt.ylabel('MB')
plt.title("Real-Time Bandwidth utilization")

ani = FuncAnimation(fig, update_data, interval = 1000)
plt.show()