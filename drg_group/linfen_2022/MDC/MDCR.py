from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.ADRG import RA1,RA2,RA4,RB1,RB2,RC1,RD1,RE1,RG1,RR1,RS1,RS2,RT1,RT2,RU1,RV1,RW1,RW2

def group(record):
  mdc_zd=["C45.100x005","C45.103","C45.706","C45.900","C46.300","C46.700","C46.800","C46.900","C46.900x002","C46.900x003","C46.900x004","C48.101","C48.102","C49.901","C76.101","C76.200x002","C76.300","C76.302","C76.305","C76.306","C76.700","C76.700x002","C76.800","C76.801","C77.107","C77.200","C77.202","C77.205","C77.206","C77.300","C77.300x001","C77.300x003","C77.301","C77.302","C77.303","C77.400x001","C77.401","C77.500","C77.501","C77.502","C77.503","C77.800","C77.900","C77.900x001","C78.604","C78.605","C79.800x804","C79.800x811","C79.800x816","C79.800x818","C79.800x837","C79.800x862","C79.811","C79.826","C79.829","C79.900","C79.900x001","C80.000","C80.000x001","C80.001","C80.900","C80.901","C80.902","C80.903","C80.904","C80.905","C81.000","C81.100","C81.200","C81.300","C81.400","C81.700","C81.701","C81.702","C81.703","C81.900","C81.900x005","C82.000","C82.100","C82.200","C82.300","C82.400","C82.500","C82.600","C82.700","C82.701","C82.702","C82.703","C82.704","C82.900","C82.901","C82.903","C83.000","C83.001","C83.002","C83.003","C83.004","C83.100","C83.101","C83.102","C83.300","C83.300x006","C83.300x007","C83.300x008","C83.300x009","C83.301","C83.302","C83.303","C83.304","C83.305","C83.306","C83.307","C83.500","C83.501","C83.502","C83.503","C83.504","C83.505","C83.700","C83.702","C83.703","C83.800","C83.800x006","C83.800x008","C83.800x009","C83.800x009","C83.801","C83.802","C83.803","C83.900","C84.000","C84.000x002","C84.000x003","C84.100","C84.400","C84.400x001","C84.401","C84.402","C84.403","C84.404","C84.405","C84.406","C84.407","C84.500","C84.500x004","C84.500x012","C84.500x016","C84.502","C84.600","C84.601","C84.700","C84.800","C84.900","C84.901","C85.100","C85.100x010","C85.100x017","C85.100x021","C85.200","C85.700","C85.700x004","C85.700x016","C85.701","C85.704","C85.705","C85.707","C85.709","C85.715","C85.900","C85.900x001","C85.900x002","C85.900x003","C85.900x004","C85.900x005","C85.900x006","C85.900x008","C85.900x009","C85.900x010","C85.900x011","C85.900x012","C85.900x013","C85.900x014","C85.900x015","C85.900x016","C85.900x017","C85.900x019","C85.900x020","C85.900x022","C85.900x023","C85.900x024","C85.900x025","C85.900x026","C85.900x027","C85.900x028","C85.900x029","C85.900x030","C85.900x031","C85.900x034","C85.900x036","C85.900x037","C85.900x038","C85.900x039","C85.900x040","C85.900x041","C85.900x042","C85.900x043","C85.901","C86.000","C86.100","C86.200","C86.300","C86.400","C86.500","C86.600","C86.601","C86.602","C86.603","C88.000","C88.000x002","C88.000x011","C88.000x012","C88.200","C88.200x011","C88.200x012","C88.201","C88.202","C88.203","C88.300","C88.301","C88.302","C88.400","C88.401","C88.402","C88.403","C88.700","C88.700x002","C88.700x003","C88.700x012","C88.700x013","C88.701","C88.900","C88.900x001","C90.000","C90.000x004","C90.000x005","C90.000x008+M90.6*","C90.000x009","C90.000x011","C90.000x012","C90.000x014","C90.000x021","C90.000x022","C90.000x023","C90.000x024","C90.000x025","C90.000x026","C90.000x027","C90.000x028","C90.000x029","C90.000x030","C90.000x031","C90.000x032","C90.000x033","C90.000x034","C90.000x035","C90.000x036","C90.000x037","C90.000x038","C90.000x039","C90.000x040","C90.000x041","C90.001","C90.002","C90.002","C90.100","C90.100x002","C90.100x011","C90.200","C90.200x008","C90.200x009","C90.200x013","C90.300","C90.300x001","C90.300x002","C90.300x003","C90.300x004","C90.300x004","C90.301","C90.302","C90.303","C90.303","C91.000","C91.000x006","C91.000x006","C91.000x007","C91.000x009","C91.000x012","C91.000x013","C91.000x014","C91.000x015","C91.000x016","C91.000x017","C91.001","C91.002","C91.003","C91.004","C91.006","C91.007","C91.008","C91.100","C91.100x011","C91.100x012","C91.101","C91.102","C91.300","C91.400","C91.400x004","C91.400x013","C91.401","C91.500","C91.500x011","C91.600","C91.700","C91.701","C91.704","C91.800","C91.800","C91.900","C91.901","C92.000","C92.000x003","C92.000x006","C92.000x011","C92.000x012","C92.000x013","C92.000x014","C92.000x015","C92.000x016","C92.000x017","C92.000x018","C92.001","C92.002","C92.003","C92.004","C92.005","C92.006","C92.007","C92.008","C92.009","C92.100","C92.100x001","C92.100x002","C92.100x004","C92.100x011","C92.100x012","C92.100x014","C92.100x016","C92.100x017","C92.100x018","C92.100x019","C92.101","C92.102","C92.103","C92.200","C92.200x001","C92.200x011","C92.201","C92.300","C92.300x001","C92.300x003","C92.300x011","C92.300x013","C92.400x011","C92.401","C92.402","C92.403","C92.500x011","C92.501","C92.502","C92.600","C92.601","C92.700","C92.700x006","C92.700x012","C92.700x013","C92.701","C92.703","C92.706","C92.800","C92.900","C92.900x001","C92.900x011","C92.901","C93.000x011","C93.000x016","C93.001","C93.002","C93.003","C93.100","C93.100x011","C93.100x012","C93.100x013","C93.101","C93.102","C93.103","C93.104","C93.300","C93.300x001","C93.700","C93.701","C93.900","C93.901","C94.000x001","C94.000x011","C94.001","C94.004","C94.200","C94.200x011","C94.201","C94.202","C94.300","C94.300x011","C94.400","C94.400x001","C94.600","C94.700","C94.700x004","C94.700x014","C94.702","C94.703","C95.000","C95.000x002","C95.000x003","C95.000x015","C95.000x016","C95.000x017","C95.000x018","C95.000x101","C95.000x102","C95.000x115","C95.000x116","C95.000x117","C95.000x118","C95.002","C95.003","C95.004","C95.005","C95.006","C95.100","C95.100x011","C95.100x012","C95.700x001","C95.700x002","C95.700x003","C95.700x011","C95.900","C95.900x003+M36.1*","C95.900x005","C95.900x012","C95.900x013+M36.1*","C95.900x015","C95.901","C96.000","C96.002","C96.004","C96.200","C96.200x005","C96.200x013","C96.201","C96.202","C96.400","C96.400x001","C96.400x002","C96.400x003","C96.400x004","C96.401","C96.402","C96.403","C96.500","C96.501","C96.502","C96.600","C96.601","C96.602","C96.603","C96.604","C96.700","C96.704","C96.705","C96.800","C96.801","C96.900","C97.x00","C97.x01","D09.700","D09.700x001","D09.900","D18.105","D18.106","D18.109","D19.700","D19.900x001","D36.700x011","D36.700x012","D36.700x016","D36.700x021","D36.700x023","D36.700x025","D36.700x028","D36.704","D36.705","D36.709","D36.710","D36.711","D45.x00","D46.001","D46.100","D46.100x002","D46.100x012","D46.200","D46.201x001","D46.203","D46.400","D46.500","D46.600","D46.600","D46.700","D46.700x001","D46.700x002","D46.700x003","D46.700x006","D46.700x007","D46.700x008","D46.900","D46.900x002","D46.900x004","D46.900x006","D46.901","D47.000","D47.001","D47.002","D47.003","D47.004","D47.100","D47.100","D47.100x004","D47.100x007","D47.100x008","D47.100x009","D47.100x017","D47.100x018","D47.100x019","D47.101","D47.200","D47.200x003","D47.200x004+G63.1*","D47.200x005+G63.1*","D47.300","D47.400","D47.401","D47.402","D47.403","D47.404","D47.500","D47.700","D47.700x005","D47.700x006","D47.700x007","D47.700x007","D47.701","D47.702","D47.703","D47.900","D47.900x001","D47.900x002","D48.700x001","D48.700x015","D48.700x023","D48.707","D48.708","D48.715","D48.716","D48.722","D48.723","D48.725","D48.900","D48.901","D48.902","D89.801","Q85.802","Q85.909","Z08.000","Z08.100","Z08.200","Z08.700","Z08.800x001","Z08.800x002","Z08.800x003","Z08.800x004","Z08.900","Z09.100","Z09.200","Z51.000x003","Z51.000x008","Z51.000x012","Z51.000x013","Z51.001","Z51.002","Z51.003","Z51.100x004","Z51.101","Z51.102","Z51.103","Z51.104","Z51.200x008","Z51.500x001","Z51.500x002","Z51.500x003","Z51.800x092","Z51.800x094","Z51.800x095","Z51.800x096","Z51.800x097","Z51.800x921","Z51.800x922","Z51.800x924","Z51.800x925","Z51.800x927","Z51.800x951","Z51.800x952","Z51.800x953","Z51.800x981","Z51.800x983","Z51.801","Z51.802","Z51.804","Z51.805","Z51.806","Z51.807","Z51.808","Z51.809","Z51.810","Z51.811","Z54.001"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCR入组条件，匹配规则：主诊断匹配')

  result=RA1.group(record)
  if result:
    return result
  result=RA2.group(record)
  if result:
    return result
  result=RA4.group(record)
  if result:
    return result
  result=RB1.group(record)
  if result:
    return result
  result=RB2.group(record)
  if result:
    return result
  result=RC1.group(record)
  if result:
    return result
  result=RD1.group(record)
  if result:
    return result
  result=RE1.group(record)
  if result:
    return result
  result=RG1.group(record)
  if result:
    return result

  if record.ssList and record.ssList[0] in SS_VALID:
    message('符合RQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'RQY'

  result=RR1.group(record)
  if result:
    return result

  result=RS1.group(record)
  if result:
    return result

  result=RS2.group(record)
  if result:
    return result

  result=RT1.group(record)
  if result:
    return result

  result=RT2.group(record)
  if result:
    return result

  result=RU1.group(record)
  if result:
    return result

  result=RV1.group(record)
  if result:
    return result

  result=RW1.group(record)
  if result:
    return result

  result=RW2.group(record)
  if result:
    return result

  message('不符合MDCR的ADRG入组条件')

