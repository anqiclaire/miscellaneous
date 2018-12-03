import glob
import csv
files = glob.glob("*.txt")
output = []
for file in files:
    line = []
    with open(file, 'r') as f:
        acc = f.read().split()[-1]
    config = file.strip(".txt").split("_")
    if config[1] == 'LSTM':
        del config[1]
    line.append(config[1]) #L/S
    line.append(config[2]) #n_neurons
    line.append(config[3]) #alpha
    line.append(acc)
    output.append(line)
with open('summary_oh.csv','w') as f:
    writer = csv.writer(f, lineterminator='\n')
    writer.writerow(['L/S', 'n_neurons', 'alpha', 'accuracy'])
    for line in output:
        writer.writerow(line)
        
