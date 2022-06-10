class Date:

    def dates(content: str):
        return content.strip()

    @classmethod
    def day_month_year(cls, content):
        return f"число: {int((cls.dates(content[0])) + (cls.dates(content[1])))}\n" \
               f"месяц: {int((cls.dates(content[3])) + (cls.dates(content[4])))}\n" \
               f"год: {((cls.dates(content[6])) + (cls.dates(content[7])) + (cls.dates(content[8])) + (cls.dates(content[9])))}"

    @staticmethod
    def valid(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 2022 >= year >= 1:
                    return "Валидация успешно завершена"
                else:
                    return f"Проверьте год"
            else:
                return f"Проверьте месяц"
        else:
            return f"Проверьте день"


example = "09.11.2022"
print(Date.dates(example))
print(Date.day_month_year(example))
print(Date.valid(9, 12, 2020))
