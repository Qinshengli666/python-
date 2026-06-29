# ===== 记账小程序 =====
# 1. 添加收入
# 2. 添加支出
# 3. 查看记录
# 4. 查看统计
# 5. 退出
# 请选择: 1
#
# 请输入金额: 5000
# 请输入类型: 工资
# 请输入备注: 月薪
# ✓ 添加成功！
#
# 请选择: 4
#
# 【财务统计】
# 总收入: 5000元
# 总支出: 0元
# 当前余额: 5000元
# #
wb ="""
===== 记账小程序 =====
1. 添加收入
2. 添加支出
3. 查看记录
4. 查看统计
5. 退出

"""

# 记录
jl = []

# 操作次数
cs = 0

#存款
ck = 0

#收入
sr =0

#支出
zc = 0

while True:
    print(wb)

    xz = int(input("请选择"))

    match xz :
        case 1:
            income = float(input("请输入金额: "))
            #存钱
            sr += income
            ck += income
            income_type = input("请输入类型: ")
            remark = input("请输入备注: ")
            print("✓ 添加成功！")
            cs += 1
            jl.append({"序号：": cs ,"类型：": "收入", "金额：": income, "收入类型：": income_type, "备注：": remark})

        case 2:
            expense = float(input("请输入金额: "))
            #取钱
            ck -= expense
            zc += expense
            expense_type = input("请输入类型: ")
            remark2 = input("请输入备注: ")
            print("✓ 添加成功！")
            cs += 1
            jl.append({"序号：": cs ,"类型：": "支出", "金额：": expense, "支出类型：": expense_type, "备注：": remark2})
        case 3:
            print("查看记录")

            for i in jl:
                print(i)

        case 4:
            # print("查看统计")
            print("【财务统计】")
            print("总收入:", sr, "元")
            print("总支出:", zc, "元")
            print("当前余额:", ck, "元")
        case 5:
            print("退出")
            break
        case _:
            print("输入错误")
