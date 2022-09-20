import platform

os = platform.system()

if os == 'Windows':
    RECORD_PATH = 'C:\\open-ephys\\data'
elif os == 'Linux':
    RECORD_PATH = '<path/to/linux/runner>' #TODO
else:
    RECORD_PATH = '<path/to/mac/runner>' #TODO

'''
Test Name: Test Synchronization
Test Description: Ensures that data synchronization is working correctly.
'''

DEBUG_MODE = False
ADDRESS = '127.0.0.1'

ACQUISITION_TIME    = 10 #Number of seconds to acquire data before starting recording (allows for synchronization)
RECORD_TIME         = 10 #Number of seconds to record data between acquistiions
NUM_RECORDINGS      = 2 #Total number of recordings in the experiments
NUM_EXPERIMENTS     = 2 #Total number of experiments

PREPEND_TEXT        = '' #Text to prepend to the beginning of the experiment name
BASE_TEXT           = '' #Text to describe the experiment name
APPEND_TEXT         = '' #Text to append to the end of the experiment name

test_params = dict(
    fetch = True, # True to fetch new data and re-run test, False to just show most recent test results 
    address = ADDRESS, 
    acq_time = ACQUISITION_TIME,
    rec_time = RECORD_TIME,
    num_rec = NUM_RECORDINGS,
    num_exp = NUM_EXPERIMENTS,
    prepend_text = '',
    base_text = '',
    append_text = '',
    parent_directory = RECORD_PATH,
    engine = 'engine=0' #BINARY_ENGINE
)