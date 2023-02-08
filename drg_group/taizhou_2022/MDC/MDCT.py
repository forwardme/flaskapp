from drg_group.taizhou_2022.Base import message,intersect,SS_VALID
from drg_group.taizhou_2022.ADRG import TB1,TR1,TR2,TS1,TS2,TT1,TT2,TU1,TV1,TW1

def group(record):
  mdc_zd=["F43.200","F60.000","F22.800","F44.200","F44.402","F32.100x011","F81.100","F43.900","F94.800","F53.101","R45.100x002","F94.200","F91.900","F44.407","F06.800x017","F20.500","F51.500","F44.902","F63.300","F70.000","F41.000","F06.811","F45.303","F33.400","F31.400","F45.200","R45.801","F60.900","F25.100x001","R48.200","F42.100","F20.200x002","R45.200x001","F45.805","F31.600","F98.800","F23.902","F42.900","F63.900","F45.803","F31.300x005","F61.x00x011","F06.800","F50.000","F06.900","F43.002","F44.600","F43.000","F38.100x002","F84.400","G47.000","R68.803","F33.800","F06.800x041","F52.201","F78.800","F32.800x001","F32.802","F32.900","F98.803","F80.201","F25.800","F23.300x002","F41.200x002","Q93.500","F91.100","F84.500","F30.200x001","F48.001","F89.x00","F59.x00x001","F71.900","F50.801","F07.100","F45.000","F63.800","F45.304","F73.800","F79.800","F62.800","F44.800x011","F30.100x001","F50.900","F45.807","F43.802","F43.803","R45.300x002","F65.500x002","F70.800","F06.800x033","F40.901","F95.000","F66.200","R45.300x001","F42.003","F44.403","R48.000x002","F40.000","F45.402","F22.002","F92.900","F06.810","F98.600","F06.800x049","F25.100","F06.800x047","F06.800x016","R45.400x001","F48.801","F06.800x021","F06.800x046","F32.901","F39.x00","F31.000","F31.803","F45.801","F68.000x001","F20.300","F06.800x025","F25.200x002","F07.900x001","F31.300x011","F32.800x002","F42.901","F06.500","F23.200x003","F30.000","R45.700x001","F06.800x006","F32.000x011","F33.300","G47.801","F81.300","F44.501","F43.200x031","F25.200","F06.800x027","F95.201","F80.203","F60.800x002","F40.200x002","F60.300","R44.000","F07.800x002","F72.900","F53.900","F62.900","F22.900","F45.900","F45.300x091","F66.900","F43.804","F45.301","F06.800x037","F51.100","R45.100x001","F30.200x002","F99.x00","F50.100","F20.301","F40.100","F32.902","F65.900","F53.100x001","F50.200","F06.800x004","G47.800x002","F30.901","F32.801","F22.800x001","F34.900","F92.000","F51.000","F52.200x002","F44.300","F23.300x003","F44.400","F06.803","Z03.200","F44.301","F45.310","F21.x00","G47.000x002","F33.200","F54.x00","F31.902","F06.700","F09.x00x004","F60.301","F09.x03","F06.300x020","F84.200","F44.000","F25.000x001","F44.600x002","F34.001","F79.000x001","F98.400","F81.200","F06.800x011","F40.200x003","F33.100x011","F44.406","F45.800x002","Q90.900","F62.100","F06.800x002","F04.x00x001","F48.900","F43.801","F90.100","F43.200x081","F25.900","F31.700","F34.002","F72.800","G47.000x001","F81.000","F45.403","F31.800x003","F30.800x002","G47.800x001","F93.900","R45.400x002","F41.001","F71.000","F31.100","F22.001","F29.x00","F05.801","F52.600","F06.800x042","F68.100","F45.804","F44.602","G47.900","F52.100x011","F53.000x001","F53.800","F05.100","F44.603","F06.806","F20.501","F81.800","F20.800x003","F31.800x002","F51.800","F81.900","F91.100x002","R46.200x002","F07.201","F70.900","R48.001","F23.800","F93.000","F45.201","F44.700","F90.000x001","F51.300","F73.900","F06.800x032","F94.000","F90.900","F44.601","F84.000","F06.808","F73.000","F59.x00","F34.000","F71.800","R48.800x002","F44.405","F48.802","F06.800x020","F38.800","F68.800","F44.802","F31.802","F94.900","F06.800x045","F60.600","F60.802","F62.000","F60.200","F50.401","R45.000","F44.900","F84.300x001","F20.802","F93.200","R48.800x004","F05.900","F45.100","F65.800","F50.501","F28.x00x011","F79.000","F06.800x024","F06.100","F06.200","F73.000x001","F45.806","F91.000","F42.000","F06.400x003","F52.500","F65.400","F60.500","F06.800x050","F91.300","F06.400","F20.400","F45.308","F41.100","F44.901","F92.800","F45.305","F23.900","R48.800x001","F38.100x001","F31.200","F90.000","F32.100x002","F51.200","F05.001","F20.800x001","R48.100","F30.200","F40.200x004","F84.000x001","F34.800","F31.500","F78.900","F41.900","F53.001","F98.100","F45.300x022","F06.800x019","F09.x00x003","F63.000","F80.202","F20.000","F80.200","F06.800x026","F28.x02","F84.900x001","F90.800","F44.805","F98.802","F06.800x043","F72.000","F05.101","F05.902","F65.300","F06.300x021","F07.900","F64.000x002","F71.000x001","F33.900","F48.000","F23.002","F68.100x001","F95.800","F06.809","F45.300x041","Q91.300","F23.301","F30.900","R45.700x002","F93.800","F06.800x015","F98.300","F06.804","F52.001","F48.100","F50.800x002","F45.300","F73.100","F52.100x002","F52.400","F45.400","F88.x00","F95.801","F41.200","Q93.400","F34.100","R44.300","F48.901","F34.102","F28.x00x012","F72.000x001","F05.000x001","R41.801","F61.x00","F43.101","F81.201","F80.800","F09.x01","F23.001","F09.x02","F52.100","Q93.500x001","F52.000","F06.800x023","F38.000x001","F60.700","F98.000","F23.200","F78.100","F06.600","F30.100","F06.302","F31.301","F64.000x001","F06.300","F93.100","F45.300x031","F84.001","F98.001","F79.900","F07.800x003","F45.300x051","F79.901","F98.500","F25.000","F63.200","F20.800x002","F80.100","F06.800x014","F06.800x013","F65.500x001","F32.301","F30.201","F31.300x002","F31.801","F44.800x012","F60.801","F07.000","F07.001","F98.101","F06.301","F45.309","F05.000","F32.200","F52.300","F78.000","F25.200x001","F06.800x008","F45.306","F79.100","F80.205","F68.000","F71.100","F06.300x030","F06.800x005","F32.000x002","F84.301","F50.502","F32.300","F60.800x003","F41.201","F45.202","F84.100","Q93.900","F20.200","F43.100","F60.800x001","F63.800x001","F22.000","F20.801","F41.800","F43.001","F06.800x018","F52.202","F51.200x003","F95.100","F24.x00","F66.100","F83.x00","F06.000","F44.903","F65.000","F63.801","F06.800x010","F28.x01","R45.800x091","F45.307","F44.800x002","F45.802","F06.800x048","F45.901","R45.200x003","F20.900","F60.400","F20.100","F31.300x012","F95.200","F07.800x001","F06.800x034","F33.100x002","F31.800x001","F41.300x001","F51.200x002","F52.900","F64.800","F06.800x040","F06.800x039","F98.200","F33.000x011","F05.802","F20.600","F23.200x011","F65.600","F06.800x007","F44.804","F80.900","F43.200x041","F82.x00","Q93.501","F06.801","F53.002","F45.300x021","F06.800x009","F69.x00","F28.x00x002","R45.500","F31.901","F42.800","F20.803","F63.100","F38.001","F66.800","F31.900","F07.200","F23.901","F91.200","F98.800x001","F91.800","F64.900","F04.x00x901","F06.800x038","R48.801","F51.400","F51.900","F23.000","F40.900","F23.100","F31.300x003","F65.500","F44.500","F06.300x010","F60.201","F06.805","F52.700","F60.100","F43.200x051","F44.401","F41.102","F42.800x001","F88.x01","F95.101","F64.200","F80.000","F84.900","F20.201","F84.800","F70.000x001","F06.300x002","F22.003","G47.100","F44.100","F52.200","F60.302","F34.101","F42.001","F50.300","F41.101","R45.600","R48.800x005","F40.200x001","F66.000","F23.903","F42.101","F70.100","F98.801","F44.801","F98.900","F93.300","F48.100x002","F33.100","F40.800","F33.000x002","F80.300","F84.002","F65.100","R46.400","F33.000","F23.300x001","F45.401","F80.204","F43.800x002","F64.100","F06.800x012","F07.901","F45.302","F44.800x021","F06.800x044","F94.100","F06.802","F06.807","F05.901","F42.200","F95.900","F65.200","F44.404","R45.200","F72.100","F06.800x003","F52.800"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCT入组条件，匹配规则：主诊断匹配')

  result=TB1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合TQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'TQY'

  result=TR1.group(record)
  if result:
    return result

  result=TR2.group(record)
  if result:
    return result

  result=TS1.group(record)
  if result:
    return result

  result=TS2.group(record)
  if result:
    return result

  result=TT1.group(record)
  if result:
    return result

  result=TT2.group(record)
  if result:
    return result

  result=TU1.group(record)
  if result:
    return result

  result=TV1.group(record)
  if result:
    return result

  result=TW1.group(record)
  if result:
    return result

  message('不符合MDCT的ADRG入组条件')

