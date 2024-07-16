
class DataReader:

    @classmethod
    def read_data(cls, ticker) -> list:
        vec = []
        lines = open("data/" + ticker + ".csv", "r").read().splitlines()
        for line in lines[1:]:
            vec.append(float(line.split(',')[4]))

        return vec
