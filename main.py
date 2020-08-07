from datetime import datetime as dt
from common.util import create_dframe, plot_ma, plot_rets


URL = 'https://kabuoji3.com/stock/'
HEADERS = {"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36"}

start_year = 2000
end_year = 2020

company = {'FUJITSU':'6702', 'HITACHI':'6502', 'NEC':'6701'}

if __name__ == '__main__':
    for company_name, company_id in company.items():
        globals()[company_name] = create_dframe(company_id, start_year, end_year, URL, HEADERS)
    
    end = dt.now()
    start = dt(end.year - 1, end.month, end.day)
    plot_ma((FUJITSU, HITACHI, NEC,), start, end)
    plot_rets((FUJITSU, HITACHI, NEC,), start, end)

