import pyperclip

text=pyperclip.paste()

if text=='':
    print('Copy lines of texts which need bullet points to the clipboard before calling the program.')
    exit()

lines=text.split('\n')
for i in range(len(lines)):
    lines[i]='* '+lines[i]

text = '\n'.join(lines)

pyperclip.copy(text)
print("The bulleted lines are copied to the clipboard.")

