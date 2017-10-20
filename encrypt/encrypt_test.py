#!/home/python3.6.3/bin/python3
# Modified  2017 nanqinlang
#

#from __future__ import division, print_function, with_statement

import sys
sys.path.append("..")
from crypto import rc4_md5, openssl, sodium, table

import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '../'))

def run(func):
	try:
		func()
	except:
		pass

def run_n(func, name):
	try:
		func(name)
	except:
		pass

def main():
	print("\n""rc4_md5")
	rc4_md5.test()
	print("\n""aes-256-cfb")
	openssl.test_aes_256_cfb()
	print("\n""aes-128-cfb")
	openssl.test_aes_128_cfb()
	print("\n""bf-cfb")
	run(openssl.test_bf_cfb)
	print("\n""camellia-128-cfb")
	run_n(openssl.run_method, "camellia-128-cfb")
	print("\n""cast5-cfb")
	run_n(openssl.run_method, "cast5-cfb")
	print("\n""idea-cfb")
	run_n(openssl.run_method, "idea-cfb")
	print("\n""seed-cfb")
	run_n(openssl.run_method, "seed-cfb")
	print("\n""salsa20")
	run(sodium.test_salsa20)
	print("\n""chacha20")
	run(sodium.test_chacha20)

if __name__ == '__main__':
	main()

