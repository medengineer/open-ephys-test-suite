import git 

EXPECTED_NUMBER_OF_SUBPROCESSORS = 10
filename = '/home/pavel/open-ephys/2021-02-17_15-56-34/Record Node 103/experiment1/recording1/sync_messages.txt'
with open(filename) as f:
    sync_messages = f.readlines()
sync_messages = [x.strip() for x in sync_messages] 

if len(sync_messages) == EXPECTED_NUMBER_OF_SUBPROCESSORS + 1: #+1 for software timestamp
    print("TEST PASSED!")
else:
    print("TEST FAILED!")