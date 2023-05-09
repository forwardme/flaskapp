from drg_group.yinchuan_2023.Base import message,intersect,SS_VALID
from drg_group.yinchuan_2023.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O00.100","O00.102","O00.106","O00.107","O00.109","O00.803","O00.807","O00.809","O00.900","O02.100","O03.100x001","O04.000x003","O04.001","O04.100x002","O04.101","O04.300","O04.400","O04.401","O04.402","O04.900x001","O04.901","O04.902","O04.905","O07.100x001","O08.100x002","O08.102","O08.602","O08.803","O08.900","O11.x01","O13.x01","O14.100x002","O24.400","O26.000","O32.101","O34.100x001","O34.102","O34.500x005","O34.800","O34.800x006","O34.800x014","O34.800x018","O35.800x001","O35.800x003","O36.401","O36.601","O41.000","O41.104","O42.000x001","O42.000x002","O42.100x012","O43.200x001","O43.200x002","O44.001","O45.900","O62.201","O68.101","O68.901","O69.101","O70.000","O70.200","O71.100x001","O72.002","O72.003","O72.100","O72.101","O72.201","O72.202","O73.002","O73.102","O88.201","O98.806","O99.101","O99.105","O99.109","O99.312","O99.415","Z39.000x001"]
  adrg_zd1=[]
  adrg_ss=["38.8609","39.7900x019","39.7906","54.1101","65.2901","65.4100","66.3201","66.3900x001","66.3900x004","68.2400","68.2500x001","68.2901","68.2903","68.2906","68.2910","68.2912","68.2913","68.2915","68.2917","68.2918","68.3903","68.4901","69.4900x005","69.4903","69.9100x001","69.9101","74.9100","74.9100x001","75.5100","75.6902","75.6905","75.8x00"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合OD1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCO_DRG.OD19_group(record):
      return 'OD19'

    return 'OD1'
  else:
    return ''

