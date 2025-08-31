"""4spach method - Four invisible Unicode characters for binary encoding."""

from .base import StegoMethod


class FourSpachMethod(StegoMethod):
    """4spach steganography method using invisible Unicode characters."""

    # Four invisible Unicode characters for binary encoding (00, 01, 10, 11)
    UNICODE_CHARS = {
        '00': '\u200B',  # Zero Width Space
        '01': '\u200C',  # Zero Width Non-Joiner
        '10': '\u200D',  # Zero Width Joiner
        '11': '\uFEFF',  # Zero Width No-Break Space
    }

    def encode(self, cover_text: str, secret_data: str, key: str = None) -> str:
        """Encode secret data using 4spach method."""
        if not secret_data:
            return cover_text

        # Convert secret to binary (handle Unicode properly)
        secret_bytes = secret_data.encode('utf-8')

        # Add length prefix (16-bit length allows up to 65535 bytes)
        data_length = len(secret_bytes)
        length_binary = format(data_length, '016b')

        # Combine length and data
        binary = length_binary + ''.join(format(byte, '08b') for byte in secret_bytes)

        # Split into 2-bit chunks and convert to Unicode
        encoded_chars = ''
        for i in range(0, len(binary), 2):
            chunk = binary[i:i+2].ljust(2, '0')  # Pad if needed
            encoded_chars += self.UNICODE_CHARS[chunk]

        # Insert into cover text
        return cover_text + encoded_chars

    def decode(self, stego_text: str, key: str = None) -> str:
        """Decode secret data from 4spach method."""
        # Create reverse mapping
        unicode_to_binary = {v: k for k, v in self.UNICODE_CHARS.items()}

        # Extract binary from Unicode characters (most recent ones)
        binary = ''
        for char in reversed(stego_text):  # Process from end to get most recent encoding
            if char in unicode_to_binary:
                binary = unicode_to_binary[char] + binary

        if not binary or len(binary) < 16:  # Need at least length prefix
            return ''

        # Read length prefix (first 16 bits)
        length_binary = binary[:16]
        data_length = int(length_binary, 2)

        if data_length == 0:
            return ''

        # Extract data based on length
        data_bits_needed = data_length * 8
        total_bits_needed = 16 + data_bits_needed

        if len(binary) < total_bits_needed:
            return ''

        # Extract just the data we need (most recent encoding)
        data_binary = binary[16:total_bits_needed]

        # Convert binary to bytes then decode as UTF-8
        secret_bytes = bytearray()
        for i in range(0, len(data_binary), 8):
            if i + 8 <= len(data_binary):
                byte = data_binary[i:i+8]
                secret_bytes.append(int(byte, 2))

        try:
            return secret_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return ''
