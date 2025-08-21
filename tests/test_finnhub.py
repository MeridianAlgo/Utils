import subprocess
import sys
import os

SCRIPT_PATH = os.path.join('..', 'UTILS - Websocket Connection', 'finnhub.py')

def test_script_runs():
    print('Testing if finnhub.py runs...')
    result = subprocess.run([sys.executable, SCRIPT_PATH], capture_output=True)
    assert result.returncode == 0
    print('finnhub.py runs successfully.')

if __name__ == '__main__':
    test_script_runs()
    print('Finnhub Websocket basic test passed.')
