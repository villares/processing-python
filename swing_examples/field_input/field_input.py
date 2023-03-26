
def setup():
    answer = input('enter your name')
    if answer:
        print('hi ' + answer)
    elif answer == "":
        print("[empty]")
    else:
        print(answer)  # Canceled dialog will print None

def input(question='', suggestion=''):
    from javax.swing import JOptionPane
    result = JOptionPane.showInputDialog(None, question, suggestion,
                                       # JOptionPane.PLAIN_MESSAGE, # no icon
                                       )
    return str(result) if result is not None else None
