import pandas
from pathlib import Path

class Card:
    no: str

    def __init__(self, no:str = None) -> None:
        self.no = no
    
    # 银行卡号验证LUHN算法验证
    def verify_luhn(self):
        sum = 0
        for i, num in enumerate(self.no[-2::-1]):
            num = int(num)
            if i % 2 == 0:
                sum += (num * 2 % 10 + int(num * 2 / 10)) if num * 2 > 9 else num * 2
            else:
                sum += num
        v = int(self.no[-1:])

        if (sum + v) % 10 == 0:
            return True
        return False

    # 标识代码验证
    def verify_card_start(self):
        bin_path = Path(__file__).parent.joinpath("bin.csv")
        df = pandas.read_csv(bin_path, sep=",")
        df["verify"] = df["bin"].map(lambda x: self.no.startswith(str(x)))
        data = df[df["verify"] == True]
        data = data.reset_index()
        if len(data) == 0:
            return False
        if len(self.no) != data.loc[0, "length"]:
            return False
        return True

    def verify_len(self):
        if self.no >= 15 and self.no <= 19:
            return True
        return False
