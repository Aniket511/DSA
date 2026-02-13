class Solution:

    def encode(self, string_to_encode: list[str]) -> str:
        encoded_string = ""
        for word in string_to_encode:
            encoded_string +=  str(len(word)) + "@" + word
        return encoded_string

    def decode(self, string_to_decode: str) -> list[str]:
        decoded_string = []
        left = right = 0
        while right < len(string_to_decode):
            while string_to_decode[right] != "@":
                right += 1
            length = int(string_to_decode[left : right])
            left = right + 1
            right = left + length
            decoded_string.append(string_to_decode[left : right])
            left = right
        return decoded_string