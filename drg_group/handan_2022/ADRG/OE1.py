from drg_group.handan_2022.Base import message,intersect,SS_VALID
from drg_group.handan_2022.DRG import MDCO_DRG

def group(record):
  adrg_zd=["O00.000","O00.001","O00.100","O00.101","O00.102","O00.103","O00.104","O00.105","O00.106","O00.107","O00.108","O00.109","O00.110","O00.111","O00.112","O00.113","O00.114","O00.115","O00.116","O00.117","O00.200","O00.201","O00.800x006","O00.801","O00.802","O00.803","O00.804","O00.805","O00.807","O00.808","O00.809","O00.900","O00.901","O00.902","O08.000","O08.006","O08.100x003","O08.104","O08.105","O08.106","O08.302","O08.500","O08.600x005","O08.700","O08.806"]
  adrg_zd1=[]
  adrg_ss=["54.1100","54.1101","54.1201","54.5100x009","65.0100x002","65.0100x002","65.0100x003","65.0101","65.0103","65.0105","65.0900x003","65.0900x005","65.0901","65.0905","65.2100","65.2200","65.2400","65.2501","65.2502","65.2505","65.2900x001","65.2900x011","65.2901","65.2902","65.2903","65.2904","65.2906","65.3100","65.3900x001","65.4100","65.4900x001","65.4901","65.5200","65.5200x001","65.5400","65.6100","65.6200x001","65.7100x001","65.7600","65.7900x010","65.7901","65.7905","65.8101","66.0100x006","66.0101","66.0102","66.0103","66.0200","66.0201","66.0202","66.0203","66.1101","66.2101","66.2200x001","66.2900x003","66.2901","66.2903","66.3100","66.3200x001","66.3201","66.3900x001","66.3900x004","66.3901","66.3902","66.4x00","66.4x02","66.5100","66.5102","66.5200","66.5201","66.6100x006","66.6100x011","66.6100x014","66.6102","66.6104","66.6200","66.6200x003","66.6200x004","66.6201","66.6300","66.6301","66.6901","66.6902","66.7100","66.7100x002","66.7200","66.7300","66.7301","66.7400","66.7401","66.7900x009","66.7901","66.7903","66.7905","66.7906","66.8x02","66.9200x001","66.9201","66.9202","66.9203","66.9204","66.9205","66.9500x001","66.9500x004","66.9600x002","66.9700","66.9900","68.2900x035","68.2900x037","68.3903","68.3905","74.3x00x006","74.3x00x010","74.3x00x011","74.3x00x012","74.3x00x012","74.3x00x013","74.3x00x014","74.3x00x015","74.3x00x016","74.3x00x017","74.3x00x018","74.3x00x019","74.3x01","74.3x02","74.3x03","74.3x04","74.3x05","74.3x06","74.3x07","74.3x08","74.3x09"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合OE1入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    if MDCO_DRG.OE19_group(record):
      return 'OE19'

    return ''
  else:
    return ''

