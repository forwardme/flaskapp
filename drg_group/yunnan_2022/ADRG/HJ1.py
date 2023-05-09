from drg_group.yunnan_2022.Base import message,intersect,SS_VALID
from drg_group.yunnan_2022.DRG import MDCH_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["34.8101","34.8102","38.0601","38.0700x003","38.0702","38.0704","38.0705","38.3000","38.6700x003","38.6700x005","38.6702","38.6704","38.7x01","38.7x02","38.7x03","38.7x04","38.8600x004","38.8600x005","38.8601","38.8602","38.8603","38.8604","38.8605","38.8606","38.8608","38.8701","38.8704","38.9100x601","38.9200","39.2600x006","39.2600x007","39.3200x004","39.5000x011","39.5000x021","39.5000x024","39.5006","39.5010","39.5017","39.5900x003","39.9003","39.9012","39.9500x005","39.9500x006","39.9501","39.9600x002","39.9600x003","39.9800x001","39.9801","40.1100x003","40.2100","40.2300","40.2400","40.2900x002","40.2900x018","40.2900x020","40.2900x023","40.2900x029","40.2901","40.2905","40.2906","40.2907","40.2908","40.2909","40.3x00x001","40.3x00x002","40.3x00x003","40.5000","40.5100","40.5101","40.5200","40.5300","40.5301","40.5400x001","40.5400x002","40.5400x003","40.5900x010","40.5906","40.5907","40.5908","40.5909","40.5910","40.5911","40.5912","40.9x00x003","40.9x00x004","40.9x00x008","40.9x00x009","40.9x00x010","40.9x00x012","40.9x00x013","40.9x00x014","40.9x00x015","40.9x00x016","40.9x09","41.1x00","41.2x02","41.2x04","41.4100","41.4200x002","41.4200x003","41.4300","41.4301","41.5x00","41.5x01","41.9300","41.9301","41.9901","42.9100x002","44.3900x003","44.9100x001","44.9100x002","44.9100x005","45.0100x005","45.3200x001","46.3900x002","46.7900x009","46.8500x005","50.0x00x004","50.0x00x008","50.0x00x016","50.0x01","50.0x02","50.0x03","50.0x04","50.0x05","50.1200","50.1400","50.2100","50.2301","50.2302","50.2303","50.2501","50.2502","50.2503","50.2600","50.2900x020","50.2900x021","50.2901","50.2902","50.2903","50.2904","50.2905","50.2906","50.2907","50.2908","50.2909","50.2910","50.6101","50.6900x002","50.6900x003","50.6901","50.9200x001","50.9201","50.9900x003","51.1301","51.1302","51.3100x001","51.8200x001","51.8200x002","51.8200x003","51.8201","52.0100","52.0101","52.0102","52.0900x001","52.0901","52.0902","52.0903","52.0904","52.1200","52.1201","52.2101","52.2102","52.2201","52.2202","52.3x00","52.4x00x004","52.4x00x007","52.4x00x008","52.4x00x009","52.4x00x010","52.4x01","52.4x02","52.4x03","52.4x04","52.4x05","52.4x06","52.4x07","52.8100","52.8400","52.8500","52.8600","52.9500x001","52.9500x002","52.9501","52.9502","52.9503","52.9504","52.9901","54.0x00x002","54.0x00x004","54.0x00x006","54.0x00x010","54.0x00x013","54.0x00x021","54.0x00x022","54.0x00x023","54.0x00x024","54.0x00x025","54.0x01","54.0x02","54.0x03","54.1100","54.1101","54.1201","54.1202","54.1900x001","54.1900x005","54.1900x010","54.1900x011","54.1900x024","54.1902","54.1903","54.1904","54.1907","54.1908","54.1909","54.2100","54.2200x003","54.2301","54.2302","54.2303","54.3x00x004","54.3x00x010","54.3x00x011","54.3x00x027","54.3x01","54.3x02","54.3x03","54.3x04","54.3x05","54.3x06","54.3x07","54.4x00x005","54.4x00x006","54.4x00x007","54.4x00x012","54.4x00x021","54.4x00x035","54.4x00x039","54.4x00x042","54.4x00x048","54.4x00x050","54.4x01","54.4x03","54.4x04","54.4x05","54.4x06","54.4x07","54.4x08","54.4x10","54.4x11","54.4x12","54.4x13","54.4x14","54.4x16","54.5100","54.5100x005","54.5100x009","54.5101","54.5102","54.5103","54.5900x007","54.5901","54.5902","54.5903","54.5904","54.5905","54.6101","54.6301","54.6400","54.6401","54.7100","54.7200x001","54.7300x001","54.7302","54.7400x001","54.7400x002","54.7400x003","54.7400x004","54.7400x005","54.7400x006","54.7401","54.7402","54.7403","54.7404","54.7405","54.7500x002","54.7501","54.7502","54.9300x001","54.9703","54.9900x010","54.9900x011","54.9900x017","54.9904","86.2200x011","86.2800x012"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss and record.ssList and intersect(record.ssList,adrg_ss):
    message('符合HJ1入组条件，匹配规则：主手术匹配、某一手术匹配')
    
    if MDCH_DRG.HJ11_group(record):
      return 'HJ11'

    if MDCH_DRG.HJ13_group(record):
      return 'HJ13'

    if MDCH_DRG.HJ15_group(record):
      return 'HJ15'

    return 'HJ1'
  else:
    return ''

