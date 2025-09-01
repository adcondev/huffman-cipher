# Huffman Cipher 🔐

A symmetric encryption system that combines Huffman coding for compression with RSA cipher for security. Achieve both data compression and encryption in a single pass.

## Overview

Huffman Cipher provides:
- **Compression**: Via Huffman coding algorithm
- **Encryption**: Using RSA cipher with key expansion
- **Efficiency**: Single-pass compression and encryption
- **Security**: Key-based symmetric encryption

## Features

- 📉 **Compression Ratio**: Average 40-60% size reduction
- 🔑 **Key Management**: Secure key generation and expansion
- 🔄 **Bidirectional**: Encrypt/decrypt and compress/decompress
- 📊 **Statistics**: Compression ratio and entropy analysis
- 🎯 **File Support**: Works with text and binary files
- ⚡ **Performance**: Optimized tree traversal

## Algorithm Details

### Encryption Process
1. Build Huffman tree from input
2. Generate Huffman codes
3. Encode data using Huffman codes
4. Apply RSA cipher

### Decryption Process
1. Extract Huffman tree
2. Apply RSA decipher
3. Decode using Huffman tree
4. Reconstruct original data

## Security Considerations

- Use strong, random keys
- Key length should be ≥ 128 bits
- Not recommended for highly sensitive data
- Best suited for moderate security needs with compression

## License

MIT License
