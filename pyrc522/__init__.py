__version__ = '0.1.0'

try:
    from .rfid import RFID
except RuntimeError:
    print("Must be used on Raspberry Pi")
