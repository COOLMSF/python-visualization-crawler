import os
import subprocess

# Read all files in topic directory
all_csv_files = os.listdir('topic')

for csv_file in all_csv_files:
    csv_filename = "topic/" + csv_file
    # handle filename
    csv_filename_with_emotion = csv_filename.split(".")[0] + "_emotion.txt"
    f_emotion_csv = open(csv_filename_with_emotion, "w")
    with open(csv_filename) as f_csv:
        csv_lines = f_csv.readlines()
        # handle every lines
        for csv_line in csv_lines:
            comment = csv_line.split(",")[6]
            # get emotion from eval.py
            cmd = "/bin/python keras-bert-emotional-classifier/eval.py %s" % comment
            try:
                comment_emotion = subprocess.check_output(cmd)
            except:
                print("run %s error" % cmd)
                os.exit(-1)
            # save to csv_filename_emotion file
            f_emotion_csv.write(csv_line + "," + comment_emotion)