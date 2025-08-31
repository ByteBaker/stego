"""Pytest configuration and fixtures."""

import pytest
import tempfile
import os


@pytest.fixture
def temp_dir():
    """Create a temporary directory for test files."""
    with tempfile.TemporaryDirectory() as temp_dir:
        yield temp_dir


@pytest.fixture
def sample_cover_text():
    """Sample cover text for testing."""
    return "Hello World! This is a sample text for steganography testing."


@pytest.fixture
def sample_secret():
    """Sample secret data for testing."""
    return "This is my secret message!"


@pytest.fixture
def sample_files(temp_dir, sample_cover_text, sample_secret):
    """Create sample files for testing."""
    cover_file = os.path.join(temp_dir, "cover.txt")
    secret_file = os.path.join(temp_dir, "secret.txt")
    
    with open(cover_file, 'w', encoding='utf-8') as f:
        f.write(sample_cover_text)
    
    with open(secret_file, 'w', encoding='utf-8') as f:
        f.write(sample_secret)
    
    return {
        'cover': cover_file,
        'secret': secret_file,
        'output': os.path.join(temp_dir, "output.txt"),
        'decoded': os.path.join(temp_dir, "decoded.txt")
    }