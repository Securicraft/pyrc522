__version__ = '0.1.1'

try:
    from .rfid import RFID
except RuntimeError:
    print("Must be used on Raspberry Pi")
