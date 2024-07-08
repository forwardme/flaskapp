from flask import Flask, request, render_template, flash, redirect, session
from backend import MakeRecord, vbv2csv, cross_merge, WEIGHT_TUPLE, DRG10_DIC, DRG9_DIC, get_icd10_yibao, get_icd9_yibao
from drg_group.chs_drg_11.GroupProxy import GroupProxy

import csv, os
import pandas as pd


app = Flask(__name__)
app.config["TEMP"] = "./tem"
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'


def csv_to_table(tem_path):
    with open(tem_path , 'r') as f:
        reader = csv.reader(f)
        table = dict()
        table["header"] = next(reader)
        table["rows"] = [row for row in reader]
        return table

def csv_to_table_pd(tem_path):
    df = pd.read_csv(tem_path)
    np_array = df.to_numpy()
    header = np_array[0]
    body = np_array[1:]
    table = {"header":header,"rows":body}
    return table

@app.route('/', methods=["GET","POST"])
def index():
    if request.method == "POST":
        # check if the post request has the file part
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        req_file = request.files["file"]
        # If the user does not select a file, the browser submits an
        # empty file without a filename.
        if req_file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        

        print(f"received csv file")
        tem_path = os.path.join(app.config["TEMP"],"upload.csv")
        req_file.save(tem_path)
        print(f"csv saved to Path:",tem_path)
        table = csv_to_table_pd(tem_path)

        return render_template("index.html", table = table)

    return render_template("index.html")

@app.route("/grouping", methods=["GET","POST"])
def grouping():
    if request.method == "POST":
        dias = request.form.get("diagnosis")
        opers = request.form.get("operation")

        # if separation is "|" , reconstruct the string with separation ","
        if "|" in dias:
            dias = vbv2csv(dias)
        if "|" in opers:
            opers = vbv2csv(opers)

        # 如果输入为ICD国临版，将其转换为ICD医保版编码
        dias_list = dias.split(",")
        opers_list = opers.split(",")
        dias = ",".join([get_icd10_yibao(dia) for dia in dias_list])
        opers  = ",".join([get_icd9_yibao(oper) for oper in opers_list])

        record = MakeRecord(zdList = dias, ssList = opers).getrecord()
        grouper = GroupProxy()
        result = grouper.group(record)

    
        return render_template("grouping.html", data = result._asdict(), weight = WEIGHT_TUPLE[result.drg])
    return render_template("grouping.html")

@app.route("/combinations", methods = ["GET", "POST"])
def combinations():
    dias = request.form.get("diagnosis")
    opers = request.form.get("operation")


    cross_data = cross_merge(dias, opers)
    grouper = GroupProxy()


    data = []
    for _, value in cross_data.iterrows():
        record = MakeRecord(zdList=value.diagnosis_all, ssList=value.operations_all).getrecord()
        result = grouper.group(record)
        res = {"main_diagnosis": value.diagnosis, "diag_name": DRG10_DIC.get(value.diagnosis), "main_operation": value.operation, "oper_name": DRG9_DIC.get(value.operation) ,"grouping_message": result, "weight": WEIGHT_TUPLE[result.drg]}
        data.append(res)

    return render_template("combinations.html", data = data)