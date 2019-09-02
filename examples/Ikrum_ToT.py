#!/usr/bin/env python
import dpx_func_python

PORT = '/dev/ttyUSB0'
CONFIG_FN = 'DPXConfig_22_6_109.conf'
CONFIG_DIR = 'config/'
CHIP_NUMS = [22, 6, 109]
IKRUM = [5, 10, 20] 

def main():
    # Establish connection
    thl_calib_files = None # [CONFIG_DIR + '/THLCalib_%d.hck' % CHIP for CHIP in CHIP_NUMS] 
    dpx = dpx_func_python.Dosepix(PORT, 2e6, CONFIG_DIR + '/' + CONFIG_FN, thl_calib_files=thl_calib_files)

    # Change Ikrum values
    new_peripherys = []
    for chip_idx in range(3):
        d = dpx.splitPerihperyDACs(dpx.peripherys + dpx.THLs[chip_idx], perc=False)
        d['I_krum'] = IKRUM[chip_idx]
        code = dpx.periheryDACsDictToCode(d, perc=False)
        dpx.peripherys = code[:-4]
        new_peripherys.append( code[:-4] )
        dpx.DPXWritePeripheryDACCommand(chip_idx + 1, code)
        print dpx.DPXReadPeripheryDACCommand(chip_idx + 1)
        print dpx.DPXReadOMRCommand(chip_idx + 1)

    for slot in range(1, 4):
        print dpx.DPXReadPeripheryDACCommand(slot)

    import hickle as hck
    # Measure ToT
    while True:
        dpx.measureToT(slot=[1, 2, 3], intPlot=False, cnt=10000, storeEmpty=False, logTemp=True, meas_time=7200) # , paramsDict=hck.load('config/paramsDict_22_6_109_Ikrum_newCalib.hck'))
        # dpx.measurePC(slot=2, measurement_time=0, frames=1000, intPlot=True)
        for slot in range(3):
            dpx.THLs[slot] = '%04x' % (int(dpx.THLs[slot], 16) - 10)
            dpx.DPXWritePeripheryDACCommand(slot + 1, new_peripherys[slot] + dpx.THLs[slot])

    # Close connection
    dpx.close()

if __name__ == '__main__':
    main()

