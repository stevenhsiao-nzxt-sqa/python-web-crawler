nums = list(range(5))  # 建立一序列的整數串列
print(nums)            # 顯示 "[0, 1, 2, 3, 4]"
print(nums[2:4])       # 切割索引2~4(不含4): 顯示 "[2, 3]"
print(nums[2:])        # 切割索引從2至最後: 顯示 "[2, 3, 4]"
print(nums[:2])        # 切割從開始至索引2(不含2): 顯示 "[0, 1]"
print(nums[:])         # 切割整個串列: 顯示 "[0, 1, 2, 3, 4]"
print(nums[:-1])       # 使用負索引切割: 顯示 "[0, 1, 2, 3]"
nums[2:4] = [7, 8]     # 使用切割來指定子串列
print(nums)            # 顯示 "[0, 1, 8, 9, 4]"


