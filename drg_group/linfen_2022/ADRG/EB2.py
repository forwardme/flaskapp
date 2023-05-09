from drg_group.linfen_2022.Base import message,intersect,SS_VALID
from drg_group.linfen_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["32.0900x004","32.0901","32.0902","32.2100","32.2100x001","32.2100x005","32.2101","32.2200","32.2300x001","32.2400x001","32.2400x002","32.2400x003","32.2700","32.2801","32.2802","32.2803","32.2804","32.2900x005","32.2900x016","32.2901","32.2902","32.2904","33.0x00x003","33.0x01","33.0x02","33.0x03","33.0x04","33.1x00x003","33.1x00x004","33.1x01","33.1x02","33.1x03","33.1x04","33.1x05","33.1x06","33.2000","33.2000x002","33.2500x002","33.2500x003","33.2800x001","33.4805","33.7101","33.7102","33.7301","33.7302","33.7802","33.7900x001","33.7900x003","33.7901","33.9101","33.9200x002","33.9300x001","33.9300x002","33.9900x002","34.0200x001","34.0600","34.0900x010","34.2000","34.2100x001","34.2301","34.2700x001","34.4x00x008","34.5901"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合EB2入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCE_DRG.EB21_group(record):
      return 'EB21'

    if MDCE_DRG.EB23_group(record):
      return 'EB23'

    if MDCE_DRG.EB25_group(record):
      return 'EB25'

    return 'EB2'
  else:
    return ''

