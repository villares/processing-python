
def setup():
  alert("Window title!", "Something weird happened!")

def alert(title, message):
    from javax.swing import JOptionPane
    return JOptionPane.showMessageDialog(None,
                                         message,
                                         title,
                                         JOptionPane.WARNING_MESSAGE,  # icon
                                         )    
