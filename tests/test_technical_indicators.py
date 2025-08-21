import subprocess
import sys
import os

SCRIPT_PATH = os.path.join('..', 'UTILS - Technical Indicators', 'technical_indicators.py')

def test_script_runs():
    print('Testing if technical_indicators.py runs...')
    result = subprocess.run([sys.executable, SCRIPT_PATH], input=b'7\n', capture_output=True)
    assert result.returncode == 0
    print('technical_indicators.py runs successfully.')

if __name__ == '__main__':
    test_script_runs()
    print('Technical Indicators Calculator basic test passed.')
