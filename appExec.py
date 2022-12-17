from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QMessageBox
import sys
import windowUI
from functions import * 
from seleniumContents import openSite, inputInformation, crnError, subjectError, numberError

termValues = ["null","202305","202301","202208","202205","202201","202108","202105","202101","202008","202005","202001","201908","201905",
"201901","201808"]

partoftermValues = ["null","A","B","S","X","D","G","Z","W","Y"]

campusValues = ["null","T","S","P","L","9","7","6","8","1","3","4","2","C"]

collegeValues = ["null","XX","SA","AT","AR","AC","AL","AS","AM","AP","BS","BC","BA","BU","BM","BP","CE","DM","EA","ED","EU","EJ","JP","EM","EP",
"EN","CS","GS","HM","HT","IN","ZZ","IP","LL","LA","LM","MS","MD","NS","NC","00",
"NR","OC","RO","BI","PH","FM","MM","SS","ST","RX","TT","FA","HC","SM","WL","US","SP"]

departmentValues = ["null","ASG","ACP","ACC","ADG","EDB","ADM","ATS","EDV","ADV","AFA","AMH","AGE","AFR","HUN","AAS","AMS","ANA","ANC","ANE","ANT","ARC","MIS",
"ART","EDA","ACD","AST","ATH","ATG","BIS","BSB","EGB","CBS","BKB","BCD","BMB","BSP","BIO","BIN","BCM","BOT","BDG","MBA","GBA","BUD","CMM","CDV","COT","CSW",
"ECM","ECH","CHM","CFS","EDR","CCR","EGX","CLA","ENT","COE","CSL","SPE","CSD","CLY","CAF","CAL","CEI","CEL","CMH","CFH","ESB","ESC","CAM","CED","CME",
"CNV","CHD","EDG","CJP","MST","CTR","CIB","CMR","CMS","EDC","CNI","CIL","DIG","DAN","DEA","WSP","DIO","DERM","DEV","DIT","EDU","EUP","ECN","EAP","CCD","EDZ"
,"EUD","ELS","EEP","EGE","EDE","BXE","EMD","ENR","END","ETK","ENG","EDT","ENP","EOH","ENV","ESP","EPB","ETH","EDS","EXS","FMH","FMD","FIN","FIA","FGN",
"FAI","FAP","FCT","FIT","FIO","FBL","FOL","EDX","FMG","FDN","FOB","EDF","GPY","GEP","GLY","GLO","CGD","GLF","GIA","GVG","GRS","GSD"
,"GRA","GST","HEN","HPM","HSL","EDH","HTY","HON","HRM","HUS","HUM","HCS","EDY","HAS","NTO","EGS","QMB","EIT","ICY","IRP"
,"BSI","IBL","EDK","ITB","IDP","CGS","IAS","LLI","IOP","ISS","IDS","IMD","IAC","ILI","INT","JDC","JMS","BFI","LKG","LLE","LAS","LPL","LCA","LEA",
"LDR","ALA","LBG","EDL","LIN","ACG","MED","MAI","MAN","MSC","MSD","MKT","COM","EDO","MTH","EDQ","EGR","DME","EME","MMI","MSG","MET",
"MDT","MDG","MDD","MHL","MIC","MLL","MFC","EDM","MGE","NVY","SPL","NEU","NSG","NWC","NUR","NRD","OBG","UCT","OCT","RO","NRO","ONC","OPH",
"ORTH","OSM","OTO","PCB","PTH","PED","PCR","PS","PMT","PHA","PHM","RXD","PHI","PEB","EDJ","EDP","PAS","PHY","PHB","POL","NRG","PRG","PDP",
"PVN","PBM","PSY","PAD","PAF","PBG","PUH","PHC","PHG","PHD","RAD","RGY","RLS","REG","REH","REL","RSH","RHL","ROM","SCT","SLCT",
"SRA","SRB","SRE","SRG","SAR","SRL","SRN","HTM","RMI","GEY","ARTD","ARH","SGS","ISM","LIS","IGS","MKI","MUS","PHT","SPF","SOK","TRD",
"EPS","EDN","EDI","SBD","SCR","ESF","SSI","EDW","SCL","SOC","SIS","SFB","SRH","SPA","SPB","SPD","SPG","SPN","STV","SAG","STL","SGC","SUR","TAL"
,"TEL","TEN","TSF","FAD","TAR","EDD","TRK","UEA","0000","UGE","USD","UAG","URL","XXX","URO","VVA","VSA","VBL","WST","WCB","WLE","MCM","ZOO"]

statusValues = ["null","O","C"]

status2Values = ["null","A","C","H","N","U"]

levelValues = ["null", "UG", "GR"]

class ExampleApp(QtWidgets.QMainWindow, windowUI.Ui_ClassChecker):
    def __init__(self, parent=None):
        super(ExampleApp, self).__init__(parent)
        self.setupUi(self)

def main():
    app = QApplication(sys.argv)
    form = ExampleApp()
    content = formContents()        
    
    def setVariables():
        content.setTerm(form.term.currentText())
        content.setpartofterm(form.partofterm.currentText())
        content.setCampus(form.campus.currentText())
        content.setCollege(form.college.currentText())
        content.setDepartment(form.departments.currentText())
        content.setcourseStatus(form.status.currentText())
        content.setcourseStatus2(form.status2.currentText())
        content.setcourseLevel(form.level.currentText())
        content.setCrn(testCRN())
        content.setSubject(subjectValidation())
        content.setNumber(testNumber())
    
    def testVariables():
        #print("Class value of selected term: " , content.getTerm())
        ##print("Class value of selected part of term: ", content.getpartofterm())
        #print("Class value of selected campus: ", content.getCampus())
        #print("Class value of selected college: ", content.getCollege())
        #print("Class value of selected department: ", content.getDepartment())
        #print("Class value of selected course status 1: ", content.getcourseStatus())
        #print("Class value of selected course status 2: ", content.getcourseStatus2())
        #print("Class value of selected course level: ", content.getcourseLevel())
        #print("Class value of selected CRN: ", content.getCRN())
        print("Term Translation: ", termTranslation())
        print("Part of term translation: ", partsoftermTranslation())
        print("Campus translation: ", campusTranslation())
        print("College Translation: ", collegeTranslation())
        print("Department translation: ", departmentTranslation())
        print("Status translation: ", statusTranslation())
        print("Status 2 translation: ", status2Translation())
        print("Level translation: " , levelTranslation())
        print("Current CRN: ", content.getCRN())
        print("Current subject: ", content.getSubject())
        print("Class Number: ", content.getNumber())

    def testCRN():
        if len(form.crn.text()) != 0:
            if form.crn.text().isdigit() and len(form.crn.text()) == 5:
                return form.crn.text()
            else:
                crnError()
                return "null"
        elif len(form.crn.text()) == 0:
            return "null"
            
    def termTranslation():
        i = form.term.currentIndex()
        termValue = termValues[i]
        return termValue

    def partsoftermTranslation():
        i = form.partofterm.currentIndex()
        partoftermValue = partoftermValues[i]
        return partoftermValue

    def campusTranslation():
        i = form.campus.currentIndex()
        campusValue = campusValues[i]
        return campusValue
    
    def collegeTranslation():
        i = form.college.currentIndex()
        collegeValue = collegeValues[i]
        return collegeValue

    def departmentTranslation():
        i = form.departments.currentIndex()
        departmentValue = departmentValues[i]
        return departmentValue

    def statusTranslation():
        i = form.status.currentIndex()
        statusValue = statusValues[i]
        return statusValue

    def status2Translation():
        i = form.status2.currentIndex()
        status2Value = status2Values[i]
        return status2Value

    def levelTranslation():
        i = form.level.currentIndex()
        levelValue = levelValues[i]
        return levelValue

    def subjectValidation():
        if len(form.crn_2.text()) != 0:
            if not form.crn_2.text().isdigit() and len(form.crn_2.text()) == 3:
                return form.crn_2.text()
            else: 
                subjectError()
                return "null"
        elif len(form.crn_2.text()) == 0:
            return "null"

    def testNumber():
        if len(form.crn_5.text()) != 0:
            if form.crn_5.text().isdigit() and len(form.crn_5.text()) == 4:
                return form.crn_5.text()
            elif len(form.crn_5.text()) == 5 and not form.crn_5.text()[4].isdigit():
                return form.crn_5.text()
            else:
                numberError()
                return "null"
        elif len(form.crn_5.text()) == 0:
            return "null"

    def debugBrowser():
        setVariables()
        print("Debug browser function called")
        driver = openSite()
        inputInformation(driver, termTranslation(), partsoftermTranslation(), campusTranslation(), collegeTranslation(), 
                         departmentTranslation(),statusTranslation(), status2Translation(), levelTranslation(), content.getCRN(), content.getNumber())

    form.pushButton.clicked.connect(setVariables)
    form.pushButton.clicked.connect(testVariables)
    form.Debug.clicked.connect(debugBrowser)
    
    #form.pushButton.clicked.connect()
    form.show()
    app.exec_()

if __name__ == '__main__':
    main()