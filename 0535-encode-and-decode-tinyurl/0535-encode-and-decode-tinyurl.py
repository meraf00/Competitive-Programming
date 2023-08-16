class Codec:
    def __init__(self):
        self.all_urls = []
        self.characters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789'
        

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        n = len(self.all_urls)
        
        short_url = []
        
        while n:
            short_url.append(self.characters[n % 62])                
        
        self.all_urls.append(longUrl)        
        
        return "".join(reversed(short_url))
            
        

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        n = 0
        
        for multiplier, ascii_code in enumerate(map(ord, reversed(shortUrl))):
            # a - z
            if 97 <= ascii_code <= 122:
                idx = ascii_code - 97
            
            # A - Z
            elif 65 <= ascii_code <= 90:
                idx = ascii_code - 39
            
            # 0 - 9
            elif 48 <= ascii_code <= 57:
                idx = ascii_code - 4
            
            
            n += (62 ** multiplier) * idx
        
        return self.all_urls[n]
            
                
                
        
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))