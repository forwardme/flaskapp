from drg_group.nanping_2023.Base import message,intersect,SS_VALID
from drg_group.nanping_2023.DRG import MDCB_DRG

def group(record):
  adrg_zd=["S01.800x011","S01.800x021","S01.800x031","S01.800x031","S01.801","S02.000","S02.000x003","S02.000x004","S02.000x005","S02.001","S02.002","S02.011","S02.012","S02.100","S02.100x002","S02.100x003","S02.100x004","S02.100x006","S02.100x008","S02.100x009","S02.101","S02.102","S02.103","S02.111","S02.112","S02.113","S02.114","S02.700x001","S02.700x002","S02.900x002","S02.902","S02.911","S04.400","S04.400","S06.000","S06.100","S06.200x001","S06.200x002","S06.200x011","S06.200x021","S06.200x031","S06.200x032","S06.200x033","S06.200x081","S06.200x082","S06.201","S06.202","S06.203","S06.204","S06.205","S06.206","S06.211","S06.300x001","S06.300x002","S06.300x011","S06.300x021","S06.300x031","S06.300x032","S06.300x041","S06.300x042","S06.300x081","S06.300x082","S06.301","S06.302","S06.310","S06.400","S06.401","S06.410","S06.500","S06.500x002","S06.500x004","S06.500x005","S06.500x006","S06.500x007","S06.501","S06.502","S06.510","S06.600","S06.600x002","S06.610","S06.700","S06.700x001","S06.700x002","S06.700x003","S06.700x004","S06.700x005","S06.700x006","S06.700x007","S06.700x008","S06.710","S06.800x002","S06.800x004","S06.800x005","S06.800x007","S06.800x009","S06.800x010","S06.800x011","S06.800x012","S06.800x013","S06.801","S06.802","S06.803","S06.804","S06.805","S06.811","S06.812","S06.813","S06.814","S06.900","S06.901","S06.910","S06.911","S06.912"]
  adrg_zd1=[]
  adrg_ss=["01.0900x006","01.0900x008","01.0900x009","01.1000x001","01.1200","01.1400","01.1500","01.1800x002","01.2100x001","01.2300","01.2400x005","01.2400x009","01.2400x013","01.2400x018","01.2401","01.2402","01.2402","01.2403","01.2404","01.2405","01.2406","01.2407","01.2408","01.2409","01.2410","01.2411","01.2413","01.2414","01.2415","01.2500x003","01.2501","01.2502","01.2503","01.2504","01.2506","01.2507","01.3101","01.3102","01.3103","01.3104","01.3105","01.3106","01.3107","01.3108","01.3201","01.3202","01.3203","01.3204","01.3205","01.3900x002","01.3900x009","01.3900x012","01.3902","01.3903","01.3904","01.3906","01.3907","01.3908","01.3908","01.3909","01.3910","01.3911","01.4101","01.4102","01.4103","01.4104","01.4105","01.4202","01.4203","01.4204","01.5100x001","01.5100x006","01.5100x007","01.5101","01.5102","01.5103","01.5104","01.5105","01.5106","01.5107","01.5108","01.5200","01.5301","01.5302","01.5303","01.5304","01.5900x022","01.5900x030","01.5900x032","01.5900x036","01.5900x037","01.5900x038","01.5900x040","01.5900x041","01.5900x043","01.5900x044","01.5900x044","01.5900x048","01.5900x049","01.5900x050","01.5901","01.5901","01.5902","01.5903","01.5904","01.5905","01.5906","01.5907","01.5908","01.5909","01.5910","01.5911","01.5912","01.5913","01.5914","01.5915","01.5916","01.5917","01.5918","01.5919","01.5920","01.5921","01.5922","01.5923","01.5924","01.5925","01.5926","01.5928","01.5929","01.5931","01.5932","01.5933","01.5935","01.5936","01.5937","01.5938","01.5939","01.5940","01.5941","01.6x00","01.6x01","02.0101","02.0102","02.0300x001","02.0400x003","02.0401","02.0402","02.0500x004","02.0500x005","02.0501","02.0502","02.0503","02.0504","02.0505","02.0600x003","02.0601","02.0602","02.0603","02.0700","02.1100x001","02.1201","02.1202","02.1203","02.1204","02.1205","02.1206","02.1207","02.1208","02.1209","02.1210","02.1211","02.1212","02.1301","02.1302","02.1401","02.1402","02.1403","02.1404","02.2102","02.9100","02.9200","02.9401","02.9402","02.9403","02.9404","02.9405","02.9501","02.9502","02.9503","02.9600","02.9901","04.0100x003","04.0101","04.0102","04.0103","04.0200x005","04.0201","04.0202","04.0203","04.0301","04.0401","04.0402","04.0404","04.0405","04.0406","04.0707","04.0708","04.0709","04.0710","04.0711","04.0722","04.0723","04.0724","04.0725","04.0726","04.0727","04.0728","04.0729","04.1101","04.4100x003","04.4100x007","04.4101","04.4102","04.4200x006","04.4200x007","04.4200x014","04.4200x016","04.4201","04.4202","04.4203","04.4204","04.4205","04.4206","04.4207","04.4208","04.4209","04.4210","04.4211","04.4213","04.5x00x005","07.1300","07.1400","07.1500","07.1700","07.5100x001","07.5200x001","07.5301","07.5400x001","07.5900","07.6100x002","07.6100x003","07.6200x003","07.6200x007","07.6201","07.6202","07.6301","07.6400x001","07.6500","07.6501","07.6800","07.6900x001","07.7100","07.7200x002","07.7200x003","07.7201","07.7202","07.7203","07.7204","07.7205","07.7901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合BB1入组条件，匹配规则：主诊断匹配、主手术匹配、某一手术匹配')
    
    if MDCB_DRG.BB11_group(record):
      return 'BB11'

    if MDCB_DRG.BB13_group(record):
      return 'BB13'

    if MDCB_DRG.BB15_group(record):
      return 'BB15'

    return 'BB1'
  else:
    return ''

