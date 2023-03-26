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
    """
    messageType - Defines the style of the message.
        # 2:OK/Cancel 0:Yes/No  1:Y/N/Cancel -1:OK
        The Look and Feel manager may lay out the dialog differently
        depending on this value, and will often provide a default icon.
        The possible values are:
            JOptionPane.ERROR_MESSAGE
            JOptionPane.INFORMATION_MESSAGE
            JOptionPane.WARNING_MESSAGE
            JOptionPane.QUESTION_MESSAGE # question mark (default)
            JOptionPane.PLAIN_MESSAGE  # No icon
    optionType - Defines the set of option buttons that appear at the bottom of the dialog box:
            JOptionPane.DEFAULT_OPTION (OK/0 only, but you can still close the window... -1)
            JOptionPane.YES_NO_OPTION
            JOptionPane.YES_NO_CANCEL_OPTION
            JOptionPane.OK_CANCEL_OPTION
    Returned results:
            0 JOptionPane.YES_OPTION
            1 JOptionPane.NO_OPTION
            2 JOptionPane.CANCEL_OPTION
            0 JOptionPane.OK_OPTION
           -1 JOptionPane.CLOSED_OPTION
    """
    from javax.swing import JOptionPane
    return JOptionPane.showConfirmDialog(None,
                                         message,
                                         title,
                                         JOptionPane.YES_NO_OPTION,
                                         # JOptionPane.QUESTION_MESSAGE,
                                         JOptionPane.PLAIN_MESSAGE  # No icon
                                         )



