from typing import List

class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        encoded = ""
        for s in strs:
            # Store length, a delimiter, and the string itself
            encoded += str(len(s)) + "#" + s
        return encoded

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        decoded = []
        i = 0
        while i < len(s):
            j = i
            # Find the delimiter to extract the length
            while s[j] != '#':
                j += 1
            length = int(s[i:j])        # Length of the next string
            i = j + 1                   # Skip the '#'
            j = i + length              # End of the actual string
            decoded.append(s[i:j])      # Extract the string
            i = j                       # Move to the next encoded segment
        return decoded