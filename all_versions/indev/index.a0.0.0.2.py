# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\a0.0.0.2.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox,QInputDialog,QFileDialog
import sys,os,json,webbrowser,easygui
from qt_material import apply_stylesheet
namespace=""
class Ui_MainWindow(QMainWindow):
    def setupUi(self, MainWindow):
        self.version="a0.0.0.2"
        self.visual_version="a0.0.0.2d Theme by Qt_Material Theme Name: dark_blue"
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 625)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.baseSetting = QtWidgets.QGroupBox(self.centralwidget)
        self.baseSetting.setGeometry(QtCore.QRect(30, 60, 321, 261))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting.setFont(font)
        self.baseSetting.setObjectName("baseSetting")
        self.baseSetting_DatapackName = QtWidgets.QLabel(self.baseSetting)
        self.baseSetting_DatapackName.setGeometry(QtCore.QRect(10, 40, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_DatapackName.setFont(font)
        self.baseSetting_DatapackName.setObjectName("baseSetting_DatapackName")
        self.baseSetting_DatapackVersion = QtWidgets.QLabel(self.baseSetting)
        self.baseSetting_DatapackVersion.setGeometry(QtCore.QRect(10, 70, 61, 16))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_DatapackVersion.setFont(font)
        self.baseSetting_DatapackVersion.setObjectName("baseSetting_DatapackVersion")
        self.baseSetting_DatapackNameInput = QtWidgets.QLineEdit(self.baseSetting)
        self.baseSetting_DatapackNameInput.setGeometry(QtCore.QRect(80, 40, 211, 20))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_DatapackNameInput.setFont(font)
        self.baseSetting_DatapackNameInput.setObjectName("baseSetting_DatapackNameInput")
        self.baseSetting_DatapackVersionSelected = QtWidgets.QComboBox(self.baseSetting)
        self.baseSetting_DatapackVersionSelected.setGeometry(QtCore.QRect(80, 70, 211, 22))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_DatapackVersionSelected.setFont(font)
        self.baseSetting_DatapackVersionSelected.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.baseSetting_DatapackVersionSelected.setObjectName("baseSetting_DatapackVersionSelected")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackVersionSelected.addItem("")
        self.baseSetting_DatapackDescriptionText = QtWidgets.QLabel(self.baseSetting)
        self.baseSetting_DatapackDescriptionText.setGeometry(QtCore.QRect(10, 100, 171, 21))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_DatapackDescriptionText.setFont(font)
        self.baseSetting_DatapackDescriptionText.setObjectName("baseSetting_DatapackDescriptionText")
        self.baseSetting_FormatCodeWikiLinkButton = QtWidgets.QPushButton(self.baseSetting)
        self.baseSetting_FormatCodeWikiLinkButton.setGeometry(QtCore.QRect(190, 100, 111, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_FormatCodeWikiLinkButton.setFont(font)
        self.baseSetting_FormatCodeWikiLinkButton.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.baseSetting_FormatCodeWikiLinkButton.setObjectName("baseSetting_FormatCodeWikiLinkButton")
        self.baseSetting_DatapackDescriptionInput = QtWidgets.QTextEdit(self.baseSetting)
        self.baseSetting_DatapackDescriptionInput.setGeometry(QtCore.QRect(10, 130, 291, 91))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_DatapackDescriptionInput.setFont(font)
        self.baseSetting_DatapackDescriptionInput.setObjectName("baseSetting_DatapackDescriptionInput")
        self.baseSetting_SaveButton = QtWidgets.QPushButton(self.baseSetting)
        self.baseSetting_SaveButton.setGeometry(QtCore.QRect(120, 230, 75, 23))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        self.baseSetting_SaveButton.setFont(font)
        self.baseSetting_SaveButton.setObjectName("baseSetting_SaveButton")
        self.title = QtWidgets.QLabel(self.centralwidget)
        self.title.setGeometry(QtCore.QRect(200, 10, 480, 31))
        font = QtGui.QFont()
        font.setFamily("微软雅黑")
        font.setPointSize(22)
        self.title.setFont(font)
        self.title.setObjectName("title")
        self.vesion_info = QtWidgets.QLabel(self.centralwidget)
        self.vesion_info.setGeometry(QtCore.QRect(10, 530, 800, 16))
        self.vesion_info.setObjectName("vesion_info")
        self.recipes_Frame = QtWidgets.QGroupBox(self.centralwidget)
        self.recipes_Frame.setGeometry(QtCore.QRect(370, 60, 500, 261))
        self.recipes_Frame.setObjectName("recipes_Frame")
        self.recipes_ListView = QtWidgets.QListView(self.recipes_Frame)
        self.recipes_ListView.setGeometry(QtCore.QRect(20, 33, 161, 221))
        self.recipes_ListView.setObjectName("recipes_ListView")
        self.recipes_TypeSelected = QtWidgets.QTabWidget(self.recipes_Frame)
        self.recipes_TypeSelected.setGeometry(QtCore.QRect(190, 20, 281, 171))
        self.recipes_TypeSelected.setTabPosition(QtWidgets.QTabWidget.North)
        self.recipes_TypeSelected.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.recipes_TypeSelected.setElideMode(QtCore.Qt.ElideNone)
        self.recipes_TypeSelected.setDocumentMode(False)
        self.recipes_TypeSelected.setTabsClosable(False)
        self.recipes_TypeSelected.setMovable(False)
        self.recipes_TypeSelected.setTabBarAutoHide(False)
        self.recipes_TypeSelected.setObjectName("recipes_TypeSelected")
        self.crafting_shaped = QtWidgets.QWidget()
        self.crafting_shaped.setObjectName("crafting_shaped")
        self.recipes_crafting_shaped_In1 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In1.setGeometry(QtCore.QRect(20, 10, 61, 20))
        self.recipes_crafting_shaped_In1.setObjectName("recipes_crafting_shaped_In1")
        self.recipes_crafting_shaped_In2 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In2.setGeometry(QtCore.QRect(90, 10, 61, 20))
        self.recipes_crafting_shaped_In2.setObjectName("recipes_crafting_shaped_In2")
        self.recipes_crafting_shaped_In3 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In3.setGeometry(QtCore.QRect(160, 10, 61, 20))
        self.recipes_crafting_shaped_In3.setObjectName("recipes_crafting_shaped_In3")
        self.recipes_crafting_shaped_In6 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In6.setGeometry(QtCore.QRect(160, 40, 61, 20))
        self.recipes_crafting_shaped_In6.setObjectName("recipes_crafting_shaped_In6")
        self.recipes_crafting_shaped_In4 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In4.setGeometry(QtCore.QRect(20, 40, 61, 20))
        self.recipes_crafting_shaped_In4.setObjectName("recipes_crafting_shaped_In4")
        self.recipes_crafting_shaped_In5 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In5.setGeometry(QtCore.QRect(90, 40, 61, 20))
        self.recipes_crafting_shaped_In5.setObjectName("recipes_crafting_shaped_In5")
        self.recipes_crafting_shaped_In7 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In7.setGeometry(QtCore.QRect(20, 70, 61, 20))
        self.recipes_crafting_shaped_In7.setObjectName("recipes_crafting_shaped_In7")
        self.recipes_crafting_shaped_In9 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In9.setGeometry(QtCore.QRect(160, 70, 61, 20))
        self.recipes_crafting_shaped_In9.setObjectName("recipes_crafting_shaped_In9")
        self.recipes_crafting_shaped_In8 = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_In8.setGeometry(QtCore.QRect(90, 70, 61, 20))
        self.recipes_crafting_shaped_In8.setObjectName("recipes_crafting_shaped_In8")
        self.recipes_crafting_shaped_Out = QtWidgets.QLineEdit(self.crafting_shaped)
        self.recipes_crafting_shaped_Out.setGeometry(QtCore.QRect(90, 120, 61, 20))
        self.recipes_crafting_shaped_Out.setObjectName("recipes_crafting_shaped_Out")
        self.recipes_crafting_shaped_InputText = QtWidgets.QLabel(self.crafting_shaped)
        self.recipes_crafting_shaped_InputText.setGeometry(QtCore.QRect(20, 90, 61, 21))
        self.recipes_crafting_shaped_InputText.setObjectName("recipes_crafting_shaped_InputText")
        self.recipes_crafting_shaped_OutputText = QtWidgets.QLabel(self.crafting_shaped)
        self.recipes_crafting_shaped_OutputText.setGeometry(QtCore.QRect(20, 120, 61, 16))
        self.recipes_crafting_shaped_OutputText.setObjectName("recipes_crafting_shaped_OutputText")
        self.recipes_crafting_shaped_OutNumberText = QtWidgets.QLabel(self.crafting_shaped)
        self.recipes_crafting_shaped_OutNumberText.setGeometry(QtCore.QRect(160, 120, 71, 16))
        self.recipes_crafting_shaped_OutNumberText.setObjectName("recipes_crafting_shaped_OutNumberText")
        self.recipes_crafting_shaped_OutNumber = QtWidgets.QSpinBox(self.crafting_shaped)
        self.recipes_crafting_shaped_OutNumber.setGeometry(QtCore.QRect(230, 120, 60, 22))
        self.recipes_crafting_shaped_OutNumber.setObjectName("recipes_crafting_shaped_OutNumber")
        self.recipes_TypeSelected.addTab(self.crafting_shaped, "")
        self.crafting_shapless = QtWidgets.QWidget()
        self.crafting_shapless.setObjectName("crafting_shapless")
        self.crafting_shapless_InList = QtWidgets.QListView(self.crafting_shapless)
        self.crafting_shapless_InList.setGeometry(QtCore.QRect(10, 10, 131, 121))
        self.crafting_shapless_InList.setObjectName("crafting_shapless_InList")
        self.crafting_shapless_Additem_btn = QtWidgets.QPushButton(self.crafting_shapless)
        self.crafting_shapless_Additem_btn.setGeometry(QtCore.QRect(150, 10, 75, 23))
        self.crafting_shapless_Delitem_btn = QtWidgets.QPushButton(self.crafting_shapless)
        self.crafting_shapless_Delitem_btn.setGeometry(QtCore.QRect(225, 10, 50, 23))
        self.crafting_shapless_Delitem_btn.setObjectName("crafting_shapless_Delitem_btn")
        self.crafting_shapless_InputID = QtWidgets.QLineEdit(self.crafting_shapless)
        self.crafting_shapless_InputID.setGeometry(QtCore.QRect(150, 60, 113, 20))
        self.crafting_shapless_InputID.setObjectName("crafting_shapless_InputID")
        self.crafting_shapless_InText = QtWidgets.QLabel(self.crafting_shapless)
        self.crafting_shapless_InText.setGeometry(QtCore.QRect(150, 40, 81, 16))
        self.crafting_shapless_InText.setObjectName("crafting_shapless_InText")
        self.crafting_shapless_OutText = QtWidgets.QLabel(self.crafting_shapless)
        self.crafting_shapless_OutText.setGeometry(QtCore.QRect(150, 80, 81, 16))
        self.crafting_shapless_OutText.setObjectName("crafting_shapless_OutText")
        self.crafting_shapless_OutputID = QtWidgets.QLineEdit(self.crafting_shapless)
        self.crafting_shapless_OutputID.setGeometry(QtCore.QRect(150, 100, 113, 20))
        self.crafting_shapless_OutputID.setObjectName("crafting_shapless_OutputID")
        self.crafting_shapless_OutputCountInput = QtWidgets.QSpinBox(self.crafting_shapless)
        self.crafting_shapless_OutputCountInput.setGeometry(QtCore.QRect(220, 121, 60, 25))
        self.crafting_shapless_OutputCountInput.setObjectName("crafting_shapless_OutputCountInput")
        self.crafting_shapless_Outputcount = QtWidgets.QLabel(self.crafting_shapless)
        self.crafting_shapless_Outputcount.setGeometry(QtCore.QRect(140, 125, 71, 21))
        self.crafting_shapless_Outputcount.setObjectName("crafting_shapless_Outputcount")
        self.recipes_TypeSelected.addTab(self.crafting_shapless, "")
        self.smoking = QtWidgets.QWidget()
        self.smoking.setObjectName("smoking")
        self.recipes_somking_comingsono = QtWidgets.QLabel(self.smoking)
        self.recipes_somking_comingsono.setGeometry(QtCore.QRect(60, 40, 161, 16))
        self.recipes_somking_comingsono.setObjectName("recipes_somking_comingsono")
        self.recipes_TypeSelected.addTab(self.smoking, "")
        self.recipes_save = QtWidgets.QPushButton(self.recipes_Frame)
        self.recipes_save.setGeometry(QtCore.QRect(280, 230, 75, 23))
        self.recipes_save.setObjectName("recipes_save")
        self.recipes_fileNameInput = QtWidgets.QLineEdit(self.recipes_Frame)
        self.recipes_fileNameInput.setGeometry(QtCore.QRect(290, 200, 113, 20))
        self.recipes_fileNameInput.setObjectName("recipes_fileNameInput")
        self.recipes_fileNameText = QtWidgets.QLabel(self.recipes_Frame)
        self.recipes_fileNameText.setGeometry(QtCore.QRect(200, 200, 71, 21))
        self.recipes_fileNameText.setObjectName("recipes_fileNameText")
        MainWindow.setCentralWidget(self.centralwidget)
        self.recipes_reflashList = QtWidgets.QPushButton(self.recipes_Frame)
        self.recipes_reflashList.setGeometry(QtCore.QRect(190, 230, 75, 23))
        self.recipes_reflashList.setObjectName("recipes_reflashList")
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 845, 23))
        self.menubar.setObjectName("menubar")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        # self.setting_menu=QtWidgets.QMenu(self.menubar)
        # self.setting_menu.setObjectName("setting_menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menu_2)
        self.menu_3.setObjectName("menu_3")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.newDatapack = QtWidgets.QAction(MainWindow)
        self.newDatapack.setObjectName("action")
        self.openDatapack = QtWidgets.QAction(MainWindow)
        self.openDatapack.setObjectName("newDatapack")
        # self.openSettingWinAction=QtWidgets.QAction(MainWindow)
        # self.openSettingWinAction.setObjectName("openSettingWinAction")
        self.shaped_crafting = QtWidgets.QAction(MainWindow)
        self.shaped_crafting.setObjectName("shaped_crafting")
        self.menu.addAction(self.newDatapack)
        self.menu.addAction(self.openDatapack)
        # self.setting_menu.addAction(self.openSettingWinAction)
        self.menu_3.addAction(self.shaped_crafting)
        self.menu_2.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())
        # self.menubar.addAction(self.setting_menu.menuAction())
        self.retranslateUi(MainWindow)
        self.recipes_TypeSelected.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.baseSetting_DatapackNameInput, self.baseSetting_DatapackVersionSelected)
        MainWindow.setTabOrder(self.baseSetting_DatapackVersionSelected, self.baseSetting_DatapackDescriptionInput)
        MainWindow.setTabOrder(self.baseSetting_DatapackDescriptionInput, self.baseSetting_SaveButton)
        MainWindow.setTabOrder(self.baseSetting_SaveButton, self.baseSetting_FormatCodeWikiLinkButton)
        self.datapack_namespace=""
        self.shapless_ItemList=[]
    def recipes_crafting_gen(self):
        #print(self.recipes_TypeSelected.currentIndex(),'currentIndex:TypeSelected')
        if self.recipes_TypeSelected.currentIndex() == 0:
            inList1=[self.recipes_crafting_shaped_In1.text(),self.recipes_crafting_shaped_In2.text(),self.recipes_crafting_shaped_In3.text(),
                    self.recipes_crafting_shaped_In4.text(),self.recipes_crafting_shaped_In5.text(),self.recipes_crafting_shaped_In6.text(),
                    self.recipes_crafting_shaped_In7.text(),self.recipes_crafting_shaped_In8.text(),self.recipes_crafting_shaped_In9.text()
            ]
            inDict={}
            type="minecraft:crafting_shaped"
            inSet=set([x for x in inList1 if inList1.count(x) > 1])
            keysL=['X','#','*','@','%','D',"&",'O','K']
            for i in inSet:
                if i!='':
                    inDict[i]=keysL[0]
                    keysL.pop(0)
            for i in inList1:
                if i!='':
                    inList1[inList1.index(i)]=inDict[i]
                else:
                    inList1[inList1.index(i)]=' '
            print(inList1)
            inList=[]
            for i in range(0,7,3):
                inList.append(inList1[i]+inList1[i+1]+inList1[i+2])
            result={
                "type":type,
                "key":{},
                "pattern":inList,
                "result":{
                    "item":self.recipes_crafting_shaped_Out.text()
                },
                "count":int(self.recipes_crafting_shaped_OutNumber.value())
            }
            for i in inDict:
                result["key"][inDict[i]]={
                    "item":i
                }
            # if datapackDir == "None" and datapackDir:
            #     QMessageBox.critical(None,"错误", "您没有选择数据包目录，请选择数据包目录！")
            #     self.newDatapackFunc()
            #     if os.path.exists(datapackDir+"/data/") == False:
            #         os.mkdir(datapackDir+"/data/")
            #     if os.path.exists(datapackDir+'/pack.mcmeta'):
            #         with open(datapackDir+"/pack.mcmeta","w",encoding="utf-8") as f:
            #             packMcmeta={
            #             "pack":{
            #                 "pack_format":12,
            #                 "description":"数据包简介\ncreate by DatapackGenerator"
            #             }
            #         }
            #             f.write(json.dumps(packMcmeta,ensure_ascii=False))
            #         if len(os.listdir(datapackDir+"/data/")) and datapackDir!='' == 0:
            #             os.mkdir(datapackDir+"/data/"+easygui.enterbox("输入命名空间名称",title="新建命名空间"))
            #             self.datapack_namespace=os.listdir(datapackDir+"/data/")[0]
            namespace=os.listdir(datapackDir+"/data/")
            if len(namespace)>=2:
                self.datapack_namespace=easygui.choicebox("选择一个命名空间","多个命名空间",namespace)
            else:
                self.datapack_namespace=namespace=namespace[0]
            with open(datapackDir+"/data/"+namespace+"/recipes/"+self.recipes_fileNameInput.text()+".json",mode="w",encoding="utf-8") as f:
                f.write(json.dumps(result))
        elif self.recipes_TypeSelected.currentIndex() == 1:
            pass
    def recipes_crafting_shapless_addItem(self):
        self.shapless_ItemList.append(self.crafting_shapless_InputID.text())
        list=QtCore.QStringListModel(self.shapless_ItemList)
        self.crafting_shapless_InList.setModel(list)
    def recipes_crafting_shapless_DelItem(self):
        #print(self.crafting_shapless_InList.currentIndex().row())
        self.shapless_ItemList.pop(self.crafting_shapless_InList.currentIndex().row())
        list=QtCore.QStringListModel(self.shapless_ItemList)
        self.crafting_shapless_InList.setModel(list)
    def recipes_ListViewClicked(self,index):
        global datapackDir,listItem
        tabDict={
            "crafting_shaped":0,
            "crafting_shapless":1,
            "blasting":2
        }
        with open(datapackDir+"/data/"+self.datapack_namespace+"/recipes/"+listItem[index.row()],"r",encoding="utf-8") as f:
            resultst=f.read()
        result=json.loads(resultst)
        recipeType=result["type"]
        recipeType=recipeType.split(":")[1]
        self.recipes_TypeSelected.currentIndex=recipeType
        self.recipes_fileNameInput.setText(listItem[index.row()].split(".")[0])
        self.recipes_TypeSelected.setCurrentIndex(tabDict[recipeType])
        #QMessageBox.information(None,"选择","你选择了第" + str(index.row())+"个 \n 类型：" + recipeType)
        if recipeType=="crafting_shaped":
            recipesTable=[]
            for i in result["pattern"]:
                for j in i:
                    recipesTable.append(j)
            print(recipesTable)
            result['key'][' ']={
                'item':''
            }
            for i in recipesTable:
                print(i,result['key'][i]["item"])
                recipesTable[recipesTable.index(i)]=result['key'][i]["item"]
            n=0
            for i in recipesTable:
                exec(f"self.recipes_crafting_shaped_In{n+1}.setText('{i}')")
                n+=1
            self.recipes_crafting_shaped_Out.setText(result["result"]['item'])
            if "count" in result:
                self.recipes_crafting_shaped_OutNumber.setValue(result["count"])
            else:
                self.recipes_crafting_shaped_OutNumber.setValue(1)
            #print(result)
    def recipes_reflashListFunc(self):
        global datapackDir,listItem
        # if datapackDir == "None" and datapackDir:
        #     QMessageBox.critical(None,"错误", "您没有选择数据包目录，请选择数据包目录！")
        #     self.newDatapackFunc()
        #     if os.path.exists(datapackDir+"/data/") == False:
        #         os.mkdir(datapackDir+"/data/")
        #     if os.path.exists(datapackDir+'/pack.mcmeta'):
        #         with open(datapackDir+"/pack.mcmeta","w",encoding="utf-8") as f:
        #             packMcmeta={
        #             "pack":{
        #                 "pack_format":12,
        #                 "description":"数据包简介\ncreate by DatapackGenerator"
        #             }
        #         }
        #             f.write(json.dumps(packMcmeta,ensure_ascii=False))
        #         if len(os.listdir(datapackDir+"/data/")) == 0:
        #             os.mkdir(datapackDir+"/data/"+easygui.enterbox("输入命名空间名称",title="新建命名空间"))
        #     with open(datapackDir+"/pack.mcmeta","r",encoding="utf-8") as f:
        #         resultstr=f.read()
        #     result=json.loads(resultstr)
        #     print(result)
        #     self.baseSetting_DatapackDescriptionInput.setText(result["pack"]["description"])
        #     self.baseSetting_DatapackNameInput.setText(datapackDir.split("/")[-1])
        #     self.baseSetting_DatapackVersionSelected.setCurrentIndex(int(result["pack"]["pack_format"])-3)
        namespace=os.listdir(datapackDir+"/data/")
        if len(namespace)>=2:
            self.datapack_namespace=easygui.choicebox("选择一个命名空间","多个命名空间",namespace)
        else:
            self.datapack_namespace=namespace=namespace[0]
        if os.path.exists(datapackDir+"/data/"+namespace+"/recipes/") == False:
            os.mkdir(datapackDir+"/data/"+namespace+"/recipes/")
        listItem=os.listdir(datapackDir+"/data/"+namespace+"/recipes/")
        list=QtCore.QStringListModel(listItem)
        list.setStringList(listItem)
        self.recipes_ListView.setModel(list)
    def saveBaseSetting(self):
        global datapackDir,namespace,version,description
        # if datapackDir == "None" and datapackDir:
        #     QMessageBox.critical(self, "错误", "您没有选择数据包目录，请选择数据包目录！")
        #     self.newDatapackFunc()
        namespace=self.baseSetting_DatapackNameInput.text()
        version=self.baseSetting_DatapackVersionSelected.currentIndex()+3
        description=self.baseSetting_DatapackDescriptionInput.toPlainText()
        if os.path.exists(datapackDir+"/data/"):
            pass
        else:
            os.mkdir(datapackDir+"/data/")
        if os.path.exists(datapackDir+"/data/"+namespace):
            pass
        else:
            os.mkdir(datapackDir+"/data/"+namespace)
        with open(datapackDir+"/pack.mcmeta",encoding="utf-8",mode="w+") as f:
            packMcmeta={
                "pack":{
                    "pack_format":int(version),
                    "description":description
                }
            }
            f.write(json.dumps(packMcmeta,ensure_ascii=False))
        print("update pack.mcmeta succ")
        QMessageBox.information(self,"信息","pack.mcmeta文件已更新")
        file = datapackDir+"/pack.mcmeta"
        file = os.path.realpath(file)
        #print(file)
        os.system(f'explorer /select, {file}')

    def newDatapackFunc(self):
        global datapackDir
        datapackDir=QFileDialog.getExistingDirectory(caption="新建数据包",directory="./")
        if(datapackDir=="" or datapackDir==None):
            QMessageBox.warning(None,"未选择目录","您取消选择了数据包目录")
        print("get datapack dir succ ",datapackDir)
        self.baseSetting.setEnabled(True)
        self.recipes_Frame.setEnabled(True)
    def openDatapackFunc(self):
        global datapackDir
        datapackDir=QFileDialog.getExistingDirectory(caption="打开数据包",directory="./")
        if(datapackDir=="" or datapackDir==None):
            QMessageBox.warning(None,"未选择目录","您取消选择了数据包目录")
            return
        elif os.path.exists(datapackDir+"/pack.mcmeta") == False:
            QMessageBox.critical(self, "错误", "您选择的目录不为数据包根目录，将新建数据包")
        print("get datapack dir succ ",datapackDir)
        try:
            with open(datapackDir+"/pack.mcmeta","r",encoding="utf-8") as f:
                resultstr=f.read()
            result=json.loads(resultstr)
            print(result)
            self.baseSetting_DatapackDescriptionInput.setText(result["pack"]["description"])
            self.baseSetting_DatapackNameInput.setText(datapackDir.split("/")[-1])
            self.baseSetting_DatapackVersionSelected.setCurrentIndex(int(result["pack"]["pack_format"])-3)
        except:
            with open(datapackDir+"/pack.mcmeta","w",encoding="utf-8") as f:
                packMcmeta={
                "pack":{
                    "pack_format":12,
                    "description":"数据包简介\ncreate by DatapackGenerator"
                }
            }
                f.write(json.dumps(packMcmeta,ensure_ascii=False))
            with open(datapackDir+"/pack.mcmeta","r",encoding="utf-8") as f:
                resultstr=f.read()
            result=json.loads(resultstr)
            print(result)
            self.baseSetting_DatapackDescriptionInput.setText(result["pack"]["description"])
            self.baseSetting_DatapackNameInput.setText(datapackDir.split("/")[-1])
            self.baseSetting_DatapackVersionSelected.setCurrentIndex(int(result["pack"]["pack_format"])-3)
        self.baseSetting.setEnabled(True)
        self.recipes_Frame.setEnabled(True)
        #print(self.baseSetting_DatapackVersionSelected.currentText(),self.baseSetting_DatapackVersionSelected.currentIndex())
    def linkFormatCode(self):
        webbrowser.open("https://minecraft.fandom.com/zh/wiki/%E6%A0%BC%E5%BC%8F%E5%8C%96%E4%BB%A3%E7%A0%81", new=0, autoraise=True)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "DatapackGenerator"))
        self.baseSetting.setTitle(_translate("MainWindow", "基本设置"))
        self.baseSetting_DatapackName.setText(_translate("MainWindow", "数据包名称"))
        self.baseSetting_DatapackVersion.setText(_translate("MainWindow", "数据包版本"))
        self.baseSetting_DatapackVersionSelected.setItemText(0, _translate("MainWindow", "3  1.13 (17w43a~17w47b)"))
        self.baseSetting_DatapackVersionSelected.setItemText(1, _translate("MainWindow", "4  1.13（17w48a）~ 1.14.4（19w46b） "))
        self.baseSetting_DatapackVersionSelected.setItemText(2, _translate("MainWindow", "5  1.15（1.15-pre1）~ 1.16.1（1.16.2-pre3） "))
        self.baseSetting_DatapackVersionSelected.setItemText(3, _translate("MainWindow", "6  1.16.2（1.16.2-rc1）~ 1.16.5（20w45a） "))
        self.baseSetting_DatapackVersionSelected.setItemText(4, _translate("MainWindow", "7  1.17（20w46a）~ 1.17.1（1.18-exp7） "))
        self.baseSetting_DatapackVersionSelected.setItemText(5, _translate("MainWindow", "8  1.18（21w37a）~ 1.18.1（22w07a） "))
        self.baseSetting_DatapackVersionSelected.setItemText(6, _translate("MainWindow", "9  1.18.2（1.18.2-pre1 ~ 正式版） "))
        self.baseSetting_DatapackVersionSelected.setItemText(7, _translate("MainWindow", "10 1.19（22w11a）~ 1.19.3"))
        self.baseSetting_DatapackVersionSelected.setItemText(8, _translate("MainWindow", "11 1.19.4快照23w03a ~ 23w05a"))
        self.baseSetting_DatapackVersionSelected.setItemText(9, _translate("MainWindow", "12 1.19.4（23w06a）及以上 "))
        self.baseSetting_DatapackDescriptionText.setText(_translate("MainWindow", "数据包介绍（支持格式化代码）"))
        self.baseSetting_FormatCodeWikiLinkButton.setText(_translate("MainWindow", "格式化代码wiki"))
        self.baseSetting_SaveButton.setText(_translate("MainWindow", "保存"))
        self.title.setText(_translate("MainWindow", "数据包生成器 DatapackGenerator"))
        self.vesion_info.setText(_translate("MainWindow", "Visual Design by Bi2Nb9O3   GUI Version "+self.visual_version+" Program Version "+self.version+""))
        self.recipes_Frame.setTitle(_translate("MainWindow", "配方"))
        self.recipes_crafting_shaped_InputText.setText(_translate("MainWindow", "输入物品ID"))
        self.recipes_crafting_shaped_OutputText.setText(_translate("MainWindow", "输出物品ID"))
        self.recipes_crafting_shaped_OutNumberText.setText(_translate("MainWindow", "输出物品数量"))
        self.recipes_TypeSelected.setTabText(self.recipes_TypeSelected.indexOf(self.crafting_shaped), _translate("MainWindow", "有序合成"))
        self.crafting_shapless_Additem_btn.setText(_translate("MainWindow", "添加物品"))
        self.crafting_shapless_InText.setText(_translate("MainWindow", "输入物品ID"))
        self.crafting_shapless_OutText.setText(_translate("MainWindow", "输出物品ID"))
        self.crafting_shapless_Outputcount.setText(_translate("MainWindow", "输出物品数量"))
        self.recipes_TypeSelected.setTabText(self.recipes_TypeSelected.indexOf(self.crafting_shapless), _translate("MainWindow", "无序合成"))
        self.recipes_somking_comingsono.setText(_translate("MainWindow", "Coming Sooooooooooooooooooon"))
        self.recipes_TypeSelected.setTabText(self.recipes_TypeSelected.indexOf(self.smoking), _translate("MainWindow", "烟熏"))
        self.recipes_save.setText(_translate("MainWindow", "保存"))
        self.recipes_fileNameText.setText(_translate("MainWindow", "配方文件名称"))
        self.recipes_reflashList.setText(_translate("MainWindow", "刷新列表"))
        self.menu.setTitle(_translate("MainWindow", "文件"))
        self.menu_2.setTitle(_translate("MainWindow", "编辑"))
        self.menu_3.setTitle(_translate("MainWindow", "新建配方"))
        self.newDatapack.setText(_translate("MainWindow", "新建数据包"))
        self.openDatapack.setText(_translate("MainWindow", "打开数据包"))
        self.shaped_crafting.setText(_translate("MainWindow", "有序合成"))
        self.crafting_shapless_Delitem_btn.setText(_translate("MainWindow","删除"))
        # self.openSettingWinAction.setText(_translate("MainWindow","设置"))
        # self.setting_menu.setTitle(_translate("MainWindow","设置"))
        #功能链接
        self.baseSetting_FormatCodeWikiLinkButton.clicked.connect(self.linkFormatCode)
        self.newDatapack.triggered.connect(self.newDatapackFunc)
        self.openDatapack.triggered.connect(self.openDatapackFunc)
        self.baseSetting_SaveButton.clicked.connect(self.saveBaseSetting)
        self.recipes_reflashList.clicked.connect(self.recipes_reflashListFunc)
        self.recipes_ListView.clicked.connect(self.recipes_ListViewClicked)
        self.recipes_save.clicked.connect(self.recipes_crafting_gen)
        self.crafting_shapless_Additem_btn.clicked.connect(self.recipes_crafting_shapless_addItem)
        # self.openSettingWinAction.triggered.connect(self.openSettingWindowFunc)
        self.crafting_shapless_Delitem_btn.clicked.connect(self.recipes_crafting_shapless_DelItem)
        #初始化
        self.baseSetting.setEnabled(False)
        self.recipes_Frame.setEnabled(False)
        #主题
        self.title.setProperty('class','title')

if __name__ == "__main__":
    datapackDir="None"
    QtCore.QCoreApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling)
    app = QtWidgets.QApplication(sys.argv) # 创建一个QApplication，也就是你要开发的软件app
    
    MainWindow = QtWidgets.QMainWindow() # 创建一个QMainWindow，用来装载你需要的各种组件、控件 
    ui = Ui_MainWindow() # ui是Ui_MainWindow()类的实例化对象 
    ui.setupUi(MainWindow)
    apply_stylesheet(app, theme='dark_blue.xml',invert_secondary=False) # 执行类中的setupUi方法，方法的参数是第二步中创建的QMainWindow 
    #apply_stylesheet(app, theme='dark_blue.xml',extra={
    #    'font-size':'20px'
    #})
    stylesheet = app.styleSheet()
    custom_css='''
.title{{
    font-size: 30px;
}}

QPushButton{{
    font-size: 10px;
}}

QLabel{{
    font-size: 12px;
}}

QSpinBox{{
    color: #fff;
}}

*{{
    font-family: "Microsoft YaHei";
}}

QComboBox{{
    color: #fff;
}}
        '''
    #print(sys.argv)
    if len(sys.argv)>=3 and (sys.argv[1] == "--custom-css" or sys.argv[1] == "-cc"):
        with open(sys.argv[2],mode="r",encoding="utf-8") as f:
            print("Load Custom CSS file")
            css_result=f.read()
        custom_css+=css_result
    app.setStyleSheet(stylesheet + custom_css.format(**os.environ))
    MainWindow.show() # 执行QMainWindow的show()方法，显示这个QMainWindow
    sys.exit(app.exec_()) # 使用exit()或者点击关闭按钮退出QApplicat
