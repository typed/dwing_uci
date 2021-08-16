import os
for root,dirs,files in os.walk(r".\img"):
    for file in files:
        src = os.path.join(root, file)
        des = src.replace("img", "img_hci")
        des_dir = os.path.dirname(des)
        if not os.path.exists(des_dir):
            os.makedirs(os.path.dirname(des))
        cmd = "imgdec {0} - | ucienc - -o \"{1}.hci\" -q 10 -Q 10".format(src,des)
        #print(cmd)
        os.system(cmd)