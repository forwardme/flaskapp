from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCF_DRG

def group(record):
  adrg_zd=["A52.000x006+I39.1*","A52.000x007+I39.1*","A52.000x011+I39.0*","A52.004+I39.1*","A52.009+I39.3*","I05.000","I05.000x001","I05.100","I05.200","I05.200x001","I05.800","I05.900","I05.900x001","I06.000","I06.100","I06.200","I06.800x001","I06.900","I07.000","I07.000x001","I07.100","I07.100x001","I07.200","I07.200x001","I07.800","I07.900","I07.900x001","I08.000","I08.000x001","I08.000x002","I08.000x003","I08.000x004","I08.000x005","I08.000x006","I08.000x007","I08.000x008","I08.000x009","I08.000x010","I08.001","I08.002","I08.003","I08.004","I08.005","I08.006","I08.007","I08.008","I08.009","I08.100","I08.100x001","I08.100x002","I08.100x003","I08.100x004","I08.100x005","I08.101","I08.102","I08.103","I08.104","I08.200","I08.200x001","I08.200x002","I08.201","I08.300","I08.300x001","I08.300x002","I08.300x003","I08.300x004","I08.300x005","I08.300x006","I08.300x007","I08.301","I08.302","I08.303","I08.304","I08.305","I08.306","I08.800","I08.800x002","I08.800x003","I08.801","I08.900","I08.901","I09.100x001","I09.100x002","I09.801","I09.802","I33.008","I33.009","I33.010","I33.011","I34.000","I34.000x001","I34.001","I34.100","I34.101","I34.102","I34.200","I34.201","I34.202","I34.800x002","I34.800x003","I34.800x005","I34.800x006","I34.801","I34.802","I34.803","I34.900","I35.000","I35.000x002","I35.000x003","I35.100","I35.100x003","I35.101","I35.200","I35.200x001","I35.800x003","I35.801","I35.802","I35.803","I35.804","I35.805","I35.806","I35.807","I35.808","I35.900","I36.000","I36.100","I36.200","I36.800x002","I36.800x003","I36.800x004","I36.800x005","I36.801","I36.900","I37.000","I37.100","I37.200","I37.800","I37.900","I38.x00x002","I38.x00x005","I38.x00x006","I38.x00x007","I38.x01","I38.x02","I38.x03","I42.100x002","I51.100x001","I51.200x001","I51.803","I97.800x016","I97.800x017","I97.800x020","T82.000","T82.000x001","T82.001","T82.003","T82.202","T82.805"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合FT3入组条件，匹配规则：主诊断匹配')
    
    
    if MDCF_DRG.FT31_group(record):
      return 'FT31'

    if MDCF_DRG.FT33_group(record):
      return 'FT33'

    if MDCF_DRG.FT35_group(record):
      return 'FT35'

    return ''
  else:
    return ''
