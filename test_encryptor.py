from cryptography.fernet import Fernet
from encryptor import Encryptor

# Load the encryption key
with open("encryption_key.key", "rb") as key_file:
    key = key_file.read()

encryptor = Encryptor(key)

# Test cases for edge cases
test_cases = [
    {"input": "", "description": "Empty string"},
    {"input": "Hello, World!", "description": "Basic string"},
    {"input": "1234567890", "description": "Numeric string"},
    {"input": "Special characters: !@#$%^&*()_+-=[]{}|;':\",./<>?", "description": "Special characters"},
    {"input": "Multiline\nString\nWith\nNewlines", "description": "Multiline string"},
    {"input": "    ", "description": "Whitespace only"},
    {"input": "你好, 世界!", "description": "Non-ASCII (Chinese characters)"},
    {"input": "😊🚀🔥🌟", "description": "Emoji characters"},
]

# Run tests
for case in test_cases:
    original_text = case["input"]
    description = case["description"]

    try:
        # Encrypt the input
        encrypted_text = encryptor.encrypt(original_text)

        # Decrypt back to original
        decrypted_text = encryptor.decrypt(encrypted_text)

        # Verify
        assert original_text == decrypted_text, f"Decryption failed for {description}!"
        print(f"Test passed: {description}")

    except Exception as e:
        print(f"Test failed: {description} - Error: {e}")
