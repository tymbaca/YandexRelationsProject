incorrect_relatives = """
{
    "citizens": [
        {
            "citizen_id": 1,
            "town": "Москва",
            "street": "Льва Толстого", 
            "building": "16к7стр5", 
            "apartment": 7,
            "name": "Иванов Иван Иванович", 
            "birth_date": "26.12.1986", 
            "gender": "male",
            "relatives": []
        },
        {
            "citizen_id": 2,
            "town": "Москва",
            "street": "Льва Толстого", "building": "16к7стр5",
            "apartment": 7,
            "name": "Иванов Сергей Иванович", 
            "birth_date": "01.04.1997",
            "gender": "male",
            "relatives": [1]
        }
    ]
}
"""
