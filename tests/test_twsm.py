"""Tests for TWSM steganography method."""

import pytest
from stego.methods.twsm import TWSMMethod


class TestTWSMMethod:
    """Test cases for TWSM method - will fail until implemented."""
    
    def test_basic_encode_decode(self, sample_cover_text, sample_secret):
        """Test basic text formatting steganography."""
        method = TWSMMethod()
        
        # Encode
        encoded = method.encode(sample_cover_text, sample_secret)
        assert encoded != sample_cover_text
        
        # Should contain formatting markers
        has_formatting = any(marker in encoded for marker in ['**', '*', '_', '~~', '__'])
        assert has_formatting
        
        # Decode
        decoded = method.decode(encoded)
        assert decoded == sample_secret
    
    def test_bold_formatting_patterns(self, sample_cover_text, sample_secret):
        """Test that bold formatting is used for encoding."""
        method = TWSMMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should contain bold markers
        assert '**' in encoded or '*' in encoded
    
    def test_italic_formatting_patterns(self, sample_cover_text, sample_secret):
        """Test that italic formatting is used for encoding."""
        method = TWSMMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should contain italic markers
        assert '_' in encoded
    
    def test_cross_platform_compatibility(self, sample_cover_text, sample_secret):
        """Test that formatting works across different platforms."""
        method = TWSMMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should use formats compatible with multiple chat apps
        compatible_formats = ['**', '*', '_', '__']
        uses_compatible = any(fmt in encoded for fmt in compatible_formats)
        assert uses_compatible
    
    def test_preserve_readability(self, sample_cover_text, sample_secret):
        """Test that formatted text remains readable."""
        method = TWSMMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should still contain original cover text words
        cover_words = sample_cover_text.split()
        for word in cover_words[:3]:  # Check first few words
            # Word should appear in some form in encoded text
            assert any(word.lower() in part.lower() for part in encoded.split())
    
    def test_binary_encoding_via_formatting(self, sample_cover_text, sample_secret):
        """Test that formatting patterns encode binary data."""
        method = TWSMMethod()
        
        # Test with simple secret to verify binary encoding
        simple_secret = "A"  # Single character
        encoded = method.encode(sample_cover_text, simple_secret)
        
        # Should be decodable
        decoded = method.decode(encoded)
        assert decoded == simple_secret
    
    def test_nested_formatting_support(self, sample_cover_text, sample_secret):
        """Test support for nested formatting (bold + italic)."""
        method = TWSMMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Might contain nested formatting like ***text***
        # This is implementation-dependent but should be tested
        decoded = method.decode(encoded)
        assert decoded == sample_secret
    
    def test_whatsapp_telegram_compatibility(self, sample_cover_text, sample_secret):
        """Test formatting that works in WhatsApp, Telegram, Discord."""
        method = TWSMMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should use commonly supported formats
        # WhatsApp: *bold*, _italic_
        # Telegram: **bold**, __italic__
        # Discord: **bold**, *italic*
        common_formats = ['*', '**', '_', '__']
        uses_common = any(fmt in encoded for fmt in common_formats)
        assert uses_common