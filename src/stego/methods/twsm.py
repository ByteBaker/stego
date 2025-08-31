"""TWSM method - Text formatting steganography using bold/italics/underline."""

from .base import StegoMethod


class TWSMMethod(StegoMethod):
    """TWSM steganography method using text formatting."""

    # Binary encoding using formatting patterns
    # Compatible with WhatsApp, Telegram, Discord
    BINARY_FORMATS = {
        '00': ('*', '*'),        # Single asterisk (italic in some platforms)
        '01': ('**', '**'),      # Double asterisk (bold)
        '10': ('_', '_'),        # Single underscore (italic)
        '11': ('__', '__'),      # Double underscore (bold italic)
    }

    def _words_to_format(self, cover_text: str, binary_string: str) -> str:
        """Apply formatting to words based on binary data."""
        words = cover_text.split()

        if not words:
            return cover_text

        formatted_text = []
        binary_index = 0
        word_index = 0

        # We need to encode all binary data, so repeat words if necessary

        while binary_index < len(binary_string):
            # Get current word (cycle through available words)
            current_word = words[word_index % len(words)]

            # Get 2-bit chunk
            chunk = binary_string[binary_index:binary_index + 2].ljust(2, '0')

            if chunk in self.BINARY_FORMATS:
                start_fmt, end_fmt = self.BINARY_FORMATS[chunk]
                formatted_word = f"{start_fmt}{current_word}{end_fmt}"
                formatted_text.append(formatted_word)
                binary_index += 2
            else:
                formatted_text.append(current_word)
                binary_index += 2  # Skip this chunk

            word_index += 1

        return ' '.join(formatted_text)

    def _extract_formatting_binary(self, stego_text: str) -> str:
        """Extract binary data from formatting patterns."""
        # Scan through text for formatting patterns
        words = stego_text.split()
        binary_string = ""

        # Sort patterns by length (longest first) to avoid wrong matches
        patterns = sorted(self.BINARY_FORMATS.items(), key=lambda x: len(x[1][0]), reverse=True)

        for word in words:
            # Check each format pattern in order (longest first)
            for binary_val, (start, end) in patterns:
                if word.startswith(start) and word.endswith(end) and len(word) > len(start + end):
                    binary_string += binary_val
                    break

        return binary_string

    def encode(self, cover_text: str, secret_data: str, key: str = None) -> str:
        """Encode secret data using TWSM method."""
        if not secret_data:
            return cover_text

        # Convert secret to bytes and then binary
        secret_bytes = secret_data.encode('utf-8')

        # Add length prefix (16-bit length)
        data_length = len(secret_bytes)
        length_binary = format(data_length, '016b')

        # Combine length and data
        binary_string = length_binary + ''.join(format(byte, '08b') for byte in secret_bytes)

        # Apply formatting to cover text based on binary data
        formatted_text = self._words_to_format(cover_text, binary_string)

        return formatted_text

    def decode(self, stego_text: str, key: str = None) -> str:
        """Decode secret data from TWSM method."""
        # Extract binary data from formatting
        binary_string = self._extract_formatting_binary(stego_text)

        if len(binary_string) < 16:  # Need at least length prefix
            return ''

        # Read length prefix
        length_binary = binary_string[:16]
        data_length = int(length_binary, 2)

        if data_length == 0:
            return ''

        # Extract data based on length
        data_bits_needed = data_length * 8
        total_bits_needed = 16 + data_bits_needed

        if len(binary_string) < total_bits_needed:
            return ''

        # Extract data binary
        data_binary = binary_string[16:total_bits_needed]

        # Convert binary to bytes
        secret_bytes = bytearray()
        for i in range(0, len(data_binary), 8):
            if i + 8 <= len(data_binary):
                byte_binary = data_binary[i:i + 8]
                secret_bytes.append(int(byte_binary, 2))

        try:
            return secret_bytes.decode('utf-8')
        except UnicodeDecodeError:
            return ''
