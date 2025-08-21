import subprocess
import sys
import os

SCRIPT_PATH = os.path.join('..', 'UTILS - Order Execution Simulator', 'order_execution_simulator.py')

def test_script_runs():
    print('Testing if order_execution_simulator.py runs...')
    result = subprocess.run([sys.executable, SCRIPT_PATH], input=b'6\n', capture_output=True)
    assert result.returncode == 0
    print('order_execution_simulator.py runs successfully.')

if __name__ == '__main__':
    test_script_runs()
    print('Order Execution Simulator basic test passed.')
