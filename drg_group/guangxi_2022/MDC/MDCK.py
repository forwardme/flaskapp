from drg_group.guangxi_2022.Base import message,intersect,SS_VALID
from drg_group.guangxi_2022.ADRG import KB1,KC1,KD1,KD2,KE1,KJ1,KR1,KS1,KT1,KU1,KV1,KZ1

def group(record):
  mdc_zd=["C48.000x002","C73.x00","C73.x00x003","C74.000","C74.100","C74.900","C75.000","C75.100","C75.800","C75.900","C79.700","C79.800x839","C79.805","C79.825","D09.300","D09.301","D09.302","D09.303","D09.304","D17.700x029","D18.000x810","D18.000x839","D34.x00","D34.x00x003","D34.x00x005","D34.x01","D35.000","D35.001","D35.100","D35.100x002","D35.200","D35.200x004","D35.200x007","D35.200x008","D35.200x009","D35.200x010","D35.200x011","D35.601","D35.700","D35.800","D35.900","D44.000x001","D44.001","D44.100x001","D44.101","D44.200x001","D44.201","D44.300x001","D44.301","D44.800","D44.800x002","D44.801","D44.802","D44.900x001","D44.901","D81.300","D81.500","E00.000","E00.000x002","E00.100","E00.100x002","E00.100x003","E00.200","E00.200x002","E00.900","E00.900x002","E00.900x004","E00.900x005","E00.901","E01.000","E01.000x002","E01.000x003","E01.100","E01.100x002","E01.100x003","E01.200","E01.200x001","E01.201","E01.800x002","E01.801","E02.x00","E03.000","E03.000x002","E03.000x004","E03.001","E03.100","E03.100x001","E03.100x002","E03.100x004","E03.101","E03.200x003","E03.201","E03.202","E03.300","E03.400","E03.801","E03.802","E03.900","E03.900x006","E03.901","E04.000","E04.001","E04.100","E04.100x005","E04.101","E04.102","E04.103","E04.104","E04.200","E04.200x001","E04.200x003","E04.201","E04.801","E04.900x001","E04.900x006","E04.901","E04.902","E04.903","E04.904","E05.000","E05.001","E05.003","E05.100","E05.200","E05.200x004","E05.201","E05.202","E05.203","E05.300","E05.301","E05.302","E05.400","E05.400x001","E05.500","E05.800x001","E05.800x005","E05.801","E05.802","E05.804","E05.805","E05.806","E05.900x001","E05.905","E06.000","E06.000x003","E06.001","E06.002","E06.100","E06.100x001","E06.100x002","E06.100x003","E06.100x004","E06.200","E06.300","E06.300x001","E06.300x004","E06.300x005","E06.301","E06.303","E06.304","E06.400","E06.400x002","E06.500x001","E06.500x002","E06.500x004","E06.501","E06.502","E06.900","E07.000","E07.000x001","E07.000x002","E07.001","E07.100","E07.100x002","E07.100x003","E07.800x001","E07.800x003","E07.800x004","E07.800x007","E07.800x009","E07.800x011","E07.801","E07.802","E07.803","E07.804","E07.805","E07.806","E07.901","E10.000","E10.000x001","E10.000x002","E10.000x005","E10.000x006","E10.001","E10.002","E10.003","E10.100","E10.100x012","E10.100x031","E10.100x051","E10.100x061","E10.101","E10.102","E10.103","E10.500x021+I79.2*","E10.500x043","E10.500x044","E10.500x045","E10.500x046","E10.500x047","E10.500x048","E10.500x049","E10.500x051","E10.501+I79.2*","E10.503","E10.504","E10.505","E10.600x042","E10.600x043","E10.600x051","E10.600x910","E10.600x911","E10.600x920","E10.600x930","E10.700","E10.700x021","E10.700x024","E10.700x025","E10.700x031","E10.700x032","E10.800","E10.900","E10.900x003","E10.900x004","E10.901","E11.000","E11.000x001","E11.000x005","E11.000x006","E11.001","E11.002","E11.003","E11.100x051","E11.101","E11.102","E11.103","E11.400x311+G99.0*","E11.500x043","E11.500x044","E11.500x045","E11.500x046","E11.500x047","E11.500x048","E11.500x049","E11.500x051","E11.503","E11.504","E11.505","E11.600x042","E11.600x043","E11.600x051","E11.600x910","E11.600x911","E11.600x920","E11.600x930","E11.700x011","E11.700x021","E11.700x024","E11.700x025","E11.700x031","E11.700x032","E11.700x033","E11.800","E11.900","E12.000","E12.100","E12.500","E12.600","E12.700","E12.800","E12.900","E13.000","E13.101","E13.102","E13.600","E13.700","E13.800","E13.900x003","E13.900x006","E13.901","E13.902","E13.903","E13.904","E13.905","E13.906","E13.907","E14.000","E14.000x001","E14.000x002","E14.000x003","E14.000x004","E14.000x005","E14.000x006","E14.100","E14.100x012","E14.100x031","E14.100x051","E14.500x011+I79.2*","E14.500x021+I79.2*","E14.500x041","E14.500x042","E14.500x043","E14.500x044","E14.500x045","E14.500x046","E14.500x047","E14.500x048","E14.500x049","E14.500x050","E14.500x051","E14.600x042","E14.600x043","E14.600x051","E14.600x910","E14.600x911","E14.600x920","E14.600x930","E14.700","E14.700x011","E14.700x021","E14.700x024","E14.700x025","E14.700x031","E14.700x032","E14.800","E14.900x001","E15.x00x001","E15.x00x002","E15.x00x004","E16.000x001","E16.100x001","E16.100x002","E16.100x004","E16.100x005","E16.100x006","E16.100x010","E16.100x013","E16.101","E16.102","E16.103","E16.104","E16.105","E16.106","E16.109","E16.110","E16.112","E16.200","E16.300","E16.300x001","E16.300x002","E16.301","E16.800x001","E16.800x002","E16.800x003","E16.800x004","E16.800x006","E16.800x007","E16.800x011","E16.800x021","E16.800x103","E16.800x104","E16.800x105","E16.800x901","E16.801","E16.802","E16.803","E16.804","E16.900x002","E16.901","E20.000","E20.100","E20.801","E20.802","E20.900","E20.901","E21.000","E21.000x007","E21.001","E21.002","E21.003","E21.004","E21.005","E21.006","E21.100x001","E21.201","E21.300","E21.300x002","E21.301","E21.400x001","E21.400x003","E21.401","E21.402","E21.500","E22.000x001","E22.000x002","E22.000x005","E22.001","E22.002","E22.100","E22.200","E22.801","E22.802","E22.900","E23.000","E23.000x005","E23.000x007","E23.000x008","E23.000x011","E23.000x014","E23.000x015","E23.001","E23.002","E23.003","E23.004","E23.005","E23.006","E23.007","E23.008","E23.009","E23.010","E23.100","E23.200","E23.200x003","E23.200x005","E23.201","E23.202","E23.203","E23.204","E23.300x001","E23.301","E23.302","E23.600x001","E23.600x005","E23.600x008","E23.600x010","E23.600x011","E23.600x014","E23.600x015","E23.600x016","E23.601","E23.602","E23.603","E23.604","E23.605","E23.606","E23.607","E23.608","E23.610","E23.611","E23.612","E23.613","E23.614","E23.615","E23.616","E23.617","E23.618","E23.619","E23.700x001","E23.701","E24.000","E24.000x001","E24.001","E24.100","E24.200","E24.200x001","E24.201","E24.202","E24.300","E24.400","E24.800x001","E24.801","E24.900","E24.901","E24.902","E25.000x007","E25.000x008","E25.001","E25.002","E25.003","E25.004","E25.005","E25.801","E25.802","E25.901","E25.902","E25.903","E26.000","E26.000x003","E26.001","E26.100","E26.800x002","E26.801","E26.802","E26.803","E26.900","E27.000x001","E27.000x002","E27.000x003","E27.000x011","E27.001","E27.100x003","E27.101","E27.200","E27.200x003","E27.300","E27.400x005","E27.400x006","E27.401","E27.402","E27.403","E27.404","E27.405","E27.406","E27.407","E27.500","E27.500x003","E27.501","E27.800x005","E27.800x010","E27.800x012","E27.800x021","E27.801","E27.802","E27.803","E27.804","E27.805","E27.806","E27.807","E27.808","E27.809","E27.810","E27.901","E30.000","E30.000x003","E30.001","E30.002","E30.100","E30.100x002","E30.101","E30.102","E30.103","E30.801","E31.000","E31.001","E31.002","E31.100","E31.800","E31.900","E31.901","E34.000","E34.100","E34.200","E34.300x002","E34.300x003","E34.300x006","E34.301","E34.302","E34.303","E34.304","E34.305","E34.400","E34.500","E34.500x001","E34.500x002","E34.500x005","E34.501","E34.800x006","E34.801","E34.802","E34.803","E34.804","E34.805","E34.900x003","E34.903","E40.x00","E41.x00","E41.x01","E42.x00","E43.x00","E43.x00x001","E43.x00x002","E44.000","E44.100","E45.x00","E45.x00x003","E46.x00x002","E46.x00x003","E46.x00x004","E46.x00x005","E46.x01","E50.100x001+H13.8*","E50.900","E51.800","E51.900","E51.900x001","E52.x00","E52.x00x002","E52.x00x003","E53.000","E53.100","E53.100x001","E53.800x010","E53.800x011","E53.800x012","E53.800x013","E53.802","E53.804","E53.900","E53.901","E54.x00","E55.002","E55.900","E56.000","E56.100","E56.800x001","E56.900","E58.x00","E59.x00","E59.x01","E60.x00","E61.000","E61.100","E61.200","E61.300","E61.400","E61.500","E61.600","E61.700","E61.800","E61.900","E63.000","E63.100","E63.800","E63.900","E64.000","E64.100","E64.200","E64.800","E64.900","E65.x00x002","E65.x00x010","E65.x00x011","E65.x00x013","E65.x01","E65.x02","E65.x03","E65.x04","E65.x05","E65.x07","E65.x08","E65.x09","E65.x10","E65.x11","E65.x12","E65.x13","E66.000","E66.100","E66.200","E66.201","E66.801","E66.900","E66.900x001","E66.901","E67.000","E67.100","E67.200","E67.300","E67.800","E68.x00","E70.000","E70.000x002","E70.100x001","E70.100x004","E70.101","E70.102","E70.200","E70.201","E70.202","E70.203","E70.204","E70.205","E70.300","E70.300x003","E70.300x004","E70.300x005","E70.301","E70.301","E70.800x001","E70.800x002","E70.800x003","E70.900","E71.000","E71.100x003","E71.100x004","E71.100x005","E71.101","E71.102","E71.103","E71.200","E71.300","E71.300x005","E71.300x011","E71.302","E71.304","E71.305","E71.307","E71.308","E71.309","E71.310","E72.001","E72.002","E72.003","E72.004","E72.005","E72.100x003","E72.100x004","E72.100x005","E72.100x006","E72.100x007","E72.101","E72.102","E72.200x002","E72.200x004","E72.200x007","E72.200x008","E72.201","E72.202","E72.203","E72.204","E72.205","E72.300x001","E72.300x002","E72.301","E72.302","E72.303","E72.304","E72.305","E72.306","E72.400","E72.400x001","E72.400x002","E72.401","E72.402","E72.500","E72.500x001","E72.500x002","E72.500x003","E72.500x004","E72.500x005","E72.800x001","E72.800x002","E72.800x004","E72.800x005","E72.900x002","E72.900x004","E72.900x006","E72.901","E72.902","E74.000","E74.000x006","E74.000x007","E74.000x008","E74.000x009","E74.000x010","E74.000x011","E74.000x012","E74.000x013","E74.000x016+I43.1*","E74.001","E74.002","E74.003","E74.004","E74.005","E74.009","E74.100","E74.100x002","E74.100x004","E74.101","E74.200","E74.200x002","E74.201","E74.300x001","E74.300x002","E74.300x003","E74.400","E74.400x005","E74.401","E74.402","E74.403","E74.800x006","E74.800x007","E74.801","E74.802","E74.803","E74.804","E74.900x002","E74.901","E75.500x001","E75.501","E75.502","E75.503","E75.504","E75.505","E75.600x001","E76.000","E76.100","E76.200x001","E76.200x002","E76.200x003","E76.200x004","E76.200x006","E76.200x007","E76.200x008","E76.200x009","E76.200x010","E76.200x011","E76.200x012","E76.201","E76.300","E76.800","E76.900x001","E77.000","E77.000x002","E77.000x003","E77.100x002","E77.100x003","E77.100x004","E77.100x005","E77.100x006","E77.801","E77.900","E78.000","E78.000x003","E78.000x004","E78.000x005","E78.000x006","E78.000x007","E78.001","E78.002","E78.003","E78.100","E78.100x002","E78.100x003","E78.100x004","E78.100x005","E78.100x007","E78.100x008","E78.200","E78.200x008","E78.200x012","E78.201","E78.202","E78.204","E78.205","E78.206","E78.207","E78.208","E78.209","E78.210","E78.300x001","E78.300x002","E78.300x003","E78.300x004","E78.401","E78.402","E78.500","E78.500x001","E78.600","E78.600x001","E78.600x003","E78.600x006","E78.600x007","E78.600x008","E78.600x009","E78.600x010","E78.600x011","E78.601","E78.602","E78.800x002","E78.801","E78.900","E78.901","E79.001","E79.100","E79.800x001","E79.900","E80.300x001","E80.301","E80.302","E80.700","E83.000","E83.000x005","E83.000x006","E83.002","E83.100","E83.200","E83.200x002","E83.300x007","E83.300x010","E83.300x014","E83.300x021+M90.8*","E83.301","E83.302","E83.303","E83.304","E83.305","E83.306","E83.309","E83.401","E83.402","E83.403","E83.500x001","E83.500x007","E83.500x008","E83.500x009","E83.500x011","E83.501","E83.502","E83.503","E83.504","E83.800","E83.900","E84.801","E84.900","E85.200x001","E85.300x002","E85.300x003","E85.400x014","E85.406","E85.800","E85.901","E86.x00x001","E86.x00x003","E86.x00x004","E86.x01","E87.001","E87.101","E87.102","E87.200x002","E87.201","E87.202","E87.203","E87.204","E87.205","E87.206","E87.301","E87.302","E87.303","E87.400","E87.500","E87.501","E87.600","E87.600x002","E87.600x003","E87.600x004","E87.700","E87.701","E87.800x004","E87.801","E87.802","E87.803","E88.000x002","E88.000x003","E88.001","E88.100x001","E88.100x002","E88.100x004","E88.100x005","E88.100x006","E88.101","E88.202","E88.203","E88.203","E88.300","E88.800x004","E88.800x005","E88.800x007","E88.800x008","E88.800x009","E88.800x013","E88.801","E88.802","E88.803","E88.804","E88.806","E88.807","E88.900x010","E88.901","E88.903","E89.000","E89.001","E89.002","E89.100","E89.101","E89.102","E89.200x001","E89.201","E89.300x002","E89.300x003","E89.301","E89.302","E89.303","E89.601","E89.800x002","E89.800x003","E89.801","N25.801","Q85.900x006","Q87.100x904","Q87.800x911","Q87.807","Q89.100","Q89.101","Q89.200x012","Q89.200x203","Q89.200x204","Q89.201","Q89.203","Q89.205","Q89.206","Q89.207","Q90.000","R29.000","R63.801","R64.x00","R73.000","R73.001","R73.002","R73.003","R73.900x001","R74.800x009","R79.801","R81.x00x001","R82.400","R82.401","R94.600","R94.700","R94.801","S37.803"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCK入组条件，匹配规则：主诊断匹配')

  result=KB1.group(record)
  if result:
    return result
  result=KC1.group(record)
  if result:
    return result
  result=KD1.group(record)
  if result:
    return result
  result=KD2.group(record)
  if result:
    return result
  result=KE1.group(record)
  if result:
    return result
  result=KJ1.group(record)
  if result:
    return result

  if record.ssList and intersect(SS_VALID,record.ssList):
    message('符合KQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'KQY'

  result=KR1.group(record)
  if result:
    return result

  result=KS1.group(record)
  if result:
    return result

  result=KT1.group(record)
  if result:
    return result

  result=KU1.group(record)
  if result:
    return result

  result=KV1.group(record)
  if result:
    return result

  result=KZ1.group(record)
  if result:
    return result

  message('不符合MDCK的ADRG入组条件')

