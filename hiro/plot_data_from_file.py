import matplotlib.pyplot as plt

def read_int_data_from_file(file_path):
    """
    Read integer data from a file separated by new line characters.

    Parameters:
    - file_path: The path to the file.

    Returns:
    - A list of integers read from the file.
    """
    int_data = []
    with open(file_path, 'r') as file:
        for line in file:
            int_data.append(float(line.strip()))
    return int_data

def plot_data(int_data):
    """
    Plot integer data.

    Parameters:
    - int_data: A list of integers to plot.
    """
    plt.plot(int_data)
    plt.xlabel('Index')
    plt.ylabel('Value')
    plt.title('Integer Data Plot')
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    file_path = "/Users/calebescobedo/cap_test/sensing-network/hiro/data/4_sensor_cap_data.txt"  # Change this to your file path
    int_data = read_int_data_from_file(file_path)
    plot_data(int_data)