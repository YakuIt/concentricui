from kivy import platform

if platform == 'android':
    from jnius import autoclass

    BluetoothAdapter = autoclass('android.bluetooth.BluetoothAdapter')
    BluetoothDevice = autoclass('android.bluetooth.BluetoothDevice')
    BluetoothSocket = autoclass('android.bluetooth.BluetoothSocket')
    UUID = autoclass('java.util.UUID')
elif platform == 'win':
    pass
    import bluetooth


class AndroidBluetoothConnectivity(object):

    def __init__(self):
        """ last_paired_device_address is used for resetting connection """
        self.last_paired_device_address = None
        self.recv_stream, self.send_stream = None, None

    def get_socket_stream_list(self):
        paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
        address_name_list = [(device.getAddress(), device.getName()) for device in paired_devices]
        print('5555555555555555555555555555555555555555555', address_name_list)
        return address_name_list

    def set_socket_stream(self, address):

        if not address:
            self.recv_stream, self.send_stream = None, None
            print('Bluetooth connection removed')
            return

        # if not paired_devices:
        #     raise Exception("socket stream list not retrieved. retrieve it with get_socket_scream_list()")
        #
        # if name not in [device.getName() for device in paired_devices]:
        #     print('paired_devices', [(type(x), x) for x in paired_devices], type(name), name)
        #     raise Exception("No device with name {} found. \n Available devices: {}".format(name, paired_devices))

        # if platform != 'android':
        #     print('wotn go further as not android......')
        #     return

        # paired_devices = self.get_socket_stream_list()

        # socket = None
        # for device in paired_devices:
        #     if device.getAddress() == address:
        device = BluetoothAdapter.getDefaultAdapter().getRemoteDevice(address)
        socket = device.createRfcommSocketToServiceRecord(
            UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
        recv_stream = socket.getInputStream()
        send_stream = socket.getOutputStream()
        # break

        #
        # if unset:
        #     socket.close()
        #     self.recv_stream, self.send_stream = None, None
        # else:
        socket.connect()
        self.recv_stream, self.send_stream = recv_stream, send_stream
        self.last_paired_device_address = address


    def send_data(self, data):

        if self.send_stream:
            try:
                self.send_stream.write(data)
                self.send_stream.flush()
                return True
            except:
                try:
                    self.set_socket_stream(address=self.last_paired_device_address)
                    self.send_stream.write(data)
                    self.send_stream.flush()
                    print(':)')
                    return True
                except Exception as e:
                    print(':(', e)
                    return False

        else:
            Warning("No send stream set up. {} not sent".format(data))
            return False

    def reset(self):

        pattern_string = '0'
        if self.send_stream:
            self.send_stream.write('{}\n'.format(pattern_string))
            self.send_stream.flush()


class WindowsBluetoothConnectivity(object):

    def __init__(self):
        """ last_paired_device_address is used for resetting connection """
        self.last_paired_device_address = None
        self.recv_stream, self.send_stream = None, None

    def get_socket_stream_list(self):

        paired_devices = bluetooth.discover_devices(lookup_names=True)

        return paired_devices

    def set_socket_stream(self, address, unset=False):

        if not address:
            if self.send_stream:
                self.send_stream.close()
            self.recv_stream, self.send_stream = None, None
            print('Bluetooth connection removed')
            return
        print('okok', address)
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            socket.connect((address, 1))
        except OSError as e:
            print('excepted!!', e)
            socket.close()
            return

        self.send_stream = socket

    def send_data(self, data):
        if self.send_stream:
            self.send_stream.send(bytes(str(data), 'UTF-8'))
        else:
            Warning("No send stream set up. {} not sent".format(data))

    def reset(self):
        pattern_string = '0'
        if self.send_stream:
            self.send_stream.write('{}\n'.format(pattern_string))
            self.send_stream.flush()


if platform == 'android':
    device_connectivity = AndroidBluetoothConnectivity
elif platform == 'win':
    device_connectivity = WindowsBluetoothConnectivity


class BluetoothConnectivity(device_connectivity):
    pass
