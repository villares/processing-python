from javax.swing import JOptionPane


def setup():
    result = yes_no_pane("oi?", "tudo bem?")
    if result == JOptionPane.YES_OPTION:
        print("Yes")
    elif result == JOptionPane.NO_OPTION:
        print("No")
    else:
        print(result)


def yes_no_pane(title, message):
    from javax.swing import JOptionPane
    return JOptionPane.showConfirmDialog(None,
                                         message,
                                         title,
                                         JOptionPane.YES_NO_OPTION,
                                         # JOptionPane.QUESTION_MESSAGE, #
                                         # default
                                         JOptionPane.PLAIN_MESSAGE  # No icon
                                         )


"""
messageType - Defines the style of the message.
    # 2:OK/Cancel 0:Yes/No  1:Y/N/Cancel -1:OK
    The Look and Feel manager may lay out the dialog differently
    depending on this value, and will often provide a default icon.
    The possible values are:
        JOptionPane.ERROR_MESSAGE
        JOptionPane.INFORMATION_MESSAGE
        JOptionPane.WARNING_MESSAGE
        JOptionPane.QUESTION_MESSAGE # question mark (se não puser nada vai este)
        JOptionPane.PLAIN_MESSAGE  # No icon
        optionType - Defines the set of option buttons that appear at the bottom of the dialog box:
        JOptionPane.DEFAULT_OPTION
        JOptionPane.YES_NO_OPTION
        JOptionPane.YES_NO_CANCEL_OPTION
        JOptionPane.OK_CANCEL_OPTION
    Results:
        JOptionPane.YES_OPTION
        JOptionPane.NO_OPTION
        JOptionPane.CANCEL_OPTION
        JOptionPane.OK_OPTION
        JOptionPane.CLOSED_OPTION
"""
