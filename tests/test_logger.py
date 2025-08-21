import subprocess
import sys
import os

SCRIPT_PATH = os.path.join('..', 'UTILS - Logging', 'logger.py')

def test_script_runs():
    print('Testing if logger.py runs...')
    result = subprocess.run([sys.executable, SCRIPT_PATH], input=b'5\n', capture_output=True)
    assert result.returncode == 0
    print('logger.py runs successfully.')

if __name__ == '__main__':
    test_script_runs()
    print('Logger (Python) basic test passed.')
