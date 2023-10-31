def palindromeIndex(s):
  def check(sub_str):
    return sub_str == sub_str[::-1]
  if s == s[::-1]:
    return -1
  for i in range(len(s) // 2):
    if s[i] != s[-(i + 1)]:
      if check(s[i + 1:len(s) - i]):
        return i
      elif check(s[i:len(s) - i - 1]):
        return len(s) - i - 1
  return -1
