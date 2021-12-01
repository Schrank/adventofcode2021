class Day1:
    @staticmethod
    def count(depths: str):
        lines = depths.splitlines()
        current_ine = 9999999
        increased = 0
        for line in lines:
            int_line = int(line)
            if current_ine < int_line:
                increased += 1
            current_ine = int_line
        return increased

    @staticmethod
    def count2(depths: str):
        lines = depths.splitlines()
        increased = 0
        sums = [0, 0]
        i = 0
        for line in lines:
            int_line = int(line)
            sums[i] += int_line
            sums[i+1] += int_line
            sums.append(0)
            sums[i+2] += int_line
            i += 1

        return Day1.count("\n".join(str(e) for e in sums[2:-1]))

