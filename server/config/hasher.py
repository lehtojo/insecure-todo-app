from django.contrib.auth.hashers import BasePasswordHasher, mask_hash
from django.contrib.auth.hashers import BasePasswordHasher
from django.utils.translation import gettext_noop as _
from django.utils.encoding import force_bytes
import hashlib

class InsecurePasswordHasher(BasePasswordHasher):
    """
    Insecure MD5 password hashing without salt
    """
    algorithm = "insecure"
    library = hashlib

    def salt(self) -> str:
        return ""

    def decode(self, encoded):
        return {
            "algorithm": self.algorithm,
            "hash": encoded,
            "salt": None,
        }

    def harden_runtime(self, password, encoded):
        pass

    def safe_summary(self, encoded):
        decoded = self.decode(encoded)
        return {
            _("algorithm"): decoded["algorithm"],
            _("hash"): mask_hash(decoded["hash"], show=3),
        }

    def encode(self, password: str, salt: str):
        hash = self.library.md5(force_bytes(password)).hexdigest()
        return f"{self.algorithm}$${hash}"

    def verify(self, password: str, encoded: str) -> bool:
        return encoded == self.encode(password, "")