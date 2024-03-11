import serial
import matplotlib.pyplot as plt
from collections import deque

SERIAL_PORT = '/dev/cu.usbmodem14201'  # Change this to your serial port
BAUD_RATE = 9600
WINDOW_SIZE = 1000
FILE_SAVE_PATH = "/Users/calebescobedo/cap_test/sensing-network/hiro/data/4_sensor_cap_data.txt"
x_data = [i for i in range(1, WINDOW_SIZE + 1)]

data = deque(maxlen=WINDOW_SIZE)
ser = serial.Serial(SERIAL_PORT, BAUD_RATE)
last_sample_time = 0.0

# plt.ion()
# fig, ax =  plt.subplots()
# line, = ax.plot(data)
# line.set_linewidth(0.3)

# ax.set_xlabel('Capacitive Sample Value')
# ax.set_ylabel('Time in Millis')
# ax.set_title('HIRO Roboskin Capacitive Sensor Measurments Over Time')

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
    with open(file_path, 'a') as file:
        file.write(str(data) + '\n')

def calculate_hz(cur_time_millis, last_time_millis):
    millis_diff = float(cur_time_millis - last_time_millis)
    sec_diff = millis_diff * 1000
    hz = 1/sec_diff
    return hz


try:
    while True:
        # Read a line from the Arduino
        data_as_str = getLatestStatus(ser)
        data_split = data_as_str.split()
        if data_as_str == "":
            continue
        else:
        # print(data_split[1], end="\n")
            cur_time = data_as_str[1]
            print(cur_time)
            print(data_as_str[1])
            # print(calculate_hz(float(cur_time), float(last_sample_time)))
            # last_sample_time = float(cur_time)

        # append_to_file(FILE_SAVE_PATH, data_read)
        # data.append(data_as_str)

        # Update plot with new data
        # if len(data) >= WINDOW_SIZE:

        #     line.set_ydata(data)
        #     line.set_xdata(x_data)
        #     ax.relim()
        #     ax.autoscale_view()
        #     plt.ylim(0, 2000)
        #     fig.canvas.draw()
        #     fig.canvas.flush_events()

except KeyboardInterrupt:
    print("Exiting...")
    ser.close()