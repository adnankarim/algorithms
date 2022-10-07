
# Have the function DashInsert(str) insert dashes ('-') between each two odd numbers in str. For example: if str is 454793 the output should be 4547-9-3. Don't count zero as an odd number.

# Once your function is working, take the final output string and replace all characters that appear in your ChallengeToken with --[CHAR]--.



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
  for i in range(len(strParam)-1):
    if int(strParam[i])%2==1 and int(strParam[i+1])%2==1:
      out+=strParam[i]+"-"
    else:
       out+=strParam[i]

  return tokenize(out)

# keep this function call here 
print StringChallenge(raw_input())


