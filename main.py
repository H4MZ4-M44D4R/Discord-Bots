import subprocess
import sys
import os

bots_dir = os.path.join(os.path.dirname(__file__), "bots")

files = [os.path.join(bots_dir, f) for f in os.listdir(bots_dir) if f.endswith(".py")]

procs = [subprocess.Popen([sys.executable, f]) for f in files]

for p in procs:
    p.wait()