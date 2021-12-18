import csv
import pandas
import matplotlib.pyplot as plt

def read_data():
    res = dict()
    vac = pandas.read_csv('us_state_vaccinations.csv')
    for _,row in vac.iterrows():
        if row['location'] == 'Illinois':
            res.setdefault(row['date'],[-1,-1])
            res[row['date']][0] = row['people_fully_vaccinated']
    infect = pandas.read_csv('all-states-history.csv')
    for _,row in infect.iterrows():
        if row['state'] == 'IL':
            res.setdefault(row['date'],[-1,-1])
            res[row['date']][1] = row['positive']

    # return three lists for draw
    labels = list()
    blue_vac = list()
    yellow_pos = list()
    for date in res:
        if res[date][0] >0 and res[date][1]>0:
            labels.append(date)
            blue_vac.append(res[date][0])
            yellow_pos.append(res[date][1])
    return (labels,blue_vac,yellow_pos)

def draw_fig(labels,blue,yellow,shift=0):

    if shift>0:
        labels = labels[shift:]
        yellow = yellow[shift:]
        blue = blue[:-shift]
        assert len(labels)==len(yellow)==len(blue)

    width = 0.5
    fig, ax = plt.subplots()
    ax.bar(labels, blue, width,label='vaccine')
    ax.bar(labels, yellow, width,bottom=blue, label='positive')
    ax.set_ylabel('people')
    ax.legend()
    plt.savefig('shift{}'.format(shift))


if __name__ == "__main__":
    print("test")

    labels,blue_vac,yellow_pos = read_data()
    draw_fig(labels,blue_vac,yellow_pos,shift=0)
    draw_fig(labels,blue_vac,yellow_pos,shift=15)

