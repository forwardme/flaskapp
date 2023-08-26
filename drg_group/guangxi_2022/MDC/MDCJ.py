from drg_group.guangxi_2022.Base import message,intersect,SS_VALID
from drg_group.guangxi_2022.ADRG import JA1_1,JA1_2,JA2_1,JA2_2,JB1,JB2,JB3,JC1,JD1,JD2,JJ1,JR1,JR2,JS1,JS2,JT1,JU1,JV1,JV2,JZ1

def group(record):
  mdc_zd=["A18.400x001","A18.400x006","A18.400x010","A18.400x013","A18.400x014","A18.400x020","A18.400x021","A18.400x022","A18.401","A18.402","A18.403","A18.404","A18.405","A18.406","A18.407","A18.408","A18.409","A18.410","A18.411","A18.412","A18.811","A36.300","A46.x00","A60.100x002","A60.100x002","B00.000","B00.100","B00.100x001","B00.100x004+H62.1*","B00.100x005","B00.101","B00.102","B00.801+L99.8*","B00.804+L99.8*","B07.x00x006","B07.x00x008","B07.x00x010","B07.x00x011","B07.x01","B07.x03","B07.x03","B07.x04","B07.x05","B08.800x007","B09.x00x002","B09.x01","B35.000","B35.000x001","B35.001","B35.002","B35.003","B35.100","B35.100x002","B35.200","B35.300","B35.400","B35.400","B35.500","B35.600","B35.600x002","B35.800x002","B35.800x003","B35.800x004","B35.801","B35.901","B36.000x001","B36.000x003","B36.000x003","B36.100","B36.100","B36.100","B36.100","B36.100","B36.200","B36.200x001","B36.300","B36.300x002","B36.901","B37.200x003","B37.201","B37.202","B37.203","B37.204","B37.205","B37.900x001","B37.900x002","B37.900x003","B38.300","B40.300","B40.301+L99.8*","B40.302+L99.8*","B41.800x002","B43.000","B43.200","B44.800x002","B45.200","B46.300x001+L99.8*","B72.x00","B72.x00x001","B78.100x001+L99.8*","B86.x00","B86.x00x003","B86.x00x004","B86.x00x005","B86.x00x006","B86.x00x007","B87.000x001+L99.8*","B88.000x004+L99.8*","B88.000x006+L99.8*","B88.001+L99.8*","C43.500","C43.501","C43.502","C43.503","C43.504","C43.505","C43.506","C43.507","C43.508","C43.600","C43.600x002","C43.601","C43.602","C43.603","C43.604","C43.605","C43.606","C43.700x001","C43.701","C43.702","C43.703","C43.704","C43.705","C43.706","C43.707","C43.800","C43.900","C43.900x003","C43.901","C44.500","C44.501","C44.502","C44.503","C44.504","C44.505","C44.506","C44.507","C44.508","C44.509","C44.600","C44.601","C44.602","C44.603","C44.604","C44.605","C44.606","C44.700","C44.701","C44.702","C44.703","C44.704","C44.705","C44.706","C44.707","C44.800","C44.900","C44.901","C46.000","C50.000","C50.000x001","C50.001","C50.100","C50.200","C50.300","C50.400","C50.500","C50.600","C50.800","C50.800x005","C50.801","C50.802","C50.803","C50.804","C50.900","C50.900x005","C50.901","C50.902","C79.200","C79.200x001","C79.200x005","C79.200x006","C79.200x007","C79.204","C79.205","C79.800x831","C79.806","C96.200x006","D03.500","D03.500x002","D03.501","D03.502","D03.503","D03.504","D03.600","D03.600x002","D03.601","D03.602","D03.700x001","D03.700x002","D03.701","D03.800","D03.900","D03.900x002","D04.500","D04.501","D04.502","D04.503","D04.504","D04.600x001","D04.601","D04.700x001","D04.701","D04.800","D04.900x001","D05.000","D05.100","D05.700","D05.900","D17.000x004","D17.100x001","D17.100x002","D17.100x003","D17.101","D17.200x001","D17.200x002","D17.200x003","D17.200x004","D17.200x005","D17.300x001","D17.300x002","D17.300x004","D17.300x005","D17.301","D17.500x010","D17.500x011","D17.900x001","D17.900x002","D18.000x010","D18.000x018","D18.000x812","D18.000x816","D18.000x828","D18.000x847","D18.000x848","D18.000x849","D18.000x850","D18.000x851","D18.000x852","D18.005","D18.006","D18.007","D18.008","D22.500","D22.500x008","D22.501","D22.502","D22.503","D22.504","D22.505","D22.506","D22.507","D22.508","D22.509","D22.510","D22.511","D22.600","D22.601","D22.602","D22.700","D22.701","D22.702","D22.900","D22.900x002","D22.900x003","D22.900x017","D22.900x021","D22.901","D23.400x003","D23.401","D23.500","D23.500x003","D23.500x006","D23.500x010","D23.501","D23.502","D23.503","D23.504","D23.505","D23.506","D23.600x001","D23.600x002","D23.601","D23.602","D23.700x001","D23.700x002","D23.701","D23.900","D24.x00","D24.x01","D24.x02","D28.000x001","D36.700x009","D36.716","D48.500x002","D48.500x003","D48.500x004","D48.500x005","D48.500x006","D48.500x007","D48.500x008","D48.500x009","D48.500x010","D48.500x011","D48.500x012","D48.500x014","D48.501","D48.502","D48.503","D48.504","D48.505","D48.506","D48.507","D48.508","D48.509","D48.510","D48.511","D48.512","D48.513","D48.514","D48.515","D48.516","D48.517","D48.600x001","D48.601","D86.300","D86.300x002","E05.906","E10.600x021","E10.600x023","E10.600x024","E10.600x025","E10.600x026","E10.600x027+L99.8*","E10.600x028","E10.600x970","E10.603+L99.8*","E11.600x021","E11.600x023","E11.600x024","E11.600x025","E11.600x026","E11.600x027+L99.8*","E11.600x028","E11.600x970","E11.603+L99.8*","E14.600x021","E14.600x022","E14.600x023","E14.600x024","E14.600x025","E14.600x026","E14.600x027+L99.8*","E14.600x028","E14.600x970","E16.300x003+L54.8*","E50.800x002+L86*","E50.801+L86*","E51.100","E51.100x005+I98.8*","E51.100x006","E83.201","E85.413+L99.0*","I89.000x004","I89.000x013","I89.000x015","I89.000x017","I89.000x026","I89.002","I89.009","I89.100x002","I89.800x012","I89.800x013","I89.800x014","I89.800x015","I89.800x020","I89.800x022","I89.800x024","I89.800x025","I89.800x026","I89.800x027","I89.800x028","I89.800x029","I89.800x030","I89.900","I97.200","L00.x00","L01.000x011","L01.000x012","L01.000x013","L01.001","L01.002","L01.003","L01.004","L01.005","L01.008","L01.100","L02.100","L02.200","L02.200x004","L02.200x009","L02.200x010","L02.201","L02.202","L02.203","L02.205","L02.206","L02.300","L02.401","L02.402","L02.403","L02.800","L02.801","L02.802","L02.803","L02.804","L02.900x001","L02.900x002","L02.900x006","L02.901","L02.902","L02.903","L03.000","L03.000x015","L03.001","L03.002","L03.003","L03.004","L03.101","L03.102","L03.103","L03.104","L03.105","L03.106","L03.107","L03.108","L03.109","L03.200","L03.300","L03.301","L03.302","L03.303","L03.304","L03.305","L03.306","L03.800","L03.801","L03.802","L03.900","L05.000","L05.000x001","L05.900","L05.901","L08.000x001","L08.000x005","L08.000x006","L08.000x007","L08.000x008","L08.000x009","L08.000x010","L08.001","L08.002","L08.003","L08.100","L08.800x005","L08.800x006","L08.800x008","L08.800x011","L08.801","L08.802","L08.803","L08.804","L08.805","L08.900","L08.900x028","L08.901","L08.902","L08.903","L08.904","L08.905","L08.906","L08.907","L08.908","L08.909","L08.910","L08.911","L10.000","L10.100","L10.200","L10.300","L10.400","L10.500","L10.800","L10.800x001","L10.800x002","L10.801","L10.900","L11.000","L11.100","L11.800","L11.900","L12.000","L12.100","L12.101","L12.102+H13.3*","L12.103+H13.3*","L12.200","L12.201","L12.202","L12.300","L12.800","L12.900","L13.000","L13.000","L13.100","L13.101","L13.800","L13.900","L13.901","L20.000","L20.801","L20.801","L20.802","L20.803","L20.804","L20.806","L20.900","L21.000","L21.001","L21.002","L21.100","L21.800","L21.900","L21.901","L22.x00","L22.x01","L23.000","L23.001","L23.002","L23.100","L23.101","L23.200","L23.300","L23.400","L23.500","L23.501","L23.502","L23.503","L23.504","L23.600","L23.700","L23.801","L23.900","L23.901","L24.000","L24.100","L24.200","L24.201","L24.202","L24.203","L24.204","L24.205","L24.206","L24.300","L24.400","L24.500","L24.501","L24.502","L24.503","L24.504","L24.600","L24.601","L24.700","L24.800","L24.800x001","L24.800x002","L24.801","L24.900","L24.901","L25.000","L25.100","L25.200","L25.201","L25.300","L25.400","L25.500","L25.800","L25.900","L26.x00","L26.x01","L27.000x004","L27.000x006","L27.002","L27.003","L27.004","L27.005","L27.100","L27.101","L27.200","L27.201","L27.800","L27.801","L27.900","L28.000","L28.000x006","L28.000x007","L28.001","L28.002","L28.003","L28.100","L28.200","L28.201","L28.202","L28.203","L29.000","L29.100","L29.300","L29.800","L29.801","L29.802","L29.900","L30.000","L30.100","L30.201","L30.202","L30.203","L30.204","L30.300","L30.301","L30.400","L30.400x004","L30.500","L30.500x003","L30.800","L30.801","L30.802","L30.803","L30.804","L30.900","L30.901","L30.902","L30.902","L30.902","L30.903","L30.904","L30.905","L40.000","L40.001","L40.002","L40.003","L40.100","L40.101","L40.102","L40.103","L40.200","L40.300","L40.301","L40.400","L40.500","L40.800","L40.801","L40.802","L40.900","L41.000","L41.000","L41.000x002","L41.100","L41.300","L41.400","L41.500","L41.801","L41.900","L42.x00","L43.000","L43.100","L43.200","L43.301","L43.800","L43.901","L43.902","L44.000","L44.100","L44.200","L44.300","L44.400","L44.800","L44.900","L50.000","L50.100","L50.200","L50.201","L50.202","L50.300","L50.400","L50.500","L50.600","L50.801","L50.802","L50.803","L50.900","L51.000","L51.100","L51.200","L51.802","L51.900","L52.x00","L53.000","L53.100","L53.101","L53.200","L53.300","L53.800","L53.801","L53.900","L53.901","L55.000","L55.100","L55.200","L55.800","L55.900","L56.000","L56.100","L56.200","L56.300","L56.400","L56.401","L56.800","L56.900","L57.000","L57.001","L57.100","L57.200","L57.300","L57.400","L57.500","L57.800x004","L57.800x005","L57.800x006","L57.801","L57.802","L57.803","L57.900","L58.000","L58.100","L58.101","L58.900","L59.000","L59.801","L59.900","L60.000","L60.100","L60.200","L60.201","L60.300","L60.301","L60.400","L60.500","L60.800x004","L60.800x005","L60.800x006","L60.800x007","L60.800x008","L60.800x009","L60.800x010","L60.800x011","L60.800x012","L60.800x013","L60.800x014","L60.800x015","L60.800x016","L60.800x017","L60.800x018","L60.800x019","L60.800x020","L60.800x021","L60.800x022","L60.800x023","L60.800x024","L60.800x025","L60.800x026","L60.800x027","L60.800x028","L60.800x029","L60.800x030","L60.800x031","L60.800x032","L60.800x033","L60.800x034","L60.801","L60.802","L60.803","L60.900","L63.000","L63.100","L63.200","L63.800","L63.900","L64.000","L64.801","L64.900","L65.000","L65.100","L65.200","L65.800x003","L65.800x004","L65.800x005","L65.801","L65.802","L65.901","L65.902","L65.903","L65.904","L66.000","L66.100","L66.200","L66.300","L66.400","L66.800","L66.900","L67.000","L67.100","L67.101","L67.102","L67.103","L67.104","L67.105","L67.106","L67.800","L67.900","L68.000","L68.100","L68.200","L68.300","L68.800","L68.900","L70.000","L70.001","L70.002","L70.003","L70.004","L70.005","L70.100","L70.200","L70.201","L70.202","L70.203","L70.300","L70.400","L70.500","L70.801","L70.802","L70.803","L70.900","L70.900x002","L71.000","L71.100","L71.800","L71.900","L72.000","L72.000x006","L72.000x007","L72.000x010","L72.000x011","L72.100","L72.101","L72.102","L72.103","L72.104","L72.105","L72.106","L72.200","L72.800x001","L72.800x003","L72.800x004","L72.900x001","L72.900x002","L72.900x003","L72.901","L72.902","L72.903","L72.904","L72.905","L73.000","L73.100","L73.200","L73.800","L73.800x005","L73.800x006","L73.800x007","L73.801","L73.802","L73.803","L73.804","L73.805","L73.900","L74.000","L74.001","L74.100","L74.200","L74.300","L74.400","L74.801","L74.900","L75.000","L75.100","L75.200","L75.201","L75.201","L75.800","L75.900","L80.x00","L81.000","L81.100","L81.200","L81.300","L81.400","L81.400x001","L81.401","L81.402","L81.403","L81.404","L81.405","L81.407","L81.500","L81.600","L81.601","L81.700x002","L81.701","L81.702","L81.703","L81.800","L81.800x003","L81.800x005","L81.801","L81.802","L81.803","L81.900","L82.x00","L82.x00","L82.x01","L82.x02","L83.x00","L83.x01","L83.x02","L84.x00x001","L84.x00x002","L84.x01","L85.000","L85.100","L85.200","L85.300","L85.800","L85.801","L85.803","L85.804","L85.900","L85.900x001","L87.001","L87.200","L87.800","L87.900","L88.x00","L89.000","L89.001","L89.002","L89.003","L89.004","L89.005","L89.006","L89.007","L89.008","L89.100","L89.101","L89.102","L89.103","L89.104","L89.105","L89.106","L89.107","L89.108","L89.200","L89.201","L89.202","L89.203","L89.204","L89.205","L89.206","L89.207","L89.208","L89.300","L89.301","L89.302","L89.303","L89.304","L89.305","L89.306","L89.307","L89.308","L89.900","L90.000","L90.100","L90.200","L90.300","L90.400","L90.401","L90.500x006","L90.500x007","L90.500x008","L90.500x009","L90.500x010","L90.500x011","L90.500x012","L90.500x013","L90.500x014","L90.500x015","L90.500x016","L90.500x017","L90.500x018","L90.500x019","L90.500x020","L90.500x021","L90.500x022","L90.500x023","L90.500x024","L90.500x025","L90.500x026","L90.500x027","L90.500x028","L90.500x029","L90.500x030","L90.500x031","L90.500x032","L90.500x033","L90.500x034","L90.500x035","L90.500x036","L90.500x037","L90.500x038","L90.500x039","L90.500x040","L90.500x041","L90.500x042","L90.500x043","L90.500x044","L90.500x045","L90.500x046","L90.500x047","L90.500x048","L90.500x049","L90.500x050","L90.500x051","L90.500x052","L90.500x053","L90.500x054","L90.500x055","L90.500x056","L90.500x057","L90.500x058","L90.500x059","L90.500x060","L90.500x061","L90.500x062","L90.500x063","L90.500x064","L90.500x065","L90.500x066","L90.500x067","L90.500x071","L90.500x072","L90.500x073","L90.500x074","L90.501","L90.502","L90.503","L90.504","L90.505","L90.600","L90.800","L90.801","L90.803","L90.804","L90.805","L90.900x001","L90.901","L90.902","L91.001","L91.002","L91.800","L91.801","L91.900","L92.000","L92.100","L92.200","L92.300","L92.301","L92.302","L92.800","L92.801","L92.901","L92.903","L93.000","L93.001","L93.100","L93.200","L93.200x003","L93.201","L93.202","L94.000","L94.100","L94.200","L94.300","L94.301","L94.400","L94.500","L94.600","L94.800","L94.900","L95.000","L95.100","L95.800","L95.800x004","L95.801","L95.802","L95.900","L95.900x001","L95.901","L97.x00","L98.000","L98.001","L98.101","L98.200","L98.300","L98.400","L98.401","L98.500","L98.501","L98.502","L98.503","L98.600","L98.700x001","L98.701","L98.701","L98.702","L98.800","L98.800x001","L98.800x007","L98.800x010","L98.800x011","L98.800x012","L98.800x013","L98.800x014","L98.800x015","L98.800x016","L98.800x017","L98.800x018","L98.800x020","L98.800x021","L98.800x022","L98.800x023","L98.800x026","L98.800x027","L98.801","L98.802","L98.803","L98.804","L98.900x002","M31.000","M31.000x005","M34.000","M34.100","M34.200","M34.803","M35.600","M54.001","M54.002","M54.003","M79.400","M79.401","M79.403","M79.404","M79.801","M79.802","M79.803","M79.804","M79.805","M79.806","M79.807","M79.809","M79.811","N60.000","N60.000x001","N60.000x002","N60.100","N60.100x002","N60.100x003","N60.101","N60.200","N60.201","N60.202","N60.300","N60.400","N60.801","N60.900","N61.x00x004","N61.x00x013","N61.x00x014","N61.x01","N61.x02","N61.x03","N61.x04","N61.x05","N61.x06","N61.x07","N62.x00","N62.x00x001","N62.x00x004","N62.x00x007","N62.x01","N62.x02","N63.x00","N63.x00","N63.x01","N64.001","N64.002","N64.100","N64.200","N64.200x001","N64.300x001","N64.400","N64.501","N64.502","N64.503","N64.504","N64.801","N64.802","N64.803","N64.804","N64.805","N64.900","Q18.301","Q18.902","Q80.000","Q80.100","Q80.200","Q80.200x002","Q80.300","Q80.400","Q80.800","Q80.800x001","Q80.900","Q81.000","Q81.100","Q81.200","Q81.800","Q81.900","Q82.000","Q82.100","Q82.200","Q82.201","Q82.300","Q82.400","Q82.500x005","Q82.501","Q82.502","Q82.503","Q82.504","Q82.505","Q82.506","Q82.507","Q82.508","Q82.800x001","Q82.800x003","Q82.800x004","Q82.800x006","Q82.800x010","Q82.800x011","Q82.800x018","Q82.800x019","Q82.801","Q82.802","Q82.803","Q82.803","Q82.804","Q82.805","Q82.806","Q82.807","Q82.808","Q82.809","Q82.810","Q82.900","Q83.000","Q83.100","Q83.100x001","Q83.100x002","Q83.200","Q83.300","Q83.800x004","Q83.800x005","Q83.801","Q83.802","Q83.803","Q83.900","Q84.000","Q84.100","Q84.101","Q84.200","Q84.201","Q84.202","Q84.300","Q84.400","Q84.500","Q84.501","Q84.502","Q84.600x001","Q84.600x002","Q84.600x003","Q84.600x004","Q84.601","Q84.602","Q84.800x012","Q84.801","Q84.900","Q85.801","Q85.900","Q85.900x009","Q85.900x022","Q85.900x024","Q85.900x025","Q85.900x026","Q85.900x028","Q85.900x049","Q85.915","R21.x00x001","R21.x00x003","R21.x00x004","R21.x01","R21.x02","R22.000x003","R22.000x004","R22.000x005","R22.002","R22.003","R22.004","R22.005","R22.006","R22.100x001","R22.100x002","R22.200x001","R22.200x002","R22.200x004","R22.202","R22.203","R22.204","R22.205","R22.206","R22.207","R22.300x001","R22.300x002","R22.302","R22.400x002","R22.400x003","R22.402","R22.700x001","R22.700x002","R22.901","R22.902","R22.903","R22.904","R23.400x001","R23.400x003","R23.401","R23.800x001","R23.800x002","R23.801","R58.x02","R60.900x003","R60.900x004","R92.x00","S20.000","S20.101","S20.200","S20.200x003","S20.201","S20.202","S20.300x001","S20.301","S20.400x001","S20.700","S20.800x002","S20.801","S20.802","S20.803","S21.000","S30.000x001","S30.000x003","S30.000x004","S30.001","S30.002","S30.003","S30.100","S30.100x001","S30.100x002","S30.100x004","S30.100x007","S30.101","S30.104","S30.700","S30.800x001","S30.800x002","S30.800x003","S30.800x004","S30.801","S30.900x001","S30.900x002","S30.900x003","S31.001","S31.002","S39.910","S39.911","S40.000x001","S40.000x002","S40.000x003","S40.001","S40.700","S40.701","S40.800x011","S40.800x012","S40.800x021","S40.800x022","S40.800x031","S40.800x032","S40.800x041","S40.800x042","S40.900","S50.000","S50.101","S50.700","S50.701","S50.800x011","S50.800x021","S50.800x031","S50.800x041","S50.800x081","S50.900","S50.901","S60.000x001","S60.100x001","S60.201","S60.202","S60.700","S60.701","S60.800x011","S60.800x012","S60.800x021","S60.800x022","S60.800x023","S60.800x031","S60.800x032","S60.800x033","S60.800x041","S60.800x042","S60.800x043","S60.801","S60.900","S60.900x002","S60.901","S60.902","S70.000","S70.100","S70.700x001","S70.700x002","S70.800x011","S70.800x012","S70.800x021","S70.800x022","S70.800x031","S70.800x032","S70.800x041","S70.800x042","S70.900x001","S70.900x002","S70.900x003","S70.901","S80.000","S80.100x002","S80.101","S80.700","S80.800x011","S80.800x012","S80.800x013","S80.800x021","S80.800x022","S80.800x023","S80.800x031","S80.800x032","S80.800x033","S80.800x041","S80.800x042","S80.800x043","S80.900","S80.901","S90.000","S90.100","S90.200","S90.300x001","S90.300x002","S90.300x003","S90.301","S90.700","S90.800x011","S90.800x012","S90.800x013","S90.800x021","S90.800x022","S90.800x023","S90.800x031","S90.800x032","S90.800x033","S90.800x041","S90.800x042","S90.800x043","S90.900x002","S90.900x003","S90.901","T00.000x001","T00.100x001","T00.200x001","T00.300x001","T00.600x001","T00.800x001","T00.900","T00.900x002","T00.900x003","T00.900x004","T00.900x005","T00.900x006","T00.900x007","T00.901","T00.902","T01.301","T01.800x001","T09.000","T09.000x011","T09.000x021","T09.000x031","T09.000x041","T09.000x051","T11.000","T11.000x021","T11.000x031","T11.000x041","T11.000x051","T11.001","T11.101","T13.000","T13.000x011","T13.000x021","T13.000x031","T13.000x041","T13.000x051","T14.000","T14.000x003","T14.000x011","T14.000x021","T14.000x031","T14.000x041","T14.001","T14.002","T14.003","T14.101","T79.700","T81.800x009","T85.400","T85.401","Z41.000","Z41.100x002","Z41.100x003","Z41.100x004","Z41.100x005","Z41.100x006","Z41.100x007","Z41.100x008","Z41.100x009","Z41.100x010","Z41.100x011","Z41.100x012","Z41.100x013","Z41.100x014","Z41.100x015","Z41.100x016","Z41.100x017","Z41.100x018","Z41.100x019","Z41.100x020","Z41.100x021","Z41.100x022","Z41.100x023","Z41.100x024","Z41.104","Z41.105","Z42.100x001","Z42.200x001","Z42.200x002","Z42.200x003","Z42.201","Z42.202","Z42.203","Z42.204","Z42.205","Z42.300x001","Z42.301","Z42.302","Z42.303","Z42.304","Z42.400x001","Z42.401","Z42.402","Z42.403","Z42.800x001","Z42.800x002","Z42.801","Z52.100"]
  dept_list=[]
  if not (True and record.zdList[0] in mdc_zd):
    return ''
  
  message('符合MDCJ入组条件，匹配规则：主诊断匹配')

  result=JA1_1.group(record)
  if result:
    return result
  result=JA1_2.group(record)
  if result:
    return result
  result=JA2_1.group(record)
  if result:
    return result
  result=JA2_2.group(record)
  if result:
    return result
  result=JB1.group(record)
  if result:
    return result
  result=JB2.group(record)
  if result:
    return result
  result=JB3.group(record)
  if result:
    return result
  result=JC1.group(record)
  if result:
    return result
  result=JD1.group(record)
  if result:
    return result
  result=JD2.group(record)
  if result:
    return result
  result=JJ1.group(record)
  if result:
    return result

  if record.ssList and intersect(SS_VALID,record.ssList):
    message('符合JQY入组条件，存在有效手术操作：'+','.join(set(record.ssList).intersection(SS_VALID)))
    return 'JQY'

  result=JR1.group(record)
  if result:
    return result

  result=JR2.group(record)
  if result:
    return result

  result=JS1.group(record)
  if result:
    return result

  result=JS2.group(record)
  if result:
    return result

  result=JT1.group(record)
  if result:
    return result

  result=JU1.group(record)
  if result:
    return result

  result=JV1.group(record)
  if result:
    return result

  result=JV2.group(record)
  if result:
    return result

  result=JZ1.group(record)
  if result:
    return result

  message('不符合MDCJ的ADRG入组条件')

