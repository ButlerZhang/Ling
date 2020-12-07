import ctypes



def getScreenSolution():
    winapi = ctypes.windll.user32
    screen_width = winapi.GetSystemMetrics(0)
    screen_height = winapi.GetSystemMetrics(1)
    return screen_width, screen_height
