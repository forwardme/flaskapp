from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCF_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["38.9300x001","38.9300x002","38.9300x003","38.9300x004","38.9300x005","38.9300x006","38.9300x007","38.9300x008","87.0800x002","88.4201","88.4202","88.4203","88.4204","88.4205","88.4300","88.4300x002","88.4400x001","88.4402","88.4403","88.4404","88.4405","88.4500","88.4700x001","88.4700x002","88.4701","88.4702","88.4703","88.4704","88.4705","88.4706","88.4707","88.4800x005","88.4800x006","88.4801","88.4900x005","88.4900x006","88.4900x007","88.4901","88.4902","88.4903","88.4904","88.5101","88.5102","88.6000","88.6200x001","88.6400x001","88.6400x002","88.6400x003","88.6401","88.6500x002","88.6500x005","88.6500x006","88.6501","88.6502","88.6503","88.6600x002","88.6601","88.6700x001","88.6701","88.6702","88.6703","99.1000x006","99.1000x007","99.1000x008","99.1000x009","99.1000x010","99.1000x011","99.1001","99.1002","99.1003","99.1004"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合FN2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    
    if MDCF_DRG.FN21_group(record):
      return 'FN21'

    if MDCF_DRG.FN23_group(record):
      return 'FN23'

    if MDCF_DRG.FN25_group(record):
      return 'FN25'

    return ''
  else:
    return ''

