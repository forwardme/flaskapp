from drg_group.zhejiang_2022.Base import message,intersect,SS_VALID
from drg_group.zhejiang_2022.DRG import MDCZ_DRG

def group(record):
  adrg_zd=["S00.102","S01.800x011","S01.800x031","S01.801","S01.803","S02.100","S02.100x002","S02.100x003","S02.100x004","S02.100x006","S02.100x008","S02.100x009","S02.101","S02.102","S02.103","S02.111","S02.112","S02.113","S02.114","S02.700x001","S02.700x002","S02.701","S02.712","S02.900x002","S02.902","S02.911","S06.000","S06.100","S06.200x001","S06.200x002","S06.200x011","S06.200x021","S06.200x031","S06.200x032","S06.200x033","S06.200x081","S06.200x082","S06.201","S06.202","S06.203","S06.204","S06.205","S06.211","S06.300x001","S06.300x002","S06.300x011","S06.300x021","S06.300x031","S06.300x032","S06.300x041","S06.300x042","S06.300x081","S06.300x082","S06.301","S06.302","S06.310","S06.400","S06.401","S06.410","S06.500","S06.500x002","S06.500x004","S06.500x005","S06.500x006","S06.500x007","S06.501","S06.502","S06.510","S06.600","S06.600x002","S06.610","S06.800x002","S06.800x004","S06.800x005","S06.800x007","S06.800x009","S06.801","S06.802","S06.803","S06.804","S06.805","S06.900","S06.901","S06.910","S06.911","S06.912","S07.000","S07.100","S07.800","S07.900","S08.900","S09.000x001","S09.100x001","S09.700","S11.001","S11.002","S11.003","S11.004","S11.201","S11.800x011","S11.800x021","S12.000","S12.000x002","S12.010","S12.100","S12.100x002","S12.100x003","S12.110","S12.200x011","S12.200x021","S12.200x031","S12.200x041","S12.200x051","S12.210","S12.700","S12.710","S12.801","S12.802","S12.803","S12.804","S12.805","S12.810","S12.811","S12.812","S12.813","S12.814","S12.815","S12.900x001","S12.900x003","S12.900x004","S12.900x005","S12.900x006","S12.910","S13.000","S13.100","S13.100x021","S13.100x022","S13.100x031","S13.100x032","S13.100x041","S13.100x042","S13.100x051","S13.100x052","S13.100x061","S13.100x062","S13.100x071","S13.100x072","S13.100x081","S13.100x082","S13.101","S13.102","S13.103","S13.104","S13.200x003","S13.201","S13.202","S13.203","S13.300","S14.001","S14.002","S14.100x011","S14.100x021","S14.100x022","S14.100x031","S14.100x032","S14.100x033","S14.100x701","S14.100x711","S14.100x721","S14.100x731","S14.100x741","S14.100x751","S14.100x761","S14.100x771","S14.100x781","S14.101","S14.200","S14.200x001","S14.300","S14.601","S15.001","S15.002","S15.003","S15.004","S15.005","S15.100","S15.200","S15.300","S15.301","S15.900x001","S17.000x001","S17.000x002","S17.001","S17.900","S18.x00x001","S19.700","S21.100","S21.100x002","S21.101","S21.200x001","S21.200x002","S21.201","S21.202","S21.203","S21.700","S21.800x011","S21.800x021","S21.800x031","S21.900x001","S21.900x003","S21.901","S22.000x003","S22.000x005","S22.000x006","S22.000x007","S22.000x009","S22.000x011","S22.000x021","S22.000x031","S22.000x041","S22.000x051","S22.000x061","S22.010","S22.100","S22.110","S22.200","S22.210","S22.300","S22.300x011","S22.310","S22.400","S22.400x011","S22.400x021","S22.400x031","S22.400x041","S22.410","S22.500","S22.900","S22.910","S23.000","S23.300","S24.000x002","S24.001","S24.100x011","S24.100x021","S24.100x022","S24.100x023","S24.100x024","S24.100x701","S24.100x711","S24.100x721","S24.100x731","S24.100x741","S24.100x751","S24.100x761","S24.100x771","S24.101","S24.200","S24.300","S24.300x001","S24.400","S24.400x001","S24.400x002","S24.400x003","S24.400x004","S24.400x005","S24.500x001","S24.600","S25.000","S25.001","S25.100x002","S25.101","S25.200x001","S25.201","S25.300x001","S25.301","S25.400","S25.401","S25.500","S25.501","S25.700","S25.800x003","S25.801","S25.802","S25.900","S26.000x001","S26.000x002","S26.010","S26.800x011","S26.800x021","S26.800x031","S26.800x082","S26.800x083","S26.801","S26.810","S26.811","S26.812","S26.813","S26.900","S26.910","S27.000","S27.010","S27.100","S27.110","S27.200","S27.210","S27.300x012","S27.300x081","S27.301","S27.302","S27.303","S27.310","S27.311","S27.312","S27.313","S27.400","S27.401","S27.410","S27.500","S27.501","S27.510","S27.600","S27.610","S27.700","S27.710","S27.800x013","S27.801","S27.802","S27.803","S27.804","S27.805","S27.806","S27.807","S27.808","S27.810","S27.811","S27.812","S27.900","S27.910","S28.000","S28.100","S29.800","S30.201","S31.000x003","S31.000x004","S31.000x005","S31.000x006","S31.003","S31.004","S31.005","S31.006","S31.100","S31.100x002","S31.100x003","S31.100x005","S31.100x007","S31.101","S31.102","S31.700","S31.800x003","S31.800x011","S31.800x012","S31.800x021","S31.800x022","S31.800x031","S31.801","S31.802","S31.803","S31.804","S31.805","S32.000x002","S32.000x011","S32.000x021","S32.000x031","S32.000x041","S32.000x051","S32.010","S32.300","S32.310","S32.400","S32.410","S32.700","S32.701","S32.702","S32.710","S32.711","S32.712","S32.800x021","S32.800x022","S32.800x023","S32.800x024","S32.800x091","S32.800x092","S32.800x093","S32.800x094","S32.800x095","S32.802","S33.000","S34.000x002","S34.001","S34.100x001","S34.100x002","S34.100x003","S34.100x701","S34.100x711","S34.100x721","S34.100x731","S34.100x741","S34.100x751","S34.100x761","S34.200x001","S34.200x002","S34.300","S34.400","S34.600","S34.601","S34.602","S34.800x001","S34.801","S34.802","S34.803","S35.000","S35.001","S35.100","S35.100x003","S35.101","S35.102","S35.200x001","S35.200x003","S35.200x004","S35.200x005","S35.200x006","S35.200x007","S35.201","S35.202","S35.203","S35.204","S35.205","S35.300x001","S35.300x002","S35.300x003","S35.300x004","S35.300x005","S35.301","S35.302","S35.400x001","S35.400x002","S35.401","S35.402","S35.500x001","S35.500x004","S35.500x005","S35.500x006","S35.500x007","S35.500x008","S35.700x001","S35.700x004","S35.800x001","S35.800x002","S35.801","S35.900x001","S35.901","S35.902","S35.903","S36.000","S36.000x021","S36.000x031","S36.000x081","S36.001","S36.002","S36.011","S36.100x001","S36.100x011","S36.100x013","S36.100x021","S36.100x031","S36.100x041","S36.100x051","S36.100x081","S36.101","S36.102","S36.103","S36.110","S36.111","S36.112","S36.113","S36.200","S36.200x001","S36.200x011","S36.200x021","S36.200x031","S36.200x091","S36.200x092","S36.201","S36.202","S36.210","S36.300","S36.301","S36.310","S36.400","S36.400x091","S36.400x093","S36.400x095","S36.401","S36.402","S36.403","S36.404","S36.405","S36.411","S36.412","S36.413","S36.414","S36.500","S36.500x011","S36.500x021","S36.500x031","S36.500x041","S36.500x091","S36.500x092","S36.500x093","S36.501","S36.511","S36.600","S36.600x003","S36.601","S36.611","S36.700","S36.701","S36.800x022","S36.801","S36.802","S36.803","S36.810","S36.811","S36.812","S36.813","S36.814","S36.900","S36.901","S36.910","S37.000","S37.000x012","S37.000x013","S37.000x015","S37.000x016","S37.000x022","S37.000x023","S37.000x031","S37.001","S37.002","S37.003","S37.004","S37.010","S37.011","S37.100","S37.101","S37.111","S37.200","S37.200x011","S37.200x022","S37.200x023","S37.200x024","S37.200x081","S37.201","S37.211","S37.300","S37.300x004","S37.300x005","S37.300x011","S37.300x021","S37.300x031","S37.300x081","S37.300x082","S37.300x083","S37.301","S37.302","S37.303","S37.310","S37.400","S37.410","S37.500","S37.510","S37.600","S37.600x002","S37.601","S37.602","S37.610","S37.700","S37.710","S37.801","S37.802","S37.803","S37.804","S37.900","S37.910","S38.000","S38.001","S38.100x002","S38.100x003","S38.100x004","S38.101","S38.200x001","S38.200x002","S38.200x003","S38.200x004","S38.200x005","S38.200x006","S38.300x001","S38.300x002","S38.301","S38.302","S38.303","S39.600","S39.700","S39.900x002","S39.900x004","S39.903","S39.907","S39.908","S41.000","S41.000x002","S41.100","S41.700","S41.800x001","S41.800x011","S41.800x012","S41.800x021","S41.800x022","S41.801","S41.802","S42.200x001","S42.200x011","S42.200x031","S42.200x041","S42.200x091","S42.200x092","S42.202","S42.203","S42.210","S42.300","S42.300x002","S42.301","S42.310","S42.311","S42.400x001","S42.400x041","S42.400x042","S42.400x043","S42.400x051","S42.400x091","S42.400x092","S42.400x093","S42.401","S42.402","S42.403","S42.404","S42.410","S42.700","S42.710","S42.900","S42.910","S44.000x001","S44.100x001","S44.101","S44.200x001","S44.300","S44.500","S44.501","S44.700x001","S44.701","S44.900x001","S44.901","S45.000","S45.001","S45.101","S45.200x002","S45.201","S45.300x001","S45.300x002","S45.301","S45.700x001","S45.701","S45.900x001","S47.x00x002","S47.x01","S48.000","S48.100x001","S49.900x001","S51.000","S51.700","S51.800x011","S51.800x021","S51.901","S52.000x001","S52.000x002","S52.000x012","S52.000x021","S52.000x091","S52.001","S52.002","S52.010","S52.011","S52.100x001","S52.100x002","S52.100x012","S52.100x091","S52.101","S52.102","S52.110","S52.200","S52.200x011","S52.201","S52.210","S52.211","S52.300","S52.300x011","S52.310","S52.400x001","S52.410","S52.500x001","S52.500x002","S52.500x003","S52.500x011","S52.500x021","S52.500x022","S52.500x091","S52.501","S52.502","S52.510","S52.600x001","S52.600x002","S52.610","S52.800x002","S52.801","S52.802","S52.803","S52.804","S52.810","S52.811","S52.812","S52.813","S52.814","S52.900","S54.000x001","S54.001","S54.100x001","S54.101","S54.200x001","S54.700x001","S54.900x001","S55.000x001","S55.100x001","S55.101","S55.200x001","S55.700x001","S55.900x001","S57.000","S57.900","S58.000x001","S58.100x001","S58.900x001","S61.000x001","S61.000x002","S61.100x001","S61.100x002","S61.700","S61.701","S61.702","S61.800x011","S61.800x012","S61.800x013","S61.800x021","S61.800x022","S61.800x023","S61.800x081","S61.900","S61.900x002","S61.900x004","S61.901","S61.902","S62.100x011","S62.100x021","S62.100x031","S62.100x041","S62.100x051","S62.100x061","S62.100x071","S62.100x091","S62.101","S62.110","S62.111","S62.400","S62.410","S64.000x001","S64.000x002","S64.100x001","S64.100x002","S64.200x001","S64.200x002","S64.300","S64.400x001","S64.700x001","S64.800","S64.900x001","S65.000x001","S65.000x002","S65.100x001","S65.100x002","S65.200","S65.300","S65.400","S65.401","S65.500","S65.501","S65.700x001","S65.900x001","S66.800","S67.000x001","S67.000x003","S67.001","S67.800x001","S67.800x003","S67.801","S68.000x002","S68.001","S68.100x002","S68.201","S68.300","S68.400x001","S68.800x001","S68.900","S69.800","S69.900x001","S69.900x002","S69.900x003","S69.900x004","S71.000","S71.100","S71.700","S71.800x011","S71.800x012","S71.800x021","S71.800x022","S71.801","S72.000","S72.000x011","S72.000x021","S72.000x031","S72.000x041","S72.000x051","S72.000x081","S72.000x082","S72.010","S72.100x001","S72.100x002","S72.100x011","S72.101","S72.110","S72.200x001","S72.210","S72.300","S72.310","S72.400x001","S72.400x012","S72.400x013","S72.400x021","S72.400x031","S72.400x041","S72.401","S72.410","S72.700","S72.710","S72.900","S74.000x001","S74.000x002","S74.000x003","S74.100x001","S74.100x002","S74.100x003","S74.700x001","S74.700x002","S74.900x001","S74.900x002","S75.000","S75.000x002","S75.000x003","S75.000x004","S75.000x005","S75.001","S75.100x001","S75.100x002","S75.100x003","S75.200","S75.200x001","S75.700x001","S75.700x002","S75.900x001","S75.900x002","S75.901","S77.000","S77.100","S77.200","S78.000","S78.100x001","S79.900x001","S81.000","S81.700","S81.800x011","S81.800x021","S81.800x081","S81.800x082","S81.800x083","S81.900","S82.000","S82.000x002","S82.000x004","S82.010","S82.100x011","S82.100x012","S82.100x081","S82.100x082","S82.100x084","S82.100x085","S82.100x086","S82.100x087","S82.100x088","S82.100x089","S82.101","S82.102","S82.110","S82.111","S82.200x011","S82.200x081","S82.201","S82.202","S82.203","S82.210","S82.211","S82.212","S82.300x011","S82.300x012","S82.300x081","S82.300x082","S82.300x083","S82.301","S82.310","S82.311","S82.400x001","S82.400x002","S82.400x011","S82.400x012","S82.400x013","S82.400x014","S82.400x091","S82.401","S82.410","S82.411","S82.500","S82.501","S82.510","S82.600","S82.601","S82.610","S82.710","S82.800x081","S82.800x082","S82.801","S82.802","S82.803","S82.810","S82.811","S82.812","S82.900","S82.910","S84.000x001","S84.000x002","S84.100x001","S84.700x001","S84.800x001","S84.800x002","S84.900x001","S85.000","S85.100x002","S85.101","S85.102","S85.200","S85.300x001","S85.400x001","S85.500","S85.700x001","S85.800x001","S85.801","S85.900x001","S86.001","S86.100x001","S86.300x002","S86.300x003","S86.300x004","S86.300x006","S86.700x001","S86.700x002","S86.701","S87.000","S87.801","S88.000x001","S88.100x001","S91.000","S91.100","S91.200","S91.300x002","S91.300x003","S91.300x812","S91.300x813","S91.300x822","S91.301","S91.700","S91.700x002","S91.700x003","S94.200x001","S94.200x002","S94.700x001","S94.900x001","S95.000","S95.100","S95.200","S95.700x001","S95.900x001","S97.000","S97.100","S97.800x002","S97.801","S98.000x001","S98.100x001","S98.200x001","S98.200x002","S99.700x001","S99.700x002","S99.900x001","S99.900x002","T01.000x001","T01.100x001","T01.101","T01.200x001","T01.300x001","T01.302","T01.600x001","T01.800x001","T02.000x001","T02.010","T02.100x001","T02.110","T02.200x001","T02.210","T02.300x001","T02.310","T02.400x001","T02.410","T02.500x001","T02.510","T02.600x001","T02.600x011","T02.610","T02.700x001","T02.710","T02.800x001","T02.810","T03.000x001","T03.000x003","T03.100x001","T03.100x003","T04.000x001","T04.100x001","T04.200x001","T04.300x001","T04.400x001","T04.700x001","T04.901","T05.000","T05.100x001","T05.200x001","T05.300","T05.300x002","T05.400x001","T05.500x001","T05.600x001","T05.800x001","T05.800x002","T06.000x001","T06.500x001","T06.500x002","T09.100","T09.300","T09.300x003","T09.300x004","T09.300x005","T09.300x006","T09.300x007","T09.301","T09.600","T09.800","T09.900","T10.x00","T10.x10","T11.100","T11.400","T11.600","T11.600x001","T13.100","T13.300","T13.600","T79.100x002","T79.500","T79.500x002","T79.501","T79.600","T79.600x003","T79.600x004","T79.600x006","T79.601","T79.602","T79.603"]
  adrg_zd1=[]
  adrg_ss=[]
  adrg_ss1=[]
  adrg_ss2=[]
  dept_list=[]
  if True and record.zdList[0] in adrg_zd and (not record.ssList or not record.ssList[0] in SS_VALID):
    message('符合ZZ1入组条件，匹配规则：主诊断匹配')
    
    if MDCZ_DRG.ZZ11_group(record):
      return 'ZZ11'

    if MDCZ_DRG.ZZ1B_group(record):
      return 'ZZ13'

    return ''
  else:
    return ''

