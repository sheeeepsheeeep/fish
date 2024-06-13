# 开一个空列表来存储购物车中的商品
cart = []

# 模型套件的数据，包括代码、名称和价格
mk = [
    {'code': 'M1', 'name': 'Bandai PG 1/60 Strike Freedom Gundam (5063056)', 'price': 899.00},
    {'code': 'M2', 'name': 'Bandai PG 1/60 Unicorn Gundam 02 Banshee Norn (5064232)', 'price': 799.00},
    {'code': 'M3', 'name': 'Bandai PG 1/60 RX-0 Unicorn Gundam (5063513)', 'price': 749.00},
    {'code': 'M4', 'name': 'Bandai PG 1/60 Strike Rouge + Sky Grasper (5064234)', 'price': 699.00},
    {'code': 'M5', 'name': 'Bandai PG 1/60 Zeta Gundam (5064233) / Z Gundam', 'price': 699.00}
]

# 模型人物的数据，包括代码、名称和价格
mf = [
    {'code': 'F1', 'name': 'GSC Freeing Hatsune Miku : My Dear Bunny Ver. Figurine', 'price': 1599.00},
    {'code': 'F2', 'name': 'GSC Star Guardian Ahri Action Figure', 'price': 1049.00},
    {'code': 'F3', 'name': 'Bandai Tamashii Nations Figuarts Zero Monkey.D.Luffy -Red Roc- ', 'price': 1199.00},
    {'code': 'F4', 'name': 'GSC Asuka Langley Figurine - Rebuild of Evangelion', 'price': 810.00},
    {'code': 'F5', 'name': 'Kotobukiya Aether / Lumine with Bonus Face Parts ', 'price': 699.00}
]

# 主菜单函数，显示可用的操作选项
def menu():
    print(" \n 1 - 查看Bandai模型套件")
    print(" 2 - 查看人物模型")
    print(" 3 - 查看购物车")
    print(" 4 - 结算")
    print(" 5 - 退出")

# 用户选择循环，提供菜单选项直到用户选择退出或结算
while True:
    print("欢迎光临Sheeeps玩具店")
    menu()
    option = int(input("请选择操作: "))

    # 退出程序
    if option == 5:
        print("感谢使用Sheeeps玩具店POS系统")
        break

    # 查看Bandai模型套件部分
    elif option == 1:
        while True:
            print(" ")
            for item in mk:
                print(f"{item['code']} {item['name']} RM {item['price']:.2f}")  # 显示每个模型套件的代码、名称和价格
            print(" ")
            
            choice = input("请输入要添加到购物车的商品代码，或输入 '退出' 返回主菜单: ")  # 输入要添加到购物车的商品代码或者输入 '退出' 返回主菜单
            
            if choice.lower() == '退出':  # 如果输入 '退出' 则退出循环
                break
            
            for item in mk:
                if item['code'] == choice:
                    cart.append(item)  # 将选择的商品添加到购物车
                    print(f"\n{item['name']} 已添加到您的购物车。")  # 显示已添加到购物车的信息
                    break
            else:
                print("\n无效的代码，请重试。")  # 如果输入的商品代码无效，则提示重试

    # 查看人物模型部分
    elif option == 2:
        print(" ")
        while True:
            for item in mf:
                print(f"{item['code']} {item['name']} RM {item['price']:.2f}")  # 显示每个人物模型的代码、名称和价格
            print("")
            
            choice = input("请输入要添加到购物车的商品代码，或输入 '退出' 返回主菜单: ")  # 输入要添加到购物车的商品代码或者输入 '退出' 返回主菜单
            
            if choice.lower() == '退出':  # 如果输入 '退出' 则退出循环
                break
            
            for item in mf:
                if item['code'] == choice:
                    cart.append(item)  # 将选择的商品添加到购物车
                    print(f"\n{item['name']} 已添加到您的购物车。")  # 显示已添加到购物车的信息
                    break
            else:
                print("\n无效的代码，请重试。")  # 如果输入的商品代码无效，则提示重试

    # 查看购物车部分，显示购物车中的所有商品信息
    elif option == 3:
        print(" ")
        print("您的购物车中的商品有: ")
        print(" ")
        for item in cart:
            print(f"{item['name']} RM {item['price']:.2f}")

    # 结算
    elif option == 4:
        
        # 检查购物车是否为空
        if len(cart) == 0:
            print("您的购物车是空的。")  # 购物车为空时的提示信息
            print(" ")
            print("感谢您光临Sheeeps玩具店，请再次光临。")  # 感谢光临的提示
            
        else:
            print(" ")
            # 计算购物车中所有商品的小计金额
            subtotal = sum(item['price'] for item in cart)
            print(f"小计金额: RM {subtotal:.2f}")
        
            # 输入税率和折扣率
            tax = float(input("请输入税率: "))  # 输入税率
            disc = float(input("请输入折扣率: "))  # 输入折扣率
            
            # 计算税额和折扣额
            tax1 = subtotal * (tax / 100)
            disc1 = subtotal * (disc / 100)
                
            # 计算加了税和减了折扣后的最终总价
            final = subtotal + tax1 - disc1
                
            print(f"税后折扣总金额: RM {final:.2f}")  # 显示加了税后减了折扣后的总金额
        
            # 输入顾客支付的金额
            payment = float(input("请输入支付金额: "))  # 输入顾客支付的金额
        
            # 计算找零金额或显示还需支付的金额
            change = payment - final
                
            if change == 0:
                print("支付成功")  # 支付成功的提示
            elif change > 0:
                print(f"找零金额: RM {change:.2f}")  # 显示找零金额
        
            elif change < 0:
                left = -change
                print(f"请支付剩余金额: RM {left:.2f}")  # 显示还需支付的金额
        
            else:
                print("无效金额。")  # 无效金额的提示
                
            # 询问是否需要打印收据
            print("1 - 是")  # 打印收据选项 - 是
            print("2 - 否")  # 打印收据选项 - 否
            receipt = int(input("是否需要打印收据?: "))  # 输入是否需要打印收据
    
    
            if receipt != 1 and receipt != 2:
                print("无效选项")  # 无效选项的提示
    
            elif receipt == 2:
                print("\n感谢您光临Sheeeps玩具店")  # 不需要打印收据时的感谢信息
    
            elif receipt == 1:
                print("--------------------------------")  # 打印收据标题
                print("       SHEEEPS TOY STORE        ")
                print("--------------------------------")
    
                print("商品                              单价")  # 商品名称和单价标题
                for item in cart:
                    print(f"{item['name']} RM {item['price']:.2f}")  # 打印购物车中每个商品的名称和单价 
    
                print(f"小计金额:               {subtotal:.2f}")  # 打印小计金额
                print(f"税额:               {tax1:.2f}")  # 打印税额
                print(f"折扣额:         {disc1:.2f}")  # 打印折扣额