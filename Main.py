from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QDataWidgetMapper
from PyQt5.QtSql import *
from MainApp import Ui_MainWindow

import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.statusbar.showMessage('Copyright@2020 by:Marcusbai V0.9', 0)
        self.okb = QMessageBox()

        self.db = QSqlDatabase.addDatabase('QSQLITE')
        self.db.setDatabaseName('./data/tdm.db')
        self.db.open()

        self.model = QSqlTableModel(None,self.db)
        self.model.setTable('tdm')
        self.model.setEditStrategy(self.model.OnManualSubmit)
        self.model.select()
        '''#基础数据展示
        self.model_base=QSqlQueryModel()
        self.sqlstr="SELECT 供应商代码,供应商名称,车型,采购代码,零件总成件号,零件名称,工装报价_o,ED_T报价_o,工装报价_PDFIN,ED_T报价_PDFIN,工装沉没成本_PDFIN,ED_T沉没成本_PDFIN,是否需要审计,审计计划,整体状态 FROM tdm"
        self.model_base.setQuery(self.sqlstr)
        self.ui.tableView.setModel(self.model_base)
        #审计数据展示
        self.model_auditstatus=QSqlQueryModel()
        self.sqlstr_a="SELECT 供应商代码,供应商名称,车型,采购代码,零件总成件号,零件名称,审计员,TDC,估价工程师,采购员,审计时间,工装报价_审计,工装已确认金额,工装待澄清金额,工装审计差异,ED_T报价_审计,ED_T已确认金额,ED_T待澄清金额,ED_T审计差异,工装差异率,ED_T差异率,总差异率,是否审完,审计报告是否签署,审计报告签署时间,估价报告,实物验证报告是否签署,说明 FROM tdm"
        self.model_auditstatus.setQuery(self.sqlstr_a)
        self.ui.tableView_2.setModel(self.model_auditstatus)
        #差异数据展示
        self.model_difference=QSqlQueryModel()
        self.sqlstr_d="SELECT 供应商代码,供应商名称,车型,采购代码,零件总成件号,零件名称,沉没成本支付金额,沉没成本支付时间,沉没成本支付凭证号,差异扣款金额,扣款时间,扣款凭证号 FROM tdm"
        self.model_difference.setQuery(self.sqlstr_d)
        self.ui.tableView_3.setModel(self.model_difference)
        '''
        self.ui.tableView.setModel(self.model)
        for id in range(15,45):
            self.ui.tableView.setColumnHidden(int(id),True)

        self.ui.tableView_2.setModel(self.model)
        for id in range(6,15):
            self.ui.tableView_2.setColumnHidden(int(id),True)
        for ida in range(37,45):
             self.ui.tableView_2.setColumnHidden(int(ida),True)

        self.ui.tableView_3.setModel(self.model)
        for id in range(6,37):
            self.ui.tableView_3.setColumnHidden(int(id),True)

        self.ui.pushButton_query.clicked.connect(self.pushButton_query)
        self.ui.pushButton_update.clicked.connect(self.pushButton_update)
        self.ui.pushButton_insert.clicked.connect(self.pushButton_insert)
        self.ui.pushButton_del.clicked.connect(self.pushButton_del)
    
    def pushButton_query(self):
        str_text = str(self.ui.lineEdit.text())
        str_text =str_text.upper()
        if str_text =="" and self.ui.pushButton_query.text()=="查询":
            self.okb.about(self,'提示','请输入KC代码')
        elif str_text != "":
            self.model.setFilter(("供应商代码 = '%s'" % (str_text)))
            self.ui.statusbar.showMessage('查询到"%s"条记录' % (self.model.rowCount()), 0)
            self.ui.pushButton_query.setText("刷新")
            que = QSqlQuery(self.db)
            que.prepare("SELECT 供应商名称 FROM tdm WHERE 供应商代码=:Nm")
            que.bindValue(":Nm",str_text)
            que.exec()
            que.next()
            data = que.value('供应商名称')
            self.ui.lineEdit_2.setText(data)

        elif str_text =="" and self.ui.pushButton_query.text()=="刷新":
            self.ui.lineEdit.setText("")
            self.model.setFilter("")
            self.ui.statusbar.showMessage('查询到"%s"条记录' % (self.model.rowCount()), 0)
            self.ui.pushButton_query.setText("查询")
            self.ui.lineEdit_2.setText("")
    def pushButton_update(self):
        self.model.database().transaction()
        if (self.model.submitAll()):
            self.model.database().commit()
        else:
            self.model.database().rollback()
            self.okb.warning(self,'警告',('天啊出错了: "%s"')%(self.model.lastError().text()))
        #撤销model->revertAll();

    def pushButton_insert(self):
        rowNum=self.model.rowCount()
        rowNum=int(rowNum)
        self.model.insertRow(rowNum)
        self.model.submitAll()
    
    def pushButton_del(self):
        curIndex=self.ui.tableView.currentIndex()
        self.model.removeRow(curIndex.row())
        ok = self.okb.warning(self,"删除当前行","你确定删除当前行吗？",self.okb.Yes | self.okb.No)
        if ok == self.okb.No:
            self.model.revertAll()
        else:
            self.model.submitAll()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainw = MainWindow()
    mainw.show()
    sys.exit(app.exec_())