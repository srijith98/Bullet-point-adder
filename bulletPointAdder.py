import pyperclip

print('Copy the lines which need bullet points to your clipboard.')
print('Enter 1 if done.')
flag=int(input())
if flag==1:
    text=pyperclip.paste()

    print('Enter 1 for numbering and 2 for bullet points:')
    bulltype=int(input())
    lines=text.split('\n')
    if bulltype==1:
        for i in range(len(lines)-1):
            lines[i]=str(i+1)+'. '+lines[i]
    elif bulltype==2:
        for i in range(len(lines)-1):
            lines[i]='* '+lines[i]
    else:
        print('Enter 1 or 2 only.')
        exit()
    text = '\n'.join(lines)

    pyperclip.copy(text)
    print("The bulleted lines are copied to the clipboard.")



