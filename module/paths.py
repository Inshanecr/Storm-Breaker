def weather_temp(path):
    if path == "info":
        return "weather/info.json"

    elif path == "result":
        return "weather/result.json"

    elif path == "error":
        return "weather/error.txt"


def nearyou_temp(path):
    if path == "info":
        return "nearyou/info.json"

    elif path == "result":
        return "nearyou/result.json"


def webcam_temp(path):
    if path == "face-app-info":
        return "camera_temp/info.json"
    
    elif path == "face-app-result":
        return "camera_temp/result.json"




def microphone_temp(path):
    if path == "microphone-info":
        return "microphone/info.json"
    
    elif path == "microphone-result":
        return "microphone/result.json"
