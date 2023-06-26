from PyQt5.QtWidgets import QApplication, QSystemTrayIcon, QMenu, QAction
from PyQt5.QtGui import QIcon

class TrayIcon(QSystemTrayIcon):
    def __init__(self, icon, parent=None):
        # Inherits from QSystemTrayIcon
        QSystemTrayIcon.__init__(self, icon, parent)

        # Creating a menu for the tray
        self.menu = QMenu()

        # Creating a QAction for the menu
        exitAction = QAction("Exit", self)
        
        # Connect the "Exit" option to the close function of the parent
        exitAction.triggered.connect(parent.quit) 

        # Adding actions to the menu
        self.menu.addAction(exitAction)

        # Setting context menu
        self.setContextMenu(self.menu)

# Main application
def main():
    app = QApplication([])
    
    # Adding an icon for the tray
    # QIcon accepts the path of .ico file.
    # Replace 'myicon.ico' with the path to your .ico file.
    trayIcon = TrayIcon(QIcon('python.png'), app)

    # Show the tray icon
    trayIcon.show()

    # Run the app
    app.exec_()

if __name__ == '__main__':
    main()
