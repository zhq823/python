from datetime import date

now = date.today()
print(now.strftime("%Y-%m-%d"))

import doctest
doctest.testmod()