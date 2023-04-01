from enum import Enum


class ProductInTurnoverOperationType(str, Enum):
    rf = "РФ"
    import_from_eas_boundary = "Импорт из-за пределов ЕАЭС"
    labeling_of_remains = "Маркировка остатков"
    import_from_eas = "Ввоз из ЕАЭС"
    relabeling = "Перемаркировка"
    accepted_from_an_individual = "Принято от физического лица"
    refunds = "Возвраты"


class ProductOutTurnoverOperationType(str, Enum):
    sale_to_end_consumer_point_sale = "Продажа конечному потребителю в точке продаж"
    remote_sale_to_end_consumer = "Дистанционная продажа конечному потребителю"
    final_sale_to_organization = "Конечная продажа организации"
    sale_under_government_contract = "Продажа по государственному контракту"
    other = "Прочий тип вывода из оборота"
    write_downs = "Списание / Вывод из оборота без получателя"
    sales_outside_rf = "Продажи за пределы РФ"
