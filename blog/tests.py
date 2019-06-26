from django.test import TestCase
import datetime

# Create your tests here.
if __name__ == '__main__':
    print(datetime.datetime.strftime(datetime.datetime.now(),"%Y-%m-%d %H:%M:%S"))