header = ['a', 'b', 'c']
values = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

data_dict = {h: v for h, v in zip(header, zip(*values))}
print data_dict

