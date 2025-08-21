import subprocess
import sys
import os

SCRIPT_PATH = os.path.join('..', 'UTILS - AI Development', 'chatbot.py')

def test_script_runs():
    print('Testing if chatbot.py runs...')
    result = subprocess.run([sys.executable, SCRIPT_PATH], input=b'exit\n', capture_output=True)
    assert result.returncode == 0
    print('chatbot.py runs successfully.')

if __name__ == '__main__':
    test_script_runs()
    print('Chatbot (Python) basic test passed.')
