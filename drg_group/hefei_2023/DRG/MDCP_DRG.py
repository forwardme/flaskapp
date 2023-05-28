from drg_group.hefei_2023.Base import has_mcc,has_cc,intersect
def PS1Z_group(record):
    return record.weight<1000
def PB19_group(record):
  return True
def PJ19_group(record):
  return True
def PC11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PK11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PR11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS21_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS31_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PS41_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PU11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PV11_group(record):
  return len(record.zdList)>1 and has_mcc(record.zdList[0],record.zdList[1:])
def PC13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PK13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PR13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PS13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PS23_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PS33_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PS43_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PU13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PV13_group(record):
  return len(record.zdList)>1 and has_cc(record.zdList[0],record.zdList[1:])
def PC15_group(record):
  return True
def PK15_group(record):
  return True
def PR15_group(record):
  return True
def PS15_group(record):
  return True
def PS25_group(record):
  return True
def PS35_group(record):
  return True
def PS45_group(record):
  return True
def PU15_group(record):
  return True
def PV15_group(record):
  return True

