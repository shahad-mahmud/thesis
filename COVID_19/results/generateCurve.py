import matplotlib.pyplot as plt

SW_Y_PTH = "contains stop words"
SW_N_PTH = "no stop words"

models = [1, 2, 3]

SW_Y_precisions = []
SW_N_precisions = []
SW_Y_recalls = []
SW_N_recalls = []

for model in models:
    print(model)
    SW_Y_file_pre = open(SW_Y_PTH + "/model{}_pre.txt".format(model), "r")
    SW_Y_temp_pre = []
    for pre in SW_Y_file_pre:
        SW_Y_temp_pre.append(float(pre))
    SW_Y_precisions.append(SW_Y_temp_pre)
    SW_Y_file_pre.close()

    SW_Y_file_rec = open(SW_Y_PTH + "/model{}_recall.txt".format(model), "r")
    SW_Y_temp_rec = []
    for rec in SW_Y_file_rec:
        SW_Y_temp_rec.append(float(rec))
    SW_Y_recalls.append(SW_Y_temp_rec)
    SW_Y_file_rec.close()

    # -------------------------------------------------

    SW_N_file_pre = open(SW_N_PTH + "/model{}_pre.txt".format(model), "r")
    SW_N_temp_pre = []
    for pre in SW_N_file_pre:
        print(pre)
        SW_N_temp_pre.append(float(pre))
    SW_N_precisions.append(SW_N_temp_pre)
    SW_N_file_pre.close()

    SW_N_file_rec = open(SW_N_PTH + "/model{}_recall.txt".format(model), "r")
    SW_N_temp_rec = []
    for rec in SW_N_file_rec:
        SW_N_temp_rec.append(float(rec))
    SW_N_recalls.append(SW_N_temp_rec)
    SW_N_file_rec.close()

print(SW_Y_precisions)
print(SW_N_precisions)
print(SW_Y_recalls)
print(SW_N_recalls)

colors = ['r', 'b', 'y']
plt.figure()
for i in range(3):
    print(len(SW_Y_recalls[i]), len(SW_Y_precisions[i]))
    plt.plot(SW_Y_recalls[i], SW_Y_precisions[i], colors[i], linestyle=(0, (3, 1, 1, 1)),
             label='model {} SW Y'.format(i + 1))
    plt.plot(SW_N_recalls[i], SW_N_precisions[i], colors[i],
             label='model {} SW N'.format(i + 1))

plt.title('precision - recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend(bbox_to_anchor=(.77, 0.5), shadow=True)
# plt.show()

plt.savefig('train_pre_rec_all.png', format='png', dpi=600)
plt.show()
