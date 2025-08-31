#!/bin/bash

# Steganography Toolkit - CLI Examples
# ====================================
# This script demonstrates all CLI commands for the steganography toolkit

echo "🔐 STEGANOGRAPHY TOOLKIT - CLI EXAMPLES"
echo "========================================"

# Check if files exist
if [ ! -f "cover_text.txt" ] || [ ! -f "secret_message.txt" ]; then
    echo "❌ Error: cover_text.txt or secret_message.txt not found"
    echo "Make sure you're in the examples directory with the required files."
    exit 1
fi

echo "📖 Using cover_text.txt and secret_message.txt"
echo ""

# 4spach method
echo "🔸 4SPACH METHOD - Invisible Unicode"
echo "-----------------------------------"
echo "Encoding with 4spach method..."
stego 4spach encode --cover cover_text.txt --data secret_message.txt --output 4spach_result.txt

if [ $? -eq 0 ]; then
    echo "✅ Encoding successful!"
    echo "Decoding to verify..."
    stego 4spach decode --input 4spach_result.txt --output 4spach_decoded.txt
    
    if [ $? -eq 0 ]; then
        echo "✅ Decoding successful!"
        echo "Original secret vs decoded:"
        echo "Original: $(cat secret_message.txt | head -c 50)..."
        echo "Decoded:  $(cat 4spach_decoded.txt | head -c 50)..."
    else
        echo "❌ Decoding failed"
    fi
else
    echo "❌ Encoding failed"
fi
echo ""

# AIT_Steg method  
echo "🔐 AIT_STEG METHOD - Encrypted Zero-Width"
echo "-----------------------------------------"
echo "Encoding with AIT_Steg method (with password)..."
stego ait-steg encode --cover cover_text.txt --data secret_message.txt --key "MyPassword123" --output ait_steg_result.txt

if [ $? -eq 0 ]; then
    echo "✅ Encoding successful!"
    echo "Decoding with correct password..."
    stego ait-steg decode --input ait_steg_result.txt --key "MyPassword123" --output ait_steg_decoded.txt
    
    if [ $? -eq 0 ]; then
        echo "✅ Decoding successful!"
        echo "Original secret vs decoded:"
        echo "Original: $(cat secret_message.txt | head -c 50)..."
        echo "Decoded:  $(cat ait_steg_decoded.txt | head -c 50)..."
    else
        echo "❌ Decoding failed"
    fi
    
    echo "Trying to decode with wrong password (should fail)..."
    stego ait-steg decode --input ait_steg_result.txt --key "WrongPassword" --output ait_steg_wrong.txt
    if [ $? -ne 0 ]; then
        echo "✅ Correctly failed with wrong password"
    else
        echo "⚠️  Should have failed with wrong password"
    fi
else
    echo "❌ Encoding failed"
fi
echo ""

# TWSM method
echo "📝 TWSM METHOD - Text Formatting"
echo "--------------------------------"
echo "Encoding with TWSM method..."
stego twsm encode --cover cover_text.txt --data secret_message.txt --output twsm_result.txt

if [ $? -eq 0 ]; then
    echo "✅ Encoding successful!"
    echo "Formatted text preview:"
    head -c 200 twsm_result.txt
    echo "..."
    echo ""
    echo "Decoding..."
    stego twsm decode --input twsm_result.txt --output twsm_decoded.txt
    
    if [ $? -eq 0 ]; then
        echo "✅ Decoding successful!"
        echo "Original secret vs decoded:"
        echo "Original: $(cat secret_message.txt | head -c 50)..."
        echo "Decoded:  $(cat twsm_decoded.txt | head -c 50)..."
    else
        echo "❌ Decoding failed"
    fi
else
    echo "❌ Encoding failed"
fi
echo ""

# Em_st method
echo "😀 EM_ST METHOD - Emoticon Encoding"
echo "-----------------------------------"
echo "Encoding with Em_st method..."
stego em-st encode --cover cover_text.txt --data secret_message.txt --output em_st_result.txt

if [ $? -eq 0 ]; then
    echo "✅ Encoding successful!"
    echo "Text with emoticons preview:"
    head -c 200 em_st_result.txt
    echo "..."
    echo ""
    echo "Decoding..."
    stego em-st decode --input em_st_result.txt --output em_st_decoded.txt
    
    if [ $? -eq 0 ]; then
        echo "✅ Decoding successful!"
        echo "Original secret vs decoded:"
        echo "Original: $(cat secret_message.txt | head -c 50)..."
        echo "Decoded:  $(cat em_st_decoded.txt | head -c 50)..."
    else
        echo "❌ Decoding failed"
    fi
else
    echo "❌ Encoding failed"
fi
echo ""

# Summary
echo "🎉 CLI EXAMPLES COMPLETED"
echo "========================="
echo "Generated files:"
ls -la *_result.txt *_decoded.txt 2>/dev/null | awk '{print "- " $9 " (" $5 " bytes)"}'

echo ""
echo "🔍 File size comparison:"
echo "Original cover text: $(wc -c < cover_text.txt) bytes"
echo "Original secret:     $(wc -c < secret_message.txt) bytes"
if [ -f "4spach_result.txt" ]; then
    echo "4spach encoded:      $(wc -c < 4spach_result.txt) bytes"
fi
if [ -f "ait_steg_result.txt" ]; then
    echo "AIT_Steg encoded:    $(wc -c < ait_steg_result.txt) bytes"
fi
if [ -f "twsm_result.txt" ]; then
    echo "TWSM encoded:        $(wc -c < twsm_result.txt) bytes"
fi
if [ -f "em_st_result.txt" ]; then
    echo "Em_st encoded:       $(wc -c < em_st_result.txt) bytes"
fi

echo ""
echo "💡 Try examining the encoded files - some changes are invisible!"
echo "💡 Use a hex editor to see the invisible Unicode characters in 4spach and AIT_Steg outputs."