"""
Stego: Simple steganography toolkit with multiple encoding methods.

Available methods:
- 4spach: Four invisible Unicode characters for binary encoding
- ait_steg: Zero-width Unicode with dynamic keys
- twsm: Text formatting (bold/italic) encoding
- em_st: Emoticon-based encoding
"""

__version__ = "0.1.0"
__author__ = "ByteBaker"

from .methods.fourspach import FourSpachMethod
from .methods.ait_steg import AITStegMethod
from .methods.twsm import TWSMMethod
from .methods.em_st import EmStMethod

__all__ = ["FourSpachMethod", "AITStegMethod", "TWSMMethod", "EmStMethod"]
