from datetime import date

from dateutil import rrule
from fastapi import Depends

from .import_vs_local import ImportVsLocalService


class ImportVsLocalSeriesService:
    def __init__(self, import_vs_local_service: ImportVsLocalService = Depends()):
        self.import_vs_local_service = import_vs_local_service

    def get(self, dt_from: date, dt_to: date, dt_forecast: date, tnved: str | None = None, tnved10: str | None = None):
        list_of_dates = rrule.rrule(rrule.MONTHLY, dtstart=dt_from, until=dt_to)

        y_rf = []
        y_eaes = []
        y_imp = []
        dates = []
        for i in range(len(list_of_dates) - 1):
            rslt_i = self.import_vs_local_service.get(
                dt_from=list_of_dates[i],
                dt_to=list_of_dates[i + 1],
                tnved=tnved,
                tnved10=tnved10,
            )
            y_rf.append(rslt_i[0])
            y_eaes.append(rslt_i[1])
            y_imp.append(rslt_i[2])
            dates.append(list_of_dates[i + 1])

        y_rf_forecast = []
        y_eaes_forecast = []
        y_imp_forecast = []
        dates_forecast = []
        list_of_dates_forecast = rrule.rrule(rrule.MONTHLY, dtstart=dt_to, until=dt_forecast)

        # print(list_of_dates_forecast)
        # TODO прогноз в y_rf_forecast, y_eaes_forecast, y_imp_forecast
        rslt = {
            "x": dates,
            "y_rf": y_rf,
            "y_eaes": y_eaes,
            "y_imp": y_imp,
            "x_forecast": list_of_dates_forecast[1:],
            "y_rf_forecast": y_rf_forecast,
            "y_eaes_forecast": y_eaes_forecast,
            "y_imp_forecast": y_imp_forecast,
        }
        return rslt
