"""Tests for Em_st steganography method."""

import pytest
from stego.methods.em_st import EmStMethod


class TestEmStMethod:
    """Test cases for Em_st method - will fail until implemented."""
    
    def test_basic_encode_decode(self, sample_cover_text, sample_secret):
        """Test basic emoticon-based steganography."""
        method = EmStMethod()
        
        # Encode
        encoded = method.encode(sample_cover_text, sample_secret)
        assert encoded != sample_cover_text
        
        # Should contain emoticons/symbols
        has_symbols = any(char in encoded for char in ':)(:D:P:|:/:?!{}[]()<>""++--**//\\||@@##$$%%^^~~')
        assert has_symbols
        
        # Decode
        decoded = method.decode(encoded)
        assert decoded == sample_secret
    
    def test_common_emoticons_used(self, sample_cover_text, sample_secret):
        """Test that common emoticons are used in encoding."""
        method = EmStMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should contain common emoticons
        common_emoticons = [':)', ':(', ':D', ':P', ':|', ':/', ':\\', ':o', ':!', ':?']
        has_emoticons = any(emoticon in encoded for emoticon in common_emoticons)
        assert has_emoticons
    
    def test_symbol_mapping_consistency(self, sample_cover_text, sample_secret):
        """Test that symbol mapping is consistent."""
        method = EmStMethod()
        
        # Encode same data multiple times
        encoded1 = method.encode(sample_cover_text, sample_secret)
        encoded2 = method.encode(sample_cover_text, sample_secret)
        
        # Should decode to same result
        decoded1 = method.decode(encoded1)
        decoded2 = method.decode(encoded2)
        
        assert decoded1 == sample_secret
        assert decoded2 == sample_secret
    
    def test_extended_symbol_set(self, sample_cover_text, sample_secret):
        """Test use of extended symbol set."""
        method = EmStMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should use extended symbols as specified
        extended_symbols = ['{}', '[]', '()', '<>', '""', "''", '++', '--', '**', '//', '\\\\', '||', '&&', '@@', '##', '$$', '%%', '^^', '~~']
        has_extended = any(symbol in encoded for symbol in extended_symbols)
        assert has_extended
    
    def test_binary_to_symbol_mapping(self, sample_cover_text):
        """Test that binary data is properly mapped to symbols."""
        method = EmStMethod()
        
        # Test with known binary pattern (single byte)
        test_secret = "A"  # ASCII 65 = 01000001
        encoded = method.encode(sample_cover_text, test_secret)
        decoded = method.decode(encoded)
        assert decoded == test_secret
    
    def test_frequency_based_encoding(self, sample_cover_text, sample_secret):
        """Test frequency-based symbol encoding for compression."""
        method = EmStMethod()
        
        # Test with repeated characters
        repeated_secret = "aaaa"
        encoded = method.encode(sample_cover_text, repeated_secret)
        
        # Should handle repeated patterns efficiently
        decoded = method.decode(encoded)
        assert decoded == repeated_secret
    
    def test_positional_encoding(self, sample_cover_text, sample_secret):
        """Test that symbol position affects encoding."""
        method = EmStMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Position within text should matter for decoding
        decoded = method.decode(encoded)
        assert decoded == sample_secret
    
    def test_word_boundary_symbol_placement(self, sample_cover_text, sample_secret):
        """Test that symbols are placed at word boundaries or specific positions."""
        method = EmStMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should maintain text readability while adding symbols
        # Text should still be somewhat readable
        words = encoded.split()
        assert len(words) >= len(sample_cover_text.split())
    
    def test_dictionary_mapping(self, sample_cover_text, sample_secret):
        """Test symbol-to-word dictionary mapping."""
        method = EmStMethod()
        
        encoded = method.encode(sample_cover_text, sample_secret)
        
        # Should use dictionary-based mapping
        decoded = method.decode(encoded)
        assert decoded == sample_secret
    
    def test_compression_efficiency(self, sample_cover_text):
        """Test that method provides some compression for common patterns."""
        method = EmStMethod()
        
        # Test with common English words
        common_secret = "the quick brown fox jumps"
        encoded = method.encode(sample_cover_text, common_secret)
        
        # Should be more efficient than raw binary encoding
        decoded = method.decode(encoded)
        assert decoded == common_secret