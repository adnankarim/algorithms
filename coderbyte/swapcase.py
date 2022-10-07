# Swap Case
# Hide Question
# Have the function SwapCase(str) take the str parameter and swap the case of each character. For example: if str is "Hello World" the output should be hELLO wORLD. Let numbers and symbols stay the way they are.

# Once your function is working, take the final output string and replace all characters that appear in your ChallengeToken with --[CHAR]--.

# Your ChallengeToken: db2nrl6p9a

def tokenize(string,token="db2nrl6p9a"):
  out=""
  for i in string:
    if i in token:
      out+="--"+i+"--"
    else:
       out+=i
  return out
def StringChallenge(strParam):

  # code goes here
  out=""
  for i in strParam:
    if i.isupper() and i.isalpha():
      out+=i.lower()
    elif i.islower() and i.isalpha():
      out+=i.upper()
    else:
      out+=i
  
  return tokenize(out)

# keep this function call here 
print StringChallenge(raw_input())