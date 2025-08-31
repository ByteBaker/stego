"""TWSM method - Text formatting steganography using bold/italics/underline."""

from .base import StegoMethod


class TWSMMethod(StegoMethod):
    """TWSM steganography method using text formatting."""
    
    def encode(self, cover_text: str, secret_data: str, key: str = None) -> str:
        """Encode secret data using TWSM method."""
        # TODO: Implement TWSM encoding
        raise NotImplementedError("TWSM encoding not implemented yet")
    
    def decode(self, stego_text: str, key: str = None) -> str:
        """Decode secret data from TWSM method."""
        # TODO: Implement TWSM decoding
        raise NotImplementedError("TWSM decoding not implemented yet")