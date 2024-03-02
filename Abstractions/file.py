
class Check: 
    def __init__(self, data_file, new_value):
        self.data_file = data_file
        self.new_value = new_value
    def is_have_duplicate(self): 
        for item in self.data_file:
            if(item[0] == self.new_value): 
                return False
            else:
                continue
        return True




class File:
    def __init__(self, path):
        self.path = path
    def read(self):
        with open(self.path, 'r') as f:
            results = []
            for line in f:
                words = line.split(',')
                results.append((words[0], words[1:]))
            return results
    def append(self, title_point, geo_point):
       modified_geo_points = geo_point
       modified_geo_points[len(modified_geo_points)-1] =  f"{modified_geo_points[len(modified_geo_points)-1]}\n" 
       check = Check(self.read(), title_point)
       try:
            if(check.is_have_duplicate()):
                file = open(self.path, "a")
                file.write(title_point + "," + ",".join(modified_geo_points))
                return " Success"
            else: 
                return f" File have point {title_point}"
       except NameError:
            return f"  not allow write in file {NameError}"


class FileAdditions(File):
    def write(self, data):
        file = open(self.path, "w")
        file.write(data)
        file.close()
    def delete(self, title_point):
        indexes_for_delete = []
        count = 0 
        for title, geo in self.read():
            if (title != title_point):
                indexes_for_delete.append([title, geo])
            count += 1
        res = ""
        for index in indexes_for_delete:
            if(index[1]):
                res += index[0] + "," + ",".join(index[1])
        self.write(res)




#print(CSV.append("Sumy", ["50.4501", "30.5234"])) 




      