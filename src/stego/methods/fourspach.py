"""4spach method - Four invisible Unicode characters for binary encoding."""

from .base import StegoMethod


class FourSpachMethod(StegoMethod):
    """4spach steganography method using invisible Unicode characters."""
    
    UNICODE_CHARS = {
        '00': '\u200B',  # Zero Width Space
        '01': '\u200C',  # Zero Width Non-Joiner  
        '10': '\u200D',  # Zero Width Joiner
        '11': '\uFEFF',  # Zero Width No-Break Space
    }
    
    def encode(self, cover_text: str, secret_data: str, key: str = None) -> str:
        """Encode secret data using 4spach method."""
        # Convert secret to binary
        binary = ''.join(format(ord(c), '08b') for c in secret_data)
        
        # Split into 2-bit chunks and convert to Unicode
        encoded = ''
        for i in range(0, len(binary), 2):
            chunk = binary[i:i+2].ljust(2, '0')
            encoded += self.UNICODE_CHARS[chunk]
        
        # Insert into cover text
        return cover_text + encoded
    
    def decode(self, stego_text: str, key: str = None) -> str:
        """Decode secret data from 4spach method."""
        # Extract Unicode characters
        unicode_to_binary = {v: k for k, v in self.UNICODE_CHARS.items()}
        binary = ''
        
        for char in stego_text:
            if char in unicode_to_binary:
                binary += unicode_to_binary[char]
        
        # Convert binary to text
        if len(binary) % 8 != 0:
            binary = binary[:-(len(binary) % 8)]
        
        secret = ''
        for i in range(0, len(binary), 8):
            if i + 8 <= len(binary):
                byte = binary[i:i+8]
                secret += chr(int(byte, 2))
        
        return secret