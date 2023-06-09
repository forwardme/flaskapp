from drg_group.chongqing_2022.Base import message,intersect,SS_VALID
from drg_group.chongqing_2022.DRG import MDCV_DRG

def group(record):
  adrg_zd=["S00.102","S07.000","S07.100","S07.800","S07.900","S08.900","S09.100x001","S09.700","S11.800x011","S11.800x021","S18.x00x001","S19.700","S21.100x002","S21.101","S21.200x001","S21.200x002","S21.201","S21.202","S21.203","S21.700","S21.800x011","S21.800x021","S21.800x031","S21.900x001","S21.900x003","S21.901","S23.300","S29.800","S30.201","S31.000x003","S31.000x004","S31.000x005","S31.000x006","S31.003","S31.004","S31.005","S31.006","S31.100","S31.100x002","S31.100x003","S31.100x005","S31.100x007","S31.101","S31.102","S31.700","S31.800x003","S31.800x011","S31.800x012","S31.800x021","S31.800x022","S31.800x031","S31.801","S31.802","S31.803","S31.804","S31.805","S37.700","S37.900","S38.100x002","S38.100x003","S38.100x004","S38.101","S38.300x001","S38.300x002","S38.301","S38.302","S38.303","S39.600","S39.700","S39.900x002","S39.900x004","S39.903","S39.907","S39.908","S41.000","S41.000x002","S41.100","S41.700","S41.800x001","S41.800x011","S41.800x012","S41.800x021","S41.800x022","S41.802","S47.x00x002","S47.x01","S48.000","S48.100x001","S49.900x001","S51.000","S51.700","S51.800x011","S51.800x021","S57.000","S57.900","S58.000x001","S58.100x001","S58.900x001","S61.000x001","S61.000x002","S61.100x001","S61.100x002","S61.700","S61.800x011","S61.800x012","S61.800x013","S61.800x021","S61.800x022","S61.800x023","S61.800x081","S61.900","S61.900x002","S61.900x004","S67.000x001","S67.000x003","S67.001","S67.800x001","S67.800x003","S67.801","S68.000x002","S68.100x002","S68.400x001","S68.800x001","S69.900x001","S69.900x002","S69.900x003","S69.900x004","S71.000","S71.100","S71.700","S71.800x011","S71.800x012","S71.800x021","S71.800x022","S71.801","S77.000","S77.100","S77.200","S78.000","S78.100x001","S79.900x001","S81.000","S81.700","S81.800x011","S81.800x021","S81.800x081","S81.800x082","S81.800x083","S81.900","S87.000","S87.801","S88.000x001","S88.100x001","S91.000","S91.100","S91.200","S91.300x002","S91.300x003","S91.300x812","S91.300x813","S91.300x822","S91.700x002","S91.700x003","S97.000","S97.100","S97.800x002","S97.801","S98.000x001","S98.100x001","S98.200x001","S98.200x002","S99.700x001","S99.700x002","S99.900x001","S99.900x002","T01.000x001","T01.100x001","T01.101","T01.200x001","T01.300x001","T01.302","T01.600x001","T01.900","T01.901","T01.902","T01.903","T01.904","T02.400x001","T02.410","T02.500x001","T02.510","T02.600x001","T02.600x011","T02.610","T02.700x001","T02.710","T04.000x001","T04.100x001","T04.200x001","T04.300x001","T04.400x001","T04.700x001","T04.901","T05.000","T05.100x001","T05.200x001","T05.300","T05.300x002","T05.400x001","T05.500x001","T05.600x001","T05.800x001","T05.800x002","T05.900","T06.300x001","T06.500x001","T06.500x002","T06.501","T07.x00","T09.100","T09.600","T09.800","T09.900","T11.100","T11.600","T11.600x001","T13.100","T13.600","T98.200x011"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd:
    message('符合VR1入组条件，匹配规则：主诊断匹配')
    
    
    if MDCV_DRG.VR11_group(record):
      return 'VR11'

    if MDCV_DRG.VR13_group(record):
      return 'VR13'

    if MDCV_DRG.VR15_group(record):
      return 'VR15'

    return ''
  else:
    return ''
