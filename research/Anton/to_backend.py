
# должны быть заданы таблицы
# df_intro - введённых товаров 
# df_remove - выведенных товаров 
# df_transactions - перемещения товаров
# df_products - Справочник продукции
# df_retailers - Справочник торговых точек
# df_organizations - Справочник участников оборота

import pandas as pd
import numpy as np
from dateutil import rrule

def on_market(dt:str, gtin:str, tnved:str = None, tnved10:str = None):
    """
    Функция подсчитывает кол-во товара с заданным gtin
    на рынке (разница между тем, сколько введено и тем,
    сколько выведено)
    Если задан tnved, то он используется вместо gtin и tnved10
    Если задан tnved10, то он используется вместо gtin и tnved
    ---
    Args:
        inn:str - хеш ИНН юрлица
        dt:str - дата в формате ISO ГГГГ-MM-ДД
        gtin:str - хеш GTIN
    """
    #TODO фильтрация по tnved10 и tnved
    # фильтрация по дате и gtin
    filtered_intro = df_intro[df_intro['gtin'] == gtin]
    filtered_intro = filtered_intro[filtered_intro['dt'] <= dt]
    
    filtered_removal = df_remove[df_remove['gtin'] == gtin]
    filtered_removal = filtered_removal[filtered_removal['dt'] <= dt]
    
    result = filtered_intro['cnt'].sum() - filtered_removal['cnt'].sum()
    
    return result

def inn_balance(inn:str, dt:str, gtin:str, tnved:str = None, tnved10:str = None):
    """
    Функция подсчитывает для юрлица inn
    приход и расход товаров с заданным gtin
    на момент dt от начала БД
    Если задан tnved, то он используется вместо gtin и tnved10
    Если задан tnved10, то он используется вместо gtin и tnved
    ---
    Args:
        inn:str - хеш ИНН юрлица
        dt:str - дата в формате ISO ГГГГ-MM-ДД
        gtin:str - хеш GTIN
    """
    #TODO фильтрация по tnved10 и tnved
    # фильтрация по вермени и коду товара
    filtered_transactions = df_transactions[df_transactions['gtin'] == gtin]
    filtered_transactions = filtered_transactions[filtered_transactions['dt'] <= dt]
    
    filtered_intro = df_intro[df_intro['gtin'] == gtin]
    filtered_intro = filtered_intro[filtered_intro['dt'] <= dt]
    
    filtered_removal = df_remove[df_remove['gtin'] == gtin]
    filtered_removal = filtered_removal[filtered_removal['dt'] <= dt]
    
    # приход
    positive_transactions = filtered_transactions[filtered_transactions['receiver_inn']==inn]
    positive_transactions_sum_cnt = positive_transactions['cnt_moved'].sum()
    intro_sum = filtered_intro[filtered_intro['inn'] == inn]['cnt'].sum()
    positive_sum_cnt = positive_transactions_sum_cnt + intro_sum
    # positive_sum_vol = positive_sum_cnt * df_products['volume'] # данные не подходят для расчёта физической размерности
    
    # расход
    negative_transactions = filtered_transactions[filtered_transactions['sender_inn']==inn]
    negative_transactions_sum_cnt = negative_transactions['cnt_moved'].sum()
    removal_sum = filtered_removal[filtered_removal['inn'] == inn]['cnt'].sum()
    negative_sum_cnt = negative_transactions_sum_cnt + removal_sum
    
    return (positive_sum_cnt, negative_sum_cnt)

def import_vs_local(dt1:str, dt2:str, tnved:str, tnved10:str = None):
    """
    Расчёт кол-ва товаров из заданной категории tnved или tnved10
    производства РФ, EAЭС и импортных,
    тренд импортозамещения и его прогноз
    Возвращает cnt товаров, введённых в оборот ( российских, из остальных стран  ЕАЭС, иностранных )
    ---
    Args:
        dt1:str - дата начала интервала ввода товара, для которого определяются доли
        dt2:str - дата конца интервала ввода товара, для которого определяются доли
        tnved:str - код ТНВЭД
        tnved10:str - опционально вместо tnved10
    """


    
    # по  operation_type поля 'Импорт. Не ЕАЭС', 'Перемаркировка', 'РФ',
    # 'Маркировка остатков', 'Импорт. ЕАЭС', 'Возврат', 'Принято от физического лица'
    
    countries_rf = ['РОССИЯ',]
    countries_eaes = ['АРМЕНИЯ', 'БЕЛАРУСЬ', 'КАЗАХСТАН', ]
    # countries_foreign = not in [*country_foreign, *country_EAES]
    
    # фильтрация по tnved или tnved10
    if(tnved is not None):
        df_products_filtered = df_products[df_products['tnved']==tnved]
    elif(tnved10 is not None):
        df_products_filtered = df_products[df_products['tnved10'] == tnved10]
    else:
        raise "Не указан ни tnved, ни tnved10"
    
    # фильтрация по стране происходжения df_products_filtered['country']
    gtins_rf = df_products_filtered[df_products_filtered['country'].isin(countries_rf)]['gtin'].to_list() # список gtin из РФ
    gtins_eaes = df_products_filtered[df_products_filtered['country'].isin(countries_eaes)]['gtin'].to_list() # список gtin из остальных стран ЕАЭС
    gtins_foreign = df_products_filtered[~df_products_filtered['country'].isin([*countries_eaes,*countries_rf])]['gtin'].to_list() # список импортных guid
    
    # фильтрация ввода товара по дате
    dates_mask = (df_intro['dt'] >= dt1) & (df_intro['dt'] <= dt2)
    df_intro_filtered = df_intro[dates_mask]
    
    # фильтрация ввода товара по gtin страны происхождения
    df_intro_filtered_rf = df_intro_filtered[df_intro_filtered['gtin'].isin(gtins_rf)]
    df_intro_filtered_eaes = df_intro_filtered[df_intro_filtered['gtin'].isin(gtins_eaes)]
    df_intro_filtered_foreign = df_intro_filtered[df_intro_filtered['gtin'].isin(gtins_foreign)]
    
    result = (df_intro_filtered_rf['cnt'].sum(), df_intro_filtered_eaes['cnt'].sum(), df_intro_filtered_foreign['cnt'].sum())
    
    return result

def import_vs_local_series(dt1:str, dt2:str, dt3:str, tnved, tnved10:None):
    """
    Возвращает результат работы функции import_vs_local
    по месяцам из интервала dt1-dt2 (даты в формате ISO)
    для товаров категории tnved или tnved10
    
    прогноз выполняется по момент dt3
    """
    
    start_date = datetime.fromisoformat(dt1)
    end_date = datetime.fromisoformat(dt2)
    forecast_date = datetime.fromisoformat(dt3)
    list_of_dates = []
    for dt in rrule.rrule(rrule.MONTHLY, dtstart=start_date, until=end_date):
        list_of_dates.append(dt.strftime('%Y-%m-%d'))
    list_of_intervals = [(list_of_dates[i], list_of_dates[i+1]) for i in range(len(list_of_dates)-1)]
    # print(list_of_intervals)
    y_rf   = []
    y_eaes = []
    y_imp  = []
    dates  = []
    for i in tqdm(range(len(list_of_dates)-1)):
        rslt_i = import_vs_local(dt1 = list_of_dates[i],
                                 dt2 = list_of_dates[i+1],
                                 tnved = tnved,
                                 tnved10 = tnved10)
        # print(rslt_i)
        y_rf.append(rslt_i[0])
        y_eaes.append(rslt_i[1])
        y_imp.append(rslt_i[2])
        dates.append(list_of_dates[i+1])
    
    y_rf_forecast   = []
    y_eaes_forecast = []
    y_imp_forecast  = []
    dates_forecast = []
    list_of_dates_forecast = []
    for dt in rrule.rrule(rrule.MONTHLY, dtstart=end_date, until=forecast_date):
        list_of_dates_forecast.append(dt.strftime('%Y-%m-%d'))
    # print(list_of_dates_forecast)
    #TODO прогноз в y_rf_forecast, y_eaes_forecast, y_imp_forecast
    rslt = {"x":dates, "y_rf":y_rf, "y_eaes":y_eaes, "y_imp":y_imp,
           "x_forecast":list_of_dates_forecast[1:], "y_rf_forecast":y_rf_forecast, "y_eaes_forecast":y_eaes_forecast, "y_imp_forecast": y_imp_forecast}
    return rslt

if __name__=="__main__":
    # тест inn_balance
    inn_balance(inn="E34F3F6C9E49FE46C87D067306AAC29B",
            dt="2022-12-01",
            gtin = "BBC31CA374A30B34CAFBFD027888A73D")
    # >> (16, 6)

    # тест on_market
    on_market(dt="2022-12-01", gtin = "BBC31CA374A30B34CAFBFD027888A73D")
    # >> 11
    
    # тест import_vs_local
    dates = [('2021-01-01', '2021-02-01'),
            ('2021-02-01', '2021-03-01'),
            ('2021-03-01', '2021-03-01'),]
    i = 0
    import_vs_local(dt1 = '2022-01-01', dt2 = '2022-02-01', tnved = "6D2580183CEF6C8AF1CC72E1C6E6FBC4")
    # >> (4825804, 95047, 3495922)
    
    # тест import_vs_local_series
    rslt = import_vs_local_series(dt1="2020-01-01", dt2="2023-01-01", dt3="2023-04-01", tnved="6D2580183CEF6C8AF1CC72E1C6E6FBC4", tnved10=None)
    print(rslt)
    # >> {'x': ['2020-01-01', '2020-02-01', '2020-03-01', '2020-04-01', '2020-05-01', '2020-06-01', '2020-07-01', '2020-08-01', '2020-09-01', '2020-10-01', '2020-11-01', '2020-12-01', '2021-01-01', '2021-02-01', '2021-03-01', '2021-04-01', '2021-05-01', '2021-06-01', '2021-07-01', '2021-08-01', '2021-09-01', '2021-10-01', '2021-11-01', '2021-12-01', '2022-01-01', '2022-02-01', '2022-03-01', '2022-04-01', '2022-05-01', '2022-06-01', '2022-07-01', '2022-08-01', '2022-09-01', '2022-10-01', '2022-11-01', '2022-12-01'], 'y_rf': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1950587, 4795483, 4825804, 4853464, 4437304, 3274525, 2569890, 2639608, 1818738, 2361100, 3167153, 3911790, 2899549, 0], 'y_eaes': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 42147, 138933, 95047, 140862, 63590, 88250, 75206, 98480, 101459, 110563, 127135, 130891, 185340, 0], 'y_imp': [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1602992, 4538471, 3495922, 3242417, 1879462, 1290417, 884664, 817241, 1710409, 2394029, 2305660, 2421518, 2076967, 0], 'x_forecast': ['2023-02-01', '2023-03-01', '2023-04-01'], 'y_rf_forecast': [], 'y_eaes_forecast': [], 'y_imp_forecast': []}