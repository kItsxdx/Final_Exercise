#66111375 กฤษดา ขันตรี


class CheckEvenOddPrime:

    result = ""

    def __init__(self, num_int):
        self.num_int = num_int

    def is_even(self):
        if self.num_int % 2 == 0:
            self.result = "เลขคู่"
        else:
            self.result = "ไม่เป็นเลขคู่"

    def is_odd(self):
        if self.num_int % 2 != 0:
            self.result = "เลขคี่"
        else:
            self.result = "ไม่เป็นเลขคี่"

    def is_prime(self):
        if self.num_int <= 1:
            self.result = "ไม่เป็นจำนวนเฉพาะ"
        elif self.num_int <= 3:
            self.result = "จำนวนเฉพาะ"
        else:
            i = 2
            while i * i <= self.num_int:
                if self.num_int % i == 0:
                    self.result = "ไม่เป็นจำนวนเฉพาะ"
                    return
                i += 2
            self.result = "จำนวนเฉพาะ"
