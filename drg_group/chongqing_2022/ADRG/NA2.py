from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCN_DRG

def group(record):
  adrg_zd=["C45.100","C46.700x001","C51.000","C51.001","C51.100","C51.200","C51.800","C51.900","C52.x00","C53.000","C53.100","C53.800","C53.801","C53.900","C54.000","C54.001","C54.100","C54.200","C54.300","C54.800","C54.900","C55.x00","C56.x00","C56.x00x003","C57.000","C57.000x002","C57.100","C57.101","C57.200","C57.300","C57.300x001","C57.301","C57.400","C57.700","C57.701","C57.702","C57.800x004","C57.800x005","C57.801","C57.802","C57.803","C57.900","C58.x00","C58.x00x002","C58.x00x003","C76.303","C76.307","C77.500x003","C79.600","C79.800x202","C79.800x205","C79.800x206","C79.800x209","C79.800x211","C79.800x213","C79.800x214","C79.800x215","C79.800x216","C79.800x218","C79.800x219","C79.800x220","C79.800x222","C79.800x223","C79.800x228","C79.812","C79.813","C79.814","C79.822","C79.823","C79.824","C79.833","D06.000","D06.100","D06.900","D07.000","D07.100","D07.200","D07.301","D07.302","D07.303","D39.000x001","D39.000x002","D39.100x003","D39.200x001","D39.200x002","D39.202","D39.203","D39.700x001","D39.700x002","D39.900x001"]
  adrg_zd1=[]
  adrg_ss=["38.8700x002","38.8700x008","54.0x01","54.4x00x039","65.0100x002","65.0100x003","65.0101","65.0103","65.0900x003","65.1200x001","65.1300","65.1400","65.2200","65.2400","65.2501","65.2502","65.2504","65.2901","65.2902","65.2904","65.3100","65.3900x001","65.4100","65.4900x001","65.4901","65.5100","65.5200","65.5200x001","65.5300","65.5400","65.6100","65.6101","65.6200x001","65.6300","65.6400","65.7200x001","65.7900x010","65.8100","65.8101","66.0101","66.1100","66.1101","66.4x02","66.5100","66.5102","66.5200","66.5201","66.6101","66.6102","66.6103","66.6104","66.7100x002","66.7401","66.9204","68.0x00x004","68.0x00x006","68.0x00x007","68.2400","68.2401","68.2500x001","68.2501","68.2900x035","68.2900x037","68.2901","68.2904","68.2905","68.2906","68.2911","68.2912","68.3100","68.3100x002","68.3101","68.3102","68.3103","68.3104","68.3105","68.3106","68.3900x003","68.3901","68.3902","68.3903","68.3904","68.3905","68.3906","68.3907","68.4100","68.4101","68.4102","68.4103","68.4104","68.4900x004","68.4901","69.1904","70.3301","70.3305","70.4x00x001","70.4x01","71.3x03","71.6100","71.6200x002"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss:
    message('符合NA2入组条件，匹配规则：主诊断匹配、主手术匹配')
    
    
    if MDCN_DRG.NA29_group(record):
      return 'NA29'

    return ''
  else:
    return ''
