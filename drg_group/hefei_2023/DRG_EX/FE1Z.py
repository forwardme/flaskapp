from drg_group.hefei_2023.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["39.7301","39.7101","39.9000x022","39.9001","39.9102","39.9000x010"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FE1Z入组条件，匹配规则：主手术匹配、某一手术匹配')
    return True