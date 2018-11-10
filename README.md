# Web

##Список команды
- Алексеев Владимир
- Колтун Дмитрий
- Чернель Евгений

## Граф визуальный прекрасный I

Необходимо разработать программу, которая визуализирует граф представленный в формате JSON
```json
{
    "idx": 1,
    "lines": [
        {
            "idx": 192,
            "length": 1,
            "points": [
                112,
                107
            ]
        },
        {
            "idx": 193,
            "length": 2,
            "points": [
                101,
                102
            ]
        },
        ...
    ],
    "name": "map01",
    "points": [
        {
            "idx": 101,
            "post_idx": 13
        },
        {
            "idx": 102,
            "post_idx": null
        },
        ...
    ]
}
```
* points - вершины графа;
* lines - рёбра графа;
* length - длинна ребра;
* idx - уникальный индекс для линии.
Каждую линию образует 2 точки (points).
Остальную информацию пока можно игнорировать, но в скором будущем она вам возможно понадобится.

Для тестирования вашей программы имеются 2 графа: [big_graph](big_graph.json) и [small_graph](small_graph.json).
Также необходимо самостоятельно создать ещё минимум 2 графа в заданном формате.

Обязательно продумайте наперёд архитектуру вашей программы, чтобы она была открыта для добавления новой функциональности.

Удачи!