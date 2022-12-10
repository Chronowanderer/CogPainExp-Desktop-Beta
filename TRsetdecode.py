import pandas as pd

TR_data = pd.read_csv('ExpData/TRSignalRecord.csv')
block_duration = []
in_block = False
start_time, prev_time = 0, 0
for i in range(len(TR_data)):
    if TR_data['TR'].loc[i] == 'TR':
        continue
    if float(TR_data['TR'].loc[i]) > 3:
        if not in_block:
            start_time = float(TR_data['timestamp'].loc[i])
            in_block = True
        prev_time = float(TR_data['timestamp'].loc[i])
    else:
        if in_block and (float(TR_data['timestamp'].loc[i]) - prev_time > 5):
            block_duration.append(prev_time - start_time)
            in_block = False

print(block_duration)
