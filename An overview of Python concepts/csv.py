class Table:
    labels=[]
    rows=[]
    def __init__(self, path=None):
        global rows,labels
        if path == None:
            labels=[]
            rows=[]
            return
        with open(path,'r') as file:
            file=file.read()
            file=file.split('\n')
            self.labels=file[0].split(',')
            for x in file[1:]:
                self.rows.append(x.split(','))
    def save(self, path):
        global rows,labels
        t=[]
        t.append(','.join(self.labels))
        for x in self.rows:
            t.append(','.join(x))
        t=('\n'.join(t))
        with open(path,'w') as file:
            file.write(t)
    def get_row_dict(self, row_index):
        global rows,labels
        c=0
        d={}
        for x in self.labels:
            d[x]=self.rows[row_index][c]
            c+=1
        return d
    def get_cell(self, row_index, label):
        global rows,labels
        return self.rows [row_index][self.labels.index(label)]
    def get_column(self, label):
        global rows,labels
        label=self.labels.index(label)
        row=[]
        for x in self.rows:
            row.append(x[label])
        return row
    def get_label_index(self, label):
        global rows,labels
        if label in self.labels:
            return self.labels.index(label)
        else : return 'KeyError'

    def to_dict(self):
        global rows,labels
        """
                format: {
                            "labels":[],
                            "rows":[[...],
                                    [...],
                                    .....
                                    .....
                                    [...]]
                        }
        """
        dic={"labels":self.labels,"rows":self.rows}
        return dic

t = Table("mytest.csv")
t.save('mytest1.csv')
print(t.to_dict()               )
print(t.get_row_dict(0)         )
print(t.get_column('number')    )
print(t.get_label_index('title'))
print(t.get_cell(0,'title')     )