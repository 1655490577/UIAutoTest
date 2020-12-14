from faker import Faker


fake = Faker('zh_CN')

a = fake.pyint(min_value=1, max_value=33, step=1)
print(a)
