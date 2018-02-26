
'''Prevent OS sleep/hibernate in windows; code from:
https://github.com/h3llrais3r/Deluge-PreventSuspendPlus/blob/master/preventsuspendplus/core.py
API documentation:
https://msdn.microsoft.com/en-us/library/windows/desktop/aa373208(v=vs.85).aspx'''
ES_CONTINUOUS = 0x80000000
ES_SYSTEM_REQUIRED = 0x00000001


def stop_sleep():
    import ctypes
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS | \
        ES_SYSTEM_REQUIRED)

def allow_sleep():
    import ctypes
    ctypes.windll.kernel32.SetThreadExecutionState(
        ES_CONTINUOUS)
