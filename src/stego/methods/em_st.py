"""Em_st method - Emoticon-based encoding system."""

from .base import StegoMethod


class EmStMethod(StegoMethod):
    """Em_st steganography method using emoticons."""

    # Symbol mapping for 4-bit encoding (16 symbols for 0-F)
    SYMBOL_MAP = {
        '0000': ':)',      # Happy
        '0001': ':(',      # Sad
        '0010': ':D',      # Very happy
        '0011': ':P',      # Tongue out
        '0100': ':|',      # Neutral
        '0101': ':/',      # Skeptical
        '0110': ':\\',     # Confused
        '0111': ':o',      # Surprised
        '1000': ':!',      # Exclamation
        '1001': ':?',      # Question
        '1010': '{}',      # Braces
        '1011': '[]',      # Brackets
        '1100': '()',      # Parentheses
        '1101': '<>',      # Angle brackets
        '1110': '++',      # Plus
        '1111': '--',      # Minus
    }

    # Extended symbols for additional patterns if needed
    EXTENDED_SYMBOLS = ['""', "''", '**', '//', '\\\\', '||', '&&',
                        '@@', '##', '$$', '%%', '^^', '~~']

    def _binary_to_symbols(self, binary_string: str) -> list:
        """Convert binary string to symbols."""
        symbols = []

        # Process in 4-bit chunks
        for i in range(0, len(binary_string), 4):
            chunk = binary_string[i:i + 4].ljust(4, '0')  # Pad if needed
            if chunk in self.SYMBOL_MAP:
                symbols.append(self.SYMBOL_MAP[chunk])

        return symbols

    def _symbols_to_binary(self, stego_text: str) -> str:
        """Extract symbols and convert back to binary."""
        # Create reverse mapping
        reverse_map = {v: k for k, v in self.SYMBOL_MAP.items()}

        # Find all symbols in text
        binary_string = ""

        # Sort symbols by length (longest first) to avoid wrong matches
        all_symbols = list(self.SYMBOL_MAP.values()) + self.EXTENDED_SYMBOLS
        symbols_sorted = sorted(set(all_symbols), key=len, reverse=True)

        # Extract symbols from text
        text_copy = stego_text
        positions = []

        for symbol in symbols_sorted:
            pos = 0
            while pos < len(text_copy):
                idx = text_copy.find(symbol, pos)
                if idx == -1:
                    break
                positions.append((idx, symbol))
                pos = idx + 1

        # Sort by position to maintain order
        positions.sort(key=lambda x: x[0])

        # Convert to binary
        for _, symbol in positions:
            if symbol in reverse_map:
                binary_string += reverse_map[symbol]

        return binary_string

    def _insert_symbols_in_text(self, cover_text: str, symbols: list) -> str:
        """Insert symbols into cover text at word boundaries."""
        words = cover_text.split()

        if not symbols:
            return cover_text

        result_words = []
        symbol_index = 0

        # Insert symbols between words and at the end
        for i, word in enumerate(words):
            result_words.append(word)

            # Add symbol after word if we have more symbols
            if symbol_index < len(symbols):
                result_words.append(symbols[symbol_index])
                symbol_index += 1

        # Add remaining symbols at the end
        while symbol_index < len(symbols):
            result_words.append(symbols[symbol_index])
            symbol_index += 1

        return ' '.join(result_words)

    def encode(self, cover_text: str, secret_data: str, key: str = None) -> str:
        """Encode secret data using Em_st method."""
        if not secret_data:
            return cover_text

        # Convert secret to bytes and then binary
        secret_bytes = secret_data.encode('utf-8')

        # Add length prefix (16-bit length)
        data_length = len(secret_bytes)
        length_binary = format(data_length, '016b')

        # Combine length and data
        binary_string = length_binary + ''.join(format(byte, '08b') for byte in secret_bytes)

        # Convert binary to symbols
        symbols = self._binary_to_symbols(binary_string)

        # Insert symbols into cover text
        encoded_text = self._insert_symbols_in_text(cover_text, symbols)

        return encoded_text

    def decode(self, stego_text: str, key: str = None) -> str:
        """Decode secret data from Em_st method."""
        # Extract binary data from symbols
        binary_string = self._symbols_to_binary(stego_text)

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
