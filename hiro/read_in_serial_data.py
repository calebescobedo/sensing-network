import serial
import matplotlib.pyplot as plt
from collections import deque
import time

SERIAL_PORT = '/dev/cu.usbmodemF412FA7763D82'  # Change this to your serial port
BAUD_RATE = 9600
WINDOW_SIZE = 100
FILE_SAVE_PATH = "/Volumes/DEBIAN/3dp_roboskin_data/05_08_24_calebs_house_30_min_no_touch_on_charger_51ohm_115200baud.txt"
LIVE_PLOT = True
SAVE_FILE = False

if SAVE_FILE:
    file = open(FILE_SAVE_PATH, 'x')

x_data = [i for i in range(1, WINDOW_SIZE + 1)]

data = deque(maxlen=WINDOW_SIZE)
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
last_sample_time = 0.0

if LIVE_PLOT:
    plt.ion()
    fig, ax =  plt.subplots()
    line, = ax.plot(data)
    line.set_linewidth(0.3)

    ax.set_ylabel('Capacitive Sample Value')
    ax.set_xlabel('Time in Millis')
    ax.set_title('HIRO Roboskin Capacitive Sensor Measurments Over Time')

def getLatestStatus(arduino):
    data_as_str = ""
    while arduino.inWaiting() > 0:
        data_as_str = arduino.readline().decode('utf-8')
        # print("After Waiting")
    # print(data_as_str)
    return data_as_str

def append_to_file(file_path, data):
    """
    Append data to a file.

    Parameters:
    - file_path: The path to the file.
    - data: The data to append to the file.
    """
    with open(file_path, 'x') as file:
        file.write(str(data) + '\n')

def calculate_hz(cur_time_millis, last_time_millis):
    millis_diff = float(cur_time_millis - last_time_millis)
    sec_diff = millis_diff * 1000
    hz = 1/sec_diff
    return hz

start_time_ms = time.time()*1000.0
min_5_ms = 300000.0
min_30_ms =1800000.0

try:
    while True:
        # Read a line from the Arduino
        cur_time_ms = time.time()*1000.0
        if cur_time_ms - start_time_ms >= min_30_ms:
            exit()
        data_as_str = getLatestStatus(ser)
        data_split = data_as_str.split()
        if data_as_str == "":
            print('empty')
            continue
        else:
            data_as_float = float(data_as_str)
            if SAVE_FILE:
                file.write(data_as_str)

        if LIVE_PLOT:
            data.append(data_as_float)
        # Update plot with new data
            if len(data) >= WINDOW_SIZE:

                line.set_ydata(data)
                line.set_xdata(x_data)
                ax.relim()
                ax.autoscale_view()
                plt.ylim(4, 5)
                fig.canvas.draw()
                fig.canvas.flush_events()

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()