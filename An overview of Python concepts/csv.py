class Table:
    labels=[]
    grows=[]
    def __init__(self, path=None):
        global grows,labels
        with open(path,'r') as file:
            file=file.read()
            file=file.replace('\n',' ').split()
            labels=file[0].split(',')
            for x in file[1:]:
                grows.append(x.split(','))
    def save(self, path):
        global grows,labels
        t=[]
        t.append(','.join(labels))
        for x in grows:
            t.append(','.join(x))
        t=('\n'.join(t))
        with open(path,'w') as file:
            file.write(t)
    def get_row_dict(self, row_index):
        global grows,labels
        c=0
        d={}
        for x in labels:
            d[x]=grows[row_index][c]
            c+=1
        return d
    def get_cell(self, row_index, label):
        global grows,labels
        return grows [row_index][labels.find(label)]
    def get_column(self, label):
        global grows,labels
        label=labels.find(label)
        row=[]
        for x in grows:
            row.append(x[label])
    def get_label_index(self, label):
        global grows,labels
        if label in labels:
            return labels.find(label)
        else : return 'KeyError'

    def to_dict(self):
        global grows,labels
        """
                format: {
                            "labels":[],
                            "grows":[[...],
                                    [...],
                                    .....
                                    .....
                                    [...]]
                        }
        """
        dic={"labels":labels,"grows":grows}
        return dic

t = Table("mytest.csv")
print(t.to_dict()               )
print(t.get_row_dict(0)         )
print(t.get_column('number')    )
print(t.get_label_index('title'))
print(t.get_cell(0,'title')     )