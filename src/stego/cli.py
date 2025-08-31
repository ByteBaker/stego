#!/usr/bin/env python3
"""
Stego CLI entry point
"""

import argparse
import sys
from .methods.fourspach import FourSpachMethod
from .methods.ait_steg import AITStegMethod  
from .methods.twsm import TWSMMethod
from .methods.em_st import EmStMethod


def create_parser():
    """Create argument parser for stego CLI."""
    parser = argparse.ArgumentParser(
        prog='stego',
        description='Advanced steganography toolkit'
    )
    
    subparsers = parser.add_subparsers(dest='method', help='Steganography method')
    
    # 4spach method
    fourspach_parser = subparsers.add_parser('4spach', help='Four invisible Unicode characters')
    fourspach_subs = fourspach_parser.add_subparsers(dest='action')
    
    encode_4spach = fourspach_subs.add_parser('encode', help='Encode data')
    encode_4spach.add_argument('--text', required=True, help='Cover text')
    encode_4spach.add_argument('--data', required=True, help='Secret data')
    encode_4spach.add_argument('--output', help='Output file')
    
    decode_4spach = fourspach_subs.add_parser('decode', help='Decode data')  
    decode_4spach.add_argument('--text', required=True, help='Stego text')
    decode_4spach.add_argument('--output', help='Output file')
    
    # AIT_Steg method
    ait_parser = subparsers.add_parser('ait-steg', help='Zero-width Unicode with dynamic keys')
    ait_subs = ait_parser.add_subparsers(dest='action')
    
    encode_ait = ait_subs.add_parser('encode', help='Encode data')
    encode_ait.add_argument('--text', required=True, help='Cover text')
    encode_ait.add_argument('--data', required=True, help='Secret data')
    encode_ait.add_argument('--key', help='Encryption key')
    encode_ait.add_argument('--output', help='Output file')
    
    decode_ait = ait_subs.add_parser('decode', help='Decode data')
    decode_ait.add_argument('--text', required=True, help='Stego text')
    decode_ait.add_argument('--key', help='Decryption key')
    decode_ait.add_argument('--output', help='Output file')
    
    # TWSM method  
    twsm_parser = subparsers.add_parser('twsm', help='Text formatting steganography')
    twsm_subs = twsm_parser.add_subparsers(dest='action')
    
    encode_twsm = twsm_subs.add_parser('encode', help='Encode data')
    encode_twsm.add_argument('--text', required=True, help='Cover text')
    encode_twsm.add_argument('--data', required=True, help='Secret data')
    encode_twsm.add_argument('--output', help='Output file')
    
    decode_twsm = twsm_subs.add_parser('decode', help='Decode data')
    decode_twsm.add_argument('--text', required=True, help='Stego text') 
    decode_twsm.add_argument('--output', help='Output file')
    
    # Em_st method
    emst_parser = subparsers.add_parser('em-st', help='Emoticon-based encoding')
    emst_subs = emst_parser.add_subparsers(dest='action')
    
    encode_emst = emst_subs.add_parser('encode', help='Encode data')
    encode_emst.add_argument('--text', required=True, help='Cover text')
    encode_emst.add_argument('--data', required=True, help='Secret data')
    encode_emst.add_argument('--output', help='Output file')
    
    decode_emst = emst_subs.add_parser('decode', help='Decode data')
    decode_emst.add_argument('--text', required=True, help='Stego text')
    decode_emst.add_argument('--output', help='Output file')
    
    return parser


def main():
    """Main CLI entry point."""
    parser = create_parser()
    args = parser.parse_args()
    
    if not args.method:
        parser.print_help()
        sys.exit(1)
        
    if not args.action:
        print(f"Error: No action specified for {args.method}")
        sys.exit(1)
    
    # Route to appropriate method
    try:
        if args.method == '4spach':
            method = FourSpachMethod()
        elif args.method == 'ait-steg':
            method = AITStegMethod()
        elif args.method == 'twsm':
            method = TWSMMethod()
        elif args.method == 'em-st':
            method = EmStMethod()
        else:
            print(f"Unknown method: {args.method}")
            sys.exit(1)
            
        # Execute action
        if args.action == 'encode':
            result = method.encode(args.text, args.data, getattr(args, 'key', None))
        elif args.action == 'decode':
            result = method.decode(args.text, getattr(args, 'key', None))
        else:
            print(f"Unknown action: {args.action}")
            sys.exit(1)
            
        # Output result
        if hasattr(args, 'output') and args.output:
            with open(args.output, 'w') as f:
                f.write(result)
            print(f"Result written to {args.output}")
        else:
            print(result)
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()