import subprocess
import sys
import os

SCRIPT_PATH = os.path.join('..', 'UTILS - Options Chain Simulator', 'options_chain_simulator.py')

def test_script_runs():
    print('Testing if options_chain_simulator.py runs...')
    result = subprocess.run([sys.executable, SCRIPT_PATH], input=b'5\n', capture_output=True)
    assert result.returncode == 0
    print('options_chain_simulator.py runs successfully.')

if __name__ == '__main__':
    test_script_runs()
    print('Options Chain Simulator basic test passed.')
