from drg_group.hefei_2023.Base import message,intersect,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["52.6x01","52.6x02","52.6x03","52.7x00","52.7x00x003","52.7x00x004","52.7x01"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HB1Z入组条件，匹配规则：主手术匹配、某一手术匹配')
    return True