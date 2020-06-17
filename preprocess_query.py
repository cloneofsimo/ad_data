import json
data = {}
with open("query.json") as f1:
    data = json.load(f1)
print(data)

f2 = open("execute_transformation.bat",'w')

cmd_string = "C:/Users/clone/Anaconda3/envs/BITCOIN/python.exe c:/Users/clone/Documents/2020spring/perstyle/style_transfer_application/ad_result/evaluate.py --in_path ./clients/XXX --out_path ./result --checkpoint_dir ./checkpoints/YYY"

if data["gender"] == "male":
    if int(data["age"]) > 30:
        cmd_string = cmd_string.replace("XXX", "bmw")
    else:
        cmd_string = cmd_string.replace("XXX", "nike")
else:
    cmd_string = cmd_string.replace("XXX", "dior")

if int(data["age"]) >= 50:
    cmd_string = cmd_string.replace("YYY", "chk_3")
if int(data["age"]) >= 20:
    cmd_string = cmd_string.replace("YYY", "chk_1")
if int(data["age"]) >= 0:
    cmd_string = cmd_string.replace("YYY", "chk_2")

print(cmd_string)
f2.write(cmd_string)
f2.close()