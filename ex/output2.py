output_a = "{:f}".format(52.273)
output_b = "{:15f}".format(52.273)
output_c = "{:+15f}".format(52.273)
output_d = "{:+015f}".format(52.273)

print(output_a)
print(output_b)
print(output_c)
print(output_d)

#소수점 아래 자릿수 지정하기
output_e = "{:15.3f}".format(52.273)
output_f = "{:15.2f}".format(52.273)
output_g = "{:15.1f}".format(52.273)

print(output_e)
print(output_f)
print(output_g)

#의미 없는 소수점 제거하기 {:g} 사용
output_h = 52.0
output_i = "{:g}".format(output_h)
print(output_h)
print(output_i)
