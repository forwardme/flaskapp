from drg_group.lanzhou_2023.Base import message,intersect,SS_VALID
from drg_group.lanzhou_2023.DRG import MDCC_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["10.0x00x001","10.1x00x001","10.1x00x002","10.2900x001","10.3101","10.3102","10.3200","10.3201","10.3300x002","10.3301","10.3302","10.4100x001","10.4101","10.4102","10.4200x001","10.4201","10.4202","10.4300x002","10.4400x001","10.4401","10.4402","10.4403","10.4900x001","10.4900x003","10.4901","10.4903","10.4904","10.5x01","10.6x00x001","10.6x00x002","10.9900x001","10.9901","11.0x00","11.1x01","11.3200","11.3201","11.3202","11.3203","11.3204","11.3900x001","11.3901","11.4100x001","11.4200","11.4300","11.4901","11.4903","11.5100","11.5101","11.5200","11.5300x001","11.5900x001","11.5900x002","11.5901","11.6000x002","11.6000x003","11.6100","11.6200x002","11.6200x003","11.6300x001","11.6300x002","11.6400x001","11.6400x002","11.6900x001","11.6900x003","11.6901","11.6902","11.7100x001","11.7100x002","11.7100x002","11.7100x005","11.7100x007","11.7101","11.7102","11.7103","11.7104","11.7300x001","11.7300x001","11.7400x001","11.7400x001","11.7500","11.7600","11.7900x001","11.7901","11.7902","11.9100x001","11.9200x001","11.9900x002","12.0200x003","12.3400","12.5900x003","12.6100","12.6200","12.6500x003","12.6500x004","12.6501","12.6502","12.6503","12.6901","12.8100","12.8200x001","12.8300x002","12.8302","12.8303","12.8304","12.8400x002","12.8400x004","12.8401","12.8402","12.8403","12.8404","12.8500x002","12.8600x001","12.8700x005","12.8701","12.8702","12.8703","12.8801","12.8802","12.8900x001","12.8900x007","12.8901","12.8902","12.8903","12.8904","12.9201","12.9202","12.9203","12.9301","12.9302","97.3801","97.3802","98.2100x001","98.2200x001","98.2200x005","98.2203"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合CC1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCC_DRG.CC1A_group(record):
      return 'CC12'

    if MDCC_DRG.CC15_group(record):
      return 'CC15'

    return 'CC1'
  else:
    return ''

