from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCH_DRG

def group(record):
  adrg_zd=["A18.817+K87.1*","B67.000x001+K77.0*","B67.500x001+K77.0*","B67.800x001+K77.0*","C22.000","C22.100","C22.101","C22.200","C22.900","C23.x00","C24.000x007","C24.001","C24.002","C24.003","C24.100","C24.101","C25.000","C25.100","C25.701","C25.801","C25.900","C78.700","C78.800x009","C78.808","D13.500x001","D13.501","D13.600","D18.013","D37.700x003","D37.705","D37.706","I72.800x072","K70.306+I98.3*","K72.100","K74.100","K74.300x006+I98.3*","K74.602","K74.603","K74.605","K74.607","K74.615+I98.3*","K74.617+I98.3*","K74.619+I98.2*","K75.000","K76.807","K76.808","K76.814","K80.101","K80.303","K80.304","K80.305","K80.501","K80.503","K80.504","K82.800x004","K83.109","K83.502","K85.102","K85.813","K85.900x003","K86.100x002","K86.200","K86.809","Q44.400","Q44.504","Q44.601","R93.302","S36.100x021","S36.100x081","S36.102","S36.200x001","S36.201"]
  adrg_zd1=[]
  adrg_ss=["50.2200x004","50.2200x007","51.3700x003","38.6600x002","39.1x07","39.1x10","50.2200","50.2200x005","50.2200x006","50.2200x007","50.2200x008","50.2201","50.2202","50.2203","50.2204","50.2205","50.3x01","50.3x02","50.3x03","50.3x05","51.3601","51.3602","51.3700x003","51.3704","52.5100x001","52.5101","52.5103","52.5201","52.5202","52.5205","52.5206","52.5901","52.5902","52.5903","52.5904","52.5905","52.5906","52.6x01","52.6x03","52.7x00","52.7x00x004","52.7x01","52.9601"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HB11_group(record):
      return 'HB11'

    if MDCH_DRG.HB15_group(record):
      return 'HB15'

    return 'HB1'
  else:
    return ''
