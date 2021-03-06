def setup():
    print(multiline_pane())

def multiline_pane(title='', default=''):
    from javax.swing import JOptionPane, JScrollPane, JTextArea
    ta = JTextArea(20, 20)
    ta.setText(default)
    result = JOptionPane.showConfirmDialog(None,
                                           JScrollPane(ta),
                                           title,
                                           JOptionPane.OK_CANCEL_OPTION,
                                           JOptionPane.PLAIN_MESSAGE,
                                           # JOptionPane.QUESTION_MESSAGE
                                           )
    if result == JOptionPane.OK_OPTION:
        return ta.getText()
    else: 
        return default
