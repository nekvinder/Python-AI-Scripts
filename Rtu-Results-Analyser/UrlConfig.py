import enum


class Types(enum.Enum):
    my_1st_sem = 1
    my_1st_sem_reval = 2
    my_2nd_sem = 3
    my_2nd_sem_reval = 4
    my_1st_sem_back_2019 = 5


class config:
    examName = ''
    url = ''
    subjectsCount = 11
    rnoFrom = 0
    rnoTo = 50

    def __init__(self, Types):
        if(Types == Types.my_1st_sem ):
            self.examName = "my-1st-sem"
            self.url = "https://www.rjlive.in/RTU/Show-Result?Examno=3256&key=A5567F5ACE5A8FCBC1754C3E72F41E18C7FF3A39&no=17emtcs0"
            self.subjectsCount = 11
            self.rnoFrom = 0
            self.rnoTo = 51
        elif Types == Types.my_1st_sem_reval:
            self.examName = "my-1st-sem-reval"
            self.url = "https://www.rjlive.in/RTU/Show-Result?Examno=3326&key=64B066C723A5810B45C1B028A9B822467DCA4163&no=17emtcs0"
            self.subjectsCount = 11
            self.rnoFrom = 0
            self.rnoTo = 51
        elif Types == Types.my_2nd_sem:
            self.examName = "my-2nd-sem"
            self.url = "https://www.rjlive.in/RTU/Show-Result?Examno=3332&key=C9397ED8F9399168690FC5BF85F1301D05C7427F&no=17emtcs0"
            self.subjectsCount = 11
            self.rnoFrom = 0
            self.rnoTo = 51
        elif Types == Types.my_2nd_sem_reval:
            self.examName = "my-2nd-sem-reval"
            self.url = "https://www.rjlive.in/RTU/Show-Result?Examno=4388&key=6407473AF8E07DF6E215922010D1C4DB8760F7DB&no=17emtcs0"
            self.subjectsCount = 11
            self.rnoFrom = 0
            self.rnoTo = 51
        elif Types == Types.my_1st_sem_back_2019:
            self.examName = "my-1st-sem-back-2019"
            self.url = "https://www.rjlive.in/RTU/Show-Result?Examno=4439&key=8B2B8A6CCB9E126E712940882203CDA4DF4EF515&no=17emtcs0"
            self.subjectsCount = 11
            self.rnoFrom = 0
            self.rnoTo = 51
