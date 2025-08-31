"""AIT_Steg method - Zero-width Unicode characters with dynamic key encryption."""

import hashlib
import time
from .base import StegoMethod


class AITStegMethod(StegoMethod):
    """AIT_Steg steganography method with dynamic keys."""

    # Zero-width Unicode characters for encoding
    ZERO_WIDTH_CHARS = [
        '\u200B',  # Zero Width Space
        '\u200C',  # Zero Width Non-Joiner
        '\u200D',  # Zero Width Joiner
        '\u2060',  # Word Joiner
        '\u2061',  # Function Application
        '\u2062',  # Invisible Times
        '\u2063',  # Invisible Separator
        '\uFEFF',  # Zero Width No-Break Space
    ]

    def _generate_dynamic_key(self, cover_text: str) -> str:
        """Generate a dynamic key from cover text content."""
        # Use content hash + timestamp for dynamic key
        content_hash = hashlib.sha256(cover_text.encode('utf-8')).hexdigest()[:16]
        time_component = str(int(time.time()) // 3600)  # Hour-based component
        return content_hash + time_component

    def _derive_key_from_content(self, cover_text: str, user_key: str = None) -> bytes:
        """Derive encryption key from content and user key."""
        if user_key:
            base_key = user_key
        else:
            base_key = self._generate_dynamic_key(cover_text)

        # Use PBKDF2-like key derivation
        return hashlib.pbkdf2_hmac('sha256',
                                   base_key.encode('utf-8'),
                                   cover_text.encode('utf-8')[:16],
                                   1000)[:16]

    def _encrypt_data(self, data: bytes, key: bytes) -> bytes:
        """Simple XOR encryption with key expansion."""
        encrypted = bytearray()
        key_len = len(key)

        for i, byte in enumerate(data):
            encrypted.append(byte ^ key[i % key_len])

        return bytes(encrypted)

    def _data_to_zero_width(self, data: bytes) -> str:
        """Convert data to zero-width characters."""
        result = ''
        for byte in data:
            # Use 3 characters per byte (8 bits = 3 chars with 8 possibilities each)
            char1 = self.ZERO_WIDTH_CHARS[byte >> 5]  # Top 3 bits
            char2 = self.ZERO_WIDTH_CHARS[(byte >> 2) & 0x07]  # Middle 3 bits
            char3 = self.ZERO_WIDTH_CHARS[byte & 0x03]  # Bottom 2 bits (pad to 3 bits)
            result += char1 + char2 + char3

        return result

    def _zero_width_to_data(self, zw_text: str) -> bytes:
        """Convert zero-width characters back to data."""
        # Extract zero-width characters
        zw_chars = [c for c in zw_text if c in self.ZERO_WIDTH_CHARS]

        if len(zw_chars) % 3 != 0:
            return b''

        data = bytearray()
        char_to_idx = {char: idx for idx, char in enumerate(self.ZERO_WIDTH_CHARS)}

        for i in range(0, len(zw_chars), 3):
            try:
                idx1 = char_to_idx[zw_chars[i]]
                idx2 = char_to_idx[zw_chars[i + 1]]
                idx3 = char_to_idx[zw_chars[i + 2]]

                # Reconstruct byte
                byte_val = (idx1 << 5) | (idx2 << 2) | (idx3 & 0x03)
                data.append(byte_val)
            except (KeyError, IndexError):
                return b''

        return bytes(data)

    def encode(self, cover_text: str, secret_data: str, key: str = None) -> str:
        """Encode secret data using AIT_Steg method."""
        if not secret_data:
            return cover_text

        # Convert secret to bytes
        secret_bytes = secret_data.encode('utf-8')

        # Derive encryption key
        enc_key = self._derive_key_from_content(cover_text, key)

        # Encrypt the data
        encrypted_data = self._encrypt_data(secret_bytes, enc_key)

        # Add length prefix
        data_length = len(encrypted_data)
        length_bytes = data_length.to_bytes(2, byteorder='big')

        # Convert to zero-width characters
        payload = length_bytes + encrypted_data
        zw_chars = self._data_to_zero_width(payload)

        # Insert zero-width characters throughout the text
        result = cover_text + zw_chars

        return result

    def decode(self, stego_text: str, key: str = None) -> str:
        """Decode secret data from AIT_Steg method."""
        # Extract data from zero-width characters
        payload = self._zero_width_to_data(stego_text)

        if len(payload) < 2:
            return ''

        # Read length
        data_length = int.from_bytes(payload[:2], byteorder='big')

        if data_length == 0 or len(payload) < 2 + data_length:
            return ''

        encrypted_data = payload[2:2 + data_length]

        # Derive key (try to extract cover text by removing zero-width chars)
        cover_text = ''.join(c for c in stego_text if c not in self.ZERO_WIDTH_CHARS)

        # Try with provided key first
        if key:
            enc_key = self._derive_key_from_content(cover_text, key)
        else:
            # Try dynamic key generation, but raise exception if it fails
            enc_key = self._derive_key_from_content(cover_text, None)

        # Decrypt
        decrypted_data = self._encrypt_data(encrypted_data, enc_key)  # XOR is symmetric

        try:
            decoded = decrypted_data.decode('utf-8')
            # Check if decoded text makes sense (basic validation)
            if not key and len([c for c in decoded if ord(c) > 127 or ord(c) < 32]) > len(decoded) * 0.3:
                # Too many non-printable characters, likely wrong key
                raise ValueError("Decoding failed - incorrect key or corrupted data")
            return decoded
        except UnicodeDecodeError:
            if not key:
                raise ValueError("Decoding failed - key required or corrupted data")
            return ''
