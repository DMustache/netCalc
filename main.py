# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

class IpAddress:
    def __init__(self, ip):
        self.address = list(map(int, ip.split('.')))
        self.bin_address = [(bin(octet)[2:]).rjust(8, '0') for octet in
                            self.address]

    def get_bin_address(self, param=0):
        if param == 1:
            return '.'.join(self.bin_address)
        else:
            return self.bin_address

    def get_address(self, param=0):
        if param == 1:
            return '.'.join([str(octet) for octet in self.address])
        else:
            return [(str(octet)).rjust(3, '0') for octet in self.address]


def main():
    host = '10.246.162.99'
    mask = '255.248.0.0'

    host = IpAddress(host)
    mask = IpAddress(mask)

    bin_host = host.get_bin_address()
    bin_mask = mask.get_bin_address()

    net_address = [int(bin_host[i], 2) & int(bin_mask[i], 2) for i in range(len(bin_host))]


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
