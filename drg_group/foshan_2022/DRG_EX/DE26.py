from drg_group.foshan_2022.Base import message,intersect,has_mcc,has_cc,SS_VALID

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["28.5x03","28.9200x002","28.6x00x005"]
  adrg_ss1=[]
  adrg_ss2=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合DE26入组条件，匹配规则：主手术匹配')
    return True