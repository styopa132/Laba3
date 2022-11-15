import timeit

print("Выберите метод сортировки: 1-Быстрая сортировка;2-Сортировка расчёской;")
s = int(input())
start_time = """
import qs
import comb


nums=[34,6,2,4,8,5,21,32,12]
if s==1:
    print("Быстрая сортировка:",qs.quick_sort(nums))
if s==2:
    print("Сортировка расчёской",comb.srt(nums))
"""
end_time = timeit.timeit(start_time, number = 1, globals=globals())
print(end_time)
#0.0004982000000000042
#0.0005126000000000852 Второй способ медленнее