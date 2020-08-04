import matplotlib.pyplot as plt

SW_Y_PTH = "contains stop words"
SW_N_PTH = "no stop words"

models = [1, 2, 3]

precisions = []
recalls = []

for model in models:
    file_pre = open(SW_Y_PTH + "/model{}_pre.txt".format(model), "r")
    temp_pre = []
    for pre in file_pre:
        temp_pre.append(float(pre))
    precisions.append(temp_pre)
    file_pre.close()

    file_rec = open(SW_Y_PTH + "/model{}_recall.txt".format(model), "r")
    temp_rec = []
    for rec in file_rec:
        temp_rec.append(float(rec))
    recalls.append(temp_rec)
    file_rec.close()

print(precisions)
print(recalls)

colors = ['r', 'b', 'y']
plt.figure()
for i in range(len(precisions)):
    plt.plot(recalls[i], precisions[i], colors[i], label='model {}'.format(i + 1))

plt.title('precision - recall curve')
plt.xlabel('Recall')
plt.ylabel('Precision')
plt.legend()
plt.show()
