# Property of Frederick Pu 69
import setup

operaters = ['+','*', '/', '^']

def transToArray(s, i):
  out = []
  currentWord = ""
  while i < len(s):
    if s[i] in operaters:
      if (currentWord != ""):
        out.append(currentWord)
      out.append(s[i])
      currentWord = ""
    elif s[i] == "(":
      if (currentWord != ""):
        out.append(currentWord)
      t = transToArray(s, i + 1)
      out.append(t[0])
      currentWord = ""
      i = t[1]
    elif s[i] == ")":
      if (currentWord != ""):
        out.append(currentWord)
      return (out, i)
    else:
      currentWord += s[i]
    i += 1
  if (currentWord != ""):
        out.append(currentWord)
  return (out, i)

def arrayToLatex(A):
  out = ""
  i = 0
  while i < len(A):
    if i + 2 < len(A) and A[i + 1] == "/":
      out += "\\frac{" + arrayToLatex(A[i]) + "}{" + arrayToLatex(A[i + 2]) + "}"
      i += 3
    elif A[i] == "*":
      out += "\cdot "
      i+=1
    elif i + 2 < len(A) and A[i + 1] == "^":
      out += arrayToLatex(A[i]) + "^{" + arrayToLatex(A[i + 2]) + "}"
      i += 3
    else:
      if (isinstance(A[i], list)):
        out += "(" + arrayToLatex(A[i]) + ")"
      else:
        out += A[i]
      i+=1
  return out

@setup.client.command()
async def toLatex(ctx, *, expression=None):
  if expression:
    await ctx.send("$"+arrayToLatex(transToArray(expression, 0)[0])+"$")