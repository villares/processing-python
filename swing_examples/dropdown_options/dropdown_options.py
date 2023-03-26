def setup():
    size(400, 300)
    print(option_pane("Escolha uma opção",
                      "qual destes?",
                      ["A", "B", "C"],
                      "B")
          )


def option_pane(title, message, options, default=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(
        None,
        message,
        title,
        JOptionPane.QUESTION_MESSAGE,
        None,  # return on cancel
        options,
        default)  # must be in options, otherwise 1st is shown


def draw():
    pass
