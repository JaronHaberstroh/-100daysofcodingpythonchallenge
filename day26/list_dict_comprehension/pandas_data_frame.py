import pandas

student_dict = {
    "student": ["Jaron", "Charles", "Charlotte"],
    "scores": [96, 27, 83]
}

student_data_frame = pandas.DataFrame(student_dict)

for (index, row) in student_data_frame.iterrows():
    # print(row)
    if row.student == "Jaron":
        print(row.scores)
