import requests
import platform

def ping_host(hostname: str) -> bool:
    try:
        # -n for Windows, -c for Linux/macOS.
        if platform.system().lower() == 'windows':
            param = '-n'
        else:
            param = '-c'
        command = ['ping', param, '1', hostname]
        result = subprocess.run(command, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode == 0:
            return True
        else:
            return False
    except Exception as e:
        return False