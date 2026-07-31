class Solution:

    def encode(self, strs: List[str]) -> str:
        encoded = [
            f"{x}\\u234" for x in strs 
        ]
        return "".join(encoded)

    def decode(self, s: str) -> List[str]:
        return s.split("\\u234")[:-1]
