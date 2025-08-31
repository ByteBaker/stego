"""Tests for 4spach steganography method."""

from stego.methods.fourspach import FourSpachMethod


class TestFourSpachMethod:
    """Test cases for FourSpach method."""

    def test_basic_encode_decode(self, sample_cover_text, sample_secret):
        """Test basic encoding and decoding functionality."""
        method = FourSpachMethod()

        # Encode
        encoded = method.encode(sample_cover_text, sample_secret)
        assert encoded != sample_cover_text
        assert len(encoded) > len(sample_cover_text)

        # Decode
        decoded = method.decode(encoded)
        assert decoded == sample_secret

    def test_empty_secret(self, sample_cover_text):
        """Test encoding and decoding empty secret."""
        method = FourSpachMethod()

        encoded = method.encode(sample_cover_text, "")
        decoded = method.decode(encoded)
        assert decoded == ""

    def test_unicode_characters_present(self, sample_cover_text, sample_secret):
        """Test that encoded text contains invisible Unicode characters."""
        method = FourSpachMethod()

        encoded = method.encode(sample_cover_text, sample_secret)

        # Should contain at least one of the invisible characters
        unicode_chars = ['\u200B', '\u200C', '\u200D', '\uFEFF']
        has_unicode = any(char in encoded for char in unicode_chars)
        assert has_unicode

    def test_long_secret(self, sample_cover_text):
        """Test encoding and decoding longer secret text."""
        method = FourSpachMethod()
        long_secret = ("This is a much longer secret message that contains "
                       "multiple sentences and various characters! 123 @#$")

        encoded = method.encode(sample_cover_text, long_secret)
        decoded = method.decode(encoded)
        assert decoded == long_secret

    def test_special_characters(self, sample_cover_text):
        """Test encoding special characters and emojis."""
        method = FourSpachMethod()
        special_secret = "Hello 🌍! Special chars: αβγ ñ ü @#$%^&*()"

        encoded = method.encode(sample_cover_text, special_secret)
        decoded = method.decode(encoded)
        assert decoded == special_secret

    def test_multiple_encode_decode_cycles(self, sample_cover_text, sample_secret):
        """Test multiple encoding/decoding cycles."""
        method = FourSpachMethod()

        text = sample_cover_text
        for i in range(3):
            encoded = method.encode(text, sample_secret)
            decoded = method.decode(encoded)
            assert decoded == sample_secret
            text = encoded  # Use encoded text as new cover
