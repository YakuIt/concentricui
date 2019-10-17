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
        """ last_paired_device_name is used for resetting connection """
        self.last_paired_device_name = None
        self.recv_stream, self.send_stream = None, None

    def get_socket_stream_list(self):
        paired_devices = BluetoothAdapter.getDefaultAdapter().getBondedDevices().toArray()
        return paired_devices

    def set_socket_stream(self, name, unset=False):

        self.last_paired_device_name = name

        paired_devices = self.get_socket_stream_list()

        if not name:
            self.recv_stream, self.send_stream = None, None
            print('Bluetooth connection removed')
            return

        if not paired_devices:
            raise Exception("socket stream list not retrieved. retrieve it with get_socket_scream_list()")

        if name not in [device.getName() for device in paired_devices]:
            print('paired_devices', [(type(x), x) for x in paired_devices], type(name), name)
            raise Exception("No device with name {} found. \n Available devices: {}".format(name, paired_devices))

        if platform != 'android':
            print('wotn go further as not android......')
            return

        socket = None
        for device in paired_devices:
            if device.getName() == name:
                socket = device.createRfcommSocketToServiceRecord(
                    UUID.fromString("00001101-0000-1000-8000-00805F9B34FB"))
                recv_stream = socket.getInputStream()
                send_stream = socket.getOutputStream()
                break

        if unset:
            socket.close()
            self.recv_stream, self.send_stream = None, None
        else:
            socket.connect()
            self.recv_stream, self.send_stream = recv_stream, send_stream

    def send_data(self, data):

        if self.send_stream:
            try:
                self.send_stream.write(data)
                self.send_stream.flush()
            except:
                try:
                    self.set_socket_stream(name=self.last_paired_device_name)
                    self.send_stream.write(data)
                    self.send_stream.flush()
                    print(':)')
                except Exception as e:
                    print(':(', e)

        else:
            Warning("No send stream set up. {} not sent".format(data))

    def reset(self):

        pattern_string = '0'
        if self.send_stream:
            self.send_stream.write('{}\n'.format(pattern_string))
            self.send_stream.flush()


class WindowsBluetoothConnectivity(object):

    def __init__(self):
        """ last_paired_device_name is used for resetting connection """
        self.last_paired_device_name = None
        self.recv_stream, self.send_stream = None, None

    def get_socket_stream_list(self):

        paired_devices = bluetooth.discover_devices(lookup_names=True)

        return paired_devices

    def set_socket_stream(self, name, unset=False):

        if not name:
            if self.send_stream:
                self.send_stream.close()
            self.recv_stream, self.send_stream = None, None
            print('Bluetooth connection removed')
            return
        print('okok', name)
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        try:
            socket.connect((name, 1))
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
