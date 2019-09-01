
file_path = "sample_data.txt"

f = open(file_path, 'r')

contents = f.read().splitlines()


# for i in contents:
#     for j in i.split(','):
#         print(j.strip())
#     print('\n')
#     #     if type(j)== str:
#     #         print(j.strip())
#     # print(i)

s = "\r\n Vinay"

print(s.strip())