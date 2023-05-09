from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCN_DRG

def group(record):
  adrg_zd=["C51.000","C51.200","C51.900","C52.x00","C53.900","C54.100","D06.000","D06.100","D06.900","D06.900x002","D07.000","D07.100","D07.100x002","D07.200x002","D25.000","D25.000x002","D25.100x001","D25.100x002","D25.900","D25.900x001","D25.901","D26.000","D26.100x002","D26.700","D26.900","D28.000","D28.100","D39.100x003","D39.701","N70.905","N71.102","N71.902","N72.x00x003","N72.x00x006","N72.x02","N73.003","N73.604","N73.902","N73.903","N75.000","N75.100","N75.802","N76.000x003","N76.400","N76.600","N76.801","N80.001","N81.200","N81.202","N81.301","N81.400","N81.601","N81.801","N81.802","N83.201","N84.001","N84.100","N84.200","N84.300","N85.001","N85.101","N85.600","N85.804","N85.807","N85.814","N86.x00x004","N87.000","N87.001","N87.002","N87.100","N87.101","N87.200x001","N87.901","N88.102","N88.300","N88.400","N88.803","N88.807","N88.808","N89.001","N89.200","N89.805","N89.806","N89.808","N89.901","N90.302","N90.400","N90.402","N90.403","N90.404","N90.700","N90.800x009","N90.800x010","N90.800x011","N90.804","N90.807","N90.808","N93.801","N93.901","N94.806","N95.000","Q52.101","Q52.300","Q52.400x006","Q52.402","R93.800x006","R93.803","S30.200x007","S30.200x010","S31.400x001","S31.401","T19.202","T83.303","T83.305"]
  adrg_zd1=[]
  adrg_ss=["67.0x00","67.0x00x002","67.2x00","67.2x01","67.3100","67.3200","67.3201","67.3202","67.3203","67.3302","67.3900x001","67.3902","67.3903","67.3904","67.3905","67.4x00x005","67.4x01","67.4x03","67.4x05","67.4x07","67.5100","67.5101","67.5900x002","67.5901","67.6901","70.1100","70.1201","70.1202","70.1400x012","70.1404","70.1406","70.1408","70.3300x003","70.3301","70.3302","70.3303","70.4x01","70.4x03","70.4x04","70.7100","70.7600","70.7902","70.7903","70.7905","70.7906","70.7908","71.0100x002","71.0900x001","71.0900x004","71.0900x006","71.0902","71.2100x001","71.2200x001","71.2200x002","71.2300x001","71.2400x001","71.2400x003","71.2900x002","71.3x00x001","71.3x00x011","71.3x00x025","71.3x01","71.3x03","71.3x04","71.3x05","71.5x00x001","71.5x00x003","71.7101","71.7102","98.1601","98.1700x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合NF1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCN_DRG.NF19_group(record):
      return 'NF19'

    return 'NF1'
  else:
    return ''
