"""Base class for steganography methods."""

from abc import ABC, abstractmethod


class StegoMethod(ABC):
    """Abstract base class for steganography methods."""

    @abstractmethod
    def encode(self, cover_text: str, secret_data: str, key: str = None) -> str:
        """Encode secret data into cover text."""
        pass

    @abstractmethod
    def decode(self, stego_text: str, key: str = None) -> str:
        """Decode secret data from stego text."""
        pass
