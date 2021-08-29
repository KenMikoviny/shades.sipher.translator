dict = {
  '╡': "a",
  "╢": "b",
  "╖": "c",
  '╕': "d",
  "Ξ": "e",
  "║": "f",
  '╗': "g",
  "╝": "h",
  "╘": "i",
  #'╡': "j",
  "╛": "k",
  "╞": "l",
  '╟': "m",  #not sure
  "╚": "n",
  "╔": "o",
  "╩": "p",
  #"╩": "q",
  "╠": "r",
  '═': "s",
  "╬": "t",
  "╧": "u",
  "╨": "v",
  "╫": "w",
  '╤': "x",
  "╥": "y",
  #"╢": "z",
  " ": " ",
}

query = "╫ ╝╡╬ ╗╔ Ξ ═ ╫╘ ╬ ╝ ╩ Ξ ╡

╚ ╧ ╬ ╢╧ ╬ ╬ Ξ╠ ╔╚ ╢╠ Ξ ╡╕"

output = []
for symbol in range(0, len(query)):
    if query[symbol] not in dict.keys() :
        output.append("_")
    else:
        output.append(dict.get(query[symbol]))

print(''.join(output))