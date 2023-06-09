from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.ADRG import XJ1,XR1,XR2,XS1,XS2,XT1,XT2,XT3

def group(record):
  mdc_zd=["B90.000","B90.001","B90.002","B90.100","B90.101","B90.200","B90.200x002","B90.200x003","B90.201","B90.202","B90.800x004","B90.800x005","B90.800x006","B90.801","B90.802","B90.803","B90.804","B90.901","B90.902","B90.903","B90.904","B91.x00","B92.x00","B94.000","B94.100","B94.101","B94.200","B94.201","B94.800x001","B94.800x003","B94.801","B94.802","B94.900","E89.900","I69.400","I69.800x002","I69.801","I69.802","J95.900","K07.601","M23.200x092","M23.201","M23.202","M23.203","M23.204","M23.205","M23.206","M23.207","M23.208","M23.209","M23.210","M23.211","M23.212","M23.213","M23.214","M23.215","M23.501","M23.800x011","M23.800x021","M23.800x031","M23.800x041","M23.800x094","M23.800x095","M24.100x071","M24.100x072","M24.100x091","M24.102","M24.202","M24.801","M24.803","M24.805","M24.806","M24.807","M24.808","M24.810","N81.800x006","Q85.914","Q87.800x905","Q89.901","Q90.100","Q90.200","Q91.000","Q91.100","Q91.200","Q91.400","Q91.500","Q91.600","Q91.700","Q92.000","Q92.100","Q92.200","Q92.300","Q92.400","Q92.500","Q92.600","Q92.700","Q92.800","Q92.900","Q93.000","Q93.100","Q93.200","Q93.600","Q93.700","Q93.800","Q95.000","Q95.100","Q95.200","Q95.300","Q95.400","Q95.500","Q95.800","Q95.900","Q96.000","Q96.100","Q96.200","Q96.400","Q96.800","Q96.900","Q97.000","Q97.100","Q97.200","Q97.300","Q97.800","Q97.900","Q98.000","Q98.100","Q98.200","Q98.300","Q98.400","Q98.500","Q98.600","Q98.700","Q98.800","Q98.900","Q99.000","Q99.100","Q99.100x003","Q99.101","Q99.102","Q99.200","Q99.800","Q99.801","Q99.802","Q99.900","R10.200x001","R10.201","R11.x01","R11.x02","R11.x03","R13.x00","R17.000","R17.001","R18.x00","R18.x00x001","R18.x00x003","R18.x00x005","R18.x01","R19.000x003","R19.000x008","R19.000x009","R19.000x012","R19.000x013","R19.000x016","R19.001","R19.002","R19.003","R19.004","R23.000","R23.100","R23.100x002","R23.101","R23.200x002","R25.200x001","R25.200x002","R25.200x004","R25.200x005","R25.200x006","R25.200x007","R25.200x008","R25.200x009","R26.100","R26.100x001","R41.000","R41.001","R41.100","R41.200","R41.300x001","R41.800x002","R46.300","R46.500","R46.800x001","R46.801","R47.000x001","R47.000x005","R47.000x006","R47.000x008","R47.001","R47.002","R47.003","R47.004","R47.100x001","R47.100x002","R47.101","R47.801","R47.802","R49.800x003","R49.801","R52.000","R52.100","R52.200","R52.900","R52.901","R53.x00x001","R53.x00x002","R53.x00x003","R53.x00x004","R53.x00x005","R53.x00x006","R53.x00x008","R53.x00x009","R53.x00x010","R53.x00x011","R53.x00x012","R54.x00","R54.x00x002","R54.x00x003","R54.x01","R58.x00x002","R58.x00x006","R60.000","R60.001","R60.100","R60.900","R60.900x003","R60.901","R61.000","R61.001","R61.100","R61.900","R61.901","R62.000x002","R62.000x003","R62.801","R62.802","R62.803","R63.000","R63.100","R63.100x002","R63.200","R63.200x002","R63.300x002","R63.300x003","R63.400","R63.500","R64.x00x002","R68.100x001","R68.100x002","R68.101","R68.200","R68.300","R68.300x002","R68.800x002","R68.800x003","R70.000","R70.100","R70.101","R74.000x001","R74.001","R74.800x003","R74.800x005","R74.800x006","R74.800x007","R74.800x008","R74.801","R74.802","R74.803","R74.804","R74.900x001","R76.000x001","R76.100","R76.100x001","R76.200","R76.200x002","R76.800x001","R76.802","R76.900","R77.000","R77.100","R77.101","R77.200","R77.200x001","R77.800x001","R77.800x002","R77.800x003","R77.800x004","R77.800x006","R77.801","R77.802","R77.803","R77.900","R77.901","R79.000","R79.000x001","R79.000x002","R79.000x003","R79.000x004","R79.000x006","R79.800x003","R79.800x005","R79.803","R79.804","R79.805","R82.100","R82.500x001","R84.900x004","R84.901","R84.902","R84.903","R84.904","R85.901","R85.902","R87.900x001","R87.900x002","R87.900x003","R89.000","R89.100","R89.200","R89.300","R89.400","R89.500","R89.600","R89.700","R89.800","R89.900x001","R89.900x002","R89.900x003","R93.202","R93.301","R93.501","R93.800x002","R93.800x003","R96.100x001","R98.x00x002","R99.x00x002","R99.x01","T69.900","T70.400","T70.900","T73.100","T73.200","T73.300","T73.800","T73.900","T75.200","T78.900","T80.202","T80.203","T80.800","T80.801","T81.601","T82.812","T84.400","T84.700","T84.700x001","T84.900","T84.901","T85.800","T85.801","T85.802","T85.806","T85.902","T86.900","T87.200","T88.901","T90.000","T90.100","T90.102","T90.200","T90.200x008","T90.200x012","T90.201","T90.202","T90.203","T90.204","T90.205","T90.206","T90.207","T90.208","T90.400x001","T90.400x002","T90.400x003","T90.400x004","T90.401","T90.500x002","T90.500x003","T90.800x002","T90.900","T90.901","T91.000x001","T91.000x002","T91.000x003","T91.000x004","T91.001","T91.002","T91.100","T91.101","T91.102","T91.103","T91.104","T91.200","T91.200x002","T91.200x005","T91.201","T91.202","T91.204","T91.205","T91.206","T91.400","T91.401","T91.500x001","T91.500x003","T91.501","T91.502","T91.800x001","T91.800x002","T91.800x003","T91.800x004","T91.800x005","T91.800x006","T91.800x007","T91.800x008","T91.800x009","T91.800x010","T91.802","T91.803","T91.900","T91.900x002","T91.900x003","T92.000","T92.001","T92.100","T92.100x004","T92.100x005","T92.100x008","T92.100x009","T92.100x010","T92.100x011","T92.101","T92.102","T92.103","T92.104","T92.105","T92.106","T92.200","T92.201","T92.202","T92.203","T92.204","T92.300","T92.300x001","T92.300x002","T92.300x005","T92.300x006","T92.300x007","T92.300x008","T92.300x011","T92.300x012","T92.300x013","T92.300x015","T92.300x016","T92.300x017","T92.301","T92.302","T92.303","T92.304","T92.305","T92.306","T92.307","T92.400","T92.400x002","T92.400x003","T92.400x004","T92.400x005","T92.400x006","T92.400x007","T92.400x008","T92.401","T92.402","T92.500x001","T92.500x002","T92.500x003","T92.500x004","T92.500x006","T92.500x007","T92.500x008","T92.500x009","T92.500x010","T92.500x011","T92.500x012","T92.500x013","T92.500x014","T92.500x015","T92.500x016","T92.500x017","T92.500x018","T92.501","T92.502","T92.503","T92.504","T92.505","T92.506","T92.600","T92.600x002","T92.600x003","T92.601","T92.602","T92.603","T92.800x001","T92.800x002","T92.801","T92.900","T93.000","T93.001","T93.100","T93.100x007","T93.101","T93.102","T93.103","T93.104","T93.200","T93.200x001","T93.200x002","T93.200x007","T93.200x008","T93.200x010","T93.200x011","T93.200x012","T93.200x013","T93.200x014","T93.201","T93.202","T93.203","T93.204","T93.205","T93.206","T93.207","T93.208","T93.300x001","T93.300x002","T93.300x003","T93.300x005","T93.300x008","T93.300x009","T93.301","T93.400","T93.400x002","T93.400x003","T93.400x004","T93.400x005","T93.400x006","T93.500x001","T93.500x002","T93.501","T93.600","T93.600x001","T93.600x002","T93.600x003","T93.800","T93.800x001","T93.800x002","T93.800x003","T93.801","T93.900","T94.000","T94.001","T94.002","T94.100","T94.102","T96.x00x001","T96.x00x002","T96.x00x003","T97.x00x003","T97.x01","T97.x02","T98.000","T98.200","T98.200x031","T98.200x032","T98.300x007","T98.301","Z00.001","Z00.300","Z00.300x001","Z00.401","Z00.500x001","Z00.600","Z01.001","Z01.002","Z01.101","Z01.102","Z01.200","Z01.300","Z01.501","Z01.502","Z01.503","Z01.600x001","Z01.600x002","Z01.700","Z01.800x001","Z01.800x002","Z01.800x004","Z01.900","Z02.000","Z02.100","Z02.300","Z02.400","Z02.500","Z02.600","Z03.100","Z03.101","Z03.102","Z03.103","Z03.300","Z03.600x001","Z03.800x701","Z03.800x711","Z03.800x721","Z03.800x731","Z03.802","Z03.803","Z03.900","Z03.900x001","Z04.601","Z04.800","Z04.900","Z09.000x001","Z09.001","Z09.300","Z09.400","Z09.700","Z09.801","Z09.802","Z09.803","Z09.804","Z09.900x001","Z10.000","Z11.000","Z11.100","Z11.200","Z11.300","Z11.400","Z11.500","Z11.600","Z11.800x001","Z11.801","Z11.802","Z11.803","Z11.901","Z11.902","Z12.000","Z12.100","Z12.200","Z12.300","Z12.400","Z12.500","Z12.600","Z12.800","Z12.900x001","Z12.901","Z13.000x001","Z13.001","Z13.100","Z13.200","Z13.300","Z13.300x002","Z13.300x003","Z13.400x001","Z13.500","Z13.500x001","Z13.501","Z13.600","Z13.700","Z13.800x011","Z13.800x021","Z13.800x022","Z13.800x031","Z13.800x032","Z13.800x041","Z13.800x051","Z13.800x061","Z13.801","Z13.900","Z20.000","Z20.001","Z20.100","Z20.200","Z20.300","Z20.400","Z20.500","Z20.600","Z20.701","Z20.702","Z20.801","Z20.802","Z20.900","Z23.000","Z23.100","Z23.200","Z23.300","Z23.400","Z23.500","Z23.600","Z23.700","Z23.800x001","Z24.001","Z24.100","Z24.200","Z24.300","Z24.400","Z24.500","Z24.600","Z24.601","Z25.000","Z25.100","Z25.800x001","Z26.000","Z26.800","Z26.900","Z27.000","Z27.100","Z27.200","Z27.300","Z27.400x001","Z27.800","Z27.900","Z28.000","Z28.100","Z28.101","Z28.201","Z28.800","Z28.900","Z29.000","Z29.100","Z29.101","Z29.200x001","Z29.201","Z29.800","Z29.900","Z30.000x001","Z30.000x002","Z30.000x003","Z30.101","Z30.102","Z30.103","Z30.201","Z30.202","Z30.203","Z30.301","Z30.302","Z30.400x001","Z30.400x003","Z30.400x004","Z30.500x011","Z30.501","Z30.503","Z30.504","Z30.505","Z30.800x001","Z30.800x002","Z30.800x003","Z30.800x004","Z30.800x005","Z30.900","Z31.202","Z31.203","Z31.400x003","Z31.400x004","Z31.401","Z31.402","Z31.500","Z31.600x001","Z31.900","Z32.000x001","Z32.100","Z39.100x001","Z39.100x002","Z39.100x003","Z39.200x001","Z40.000x001","Z40.900x001","Z41.300","Z41.800x002","Z41.801","Z41.900","Z42.000","Z42.900","Z43.000","Z43.000x002","Z43.001","Z43.100","Z43.101","Z43.102","Z43.200","Z43.201","Z43.300","Z43.301","Z43.302","Z43.400x002","Z43.400x003","Z43.400x004","Z43.400x005","Z43.401","Z43.402","Z43.403","Z43.500","Z43.600x002","Z43.601","Z43.602","Z43.603","Z43.604","Z43.700","Z43.801","Z43.802","Z43.900x001","Z44.300","Z45.101","Z45.200","Z45.201","Z45.202","Z45.802","Z45.803","Z45.804","Z45.805","Z45.806","Z45.807","Z45.900","Z46.500x001","Z46.501","Z46.502","Z46.503","Z46.700","Z46.701","Z47.800x003","Z47.800x004","Z47.800x005","Z47.800x006","Z47.800x007","Z47.800x008","Z47.800x009","Z47.800x010","Z47.800x011","Z47.800x012","Z47.800x013","Z47.800x014","Z47.800x015","Z47.800x016","Z47.800x017","Z47.800x018","Z47.800x019","Z47.800x020","Z47.800x021","Z47.800x022","Z47.800x023","Z47.800x024","Z47.800x025","Z47.800x026","Z47.800x027","Z47.800x028","Z47.800x029","Z47.800x030","Z47.800x031","Z47.800x032","Z47.800x033","Z47.800x034","Z47.800x035","Z47.800x036","Z47.900","Z48.000x001","Z48.000x002","Z48.900x001","Z50.000","Z50.100x001","Z50.101","Z50.200","Z50.300","Z50.400x001","Z50.500","Z50.501","Z50.600","Z50.700x001","Z50.800x002","Z50.801","Z50.900x001","Z51.300","Z51.400x002","Z51.400x003","Z51.600","Z51.901","Z52.000","Z52.001","Z52.300x002","Z52.900","Z54.000","Z54.000x002","Z54.000x003","Z54.000x004","Z54.000x005","Z54.000x006","Z54.000x007","Z54.000x008","Z54.000x009","Z54.000x010","Z54.000x012","Z54.000x013","Z54.000x014","Z54.000x015","Z54.000x016","Z54.000x017","Z54.000x018","Z54.000x019","Z54.000x020","Z54.000x021","Z54.000x022","Z54.100","Z54.200x001","Z54.300","Z54.400","Z54.700","Z54.800x001","Z54.800x002","Z54.800x003","Z54.800x004","Z54.800x005","Z54.800x006","Z54.800x007","Z54.800x008","Z54.800x009","Z54.800x010","Z54.900x001","Z57.000","Z57.100","Z57.201","Z57.300","Z57.400","Z57.501","Z57.502","Z57.503","Z57.504","Z57.505","Z57.506","Z57.507","Z57.508","Z57.600","Z57.700","Z57.800","Z57.900","Z58.000","Z58.100","Z58.200","Z58.300","Z58.400","Z58.500","Z58.600","Z58.700","Z59.000x001","Z60.000x001","Z60.100x001","Z60.200x001","Z60.300x002","Z61.000x001","Z61.100x001","Z61.200x001","Z61.300x001","Z61.400x001","Z61.500x001","Z61.600x001","Z61.700x001","Z61.900x001","Z62.000x001","Z62.100x001","Z62.200x001","Z62.300x001","Z62.400x001","Z62.500x001","Z62.600x001","Z63.100x001","Z63.200x001","Z63.300x001","Z63.400x001","Z63.400x002","Z63.400x003","Z63.500x001","Z63.500x002","Z63.500x003","Z63.700x001","Z63.700x011","Z63.700x021","Z63.700x091","Z63.700x092","Z63.700x093","Z63.800x001","Z63.800x002","Z63.800x003","Z63.800x004","Z64.100x001","Z64.400x001","Z64.400x002","Z64.400x003","Z65.100x001","Z65.300x001","Z65.300x002","Z65.300x003","Z65.300x004","Z65.300x005","Z65.400x001","Z65.400x002","Z65.400x003","Z65.500x001","Z65.500x002","Z65.500x003","Z73.100x001","Z74.100x001","Z75.800x001","Z75.900x001","Z76.800x001"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCX入组条件，匹配规则：主诊断匹配')

  result=XJ1.group(record)
  if result:
    return result

  if False and record.ssList and intersect(SS_VALID,record.ssList):
    message('符合XQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'XQY'

  result=XR1.group(record)
  if result:
    return result

  result=XR2.group(record)
  if result:
    return result

  result=XS1.group(record)
  if result:
    return result

  result=XS2.group(record)
  if result:
    return result

  result=XT1.group(record)
  if result:
    return result

  result=XT2.group(record)
  if result:
    return result

  result=XT3.group(record)
  if result:
    return result

  message('不符合MDCX的ADRG入组条件')

