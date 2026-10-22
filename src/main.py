import sys
import run

if len(sys.argv) < 2:
    print("Usage: nyxium <file.nyx>")
    sys.exit(0)

filename = sys.argv[1]

if not filename.endswith(".nyx"):
    print("Error: Nyxium file not found")
    sys.exit()

with open(filename, "r") as file:
    code = file.read()

run.run(code)