from collections import namedtuple
import csv
import pandas as pd


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

def get_drg10_dict(drg10_file):
    drg10_dict = {}
    with open(drg10_file, 'r', encoding="UTF-8-sig") as df:
        reader = csv.reader(df)
        for diag, diag_code in reader:
            drg10_dict[diag_code] = diag
    return drg10_dict

def get_drg9_dict(drg9_file):
    drg9_dict = {}
    with open(drg9_file, 'r', encoding="UTF-8-sig") as df:
        reader = csv.reader(df)
        for oper, oper_code in reader:
            drg9_dict[oper_code] = oper
    return drg9_dict

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
    
    cross_merged_df = pd.merge(pd.DataFrame({"diagnosis":dias_list}), pd.DataFrame({"operation":opers_list}), how="cross").drop_duplicates()
    
    cross_merged_df["diagnosis_all"] = cross_merged_df.diagnosis.map(get_one2list(dias_list))
    cross_merged_df["operations_all"] = cross_merged_df.operation.map(get_one2list(opers_list))

    return  cross_merged_df