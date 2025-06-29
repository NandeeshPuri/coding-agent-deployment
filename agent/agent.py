import os
import subprocess
import sys
import json
from context_manager import ContextManager

WORKSPACE = '/workspace'
OUTPUT_FILE = os.path.join(WORKSPACE, 'output.txt')
TASK = os.environ.get('TASK', '')

ctx = ContextManager()

def log_action(action, result):
    ctx.add({'action': action, 'result': result})

def run_shell(cmd):
    try:
        result = subprocess.check_output(cmd, shell=True, stderr=subprocess.STDOUT, cwd=WORKSPACE, timeout=60).decode()
    except Exception as e:
        result = str(e)
    log_action({'shell': cmd}, result)
    return result

def run_python(code):
    try:
        result = subprocess.check_output([sys.executable, '-c', code], stderr=subprocess.STDOUT, cwd=WORKSPACE, timeout=60).decode()
    except Exception as e:
        result = str(e)
    log_action({'python': code}, result)
    return result

def run_typescript(code):
    ts_file = os.path.join(WORKSPACE, 'temp.ts')
    with open(ts_file, 'w') as f:
        f.write(code)
    try:
        result = subprocess.check_output(['npx', 'ts-node', ts_file], stderr=subprocess.STDOUT, cwd=WORKSPACE, timeout=60).decode()
    except Exception as e:
        result = str(e)
    log_action({'typescript': code}, result)
    return result

def run_xdot(cmd):
    try:
        result = subprocess.check_output(['xdotool'] + cmd.split(), stderr=subprocess.STDOUT, timeout=30).decode()
    except Exception as e:
        result = str(e)
    log_action({'xdot': cmd}, result)
    return result

def run_filesystem(action, args):
    try:
        if action == 'write':
            with open(os.path.join(WORKSPACE, args['path']), 'w') as f:
                f.write(args['content'])
            result = 'written'
        elif action == 'read':
            with open(os.path.join(WORKSPACE, args['path'])) as f:
                result = f.read()
        elif action == 'delete':
            os.remove(os.path.join(WORKSPACE, args['path']))
            result = 'deleted'
        else:
            result = 'unknown action'
    except Exception as e:
        result = str(e)
    log_action({'filesystem': action, 'args': args}, result)
    return result

def main():
    # For demo, just echo the task and log it
    with open(OUTPUT_FILE, 'w') as f:
        f.write(f"Task: {TASK}\n")
        log_action('task', TASK)
        # Here you would parse TASK and call the appropriate runner
        f.write("Agent completed task. (Demo)\n")

if __name__ == '__main__':
    main() 