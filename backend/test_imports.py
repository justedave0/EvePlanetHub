#!/usr/bin/env python3

import sys
print("Python version:", sys.version)
print("Python path:")
for p in sys.path:
    print("  ", p)

try:
    import pydantic_settings
    print("pydantic_settings imported successfully")
    print("pydantic_settings version:", pydantic_settings.__version__)
except Exception as e:
    print("Failed to import pydantic_settings:", str(e))

try:
    from pydantic_settings import BaseSettings
    print("BaseSettings imported successfully")
except Exception as e:
    print("Failed to import BaseSettings:", str(e))
    
try:
    import pydantic
    print("pydantic imported successfully")  
    print("pydantic version:", pydantic.__version__)
except Exception as e:
    print("Failed to import pydantic:", str(e))

# Try the actual import from config.py 
try:
    print("\nTrying to import from config.py directly...")
    from config import settings
    print("Settings imported successfully")
except Exception as e:
    print("Failed to import from config.py:", str(e))
    import traceback
    traceback.print_exc()