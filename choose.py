import sys,random
from PyQt5.QtWidgets import QWidget, QApplication, QPushButton, QLabel, QGridLayout
from PyQt5.QtGui import QIcon, QPixmap, QPalette, QBrush, QFont
from PyQt5.QtCore import Qt,QTimer
import pandas as pd


class MyEnter(QWidget):
    def __init__(self):
        super(MyEnter, self).__init__()
        self.name_list = pd.read_excel('./names.xlsx')
        self.initUI()

    def initUI(self):
        # 设置窗口的基本属性（窗口名,初始化大小）
        self.setWindowTitle('随机点名')
        self.resize(450, 300)

        # 添加按钮
        self.btn_start = QPushButton('开始')
        self.btn_stop = QPushButton('停止')

        # 添加标签
        self.label = QLabel('待开始')
        self.label.setAlignment(Qt.AlignCenter)
        self.label.setFont(QFont('微软雅黑',70))

        # 网格布局添加控件
        self.grid_layout = QGridLayout(self)
        self.grid_layout.addWidget(self.label,0,0,1,2)
        self.grid_layout.addWidget(self.btn_start,1,0)
        self.grid_layout.addWidget(self.btn_stop,1,1)
        
        # 设置触发函数
        self.btn_start.clicked.connect(self.start_event)
        self.btn_stop.clicked.connect(self.stop_event)

        # 显示
        self.show()

    def start_event(self):
        self.btn_start.setEnabled(False)
        self.btn_stop.setEnabled(True)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.setname)
        self.timer.start(100)
            
    
    def stop_event(self):
        if self.label.text() != '待开始':
            self.btn_start.setEnabled(True)
            self.btn_stop.setEnabled(False)
            self.timer.stop()

    def setname(self):
        name = self.name_list.at[random.randint(0, len(self.name_list) - 1),'姓名']
        self.label.setText(name)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ME = MyEnter()
    app.exec_()
