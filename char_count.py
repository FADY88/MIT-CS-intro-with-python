def char_counts(s):
  """ s is a string of lowercase chars
  return a tuple where the first element is the
  number of vowels in s and the second element
  is the number of consonants in s"""
  vowels = "aeiou"
  v, c = 0, 0
  for ch in s:
    if ch in vowels:
      v += 1
    else:
      c += 1
  return (v, c)



print(char_counts("fady"))
