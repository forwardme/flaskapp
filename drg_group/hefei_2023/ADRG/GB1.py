from drg_group.hefei_2023.Base import message,intersect,SS_VALID
from drg_group.hefei_2023.DRG import MDCG_DRG
from drg_group.hefei_2023.DRG_EX import GB1Z

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["30.3x03","31.7301","34.7300x001","40.5000","40.5200","40.5900x010","40.5900x013","40.5900x015","40.5900x019","40.5902","40.5907","42.3200x006","42.4000","42.4100","42.4100x008","42.4101","42.4102","42.4103","42.4104","42.4200x001","42.4200x002","42.4201","42.4202","42.4203","42.5100","42.5200","42.5200x005","42.5201","42.5202","42.5300x001","42.5401","42.5402","42.5403","42.5500x001","42.5600","42.5800x001","42.5801","42.5802","42.5803","42.5900x001","42.6100","42.6200","42.6300","42.6400x002","42.6401","42.6402","42.6403","42.6500","42.6601","42.6800","42.6900","43.3x00x003","43.3x00x004","43.3x01","43.4201","43.4202","43.4203","43.5x00x003","43.5x00x007","43.5x01","43.5x02","43.5x03","43.6x00x005","43.6x00x006","43.6x01","43.6x02","43.7x00x001","43.7x00x002","43.7x01","43.7x02","43.7x03","43.8100","43.8901","43.8902","43.8903","43.9101","43.9102","43.9900x002","43.9900x003","43.9900x004","43.9901","43.9902","43.9903","43.9904","43.9905","43.9906","44.2100x001","44.2100x002","44.2900x001","44.2901","44.3801","44.3802","44.3803","44.3804","44.3900x003","44.3901","44.3902","44.3903","44.3904","44.6600x002","44.6601","45.6200x005","45.6200x006","45.6203","45.6300x001","51.8300x003","51.8301","52.6x01","52.7x00","52.7x00x003"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合GB1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if GB1Z.group(record):
      return 'GB1Z'

    
    if MDCG_DRG.GB11_group(record):
      return 'GB11'

    if MDCG_DRG.GB13_group(record):
      return 'GB13'

    if MDCG_DRG.GB15_group(record):
      return 'GB15'

    return ''
  else:
    return ''

