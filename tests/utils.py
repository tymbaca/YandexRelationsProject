import random
from datetime import datetime, date, timedelta
import citizen_analyzer.settings as api_settings
import tests.settings as settings


def random_date(start: str = settings.START_BIRTH_DATE, stop: str = settings.STOP_BIRTH_DATE) -> date:
    """Choosing random date in dates range"""
    start_date = datetime.strptime(start, api_settings.DATE_PATTERN).date()
    stop_date = datetime.strptime(stop, api_settings.DATE_PATTERN).date()
    delta = stop_date - start_date
    # Selecting random day count between dates
    date_offset = timedelta(random.randint(0, delta.days))
    return start_date + date_offset



