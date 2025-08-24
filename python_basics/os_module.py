import platform
import os

print("------------------OS DETAILS-----------------------")
print("OS Name:", os.name)   # 'posix' (Linux/Mac), 'nt' (Windows)
print("User:", os.getlogin())
print("CPU Count:", os.cpu_count())
print("Environment Variables:", os.environ)

print("------------------SYSTEM DETAILS-----------------------")
print("System:", platform.system())        # Windows / Linux / Darwin (Mac)
print("Node Name:", platform.node())       # Computer's network name
print("Release:", platform.release())      # OS release (e.g. '10', '5.15.0')
print("Version:", platform.version())      # Detailed version info
print("Machine:", platform.machine())      # x86_64 / AMD64 / arm64
print("Processor:", platform.processor())  # CPU type
print("Platform:", platform.platform())    # Full description
print("Python Version:", platform.python_version())
