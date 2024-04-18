def getSumWithMaxCap(maxCapacity, bucketBallNums):
    # 如果原来bucketBallNums中的元素num小于maxCapacity，则无需取出，保留num
    # 如果原来bucketBallNums中的元素num大于maxCapacity，则需要取出若干球，直到num变为maxCapacity
    # 故设置了容量最大值maxCapacity后，每一个桶中的球数为min(num, maxCapacity)，再求和即可
    return sum(min(num, maxCapacity) for num in bucketBallNums)


SUM, n = map(int, input().split())
bucketBallNums = list(map(int, input().split()))


# 如果初始列表bucketBallNums中的小球总数小于给定的总数SUM
# 无需设置容量最大值maxCapacity，直接输出一个列表
if sum(bucketBallNums) < SUM:
    print([])
# 否则需要设置容量最大值maxCapacity，进行二分查找
else:
    # 如果left取值为0，那么需要取出所有小球，此时剩余小球数量为0，必定小于等于SUM
    # 故左闭区间left取0
    # 如果right取值为bucketBallNums中的最大值，则无需取出任何小球
    # bucketBallNums等同于初始状态，必然大于SUM
    # maxCapacity = max(bucketBallNums)一定不是正确的最大容量值，
    # 故右开区间right取max(bucketBallNums)
    left, right = 1, max(bucketBallNums)+1

    # 左闭右开区间，退出循环时存在 left = right = mid
    # 循环不变量为left < right
    while left < right:
        mid = (left + right) // 2
        # 设置的maxCapacity使得bucketBallNums中的元素和大于SUM，说明移除的小球太少
        # 最大容量值maxCapacity设置得太大，right需要左移
        if getSumWithMaxCap(mid, bucketBallNums) > SUM:
            right = mid
        # 设置的maxCapacity使得bucketBallNums中的元素和小于等于SUM，说明移除的小球太多
        # 最大容量值说明maxCapacity设置得太小，left需要右移
        else:
            left = mid + 1

    # 跳出二分查找的while循环时，存在 left = right 使得
    # getSumWithMaxCap(left, bucketBallNums) > SUM 是恰好满足的最小的maxCapacity
    # 故left-1是使得getSumWithMaxCap(left, bucketBallNums) <= SUM恰好满足的最大maxCapacity
    maxCapacity = left-1

    # 构建最终要输出的答案列表，表示在取了maxCapacity的前提下，bucketBallNums列表中每一个桶要取出多少小球
    ans = [0 if num < maxCapacity else num - maxCapacity for num in bucketBallNums]

    print(ans)