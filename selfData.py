import datetime
import time
from datetime import date, timedelta


class Date:

    def __init__(self, day: int, month: int, year: int):
        """
        constructor init day/month/year (integer type) put in objact

        """
        self.day = day
        self.month = month
        self.year = year

    def __str__(self):
        """
        This Date ToString func
        :return: date in string type
        """
        res = f"date {self.day}.  {self.month}. {self.year} "
        return res

    def check_valid(self):
        """
        Check if input is not error return true
        :return: True/False
        """
        if  datetime.date(self.year, self.month, self.day) != ValueError:
            return True
        else:
            return False


    def get_next_days(self,  *others:int):
        """
        Add n days to this date
        1 or user cohise(input others)
        :param others: int
        :return: date + others
        """
        if others==None:
            d1 = date(self.year, self.month, self.day)
            d2 = d1 + timedelta(others)
            res = Date(d2.day, d2.month, d2.year)
            return res
        else:
            d1 = date(self.year, self.month, self.day)
            d2 = d1 + timedelta(1)
            res = Date(d2.day, d2.month, d2.year)
            return res

    def __eq__(self, others):
        """
        if this date equal to other date
        :param other:
        :return: True/False
        """
        d1 = date(self.year, self.month, self.day)
        d2 = date(others.year, others.month, others.day)
        return d1 == d2

    def __gt__(self, others):
        """
        if this date after input date
        :param other: input date
        :return: True/False
        """
        d1 = date(self.year, self.month, self.day)
        d2 = date(others.year, others.month, others.day)
        return d1 > d2


    def __lt__(self, others):
        """
         if this date before input date
        :param other: input date
        :return: True/False
        """
        d1 = date(self.year, self.month, self.day)
        d2 = date(others.year, others.month, others.day)
        return d1 < d2


    def __sub__(self, others):
        """
        Return date difference
        if this date before return a negative number
        :param other:input date
        :return:difference
        """
        d1 = date(self.year, self.month, self.day)
        d2 = date(others.year, others.month, others.day)
        res = d1 - d2
        return res.days

date1= Date(28,2,2022)
date2= Date(28,3,2022)
