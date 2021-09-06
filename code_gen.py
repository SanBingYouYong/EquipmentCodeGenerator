import string
import random


class Generator():
    def __init__(self):
        self.upper = list(string.ascii_uppercase)
        self.lower = list(string.ascii_lowercase)
        self.nums = list(range(1,101))
        self.chinese_suffix = [" 型", " 式", " 号"]
        self.chinese_actors = [" 高达 ", " 扎古 ", " 直升机 ", " 轻型坦克 ", " 主战坦克 ", " 护卫舰 ", " 歼星舰 ", " 小型登陆艇 ", " 决战兵器 ", " 坦克歼击车 ", " 护卫战机 ", " 突袭者机器人 "]
        self.chinese_verbs = [" 发射了 ", " 使用了 ", " 射出了 "]
        self.chinese_usage = [" 火箭弹 ", " 反坦克导弹 ", " 机炮 ", " 电磁炮 ", " 烧饼导弹 ", " 死星射线 ", " 防空导弹 ", " bvvd ", " 红外线制导导弹 ", " 钻地炸弹 ", " 5.8mm步枪弹 ", " 舰载机 "]
        self.chinese_describes = [" 击毁了 ", " 击中了 ", " 重创了 ", " 打中了 "]
        # self.chinese_terms = ["击毁了", "击中了", "重创了"]
        # , ""
    
    def choice_num(self):
        chosen_num = random.choice(self.nums)
        # print(chosen_nums)
        return str(chosen_num)
    
    def choice_letter(self, len=1):
        chosen_letters = random.sample(self.upper, len)
        # print(chosen_letters)
        return "".join(chosen_letters)
    
    def generate_by_seed(self, seed):  # seed -> string of nums
        print("using seed: " + seed)
        seed_sum = 0
        seed_product = 1

        for num in seed:
            num = int(num)
            seed_sum += num
            seed_product *= num
        # print(seed_sum, seed_product)

        letter_len = seed_sum % 3 + 1  # A AA AAA
        final_letters = self.choice_letter(letter_len)

        # num_len = seed_product % 3 + 1  # 1 10 101
        final_nums = self.choice_num()

        extend = True if seed_sum % 2 == 0 else False
        extend_more = True if seed_product % 3 == 0 else False

        if not extend:
            # AB-10
            final = final_letters + "-" + str(final_nums)
        else:
            if not extend_more:
                # AB-10C
                final = final_letters + "-" + str(final_nums) + self.choice_letter()
            else:
                pass  # AB-10C-3
                final = final_letters + "-" + str(final_nums) + self.choice_letter() + "-" + str(self.choice_num())
        
        # print(final)
        return final
    
    def generate_by_seed_bool(self, seed):  # seed -> string of nums
        # print("using seed: " + seed)
        result = ""

        # print(seed[0])
        num_first_lets = int(seed[0]) % 3 + 1
        first_lets = self.choice_letter(num_first_lets)
        # print(first_lets)

        result += first_lets

        if int(seed[1]) % 2 == 0:
            result += "-"

        first_nums = self.choice_num()
        result += first_nums

        if int(seed[2]) % 2 == 0:
            result += "-"
            if int(seed[3]) >= 5:
                result += self.choice_num()
            else:
                result += self.choice_letter()
        else:
            result += self.choice_letter()
        
        if int(seed[4]) >= 3:
            result += "-"
            if int(seed[5]) >= 7:
                result += self.choice_num()
            else:
                result += self.choice_letter()
        else:
            result += self.choice_letter()

        # print(result)
        return result

    def generate_random_bool(self):
        random_nums = []
        for i in range(6):
            random_nums.append(random.randint(1,9))
        random_nums = "".join(list(map(str, random_nums)))
        return self.generate_by_seed_bool(random_nums)

    def generate_random(self):
        seed_len = random.randint(6, 8)
        # print(seed_len)
        random_nums = []
        for i in range(seed_len):
            random_nums.append(random.randint(1,9))
        random_nums = "".join(list(map(str, random_nums)))
        return self.generate_by_seed(random_nums)
        
    def generate_bullshit(self, codes):  # len(codes) == 10 (see main)
        bullshit = codes[0]
        bullshit += random.choice(self.chinese_suffix)
        bullshit += random.choice(self.chinese_actors)
        bullshit += random.choice(self.chinese_verbs)
        bullshit += codes[1]
        bullshit += random.choice(self.chinese_suffix)
        bullshit += random.choice(self.chinese_usage)
        bullshit += random.choice(self.chinese_describes)
        bullshit += codes[2]
        bullshit += random.choice(self.chinese_suffix)
        bullshit += random.choice(self.chinese_actors)
        bullshit += "；\n而 "
        bullshit += codes[3]
        bullshit += random.choice(self.chinese_suffix)
        bullshit += random.choice(self.chinese_actors)
        bullshit += " 则 "
        bullshit += random.choice(self.chinese_verbs)
        bullshit += codes[4]
        bullshit += random.choice(self.chinese_suffix)
        bullshit += random.choice(self.chinese_usage)
        bullshit += random.choice(self.chinese_describes)
        bullshit += codes[5]
        bullshit += random.choice(self.chinese_suffix)
        bullshit += random.choice(self.chinese_actors)

        print(bullshit)
        return bullshit


if __name__ == "__main__":
    code_generator = Generator()
    # code_generator.generate_by_seed("197665")
    # code_generator.choice_num()
    codes = []
    for i in range(10):
        codes.append(code_generator.generate_random_bool())
    # print(codes)
    code_generator.generate_bullshit(codes)


# print(upper,lower,nums)
