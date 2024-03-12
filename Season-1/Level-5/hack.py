# For this level check the CodeQL alerts produced by GitHub code scanning.

# Enable CodeQL [Text]: https://github.co/3rOmI2k
# Enable CodeQL [Video]: https://youtu.be/MdRvrbExaFk
# Learn more: https://codeql.github.com/

# Is it enough though for the code to be 100% secure? ;)

# Fixes
# "random" library is prone to psudo random number generation (predictable)
# salt should be unpredictable
# MD5 collision possible

# https://security.stackexchange.com/questions/4781/do-any-security-experts-recommend-bcrypt-for-password-storage
# NIST does not mention bcrypt, only PBKDF2

# rainbow attack not possible
# salt can be stored as plaintext alongside hash

# Missed information 
# secrets module more secure than random

import code as c
import unittest
class TestDatabase(unittest.TestCase):

    def test_1(self):
        rng = c.Random_generator()
        sha = c.SHA256_hasher()
        password = rng.generate_token()
        salt = rng.generate_salt()
        hash = sha.password_hash(password, salt)
        self.assertTrue(sha.password_verification(password, hash))

if __name__ == '__main__':
    unittest.main()