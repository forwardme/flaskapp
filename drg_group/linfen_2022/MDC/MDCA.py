from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.ADRG import AB1,AG2,AH1

def group(record):
  mdc_zd=[]
  dept_list=[]
  if not (True and record.ssList and record.ssList[0] in SS_VALID):
    return ''
  
  message('符合MDCA入组条件，匹配规则：存在手术')

  result=AB1.group(record)
  if result:
    return result
  result=AG2.group(record)
  if result:
    return result
  result=AH1.group(record)
  if result:
    return result

  if False and record.ssList and record.ssList[0] in SS_VALID:
    message('符合AQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'AQY'

  message('不符合MDCA的ADRG入组条件')

