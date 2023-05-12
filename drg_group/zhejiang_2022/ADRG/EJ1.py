from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCE_DRG

def group(record):
  adrg_zd=[]
  adrg_zd1=[]
  adrg_ss=["04.0300x012","04.2x10","29.9900","30.0100","30.0900x016","30.0900x021","30.0900x024","30.0900x038","30.0900x039","30.0900x040","30.0901","30.0902","30.1x00","30.2100","30.2101","30.2200","30.2201","30.2202","30.2203","30.2204","30.2900x001","30.2900x002","30.2900x003","30.2900x009","30.2900x013","30.2900x014","30.2901","30.2902","30.2903","30.2904","30.2905","30.2906","30.2907","30.2908","30.2909","30.2910","30.2911","30.2912","30.3x00","30.3x04","30.4x00x002","31.2900x001","31.3x00x001","31.3x00x005","31.3x00x008","31.3x01","31.3x02","31.3x03","31.3x04","31.4501","31.4502","31.5x00x003","31.6100","31.6201","31.6202","31.6300","31.6400","31.6900x013","31.6901","31.6902","31.6903","31.6904","31.6905","31.6906","31.6907","31.6912","31.6913","31.7300x001","31.7501","31.7502","31.7504","31.7900x004","31.9100x001","31.9100x002","31.9201","31.9202","31.9203","31.9204","31.9301","31.9302","31.9303","31.9304","31.9400","31.9500","31.9501","31.9801","31.9802","31.9803","31.9805","31.9806","31.9807","31.9808","31.9902","31.9903","32.0100x004","32.0101","32.0102","32.2600","33.2402","33.2700x001","33.2702","33.3100x001","33.3201","33.3202","33.3300","33.9800","34.0100x002","34.0102","34.0500","34.0900x006","34.2400x001","34.6x00","34.6x01","34.7200","34.8900x002","34.8900x003","34.8900x004","40.1100x005","40.1100x007","40.1100x008","40.1100x009","40.1100x012","40.1900x002","40.2100","40.2200","40.2300","40.2900x002","40.2901","40.3x00x001","40.3x00x002","40.3x00x003","40.3x00x005","40.4000","40.4100","40.4200","40.9x00x003","40.9x00x004","40.9x00x008","40.9x00x009","40.9x00x010","40.9x00x013","40.9x00x014","40.9x00x015","40.9x00x016","54.1900x024","54.1908","96.0500x001","96.0501","96.0502","98.1501","98.1502","98.1503","98.1504","98.1800x001"]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.ssList and record.ssList[0] in adrg_ss:
    message('符合EJ1入组条件，匹配规则：主手术匹配')
    
    if MDCE_DRG.EJ11_group(record):
      return 'EJ11'

    if MDCE_DRG.EJ13_group(record):
      return 'EJ13'

    if MDCE_DRG.EJ15_group(record):
      return 'EJ15'

    return ''
  else:
    return ''

