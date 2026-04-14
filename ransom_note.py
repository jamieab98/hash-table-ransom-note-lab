def can_construct(ransomNote: str, magazine: str) -> bool:
    """
    Determines if ransomNote can be constructed using letters from magazine.
    Each letter in magazine can only be used once.

    Parameters:
        ransomNote (str): The target string to construct.
        magazine (str): The source string with available characters.

    Returns:
        bool: True if ransomNote can be constructed, False otherwise.
    """
    counts = {}
    for ch in magazine:
        counts[ch] = counts.get(ch, 0) + 1
        
    for l in ransomNote:
        if l not in counts:
            return False
        
        elif counts[l] == 0:
            return False
        
        else:
            counts[l] = counts.get(l) -1

    return True

    pass  # TODO: Implement this function

rNote = "a"
mag = "b"

print(can_construct(rNote, mag))