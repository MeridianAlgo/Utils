import subprocess
import sys
import os

# Test Portfolio Tracker CLI by running as a subprocess
SCRIPT_PATH = os.path.join('..', 'UTILS - Portfolio Tracker', 'portfolio_tracker.py')

def test_script_runs():
    print('Testing if portfolio_tracker.py runs...')
    result = subprocess.run([sys.executable, SCRIPT_PATH], input=b'7\n', capture_output=True)
    assert result.returncode == 0
    print('portfolio_tracker.py runs successfully.')

if __name__ == '__main__':
    test_script_runs()
    print('Portfolio Tracker basic test passed.')
