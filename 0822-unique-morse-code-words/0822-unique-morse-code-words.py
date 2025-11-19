class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        MORSE = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        
        transformations = set()
        for word in words:
            transformation = []
            for char in word:
                transformation.append(MORSE[ord(char) - ord('a')])
            transformations.add("".join(transformation))
            
        return len(transformations)
        