from pathlib import Path
import pytest
from main import is_valid_url, create_directory, generate_qr_code

def test_is_valid_url_success():
    """Test that valid URLs pass validation."""
    assert is_valid_url("https://github.com/Chiraagrah") is True
    assert is_valid_url("https://example.com") is True

def test_is_valid_url_failure():
    """Test that invalid strings fail URL validation."""
    assert is_valid_url("not_a_url") is False
    assert is_valid_url("htp://invalid-url") is False

def test_create_directory(tmp_path):
    """Test that directory creation works correctly using pytest's tmp_path fixture."""
    test_dir = tmp_path / "qr_codes_test"
    create_directory(test_dir)
    assert test_dir.exists()
    assert test_dir.is_dir()

def test_generate_qr_code_success(tmp_path):
    """Test that a valid URL successfully generates and saves a QR code PNG file."""
    file_path = tmp_path / "test_code.png"
    generate_qr_code("https://example.com", file_path)
    
    assert file_path.exists()
    assert file_path.is_file()
    assert file_path.stat().st_size > 0  # Ensure the image file isn't empty

def test_generate_qr_code_invalid_url(tmp_path):
    """Test that an invalid URL returns early and does not create an image file."""
    file_path = tmp_path / "invalid_code.png"
    generate_qr_code("invalid-url-string", file_path)
    
    assert not file_path.exists()