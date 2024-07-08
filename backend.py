from collections import namedtuple
import csv
import pandas as pd

WEIGHT_FILE_PATH = "./tem/DRG_weights.csv"
DRG10_FILE_PATH = "./tem/drg10.csv"
DRG9_FILE_PATH = "./tem/drg9.csv"
ICD10_GUOLIN_YIBAO_PATH = "./tem/ICD10guolin2yibao.csv"
ICD9_GUOLIN_YIBAO_PATH = "./tem/ICD9guolin2yibao.csv"
ICD10DF = pd.read_csv(ICD10_GUOLIN_YIBAO_PATH)
ICD9DF = pd.read_csv(ICD9_GUOLIN_YIBAO_PATH)

class MakeRecord:
    def __init__(self, zdList, ssList, Index = 112, gender = 1, age = 65, ageDay = 11, weight = 60, dept = 'Cir', inHospital = 601, leavingType = 'C'):
        self.Index = Index
        self.gender = gender
        self.age = age
        self.ageDay = ageDay
        self.weight = weight
        self.dept = dept
        self.inHospital = inHospital
        self.leavingType = leavingType
        self.zdList = zdList
        self.ssList = ssList
        self.MR =  namedtuple("medical_record", ["Index","gender","age","ageDay","weight","dept","inHospitalTime","leavingType","zdList","ssList"])


    def getrecord(self):
        return self.MR(self.Index, self.gender, self.age, self.ageDay, self.weight, self.dept, self.inHospital, self.leavingType, self.zdList,self.ssList)

# def csv2vbv(csvstring):
    # return "|".join(csvstring.split(','))

def vbv2csv(vbvstring):
    return ",".join(vbvstring.split('|'))

def DRG_weights_tuple(weights_file):
    weights_turple = {}
    with open(weights_file, 'r', encoding="UTF-8-sig") as wf:
        reader = csv.reader(wf)
        for drg, score in reader:
            weights_turple[drg] = score
    return weights_turple

WEIGHT_TUPLE = DRG_weights_tuple(WEIGHT_FILE_PATH)

def get_drg10_dict(drg10_file):
    drg10_dict = {}
    with open(drg10_file, 'r', encoding="UTF-8-sig") as df:
        reader = csv.reader(df)
        for diag, diag_code in reader:
            drg10_dict[diag_code] = diag
    return drg10_dict

DRG10_DIC = get_drg10_dict(DRG10_FILE_PATH)

def get_drg9_dict(drg9_file):
    drg9_dict = {}
    with open(drg9_file, 'r', encoding="UTF-8-sig") as df:
        reader = csv.reader(df)
        for oper, oper_code in reader:
            drg9_dict[oper_code] = oper
    return drg9_dict

DRG9_DIC = get_drg9_dict(DRG9_FILE_PATH)

# A factory function return a mapping function with optional argument original_list, 
# It can be dias or opers. 
def get_one2list(original_list):
    def inner(one):
        copy_list = original_list[:]
        copy_list.remove(one)
        copy_list.insert(0, one)
        return ",".join(copy_list)
    return inner

# Return a pandas dataframe with all combinations of dias list and opers list.
# With each item extended with original list remove the item in the field, and convert to csv.
def cross_merge(dias, opers):

    if "|" in dias:
        dias_list = dias.split("|")
    elif "," in dias:
        dias_list = dias.split(",")
    else:
        if not dias:
            return pd.DataFrame({})
        dias_list = [dias]
    
    if "|" in opers:
        opers_list = opers.split("|")
    elif "," in opers:
        opers_list = opers.split(",")
    else:
        opers_list = [opers]
        # if not opers:
        #     opers_list = ["Nan"]
        # else:
        #     opers_list = [opers]
    
    # 如果输入为ICD国临版，将其转换为ICD医保版编码
    dias_list = [get_icd10_yibao(dia) for dia in dias_list]
    opers_list = [get_icd9_yibao(oper) for oper in opers_list]
    
    cross_merged_df = pd.merge(pd.DataFrame({"diagnosis":dias_list}), pd.DataFrame({"operation":opers_list}), how="cross").drop_duplicates()
    
    cross_merged_df["diagnosis_all"] = cross_merged_df.diagnosis.map(get_one2list(dias_list))
    cross_merged_df["operations_all"] = cross_merged_df.operation.map(get_one2list(opers_list))

    return  cross_merged_df


# ICD国临版与ICD医保版编码不同，grouping模块默认接受ICD医保版，
# 首页诊断编码为ICD临床版，这个函数增加了临床版到医保版的转换功能。
def get_icd10_yibao(icd:str) -> str:
    if icd in ICD10DF["医保版2.0编码"].values:
        return icd
    elif icd in ICD10DF["国临版编码"].values:
        guolin_icds = [icd]
        guolin_mask = ICD10DF["国临版编码"].isin(guolin_icds)
        selected_icds = ICD10DF[guolin_mask]
        icd_yibao = selected_icds["医保版2.0编码"]
        return str(*icd_yibao.values)
    else:
        return ""


def get_icd9_yibao(icd:str) -> str:
    if icd in ICD9DF["医保2.0手术代码"].values:
        return icd
    elif icd in ICD9DF["国临3.0手术代码"].values:
        guolin_icds = [icd]
        guolin_mask = ICD9DF["国临3.0手术代码"].isin(guolin_icds)
        selected_icds = ICD9DF[guolin_mask]
        icd_yibao = selected_icds["医保2.0手术代码"]
        return str(*icd_yibao.values)
    else:
        return ""