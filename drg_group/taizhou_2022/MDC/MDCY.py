from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.ADRG import YC1,YR1,YR2

def group(record):
  mdc_zd=["B23.800x002","B20.600x001","B20.400x001","B22.000x003","B22.000x004","B22.200","I33.000x018","B20.100x001","B20.006","B21.000x001","B23.800","B23.800x001","B23.100","B20.301","B20.000x001","B23.801","B22.701","B23.100x001","B20.700x001","B21.200x001","B20.901","B22.000x001","B23.000","B24.x01","B20.005","B21.800","B21.700","B22.001+F02.4*","Z20.600","B20.002","B21.100x001","B22.700","B21.300","B20.004","B23.201","B20.200x001","B20.003","B20.001","B21.900","O98.700","Z21.x00x001","B20.300x001","B20.500x001","B22.100","R75.x00x001","B23.200","B22.000x005","B23.100x002","B20.801"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCY入组条件，匹配规则：主诊断匹配')

  result=YC1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合YQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'YQY'

  result=YR1.group(record)
  if result:
    return result

  result=YR2.group(record)
  if result:
    return result

  message('不符合MDCY的ADRG入组条件')

