from drg_group.nanping_2023.Base import message,intersect,SS_VALID
from drg_group.nanping_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["01.0900x006","01.0900x008","01.0900x009","01.1000x001","01.1200","01.1200x001","01.1400","01.1400x001","01.1500","01.1800x002","01.2100x001","01.2300","01.2400x005","01.2400x009","01.2400x013","01.2400x018","01.2401","01.2402","01.2402","01.2403","01.2404","01.2405","01.2406","01.2407","01.2408","01.2409","01.2410","01.2411","01.2413","01.2414","01.2415","01.3101","01.3102","01.3103","01.3104","01.3105","01.3106","01.3107","01.3108","01.3201","01.3202","01.3203","01.3204","01.3205","01.3206","01.3900x002","01.3900x009","01.3900x012","01.3900x017","01.3902","01.3903","01.3904","01.3905","01.3906","01.3907","01.3908","01.3909","01.3910","01.3911","01.4101","01.4102","01.4103","01.4104","01.4105","01.4201","01.4202","01.4203","01.4204","01.5100x001","01.5100x006","01.5100x007","01.5101","01.5102","01.5103","01.5104","01.5105","01.5106","01.5107","01.5108","01.5200","01.5301","01.5302","01.5303","01.5304","01.5900x022","01.5900x030","01.5900x032","01.5900x036","01.5900x037","01.5900x038","01.5900x040","01.5900x041","01.5900x043","01.5900x044","01.5900x044","01.5900x048","01.5900x049","01.5900x050","01.5900x051","01.5901","01.5901","01.5902","01.5903","01.5904","01.5905","01.5906","01.5907","01.5908","01.5909","01.5910","01.5911","01.5912","01.5913","01.5914","01.5915","01.5916","01.5917","01.5918","01.5919","01.5920","01.5921","01.5922","01.5923","01.5924","01.5925","01.5926","01.5927","01.5928","01.5929","01.5931","01.5932","01.5933","01.5935","01.5936","01.5937","01.5938","01.5939","01.5940","01.5941","01.6x00","01.6x01","02.0101","02.0102","02.0300x001","02.0400x003","02.0401","02.0402","02.0500x004","02.0500x005","02.0501","02.0502","02.0503","02.0504","02.0505","02.0600x003","02.0601","02.0602","02.0603","02.0700","02.1100x001","02.1200x001","02.1200x002","02.1200x003","02.1201","02.1202","02.1203","02.1204","02.1205","02.1206","02.1207","02.1208","02.1209","02.1210","02.1211","02.1212","02.1300x001","02.1301","02.1302","02.1400x001","02.1401","02.1402","02.1403","02.1404","02.2102","02.9100","02.9200","02.9401","02.9402","02.9403","02.9404","02.9405","02.9501","02.9502","02.9503","02.9600","02.9901","04.0100x003","04.0101","04.0102","04.0103","04.0200x005","04.0201","04.0202","04.0203","04.0301","04.0303","04.0304","04.0401","04.0402","04.0404","04.0406","04.0701","04.0702","04.0707","04.0708","04.0709","04.0710","04.0711","04.0722","04.0723","04.0724","04.0725","04.0726","04.0729","04.4100x003","04.4100x007","04.4101","04.4102","04.4200x006","04.4200x014","04.4200x016","04.4201","04.4202","04.4203","04.4204","04.4205","04.4206","04.4207","04.4208","04.4209","04.4210","04.4211","04.4213","04.5x00x005","07.1300","07.1400","07.1500","07.1700","07.5100x001","07.5200x001","07.5301","07.5400x001","07.5900","07.6100x002","07.6100x003","07.6200x003","07.6200x007","07.6201","07.6202","07.6301","07.6400x001","07.6500","07.6501","07.6800","07.6900x001","07.7100","07.7200x002","07.7200x003","07.7201","07.7202","07.7203","07.7204","07.7205","07.7901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BB2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BB21_group(record):
      return 'BB21'

    if MDCB_DRG.BB23_group(record):
      return 'BB23'

    if MDCB_DRG.BB25_group(record):
      return 'BB25'

    return 'BB2'
  else:
    return ''

