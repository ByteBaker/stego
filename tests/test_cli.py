"""Tests for CLI functionality."""

import subprocess
import os


class TestCLIIntegration:
    """Integration tests for the CLI interface."""

    def test_cli_help(self):
        """Test that CLI help works."""
        result = subprocess.run(['stego', '--help'], capture_output=True, text=True)
        assert result.returncode == 0
        assert 'steganography toolkit' in result.stdout.lower()
        assert '4spach' in result.stdout
        assert 'ait-steg' in result.stdout
        assert 'twsm' in result.stdout
        assert 'em-st' in result.stdout

    def test_4spach_help(self):
        """Test 4spach method help."""
        result = subprocess.run(['stego', '4spach', '--help'], capture_output=True, text=True)
        assert result.returncode == 0
        assert 'encode' in result.stdout
        assert 'decode' in result.stdout

    def test_4spach_encode_help(self):
        """Test 4spach encode help."""
        result = subprocess.run(['stego', '4spach', 'encode', '--help'], capture_output=True, text=True)
        assert result.returncode == 0
        assert '--cover' in result.stdout
        assert '--data' in result.stdout
        assert '--output' in result.stdout

    def test_4spach_full_workflow(self, sample_files):
        """Test complete 4spach encode/decode workflow via CLI."""
        # Encode
        encode_result = subprocess.run([
            'stego', '4spach', 'encode',
            '--cover', sample_files['cover'],
            '--data', sample_files['secret'],
            '--output', sample_files['output']
        ], capture_output=True, text=True)

        assert encode_result.returncode == 0
        assert os.path.exists(sample_files['output'])

        # Decode
        decode_result = subprocess.run([
            'stego', '4spach', 'decode',
            '--input', sample_files['output'],
            '--output', sample_files['decoded']
        ], capture_output=True, text=True)

        assert decode_result.returncode == 0
        assert os.path.exists(sample_files['decoded'])

        # Verify content
        with open(sample_files['decoded'], 'r', encoding='utf-8') as f:
            decoded_content = f.read()

        with open(sample_files['secret'], 'r', encoding='utf-8') as f:
            original_content = f.read()

        assert decoded_content == original_content

    def test_ait_steg_full_workflow(self, sample_files):
        """Test complete AIT_Steg encode/decode workflow via CLI."""
        # Encode
        encode_result = subprocess.run([
            'stego', 'ait-steg', 'encode',
            '--cover', sample_files['cover'],
            '--data', sample_files['secret'],
            '--key', 'test_key',
            '--output', sample_files['output']
        ], capture_output=True, text=True)

        assert encode_result.returncode == 0
        assert os.path.exists(sample_files['output'])

        # Decode
        decode_result = subprocess.run([
            'stego', 'ait-steg', 'decode',
            '--input', sample_files['output'],
            '--key', 'test_key',
            '--output', sample_files['decoded']
        ], capture_output=True, text=True)

        assert decode_result.returncode == 0
        assert os.path.exists(sample_files['decoded'])

        # Verify content
        with open(sample_files['decoded'], 'r', encoding='utf-8') as f:
            decoded_content = f.read()

        with open(sample_files['secret'], 'r', encoding='utf-8') as f:
            original_content = f.read()

        assert decoded_content == original_content

    def test_twsm_full_workflow(self, sample_files):
        """Test complete TWSM encode/decode workflow via CLI."""
        # Encode
        encode_result = subprocess.run([
            'stego', 'twsm', 'encode',
            '--cover', sample_files['cover'],
            '--data', sample_files['secret'],
            '--output', sample_files['output']
        ], capture_output=True, text=True)

        assert encode_result.returncode == 0
        assert os.path.exists(sample_files['output'])

        # Decode
        decode_result = subprocess.run([
            'stego', 'twsm', 'decode',
            '--input', sample_files['output'],
            '--output', sample_files['decoded']
        ], capture_output=True, text=True)

        assert decode_result.returncode == 0
        assert os.path.exists(sample_files['decoded'])

        # Verify content
        with open(sample_files['decoded'], 'r', encoding='utf-8') as f:
            decoded_content = f.read()

        with open(sample_files['secret'], 'r', encoding='utf-8') as f:
            original_content = f.read()

        assert decoded_content == original_content

    def test_em_st_full_workflow(self, sample_files):
        """Test complete Em_st encode/decode workflow via CLI."""
        # Encode
        encode_result = subprocess.run([
            'stego', 'em-st', 'encode',
            '--cover', sample_files['cover'],
            '--data', sample_files['secret'],
            '--output', sample_files['output']
        ], capture_output=True, text=True)

        assert encode_result.returncode == 0
        assert os.path.exists(sample_files['output'])

        # Decode
        decode_result = subprocess.run([
            'stego', 'em-st', 'decode',
            '--input', sample_files['output'],
            '--output', sample_files['decoded']
        ], capture_output=True, text=True)

        assert decode_result.returncode == 0
        assert os.path.exists(sample_files['decoded'])

        # Verify content
        with open(sample_files['decoded'], 'r', encoding='utf-8') as f:
            decoded_content = f.read()

        with open(sample_files['secret'], 'r', encoding='utf-8') as f:
            original_content = f.read()

        assert decoded_content == original_content

    def test_missing_arguments(self):
        """Test CLI error handling for missing arguments."""
        # No method specified
        result = subprocess.run(['stego'], capture_output=True, text=True)
        assert result.returncode != 0

        # No action specified
        result = subprocess.run(['stego', '4spach'], capture_output=True, text=True)
        assert result.returncode != 0

        # Missing required arguments
        result = subprocess.run(['stego', '4spach', 'encode'], capture_output=True, text=True)
        assert result.returncode != 0

    def test_nonexistent_files(self, temp_dir):
        """Test CLI behavior with nonexistent files."""
        nonexistent = os.path.join(temp_dir, "nonexistent.txt")
        output_file = os.path.join(temp_dir, "output.txt")

        result = subprocess.run([
            'stego', '4spach', 'encode',
            '--cover', nonexistent,
            '--data', nonexistent,
            '--output', output_file
        ], capture_output=True, text=True)

        assert result.returncode != 0
        assert ('error' in result.stderr.lower() or 'no such file' in result.stderr.lower() or
                'error' in result.stdout.lower() or 'no such file' in result.stdout.lower())

    def test_unicode_file_handling(self, temp_dir):
        """Test CLI handling of files with Unicode content."""
        # Create files with Unicode content
        cover_file = os.path.join(temp_dir, "unicode_cover.txt")
        secret_file = os.path.join(temp_dir, "unicode_secret.txt")
        output_file = os.path.join(temp_dir, "unicode_output.txt")
        decoded_file = os.path.join(temp_dir, "unicode_decoded.txt")

        unicode_cover = "Hello 🌍! This is Unicode text with émojis and spéciál characters ñ ü"
        unicode_secret = "Sécret messàge with 🔐 and spéciál chars ñóñé"

        with open(cover_file, 'w', encoding='utf-8') as f:
            f.write(unicode_cover)
        with open(secret_file, 'w', encoding='utf-8') as f:
            f.write(unicode_secret)

        # Test encode
        encode_result = subprocess.run([
            'stego', '4spach', 'encode',
            '--cover', cover_file,
            '--data', secret_file,
            '--output', output_file
        ], capture_output=True, text=True)

        assert encode_result.returncode == 0

        # Test decode
        decode_result = subprocess.run([
            'stego', '4spach', 'decode',
            '--input', output_file,
            '--output', decoded_file
        ], capture_output=True, text=True)

        assert decode_result.returncode == 0

        # Verify Unicode content preserved
        with open(decoded_file, 'r', encoding='utf-8') as f:
            decoded_content = f.read()

        assert decoded_content == unicode_secret
