"""
NIDAQMX trigger
"""
import nidaqmx
import time


class Trigger():
    def __init__(self, daqtype, dev = '1', channel = 'ao0'):

        if daqtype == 'NIDAQ':
            self.daq = True
            self.dev = dev
            print('Using NIDAQ: ' + self.dev)

        elif daqtype == 'FAKE' or daqtype is None or daqtype is False:
            self.daq = False
            print('WARNING: NIDAQ using a fake trigger.')

    def five_volt(self, channel = 'ao0'):
        """
        create a 5V square wave pulse for triggering
        """
        if self.daq:
            dev_chan = 'Dev' + self.dev + '/' + channel
            stim = [0] * 1 + [5] * 3 + [0] * 1
            stim_10 = stim * 10  # x10 in 50ms, 200Hz
            print('[NIDAQ] Sending NI trigger ' + dev_chan + '.')
            with nidaqmx.Task() as task:
                task.ao_channels.add_ao_voltage_chan(dev_chan)
                # task.write(stim, auto_start = True)
                task.write(stim_10, auto_start = True)

        else:
            print('[NIDAQ] Sending fake trigger.')
            time.sleep(0.02)


if __name__ == "__main__":
    task = nidaqmx.Task()
    stim = [0] * 5 + [5] * 10 + [0] * 5
    task.ao_channels.add_ao_voltage_chan("Dev1/ao0")
    # task.ao_channels.add_ao_voltage_chan("Dev1/ao1")
    task.write(stim, auto_start = True)
