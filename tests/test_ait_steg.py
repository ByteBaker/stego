"""Tests for AIT_Steg steganography method."""

import pytest
from stego.methods.ait_steg import AITStegMethod


class TestAITStegMethod:
    """Test cases for AIT_Steg method - will fail until implemented."""

    def test_basic_encode_decode_with_key(self, sample_cover_text, sample_secret):
        """Test basic encoding and decoding with encryption key."""
        method = AITStegMethod()
        key = "test_password_123"

        # Encode
        encoded = method.encode(sample_cover_text, sample_secret, key)
        assert encoded != sample_cover_text
        assert len(encoded) >= len(sample_cover_text)

        # Decode
        decoded = method.decode(encoded, key)
        assert decoded == sample_secret

    def test_decode_without_key_fails(self, sample_cover_text, sample_secret):
        """Test that decoding without key fails or returns wrong result."""
        method = AITStegMethod()
        key = "correct_password"

        encoded = method.encode(sample_cover_text, sample_secret, key)

        # Should fail or return incorrect result without key
        with pytest.raises(Exception):
            method.decode(encoded, None)

    def test_wrong_key_fails(self, sample_cover_text, sample_secret):
        """Test that wrong key produces wrong result."""
        method = AITStegMethod()
        correct_key = "correct_password"
        wrong_key = "wrong_password"

        encoded = method.encode(sample_cover_text, sample_secret, correct_key)
        decoded_wrong = method.decode(encoded, wrong_key)

        # Should not match original secret
        assert decoded_wrong != sample_secret

    def test_dynamic_key_generation(self, sample_cover_text, sample_secret):
        """Test that method can generate dynamic keys based on content or time."""
        method = AITStegMethod()

        # Test with no explicit key (should use dynamic key generation)
        encoded = method.encode(sample_cover_text, sample_secret)
        decoded = method.decode(encoded)
        assert decoded == sample_secret

    def test_zero_width_characters(self, sample_cover_text, sample_secret):
        """Test that encoded text contains zero-width Unicode characters."""
        method = AITStegMethod()
        key = "test_key"

        encoded = method.encode(sample_cover_text, sample_secret, key)

        # Should contain zero-width characters used by AIT_Steg
        zero_width_chars = ['\u200B', '\u200C', '\u200D', '\u2060', '\u2061', '\u2062', '\u2063']
        has_zero_width = any(char in encoded for char in zero_width_chars)
        assert has_zero_width

    def test_encryption_integrity(self, sample_cover_text, sample_secret):
        """Test that the same input produces consistent output with same key."""
        method = AITStegMethod()
        key = "consistent_key"

        encoded1 = method.encode(sample_cover_text, sample_secret, key)
        encoded2 = method.encode(sample_cover_text, sample_secret, key)

        # With same key, should be able to decode both
        decoded1 = method.decode(encoded1, key)
        decoded2 = method.decode(encoded2, key)

        assert decoded1 == sample_secret
        assert decoded2 == sample_secret

    def test_key_derivation_from_content(self, sample_cover_text, sample_secret):
        """Test key derivation from cover text content."""
        method = AITStegMethod()

        # Should be able to derive key from content itself
        encoded = method.encode(sample_cover_text, sample_secret)
        decoded = method.decode(encoded)
        assert decoded == sample_secret
