Программист, который работал на проекте до вас, разбросал все функции, связанные с математическими вычислениями по разным модулям с именами numbers1, numbers2 и numbers3 (расположенным, к счастью, в одном пакете solution). Причем имена функций тоже сделал странными: все функции в модуле numbers2 заканчиваются на двойку, например, sum2.
Вы быстро поняли, что это неудобно и нужно создать единый интерфейс для доступа к ним (говорят "фасад"). Для этого необходимо импортировать все функции из всех перечисленных модулей в модуль solution/__init__.py.


src/solution/init.py

Задача состоит в том, чтобы файл solution/__init__.py импортировал в себя все функции из трех описанных выше модулей и выставил их наружу (перечислил в списке __all__) под следующими именами: power(), add(), sub(), sqrt() и mul().
В этом задании специально не сказано, где какая функция и под каким именем лежит. Цель этого задания в том, чтобы вы хорошо разобрались с системой пакетов и модулей, что очень упростит вашу жизнь в дальнейшем. Огромная просьба не подсматривать решение и подумать самостоятельно, а в случае чего задать вопрос в комьюнити.

Не забудьте проанализировать файл с тестами, чтобы понять, как используется пакет solution.


Примечания

Если вы импортируете в свой модуль что-то из другого модуля, но никак это что-то не используете, то линтер будет жаловаться на "не используемый импорт". Эта жалоба вполне правомерна, так как забытые импорты замедляют загрузку программы и могут даже привести к ошибкам. Да и просто неиспользуемые импорты выглядят неряшливо. Однако специально для такого случая — сбора определений из нескольких модулей в один — существует способ успокоить линтер: задание списка __all__. В том модуле, в который вы импортируете какие-то имена с целью использования в дальнейшем оных, как элементов модуля, вам нужно завести в этом модуле переменную __all__, значением которой должен быть список или кортеж из строк, соответствующих "экспортируемым" именам. Вот пример такого списка:

from foo import bar

from spam import eggs

__all__ = (
    'bar',
    'eggs',
)